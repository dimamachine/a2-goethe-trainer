"""Thin out leading interjections (64% -> ~40% of lines) + dedup closing
formulas repeated within one line. Never drops Nein/Schade/Aber/Bitte/Danke.
Usage: python3 tools/_thin_interj.py [--apply]"""
import json, re, glob, sys

DROP = {'Ja', 'Genau', 'Klar', 'Super', 'Gut', 'Schön', 'Schoen', 'Stimmt',
        'Toll', 'Prima', 'Okay', 'Richtig', 'Sicher', 'Wunderbar', 'Klasse',
        'Stark', 'Verstehe'}
INTERJ = DROP | {'Nein', 'Schade', 'Aber', 'Bitte', 'Danke', 'Doch', 'Hallo',
                 'Prost', 'Puh', 'Ach', 'Oh', 'Na', 'Toll', 'Super'}
FORMULAS = ['viel spaß', 'tschüss', 'bis bald', 'bis morgen', 'gute nacht',
            'mach es gut', 'viel glück', 'gute reise', 'gute besserung',
            'viel erfolg', 'bis dann']

def starts_interj(t):
    w = t.split()[0].rstrip(',!') if t.split() else ''
    return w in INTERJ

def process(apply=False):
    stats = {'doubles': 0, 'drops': 0, 'dedup': 0}
    for path in sorted(glob.glob('tools/_test*_data.json')):
        d = json.load(open(path, encoding='utf-8'))
        if 'teile' not in d or len(d['teile']) < 2 or 'lines' not in d['teile'][1]:
            continue
        te = d['teile'][1]
        lines = te['lines']
        dirty = False
        # R1: "Ja, klar! ..." -> "Klar! ..."
        for l in lines:
            ns = re.sub(r'^(Ja|Doch), (klar|bitte|genau|gut|stimmt|super)!',
                        lambda m: m.group(2).capitalize() + '!', l['text'], count=1)
            if ns != l['text']:
                l['text'] = ns; stats['doubles'] += 1; dirty = True
        # R2: drop "WORD, " when prev line also starts with interjection
        for i, l in enumerate(lines):
            m = re.match(r'^([A-ZÄÖÜ][a-zäöüß]+), (.*)$', l['text'], re.S)
            if m and m.group(1) in DROP and i > 0 and starts_interj(lines[i-1]['text']):
                rest = m.group(2)
                if rest:
                    l['text'] = rest[0].upper() + rest[1:]
                    stats['drops'] += 1; dirty = True
        # R3: if still >45%, drop every 3rd interjection-starting "WORD, " line
        starts = [i for i, l in enumerate(lines)
                  if re.match(r'^[A-ZÄÖÜ][a-zäöüß]+, ', l['text'])
                  and l['text'].split()[0].rstrip(',') in DROP]
        if len(starts) / max(1, len(lines)) > 0.45:
            for k, i in enumerate(starts):
                if k % 3 == 2:
                    m = re.match(r'^[A-ZÄÖÜ][a-zäöüß]+, (.*)$', lines[i]['text'], re.S)
                    rest = m.group(1)
                    if rest:
                        lines[i]['text'] = rest[0].upper() + rest[1:]
                        stats['drops'] += 1; dirty = True
        # R4: within-line dup of closing formulas in last 3 lines
        for l in lines[-3:]:
            low = l['text'].lower()
            for f in FORMULAS:
                if low.count(f) >= 2:
                    # drop 2nd occurrence + stranded connector
                    idx = low.find(f, low.find(f) + 1)
                    pre, post = l['text'][:idx], l['text'][idx+len(f):]
                    pre = re.sub(r'\s*(und|oder|,)\s*$', '', pre)
                    new = (pre + post).strip()
                    new = re.sub(r'\s{2,}', ' ', new)
                    if new and new.count(',') <= 2:
                        l['text'] = new
                        low = new.lower()
                        stats['dedup'] += 1; dirty = True
        if dirty and apply:
            json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
            open(path, 'a', encoding='utf-8').write('\n')
    print('stats:', stats)

if __name__ == '__main__':
    process(apply='--apply' in sys.argv)
