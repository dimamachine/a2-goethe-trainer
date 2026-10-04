#!/usr/bin/env python3
"""Fix MC Teile (Teil 1 + Teil 3) whose answer key is all-identical.

Goethe A2 answer keys are spread across a/b/c; an all-"b" key is an AI tell and
is gameable. For each affected Teil we reorder each item's `opts` so the SAME
correct option text lands at a varied position, then update `correct`. The
spoken transcript/dialogue is never touched, so audio stays valid.

Deterministic: a per-(test, teil) seed picks a balanced target pattern that
contains all three of a/b/c, so no Teil is monotone and patterns differ across
tests. Idempotent-ish: only rewrites Teile that are currently all-identical.
"""

import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / 'tools'

MC_TEILE = (0, 2)  # Teil 1 and Teil 3 are type 'mc'


def balanced_pattern(seed, n=5):
    """Length-n list over {0,1,2} containing all three values (well spread)."""
    rng = random.Random(seed)
    while True:
        pat = [rng.randint(0, 2) for _ in range(n)]
        if len(set(pat)) == 3 and max(pat.count(k) for k in range(3)) <= 2:
            return pat


def move_correct(opts, correct, target):
    """Return new opts list with the correct text moved to `target` index."""
    correct_text = opts[correct]
    rest = [o for j, o in enumerate(opts) if j != correct]
    new = [None, None, None]
    new[target] = correct_text
    fill = iter(rest)
    for k in range(3):
        if new[k] is None:
            new[k] = next(fill)
    return new


def fix_file(path):
    data = json.loads(path.read_text(encoding='utf-8'))
    tnum = int(re.search(r'_test(\d+)_', path.name).group(1))
    changed = False
    for ti in MC_TEILE:
        teil = data['teile'][ti]
        items = teil.get('items', [])
        keys = [it.get('correct') for it in items]
        if len(items) == 5 and len(set(keys)) == 1:
            pattern = balanced_pattern(tnum * 10 + ti)
            for it, target in zip(items, pattern):
                opts = it['opts']
                if len(opts) != 3:
                    continue
                it['opts'] = move_correct(opts, it['correct'], target)
                it['correct'] = target
            changed = True
    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n',
                        encoding='utf-8')
    return changed


def main():
    files = sorted(TOOLS.glob('_test*_data.json'),
                   key=lambda p: int(re.search(r'_test(\d+)_', p.name).group(1)))
    fixed = []
    for f in files:
        if fix_file(f):
            fixed.append(f.name)
    print(f"Fixed answer-key distribution in {len(fixed)} file(s):")
    for name in fixed:
        print("  - " + name)


if __name__ == '__main__':
    main()
