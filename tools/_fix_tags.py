"""Fix dangling tag mumbles: 'oder. Was meinst du und genau?', ' oder und ',
trailing ' und genau?'. Drops only non-option words, keeps comma budget <=2.
Usage: python3 tools/_fix_tags.py [--apply]"""
import json, re, glob, sys


def optwords(te):
    o = set()
    for x in te.get('options', []):
        o.update(re.findall(r'[a-zäöüß]+', x['text'].lower()))
    return o


def process(apply=False):
    stats = {'p1': 0, 'p2': 0, 'p3': 0}
    for path in sorted(glob.glob('tools/_test*_data.json')):
        d = json.load(open(path, encoding='utf-8'))
        if 'teile' not in d or len(d['teile']) < 2 or 'lines' not in d['teile'][1]:
            continue
        te = d['teile'][1]
        ow = optwords(te)
        dirty = False
        for l in te['lines']:
            t = l['text']
            # p1: "X oder. Was meinst du und genau?" -> "X, oder was meinst du?"
            ns = re.sub(r' oder\. Was meinst du und genau\?', ', oder was meinst du?', t, count=1)
            if ns != t and ns.count(',') <= 2 and 'genau' not in ow:
                t = ns; stats['p1'] += 1
            # p1b: "X oder. Sag mal und genau?" -> "X, oder? Sag mal!"
            ns = re.sub(r' oder\. (Sag mal) und genau\?', r', oder? \1!', t, count=1)
            if ns != t and ns.count(',') <= 2 and 'genau' not in ow:
                t = ns; stats['p1'] += 1
            # p2: " oder und " -> " oder " (stray und)
            if re.search(r' oder und ', t):
                ns = t.replace(' oder und ', ' oder ', 1)
                if ns.count(',') <= 2:
                    t = ns; stats['p2'] += 1
            # p3: trailing " und genau?" -> ", genau?" (budget) else drop
            m = re.search(r' und genau\?$', t)
            if m and 'genau' not in ow:
                if t.count(',') <= 1:
                    t = t[:m.start()] + ', genau?'
                else:
                    t = t[:m.start()] + '?'
                stats['p3'] += 1
            if t != l['text']:
                assert t.count(',') <= 2, t
                l['text'] = t; dirty = True
        if dirty and apply:
            json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
            open(path, 'a', encoding='utf-8').write('\n')
    print('stats:', stats)


if __name__ == '__main__':
    process(apply='--apply' in sys.argv)
