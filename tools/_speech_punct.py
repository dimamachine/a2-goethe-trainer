#!/usr/bin/env python3
"""Soften written fragments so edge-tts does not radio-pause on them.

Azure/edge-tts treats "." as a full stop. Goethe-style replies like
"Ja." / "Genau." / "Seit acht Jahren." then get a long pause before the
next clause. Official spoken German here is a comma (or a joined clause).

Also used as a TTS-time safety net in generate_audio.py.
"""
import json
import re
from pathlib import Path

INTERJECTIONS = sorted((
    'Ja, sehr', 'Leider ja', 'Kein Problem', 'Klingt gut', 'Gute Idee',
    'Sehr unterschiedlich', 'Sehr wichtig', 'Sehr stark', 'Alles klar',
    'Ach so', 'Na ja',
    'Ja', 'Nein', 'Genau', 'Super', 'Gut', 'Klar', 'Okay', 'Ok', 'Stimmt',
    'Prima', 'Wunderbar', 'Toll', 'Schön', 'Danke', 'Bitte', 'Verstehe',
    'Perfekt', 'Gerne', 'Notiert', 'Schade', 'Manchmal', 'Schwer', 'Sehr',
), key=len, reverse=True)

_INTERJ_RE = re.compile(
    r'(?:(?<=^)|(?<=[.!?]\s))('
    + '|'.join(re.escape(w) for w in INTERJECTIONS)
    + r')\.\s+([A-ZÄÖÜ])'
)

# "Seit acht Jahren. Ich habe …" → "Seit acht Jahren habe ich …"
_SEIT_ICH_RE = re.compile(
    r'(Seit\s+(?:dem\s+)?[^.!?]{1,50}?)\.\s+Ich\s+'
    r'(habe|bin|arbeite|wohne|lerne|mache|gehe|komme|koche|spiele|'
    r'fahre|nehme|helfe|kaufe|organisiere|studiere|lebe|kenne)\b',
    re.IGNORECASE,
)

# leftover "Seit X. Something" → comma + lowercase
_SEIT_RE = re.compile(
    r'(Seit\s+(?:dem\s+)?[^.!?]{1,50}?)\.\s+([A-ZÄÖÜ])'
)


def soften(text: str) -> str:
    def interj(m):
        return m.group(1) + ', ' + m.group(2).lower()

    def seit_ich(m):
        return m.group(1) + ' ' + m.group(2).lower() + ' ich'

    def seit_comma(m):
        return m.group(1) + ', ' + m.group(2).lower()

    text = _INTERJ_RE.sub(interj, text)
    text = _SEIT_ICH_RE.sub(seit_ich, text)
    text = _SEIT_RE.sub(seit_comma, text)
    return text


def walk_spoken(obj, fn):
    """Apply fn to every spoken string; return how many strings changed."""
    n = 0
    if isinstance(obj, dict):
        if 'transcript' in obj and isinstance(obj['transcript'], str):
            new = fn(obj['transcript'])
            if new != obj['transcript']:
                obj['transcript'] = new
                n += 1
        if 'text' in obj and isinstance(obj['text'], str) and 'speaker' in obj:
            new = fn(obj['text'])
            if new != obj['text']:
                obj['text'] = new
                n += 1
        for v in obj.values():
            n += walk_spoken(v, fn)
    elif isinstance(obj, list):
        for v in obj:
            n += walk_spoken(v, fn)
    return n


def main():
    tools = Path(__file__).resolve().parent
    files = sorted(tools.glob('_test*_data.json'),
                   key=lambda p: int(re.search(r'(\d+)', p.name).group(1)))
    total = 0
    for p in files:
        data = json.loads(p.read_text(encoding='utf-8'))
        n = walk_spoken(data, soften)
        if n:
            p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n',
                         encoding='utf-8')
        print(f'{p.name:28} {n:3} strings')
        total += n
    print(f'\n{total} spoken strings updated in {len(files)} tests')


if __name__ == '__main__':
    main()
