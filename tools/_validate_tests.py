#!/usr/bin/env python3
"""Validate all _testN_data.json files for structural / answer-key correctness.

Checks each test against the Goethe A2 Hören schema used by this project and
verifies the matching audio (12 mp3 per test). Exits non-zero if any errors.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / 'tools'
AUDIO = ROOT / 'assets' / 'audio'

errors = []
warnings = []


def err(tid, msg):
    errors.append(f"[{tid}] {msg}")


def warn(tid, msg):
    warnings.append(f"[{tid}] {msg}")


def check_gender(tid, where, obj):
    g = obj.get('gender')
    if g not in ('m', 'f'):
        err(tid, f"{where}: gender is {g!r}, expected 'm' or 'f'")


def validate(path):
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f"[{path.name}] invalid JSON: {e}")
        return None
    tid = data.get('id', path.name)

    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', tid):
        err(tid, f"id {tid!r} not a lowercase slug")
    if not data.get('name'):
        err(tid, "missing name")

    teile = data.get('teile')
    if not isinstance(teile, list) or len(teile) != 4:
        err(tid, f"expected 4 Teile, got {len(teile) if isinstance(teile, list) else teile}")
        return tid
    types = [t.get('type') for t in teile]
    if types != ['mc', 'match', 'mc', 'jn']:
        err(tid, f"Teil types {types} != ['mc','match','mc','jn']")

    # Teil 1: mc, 5 monologue items
    t1 = teile[0]
    items = t1.get('items', [])
    if len(items) != 5:
        err(tid, f"Teil 1: {len(items)} items, expected 5")
    for i, it in enumerate(items, 1):
        w = f"Teil1.item{i}"
        if not it.get('transcript'):
            err(tid, f"{w}: missing transcript")
        check_gender(tid, w, it)
        opts = it.get('opts', [])
        if len(opts) != 3:
            err(tid, f"{w}: {len(opts)} opts, expected 3")
        c = it.get('correct')
        if not isinstance(c, int) or not (0 <= c < len(opts)):
            err(tid, f"{w}: correct={c!r} out of range for {len(opts)} opts")
        if not it.get('q'):
            err(tid, f"{w}: missing q")

    # Teil 2: match
    t2 = teile[1]
    lines = t2.get('lines', [])
    options = t2.get('options', [])
    mitems = t2.get('items', [])
    if len(options) != 9:
        err(tid, f"Teil 2: {len(options)} options, expected 9 (a-i)")
    letters = [o.get('letter') for o in options]
    if letters != list('abcdefghi'):
        err(tid, f"Teil 2: option letters {letters} != a-i")
    for o in options:
        if not o.get('text'):
            err(tid, f"Teil 2: option {o.get('letter')} missing text")
    if len(mitems) != 5:
        err(tid, f"Teil 2: {len(mitems)} items, expected 5")
    seen = []
    line_speakers = {l.get('speaker') for l in lines}
    for it in mitems:
        person = it.get('person')
        c = it.get('correct')
        if c not in letters:
            err(tid, f"Teil 2: item {person!r} correct={c!r} not a valid letter")
        if c in seen:
            err(tid, f"Teil 2: duplicate correct letter {c!r}")
        seen.append(c)
        # person should be referenced somewhere in the conversation
        if person and not any(person in (l.get('text', '') + ' ' + str(l.get('speaker', ''))) for l in lines):
            warn(tid, f"Teil 2: person {person!r} not mentioned in conversation lines")
    for l in lines:
        check_gender(tid, f"Teil2.line[{l.get('speaker')}]", l)

    # Teil 3: mc, 5 dialogue items
    t3 = teile[2]
    items = t3.get('items', [])
    if len(items) != 5:
        err(tid, f"Teil 3: {len(items)} items, expected 5")
    for i, it in enumerate(items, 1):
        w = f"Teil3.item{i}"
        dl = it.get('lines', [])
        if len(dl) < 2:
            err(tid, f"{w}: dialogue has {len(dl)} lines")
        for l in dl:
            check_gender(tid, f"{w}.line[{l.get('speaker')}]", l)
        opts = it.get('opts', [])
        if len(opts) != 3:
            err(tid, f"{w}: {len(opts)} opts, expected 3")
        c = it.get('correct')
        if not isinstance(c, int) or not (0 <= c < len(opts)):
            err(tid, f"{w}: correct={c!r} out of range")
        if not it.get('q'):
            err(tid, f"{w}: missing q")

    # Teil 4: jn interview
    t4 = teile[3]
    transcript = t4.get('transcript', [])
    if len(transcript) < 4:
        err(tid, f"Teil 4: transcript has {len(transcript)} lines")
    for l in transcript:
        check_gender(tid, f"Teil4.line[{l.get('speaker')}]", l)
    jitems = t4.get('items', [])
    if len(jitems) != 5:
        err(tid, f"Teil 4: {len(jitems)} items, expected 5")
    for i, it in enumerate(jitems, 1):
        if it.get('correct') not in ('ja', 'nein'):
            err(tid, f"Teil4.item{i}: correct={it.get('correct')!r} not 'ja'/'nein'")
        if not it.get('q'):
            err(tid, f"Teil4.item{i}: missing q")

    # all-same-answer-key sanity (a too-easy/broken key often shows as all identical)
    t1c = [it.get('correct') for it in teile[0].get('items', [])]
    if len(set(t1c)) == 1:
        warn(tid, f"Teil 1 answer key all identical: {t1c}")
    t3c = [it.get('correct') for it in teile[2].get('items', [])]
    if len(set(t3c)) == 1:
        warn(tid, f"Teil 3 answer key all identical: {t3c}")
    jnc = [it.get('correct') for it in teile[3].get('items', [])]
    if len(set(jnc)) == 1:
        warn(tid, f"Teil 4 ja/nein key all identical: {jnc}")

    # audio
    adir = AUDIO / tid
    n = len(list(adir.glob('*.mp3'))) if adir.exists() else 0
    if n != 12:
        err(tid, f"audio: {n}/12 mp3 files in {adir}")

    return tid


def main():
    files = sorted(TOOLS.glob('_test*_data.json'),
                   key=lambda p: int(re.search(r'_test(\d+)_', p.name).group(1)))
    seen_ids = {}
    for f in files:
        tid = validate(f)
        if tid:
            seen_ids.setdefault(tid, []).append(f.name)
    for tid, fs in seen_ids.items():
        if len(fs) > 1:
            errors.append(f"[{tid}] duplicate id across files: {fs}")

    print(f"Validated {len(files)} test files.")
    if warnings:
        print(f"\n{len(warnings)} WARNING(s):")
        for w in warnings:
            print("  ! " + w)
    if errors:
        print(f"\n{len(errors)} ERROR(s):")
        for e in errors:
            print("  ✗ " + e)
        sys.exit(1)
    print("\n✓ All tests structurally valid; audio complete (12/12 each).")


if __name__ == '__main__':
    main()
