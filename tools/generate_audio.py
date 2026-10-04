#!/usr/bin/env python3
"""
Generate audio for Hören tests using edge-tts.

- Random voice selection per "story" from a pool of 4 German neural voices
- Multi-voice for dialogues/interviews (one male + one female randomly)
- Output: assets/audio/{test_id}/{teil-item}.mp3

Usage:
    python3 tools/generate_audio.py            # generate all tests
    python3 tools/generate_audio.py --test ai-1  # one test only
    python3 tools/generate_audio.py --force    # regenerate even if file exists
"""

import asyncio
import edge_tts
import json
import random
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOEREN_HTML = ROOT / 'hoeren.html'
DATA_JS = ROOT / 'assets' / 'data' / 'hoeren-tests.js'
AUDIO_DIR = ROOT / 'assets' / 'audio'
TMP_DIR = Path('/tmp/a2_hoeren_tts_chunks')
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _speech_punct import soften as for_speech  # noqa: E402

# Voice pools. T1/T3/T4 use Hochdeutsch (DE) voices only (exam-like).
# T2 dialogues with up to 5 same-gender speakers need bigger pools:
# DE voices first, AT/CH only as overflow for the 4th/5th same-gender voice.
MALE_VOICES = [
    'de-DE-ConradNeural',
    'de-DE-FlorianMultilingualNeural',
    'de-DE-KillianNeural',
]
FEMALE_VOICES = [
    'de-DE-KatjaNeural',
    'de-DE-SeraphinaMultilingualNeural',
    'de-DE-AmalaNeural',
]
T2_MALE_EXTRA = [
    'de-AT-JonasNeural',
    'de-CH-JanNeural',
]
T2_FEMALE_EXTRA = [
    'de-AT-IngridNeural',
    'de-CH-LeniNeural',
]
ALL_VOICES = MALE_VOICES + FEMALE_VOICES

RATE = '-5%'  # speech rate (-50% to +100%) — exam-calm, slightly slower than default

def extract_tests():
    """Use node to safely eval the TESTS array from assets/data/hoeren-tests.js."""
    node_code = '''
const fs = require('fs');
const html = fs.readFileSync(process.argv[1], 'utf-8');
const startMarker = 'window.HOEREN_TESTS = [';
const start = html.indexOf(startMarker);
if (start === -1) { console.error('TESTS not found'); process.exit(1); }
const endMarker = '\\n];';
const end = html.indexOf(endMarker, start);
if (end === -1) { console.error('TESTS end not found'); process.exit(1); }
const body = html.slice(start + startMarker.length, end);
const arr = new Function('return [' + body + ']')();
console.log(JSON.stringify(arr));
'''
    result = subprocess.run(
        ['node', '-e', node_code, str(DATA_JS)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print('Node parse failed:', result.stderr)
        sys.exit(1)
    return json.loads(result.stdout)


def pick_single_voice():
    """One random voice from all 4."""
    return random.choice(ALL_VOICES)


def pick_voice_for_gender(gender, exclude=(), extended=False):
    """Pick a random voice matching the requested gender, excluding ones already used.
    DE voices first; with extended=True, AT/CH voices fill in past the DE pool."""
    pool = MALE_VOICES if gender == 'm' else FEMALE_VOICES
    extra = T2_MALE_EXTRA if gender == 'm' else T2_FEMALE_EXTRA
    available = [v for v in pool if v not in exclude]
    if not available and extended:
        available = [v for v in extra if v not in exclude]
    if not available:
        available = pool  # fall back to reuse if all in same-gender pool are used
    return random.choice(available)


def pick_dialog_voices(speakers_info, extended=False):
    """Assign voice per speaker, matching gender.
    speakers_info: list of (speaker_name, gender) tuples preserving conversation order.
    For multiple same-gender speakers, picks DIFFERENT voices of that gender.
    extended=True (Hören T2): allow AT/CH overflow voices past the DE pool."""
    voices_map = {}
    used = []
    for name, gender in speakers_info:
        if name in voices_map:
            continue
        v = pick_voice_for_gender(gender, exclude=used, extended=extended)
        voices_map[name] = v
        used.append(v)
    return voices_map


def extract_speakers_info(lines):
    """From a list of {speaker, text, gender?} dicts, return ordered unique
    (speaker, gender) tuples. Default gender 'm' if absent."""
    seen = {}
    order = []
    for ln in lines:
        sp = ln['speaker']
        if sp not in seen:
            seen[sp] = ln.get('gender', 'm')
            order.append(sp)
    return [(sp, seen[sp]) for sp in order]


# Pause design (native edge-tts full stops are ~1 s at slow rates — too long):
# sentences inside one turn get a short gap, turn changes a medium one.
SENT_GAP_MS = 500
LINE_GAP_MS = 800

_ABBR = ('z. B.', 'Dr.', 'Prof.', 'Nr.', 'ca.', 'bzw.', 'Tel.', 'Str.', 'St.',
         'inkl.', 'exkl.', 'ggf.', 'evtl.', 'Hr.', 'Fr.', 'Mio.', 'Mrd.')


def split_sentences(text):
    """Split on [.?!] + space, protecting common abbreviations."""
    tmp = text
    for a in _ABBR:
        tmp = tmp.replace(a, a.replace('.', ''))
    parts = re.split(r'(?<=[.?!])\s+', tmp.strip())
    return [p.replace('', '.').strip() for p in parts if p.strip()]


_sil_cache = {}


def get_silence(ms):
    if ms not in _sil_cache:
        TMP_DIR.mkdir(parents=True, exist_ok=True)
        p = TMP_DIR / f'silence_{ms}.wav'
        if not p.exists():
            subprocess.run([
                'ffmpeg', '-f', 'lavfi', '-i', 'anullsrc=channel_layout=mono:sample_rate=24000',
                '-t', str(ms / 1000), '-c:a', 'pcm_s16le', '-ar', '24000', '-ac', '1', '-y', str(p)
            ], capture_output=True, check=True)
        _sil_cache[ms] = p
    return _sil_cache[ms]


def trim_silence(src, dst):
    """Cut leading/trailing digital silence from a TTS chunk (wav out)."""
    subprocess.run([
        'ffmpeg', '-i', str(src),
        '-af', 'silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.05,'
               'areverse,'
               'silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.05,'
               'areverse',
        '-c:a', 'pcm_s16le', '-ar', '24000', '-ac', '1', '-y', str(dst)
    ], capture_output=True, check=True)


async def synth_trimmed(text, voice, out_path, retries=6):
    raw = out_path.with_name(out_path.stem + '.raw.mp3')
    last_err = None
    for attempt in range(retries):
        try:
            comm = edge_tts.Communicate(for_speech(text), voice, rate=RATE)
            await asyncio.wait_for(comm.save(str(raw)), timeout=180)
            break
        except Exception as e:
            last_err = e
            print(f'    retry {attempt + 1}/{retries} ({type(e).__name__}) {text[:60]!r}')
            await asyncio.sleep(8 * (attempt + 1))
    else:
        raise RuntimeError(f'TTS failed after {retries} tries: {last_err}')
    trim_silence(raw, out_path)
    raw.unlink()


def concat_segments(seg_paths, gaps_after, out_path):
    """Concat mp3 chunks with a silence file of gaps_after[i] ms after chunk i."""
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    list_file = TMP_DIR / 'list.txt'
    with open(list_file, 'w') as f:
        for i, ch in enumerate(seg_paths):
            f.write(f"file '{ch.as_posix()}'\n")
            if i < len(seg_paths) - 1 and gaps_after[i] > 0:
                f.write(f"file '{get_silence(gaps_after[i]).as_posix()}'\n")
    subprocess.run([
        'ffmpeg', '-f', 'concat', '-safe', '0', '-i', str(list_file),
        '-c:a', 'libmp3lame', '-b:a', '64k', '-ar', '24000', '-ac', '1',
        '-y', str(out_path)
    ], capture_output=True, check=True)
    list_file.unlink()


async def gen_single(text, voice, out_path):
    sents = split_sentences(text)
    if len(sents) <= 1:
        await synth_trimmed(text, voice, out_path)
        return
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    chunks = []
    for i, s in enumerate(sents):
        ch = TMP_DIR / f'sent_{i:03}.wav'
        await synth_trimmed(s, voice, ch)
        chunks.append(ch)
    concat_segments(chunks, [SENT_GAP_MS] * (len(chunks) - 1) + [0], out_path)
    for ch in chunks:
        ch.unlink()


async def gen_dialog(lines, voices_map, out_path):
    """Generate each line with assigned voice, concat with ffmpeg."""
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    chunks = []
    gaps = []
    idx = 0
    for li, line in enumerate(lines):
        voice = voices_map[line['speaker']]
        sents = split_sentences(line['text'])
        for si, sent in enumerate(sents):
            ch = TMP_DIR / f'chunk_{idx:03}.wav'
            await synth_trimmed(sent, voice, ch)
            chunks.append(ch)
            last_line = (li == len(lines) - 1)
            last_sent = (si == len(sents) - 1)
            gaps.append(0 if (last_line and last_sent) else (LINE_GAP_MS if last_sent else SENT_GAP_MS))
            idx += 1
    concat_segments(chunks, gaps, out_path)
    for ch in chunks:
        ch.unlink()


async def gen_test(test, force=False):
    tid = test['id']
    test_dir = AUDIO_DIR / tid
    test_dir.mkdir(parents=True, exist_ok=True)
    print(f'\n=== Test {tid}: {test["name"]} ===')

    for ti, teil in enumerate(test['teile']):
        teil_num = ti + 1
        t_type = teil['type']

        if t_type == 'mc':
            # 5 items, each its own audio
            for ii, item in enumerate(teil['items']):
                out = test_dir / f't{teil_num}-{ii + 1}.mp3'
                if out.exists() and not force:
                    print(f'  skip {out.name} (exists)')
                    continue

                if 'lines' in item:
                    # multi-speaker short dialog (Teil 3 style)
                    speakers_info = extract_speakers_info(item['lines'])
                    vmap = pick_dialog_voices(speakers_info)
                    voices_summary = ', '.join(f'{sp}({g})→{vmap[sp].split("-")[-1].replace("Neural","").replace("Multilingual","")}' for sp, g in speakers_info)
                    print(f'  {out.name} ← dialog ({len(item["lines"])} lines, {voices_summary})')
                    await gen_dialog(item['lines'], vmap, out)
                else:
                    # monologue: respect gender field on item if present
                    gender = item.get('gender', random.choice(['m', 'f']))
                    voice = pick_voice_for_gender(gender)
                    vname = voice.split('-')[-1].replace('Neural', '').replace('Multilingual', '')
                    print(f'  {out.name} ← monologue ({gender}, {vname})')
                    await gen_single(item['transcript'], voice, out)

        elif t_type == 'match':
            # Long conversation, voices matched by gender
            out = test_dir / f't{teil_num}.mp3'
            if out.exists() and not force:
                print(f'  skip {out.name} (exists)')
                continue
            speakers_info = extract_speakers_info(teil['lines'])
            vmap = pick_dialog_voices(speakers_info, extended=True)
            voices_summary = ', '.join(f'{sp}({g})→{vmap[sp].split("-")[-1].replace("Neural","").replace("Multilingual","")}' for sp, g in speakers_info)
            print(f'  {out.name} ← conversation ({len(teil["lines"])} lines, {voices_summary})')
            await gen_dialog(teil['lines'], vmap, out)

        elif t_type == 'jn':
            # Interview, voices matched by gender
            out = test_dir / f't{teil_num}.mp3'
            if out.exists() and not force:
                print(f'  skip {out.name} (exists)')
                continue
            speakers_info = extract_speakers_info(teil['transcript'])
            vmap = pick_dialog_voices(speakers_info)
            voices_summary = ', '.join(f'{sp}({g})→{vmap[sp].split("-")[-1].replace("Neural","").replace("Multilingual","")}' for sp, g in speakers_info)
            print(f'  {out.name} ← interview ({len(teil["transcript"])} lines, {voices_summary})')
            await gen_dialog(teil['transcript'], vmap, out)

        else:
            print(f'  ! unknown teil type: {t_type}')


async def main():
    global RATE
    args = sys.argv[1:]
    only_test = None
    force = False
    if '--force' in args:
        force = True
        args.remove('--force')
    if '--rate' in args:
        idx = args.index('--rate')
        RATE = args[idx + 1]
        args = args[:idx] + args[idx + 2:]
        print(f'Override speech rate: {RATE}')
    if '--test' in args:
        idx = args.index('--test')
        only_test = args[idx + 1]

    tests = extract_tests()
    print(f'Found {len(tests)} test(s) in hoeren.html')

    for t in tests:
        if only_test and t['id'] != only_test:
            continue
        await gen_test(t, force=force)

    # Cleanup tmp dir
    if TMP_DIR.exists():
        shutil.rmtree(TMP_DIR, ignore_errors=True)

    print('\n✓ Audio generation done.')
    print(f'  Output: {AUDIO_DIR}')


if __name__ == '__main__':
    asyncio.run(main())
