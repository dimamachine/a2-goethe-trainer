"""Bulk-fix staccato commas in T2 (Hoeren Teil 2).
Target: <=2 commas per line, <=22 total per dialogue.
Method: keep all content words; only punctuation + drop stacked single-word
fillers that are NOT option words / names. Never touches speakers/line count.
Usage: python3 tools/_fix_commas_t2.py            (dry-run report)
       python3 tools/_fix_commas_t2.py --apply     (write JSONs)
"""
import json, re, glob, sys

SUBORD = {'weil','dass','wenn','wie','wo','als','ob','damit','bevor','nachdem','obwohl','während','falls','sodass'}
COORD = {'und','oder','aber','denn','sondern'}
PREP = {'mit','seit','nach','aus','für','zum','zur','beim','im','am','um','bei','von','vom',
        'zu','zum','in','ins','auf','ans','an','über','unter','durch','ohne','gegen','pro',
        'während','trotz','statt','wegen','hinter','neben','zwischen','vor','bis','ab','à'}
ADV = {'leider','wirklich','sicher','klar','gern','gerne','sehr','endlich','heute','morgen',
       'bitte','ja','schon','noch','auch','nur','nie','immer','oft','fast','ganz','schön',
       'gut','super','toll','genug','wohl','etwa','halt','mal','doch','eben','sogar',
       'pünktlich','gemütlich','gemuetlich','schnell','langsam','ruhig','leise','laut',
       'vorsichtig','gemeinsam','zusammen','allein','sorgfältig','ordentlich','bequem',
       'früh','spät','fleiβig','locker','zusammen'}
# sentence-final tags whose comma must be KEPT (", ja!" is natural)
TAGTAIL = {'ja!','ja.','ja?','oder?','oder!','bitte!','bitte?','gell?','ne?','okay?','klar?'}
VERBS = {'ist','sind','war','waren','wird','werden','hat','haben','hatte','hatten','braucht',
         'brauche','brauchen','macht','machen','geht','gehen','kommt','kommen','gibt','geben',
         'glaub','glaubst','glaubt','glauben','kostet','kosten','dauert','reicht','reichen',
         'hilft','helfen','steht','stehen','liegt','liegen','findet','finden','weiß','sagt',
         'sagen','denkt','denken','kennt','kennen','bleibt','fährt','fährt','läuft','läuft',
         'schläft','wohnt','arbeitet','spielt','lacht','wartet','freut','passt','gehört',
         'bringt','bringen','nimmt','nehmen','sieht','sehen','liest','lesen','schreibt',
         'fährt','fahren','isst','essen','trinkt','schläft','schlafen','putzt','kocht',
         'baut','zahlt','bestellt','holt','räumt','liegt','fehlt','stimmt','tut','kann'}
IMPER = {'glaub','schau','schauen','komm','hör','sag','warte','stell','nimm','iss','trink',
         'bleib','geh','mach','pass','putz','räum','lies','sieh','plauder'}
FILLERS = {'super','toll','schön','schoen','gut','modern','schick','cool',
           'herrlich','prima','wirklich','sicher','klar','gern','gerne','sehr','endlich',
           'heute','morgen','leider','bitte','echt','total'}
DISC_END = ('Ja','Nein','Genau','Super','Gut','Klar','Okay','Stimmt','Prima','Toll','Danke','Gerne','Schade')
# fillers that may be dropped at line END ("..., sicher, klar." -> "..., sicher.")
ENDFILL = FILLERS - {'ja','oder','bitte'}

def nameset(te):
    names = set(l['speaker'] for l in te['lines'])
    for it in te['items']:
        for w in re.findall(r"[A-ZÄÖÜ][a-zäöüß]+", it['person']):
            names.add(w)
    return names

def has_verb(tail_s):
    for w in re.findall(r"[A-Za-zäöüß]+", tail_s.lower()):
        if w in VERBS or w in IMPER:
            return True
    return False

def join_tail(head, tail_s, stats):
    """Attach tail (text after removed comma) with und / space / new sentence."""
    tw = tail_s.split()
    first = tw[0].lower().rstrip('.?!,') if tw else ''
    if first in COORD:
        stats['coord'] += 1
        return head + ' ' + tail_s
    if first in SUBORD:
        return None  # signal: keep comma, split earlier
    if tail_s.strip().lower() in TAGTAIL:
        return None  # keep natural tag comma (", ja!" / ", oder?")
    if has_verb(tail_s) or len(tw) >= 5:
        cap = tail_s[0].upper() + tail_s[1:] if tail_s else ''
        mh = re.search(r'(\b\w+)\s*$', head)
        if mh and mh.group(1) in DISC_END:
            stats['split'] += 1
            return head + '! ' + cap
        stats['split'] += 1
        return head + '. ' + cap
    if first in PREP or first in ADV:
        stats['attach'] += 1
        return head + ' ' + tail_s
    # adjective-ish short tail: always und (polysyndeton ok, never jam words)
    stats['und'] += 1
    return head + ' und ' + tail_s

def cleanup(s, names, stats):
    """Safe normalizations applied regardless of comma budget."""
    ns = re.sub(r',\s*(und|oder|aber|denn|sondern)\b', r' \1', s)
    if ns != s:
        stats['coord'] += 1; s = ns
    m = re.search(r',\s*([A-ZÄÖÜ][a-zäöüß]+)\s*,\s*((?:[Bb]ei|[Mm]it|[Ff]ür|[Vv]on|[Zz]u|[Nn]ach|[Aa]us|[Uu]m|[Ii]n|[Aa]n|[Aa]uf)\s+[A-Za-zäöüß]+|[A-Za-zäöüß]+)', s)
    if m and m.group(1) in names and m.group(2).lower() not in PREP:
        s = s[:m.start()] + ' ' + m.group(2) + ', ' + m.group(1) + s[m.end():]
        stats['voc'] += 1
    m2 = re.search(r',\s*([a-zäöüß]+\s+und\s+[a-zäöüß]+)\s*,', s)
    if m2 and m2.group(1).split()[0].lower() not in SUBORD:
        s = s[:m2.start()] + ' ' + m2.group(1) + ' ' + s[m2.end():]
        s = re.sub(r'\s{2,}', ' ', s)
        stats['appo'] += 1
    return s

def collapse_chains(s, optwords, stats):
    """Drop trailing chains of bare filler segments: '..., gut, toll, super?' -> '...?'."""
    m = re.search(r'((?:,\s*[a-zäöüß]+(?:\s+und\s+[a-zäöüß]+)?)+)\s*([.?!])\s*$', s)
    if not m or m.group(0).count(',') < 2:
        return s
    segs = [x.strip() for x in m.group(1).split(',') if x.strip()]
    punct = m.group(2)
    keep = []
    dropped = []
    for idx_sg, sg in enumerate(segs):
        words = re.findall(r'[a-zäöüß]+', sg.lower())
        is_last = (idx_sg == len(segs) - 1)
        if is_last and ((sg + punct).lower() in TAGTAIL or sg.lower() in ('ja', 'oder', 'bitte')):
            keep.append(sg)  # never drop a sentence-final tag
            continue
        if (words and all(w in FILLERS or w in ADV for w in words)
                and not any(w in optwords for w in words)):
            dropped.append(sg)
            continue
        keep.append(sg)
    if not dropped:
        return s
    stats['chain'] += len(dropped)
    # keep first two dropped fillers as an und-pair (no extra commas, keeps length+liveliness)
    pair = ' und '.join(dropped[:2])
    head = s[:m.start()]
    if keep:
        s = head + ', ' + ', '.join(keep + [pair]) + punct
    else:
        s = head.rstrip() + ', ' + pair + punct
    return re.sub(r'\s{2,}', ' ', s)

def drop_extra_tags(s, stats):
    """Max 1 discourse tag per line: oder?/sag mal/weißt du/genau as tags."""
    tags = re.findall(r',\s*(oder\?|sag mal,|weißt du,|weißt du\?|genau[?,]|richtig[?,]|stimmt[?,])', s)
    if len(tags) <= 1:
        return s
    # keep first, drop the rest
    first = True
    def repl(m):
        global _drop_first_done
        return m.group(0)
    out = s
    count = [0]
    def sub(m):
        count[0] += 1
        if count[0] == 1:
            return m.group(0)
        stats['tagdrop'] += 1
        return ''
    out = re.sub(r',\s*(oder\?|sag mal,|weißt du,|weißt du\?|genau[?,]|richtig[?,]|stimmt[?,])', sub, out)
    return re.sub(r'\s{2,}', ' ', out)

def drop_dup_seg(s, stats):
    """', X, X' repeated segment -> ', X'."""
    ns = re.sub(r',\s*([^,?.!]+?),\s*\1(?=[,.?!])', r', \1', s)
    if ns != s:
        stats['dup'] += 1
    return ns

def final_touch(s, optwords, stats):
    # "Toll. X" -> "Toll! X" (checker PUNCT + better TTS)
    ns = re.sub(r'\b(Ja|Nein|Genau|Super|Gut|Klar|Okay|Stimmt|Prima|Toll|Danke|Gerne|Schade)\. ([A-ZÄÖÜ])',
                r'\1! \2', s)
    if ns != s:
        stats['punct'] += 1; s = ns
    # space-separated filler piles: "Super schön gut und neu" -> "Super und neu"
    pile = re.findall(r'(?:[Ss]uper|[Tt]oll|[Ss]chön|[Gg]ut|[Nn]eu|[Mm]odern|[Cc]ool|[Pp]rima|[Hh]errlich)(?:\s+(?:und\s+)?(?:super|toll|schön|gut|neu|modern|cool|prima|herrlich|bequem|groß|klein))+\b', s)
    for p in pile:
        words = re.findall(r'[A-Za-zäöüß]+', p)
        core = [w for w in words if w.lower() not in ('und',)]
        if len(core) >= 3 and not any(w.lower() in optwords for w in core):
            first, last = core[0], core[-1]
            # keep first + last with und (drop middle fillers)
            mid = ' und '.join([first[0].upper()+first[1:] if p[0].isupper() else first, last]) \
                if False else None
            rep = (first + ' und ' + last)
            s = s.replace(p, rep, 1)
            stats['pile'] += 1
    return s

def fix_loop(s, names, optwords, stats, budget=2):
    s = collapse_chains(s, optwords, stats)
    s = drop_extra_tags(s, stats)
    s = drop_dup_seg(s, stats)
    for _ in range(20):
        if s.count(',') <= budget:
            break
        # 0) leading adverbial comma drop
        m0 = re.match(r'^((?:Also|Na ja|Zum Glück|Heute|Morgen|Abends|Morgens|Sonst))\s*,\s*', s)
        if m0:
            s = m0.group(1) + ' ' + s[m0.end():]
            stats['lead'] += 1
            continue
        # d) drop stacked filler ", filler," if not option word
        m3 = re.search(r',\s*([a-zäöüß]+)\s*,', s)
        if m3 and m3.group(1).lower() in FILLERS and m3.group(1).lower() not in optwords and s.count(',') >= 3:
            s = s[:m3.start()] + s[m3.end()-1:]
            s = re.sub(r'\s{2,}', ' ', s)
            stats['drop'] += 1
            continue
        # d2) drop filler at very end "..., sicher, klar." -> "..., sicher."
        m4 = re.search(r',\s*([a-zäöüß]+)\s*([.!?])\s*$', s)
        if m4 and m4.group(1).lower() in ENDFILL and m4.group(1).lower() not in optwords and s.count(',') >= 4:
            s = s[:m4.start()] + m4.group(2)
            s = re.sub(r'\s{2,}', ' ', s)
            stats['enddrop'] += 1
            continue
        before = s
        s = cleanup(s, names, stats)
        if s != before:
            continue
        # e) generic last comma
        idx = s.rfind(',')
        head, tail = s[:idx], s[idx+1:]
        tail_s = tail.strip()
        first = tail_s.split()[0].lower().rstrip('.?!,') if tail_s.split() else ''
        if first in SUBORD or tail_s.lower() in TAGTAIL:
            idx2 = head.rfind(',')
            if idx2 == -1:
                # stuck: split AT the subordinate comma (dialogue fragment ok)
                cap = tail_s[0].upper() + tail_s[1:] if tail_s else ''
                s = head + '. ' + cap
                stats['splitsub'] += 1
                continue
            h2, t2 = head[:idx2], head[idx2+1:]
            joined = join_tail(h2, t2.strip(), stats)
            if joined is None:
                # earlier part also protected: split AT the subordinate comma
                cap = tail_s[0].upper() + tail_s[1:] if tail_s else ''
                s = head + '. ' + cap
                stats['splitsub'] += 1
                continue
            s = joined + ',' + tail
            continue
        s = join_tail(head, tail_s, stats)
    return s

def fix_line(text, names, optwords, stats, budget=2):
    parts = re.split(r'(?<=[.?!])\s+', text)
    out = []
    for p in parts:
        p = cleanup(p, names, stats)
        p = collapse_chains(p, optwords, stats)
        p = drop_extra_tags(p, stats)
        p = drop_dup_seg(p, stats)
        if p.count(',') > budget:
            p = fix_loop(p, names, optwords, stats, budget)
        out.append(p)
    s = ' '.join(out)
    s = cleanup(s, names, stats)
    if s.count(',') > budget:
        s = fix_loop(s, names, optwords, stats, budget)
    before_ft = s
    s = final_touch(s, optwords, stats)
    if s != before_ft and s.count(',') > budget:
        s = fix_loop(s, names, optwords, stats, budget)
        s = final_touch(s, optwords, stats)
    s = re.sub(r'\s{2,}', ' ', s)
    s = re.sub(r'\s+([.?!])', r'\1', s)
    s = re.sub(r'\.\s*\.', '.', s)
    s = re.sub(r'([.?!])\s+([a-zäöüß])', lambda m: m.group(1)+' '+m.group(2).upper(), s)
    return s.strip()

def process(apply=False):
    from collections import Counter
    stats = Counter()
    changed_lines = 0; changed_files = 0
    alldata = []
    for path in sorted(glob.glob('tools/_test*_data.json')):
        d = json.load(open(path, encoding='utf-8'))
        if 'teile' not in d or len(d['teile']) < 2:
            continue
        te = d['teile'][1]
        if 'lines' not in te:
            continue
        optwords = set()
        if 'options' in te:
            for o in te['options']:
                optwords.update(re.findall(r'[a-zäöüß]+', o['text'].lower()))
        names = nameset(te)
        alldata.append((path, d, te, optwords, names))
    # pass 1: per-line budget 2
    for path, d, te, optwords, names in alldata:
        for l in te['lines']:
            new = fix_line(l['text'], names, optwords, stats)
            if new != l['text']:
                l['text'] = new
    # pass 2: per-dialogue total <= 22 -> budget 1 for remaining 2-comma lines
    for path, d, te, optwords, names in alldata:
        total = sum(l['text'].count(',') for l in te['lines'])
        if total <= 22:
            continue
        for l in te['lines']:
            if total <= 22:
                break
            if l['text'].count(',') == 2:
                new = fix_line(l['text'], names, optwords, stats, budget=1)
                if new != l['text']:
                    total -= (l['text'].count(',') - new.count(','))
                    l['text'] = new
    for path, d, te, optwords, names in alldata:
        n0 = 0
        for l in te['lines']:
            pass
        if apply:
            json.dump(d, open(path,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
            open(path,'a',encoding='utf-8').write('\n')
    # recount changed vs backup? report totals instead
    over = sum(1 for _, d, te, _, _ in alldata
               for _ in [sum(l['text'].count(',') for l in te['lines'])] if _ > 22)
    bad = sum(1 for _, d, te, _, _ in alldata for l in te['lines'] if l['text'].count(',') >= 3)
    print('lines>=3:', bad, 'dialogues total>22:', over)
    print('stats:', dict(stats))

if __name__ == '__main__':
    if '--selftest' in sys.argv:
        names={'Markus','Lisa','Anna','Tom','Sara','Tim','Mama','Papa','Lukas','Jonas','Mutter','Vater','Mia','Lena','Marie','Jan','Tanja','Oma','Opa'}
        from collections import Counter
        tests=['Klar, ich bringe Wein mit, roten und weißen, vom guten Laden an der Ecke.',
'Schön! Was ist mit Brot, bringt jemand Brot mit, frisches, vom Bäcker?',
'Stimmt! Also, bis morgen, um drei, bei euch, pünktlich, ja!',
'Na ja! Abends schlecht, mit Licht, leider, seit Wochen.',
'Genau, ich brauche Kontaktlinsen, weiche, jeden Tag, neue, super, bequem.',
'Ja, Tom braucht eine Lesebrille, plus eins, zum Lesen, gemütlich, auf dem Sofa.',
'Nein, keiner, eine reicht, wirklich, glaub mir, sicher, klar.',
'Also, morgen ist das Familienfest! Freust du dich schon, Markus, sehr?',
'Gern! Sag mal, ist das Paket da, mit der Tasche, aus Berlin, endlich?',
'Nein, eine neue Kreditkarte, endlich da, nach langen Wochen.',
'Ja, Tim braucht eine Augen-Operation, kurz und gut, ohne Angst, mit viel Mut.',
'Nein, keiner, eine reicht, wirklich, glaub mir, sicher, klar.']
        for t in tests:
            f=fix_line(t,names,set(),Counter())
            print(f'IN : {t} [{t.count(chr(44))}]')
            print(f'OUT: {f} [{f.count(chr(44))}]')
            print()
    else:
        process(apply='--apply' in sys.argv)
