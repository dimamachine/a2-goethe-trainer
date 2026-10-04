"""Genre checker for new-format T2: 2 speakers discuss five persons.
Principles: tools/_t2_principles.md
Usage: python3 tools/_checkT2b.py 3 28 40"""
import json, re, sys

def W(t): return len(re.findall(r"[A-Za-zÄÖÜäöüß]+", t))
def norm(s): return s.lower().replace("ä","a").replace("ö","o").replace("ü","u").replace("ß","ss")
STOP = {'eine','einen','einem','einer','eines','und','fuer','mit','die','der','das','den','dem',
        'des','vom','beim','sich','macht','geht','kauft','bringt','alle','wird','werde','werden',
        'haben','hat','habe','sind','ist','bin','tut','mache','wieder','auch','noch','nur',
        'ein','einem','einen','einer','eines','kein','keine','keinen','keinem','keiner',
        'diese','dieser','dieses','diesen','jed','jede','jeder','jedes','jeden','welche',
        'alle','alles','man','sich','uns','euch','ihn','ihm','ihnen','mir','dir','sich'}

try:
    A2 = set(json.load(open("/tmp/a2_goethe.json", encoding="utf-8")))
    B1 = set(json.load(open("/tmp/b1_goethe.json", encoding="utf-8")))
except OSError:
    A2, B1 = set(), set()
_A2_MANUAL = ['monat', 'danach', 'starten', 'zweimal', 'zweihundert', 'hundert', 'tausend',
    'zwanzig', 'dreissig', 'vierzig', 'fünfzig', 'sechzig', 'siebzig',
    'achtzig', 'neunzig', 'rotkappchen', 'mars', 'moskau', 'paris', 'rom',
    'london', 'wien', 'prag', 'bern', 'hamburg', 'muenchen', 'koeln', 'venedig',
    'viertel', 'halb', 'dreimal', 'montag', 'dienstag', 'mittwoch', 'donnerstag', 'freitag',
    'samstag', 'sonntag', 'eins', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun',
    'zehn', 'elf', 'zwölf', 'rot', 'grün', 'blau', 'gelb', 'braun', 'weiss', 'schwarz',
    'rosa', 'orange', 'lila', 'grau', 'toll', 'heft', 'zeitung', 'ding', 'leute', 'mensch',
    'welt', 'englisch', 'französisch', 'spanisch', 'russisch', 'chinesisch', 'italienisch',
    'farbe', 'feierabend', 'flasche', 'gabel', 'glas', 'herd', 'hut', 'löffel', 'messer',
    'pfanne', 'schirm', 'stiefel', 'tasse', 'teller', 'topf', 'januar', 'februar', 'märz',
    'april', 'mai', 'juni', 'juli', 'august', 'september', 'oktober', 'november', 'dezember',
    'frühling', 'sommer', 'herbst', 'winter']
A2 = {norm(w) for w in A2} | {norm(w) for w in _A2_MANUAL}
B1 = {norm(w) for w in B1}
ALLOW = {'okay','cool','super','perfekt','herrlich','hey','hurra','tschuss','prost','juhu','brrr','pow'}
INF = {'freust':'freuen','freue':'freuen','kochst':'kochen','kocht':'kochen',
 'räume':'räumen','schau':'schauen','surfe':'surfen','surft':'surfen','taucht':'tauchen',
 'bringt':'bringen','bringe':'bringen','bringst':'bringen','macht':'machen','mache':'machen',
 'geht':'gehen','gehe':'gehen','gehst':'gehen','kommt':'kommen','komme':'kommen',
 'sieht':'sehen','liest':'lesen','fährt':'fahren','fahre':'fahren','gibt':'geben',
 'nimmt':'nehmen','nehme':'nehmen','hilft':'helfen','spricht':'sprechen','spreche':'sprechen',
 'sprichst':'sprechen','fällt':'fallen','lässt':'lassen','lasse':'lassen','baut':'bauen',
 'findet':'finden','schickt':'schicken','liegt':'liegen','zahlst':'zahlen','will':'wollen',
 'wollten':'wollen','weiß':'wissen','weißt':'wissen','wäre':'sein','wird':'werden',
 'worden':'werden','geworden':'werden','bin':'sein','bist':'sein','sind':'sein','ist':'sein',
 'hat':'haben','hast':'haben','habe':'haben','haben':'haben','tut':'tun','kann':'können',
 'mag':'mögen','magst':'mögen','muss':'müssen','darf':'dürfen','soll':'sollen','helfen':'helfen',
 'gefallen':'fallen','gelacht':'lachen','gewartet':'warten','backe':'backen','meinst':'meinen',
 'komm':'kommen','surfst':'surfen','beschweren':'beschweren','räumt':'räumen','schaut':'schauen',
 'nehme':'nehmen','nimmst':'nehmen','nimmt':'nehmen','nehmt':'nehmen','nimm':'nehmen',
 'esse':'essen','isst':'essen','trifft':'treffen','triffst':'treffen','stiehlt':'stehlen',
 'empfiehlt':'empfehlen','wurde':'werden','wurdest':'werden','wirst':'werden','warst':'sein',
 'waren':'sein','wart':'sein','hatten':'haben','hattest':'haben','läufst':'laufen',
 'fährst':'fahren','schläfst':'schlafen','wäschst':'waschen','hältst':'halten',
 'fängst':'fangen','wächst':'wachsen','stirbt':'sterben','vergisst':'vergessen',
 'liest':'lesen','siehst':'sehen','sieht':'sehen','gibst':'geben','gibt':'geben',
 'hilfst':'helfen','spricht':'sprechen','wirfst':'werfen','wirft':'werfen',
 'stimmt':'stimmen','fällt':'fallen','läuft':'laufen','schläft':'schlafen','wäscht':'waschen',
 'versprochen':'versprechen','bestelle':'bestellen','bestellt':'bestellen','hole':'holen',
 'verloren':'verlieren','verliert':'verlieren',
 'packe':'packen','packst':'packen','singt':'singen','liebt':'lieben','kennt':'kennen',
 'sagt':'sagen','findet':'finden','kauft':'kaufen','fehlt':'fehlen','drückt':'drücken',
 'schickt':'schicken','fütterst':'füttern','fuetterst':'füttern',
 'besten':'gut','bestem':'gut','bester':'gut','bestes':'gut','beste':'gut','besseren':'gut'}
NINF = {norm(k): v for k, v in INF.items()}
RINF_KEYS = list(NINF.keys())
VSTOP = {'und','oder','aber','denn','mit','ohne','für','gegen','durch','über','unter',
 'zwischen','hinter','neben','beim','vom','zum','zur','einer','einem','einen','eine','eines',
 'der','die','das','den','dem','des','ein','sich','mich','dich','uns','euch','mein','dein',
 'sein','ihr','unser','euer','meine','deine','seine','ihre','kein','keine','nicht','auch',
 'nur','schon','noch','sehr','wieder','heute','morgen','jetzt','dann','hier','dort','alle',
 'alles','beide','jede','jeder','jedes','welche','dieser','diese','dieses','man','sie','wir',
 'euch','ihn','ihm','ihnen','dir','mir','was','wer','wen','wem','wie','wann','warum','woher',
 'wohin','dass','weil','wenn','als','bevor','nachdem','damit','sondern','doch','nein','bitte',
 'danke','also','halt','mal','etwa','fast','ganz','gar','wohl','bereits','immer','später',
 'genug','genau','etwas','nichts','viel','viele','wenig','mehr','erste','letzte','nächste',
 'andere','solche','jeden','jedem','allen','aller','zwei','drei','keiner','deins','meins',
 'deinen','seinen','lange','neue','gute','große','kleine','alte','letztes','letzte','ihrer',
 'eure','euere','euren','unserer','unseren','meinen','meinem','meiner','deinem','deiner',
 'seinem','seiner','ihrem','ihren','ihrem','keinem','keinen','keiner','jedem','jeden',
 'diesem','diesen','welchen','welchem','solchen','solchem','manchen','mancher','vieler',
 'vielen','weniger','wenigen','anderen','anderem','anderen','ersten','letzten','nächsten',
 'dazu','daran','darauf','dafür','dagegen','dabei','damit','davon','dafür',
 'fürs','fürs','meines','deines','seines','ihres','unseres','allem','alle','alles'}
_NAMES_RAW = {'markus','sara','lisa','anna','tim','lukas','tom','oma','opa','tante','onkel',
 'spanien','berlin','mama','papa','lars','sven','marie','jonas','robert','tanja','sophie',
 'mara','eva','jan','tobias','müller','schmidt','weber','fischer','meyer','frankreich',
 'italien','russland','china','japan','amerika','europa','deutschland','österreich','schweiz',
 'york','tokio','istanbul','amsterdam','madrid','wien','leipzig','stuttgart','münchen','kanada',
 'mia','lena','belgien','mickey','disneyland','mozart',
 'frankfurt','dresden','köln','nürnberg','porsche','tesla','audi','bmw','ford','mercedes',
 'opel','mini','cooper','volkswagen','ägypten','youtube','rotkäppchen','schneewittchen',
'weihnachtsmann','osterhase'}
NAMES = {norm(w) for w in _NAMES_RAW}

def stems(w):
    out = {w}
    for suf in ('esten','sten','stem','ster','stes','ern','en','em','er','es','est','ete','eten','e','n','s','t','st','test','ung','heit','keit','schaft','te','ste'):
        if len(w) > len(suf) + 2 and w.endswith(suf):
            out.add(w[:-len(suf)])
    # re-add infinitive -en/-n to stripped verb roots: find->finden, sing->singen
    for x in list(out):
        if len(x) > 3:
            out.add(x + 'en')
            out.add(x + 'n')
    # participles ge-...-t/-en: gestellt->stellen, geschlafen->schlafen
    if w.startswith('ge') and len(w) > 5:
        core = w[2:]
        out.add(core)
        for suf in ('t','en','et'):
            if core.endswith(suf) and len(core) > len(suf) + 2:
                out.add(core[:-len(suf)])
                out.add(core[:-len(suf)] + 'en')
    # e-epenthesis for el/er adjectives: dunkl->dunkel, teur->teuer
    for x in list(out):
        if len(x) > 3 and x[-1] in 'rlmn':
            out.add(x[:-1] + 'e' + x[-1])
    return out

def _in_a2(x):
    return bool(set(stems(x)) & A2S)

def compound_ok(wl, depth=0):
    if depth > 2:
        return False
    for i in range(3, len(wl) - 2):
        a, b = wl[:i], wl[i:]
        if len(a) < 3 or len(b) < 3:
            continue
        if _in_a2(a) and (_in_a2(b) or compound_ok(b, depth + 1)):
            return True
    return False

def _stemset(words):
    out = set()
    for w in words:
        out |= stems(w)
    return out

A2S = _stemset(A2)
B1S = _stemset(B1)

def vocab_level(wl):
    forms = set(stems(wl)) | {NINF.get(wl, wl)}
    forms |= {NINF.get(f, f) for f in list(forms)}
    if forms & A2S or compound_ok(wl):
        return 0
    if wl in ALLOW:
        return 1
    if forms & B1S:
        return 1
    return 2

def person_tag(p, tags):
    full = p.split("(")[0].strip()
    if full in tags:
        return full
    tag = full
    for pre in ("Annas ", "Toms ", "Lisas ", "Markus' "):
        if tag.startswith(pre):
            tag = tag[len(pre):]
    return tag

def check(n):
    d = json.load(open(f"tools/_test{n}_data.json", encoding="utf-8"))
    te = d["teile"][1]; iss = []
    tot = sum(W(l["text"]) for l in te["lines"])
    if not (120 <= tot <= 170): iss.append(f"LEN {tot}")
    if not (12 <= len(te["lines"]) <= 16): iss.append(f"TURNS {len(te['lines'])}")
    spk = sorted(set(l["speaker"] for l in te["lines"]))
    if len(spk) != 2: iss.append(f"SPEAKERS {spk} (want exactly 2)")
    tags = set(l["speaker"] for l in te["lines"])
    ptags = []
    for i in te["items"]:
        p = i["person"]
        if " und " in p:
            ptags.append(person_tag(p, tags).split(" und "))
        else:
            ptags.append([person_tag(p, tags)])
    # first-mention order (text mention or self-talk line)
    first = []
    for tlist in ptags:
        idx = None
        for j, l in enumerate(te["lines"]):
            txt = norm(l["text"])
            if l["speaker"] in tlist or any(re.search(r'\b' + re.escape(norm(t)) + r's?\b', txt) for t in tlist):
                idx = j
                break
        first.append(idx)
    if any(i is None for i in first):
        iss.append(f"NAMES missing {[te['items'][k]['person'] for k,i in enumerate(first) if i is None]}")
    elif first != sorted(first):
        iss.append(f"MENTION-ORDER {first} (want ascending)")
    # correct-concept spread: turn where correct tokens appear within ±2 of a person-line
    pos = []
    for k, it in enumerate(te["items"]):
        tlist = ptags[k]
        opt = next(o["text"] for o in te["options"] if o["letter"] == it["correct"])
        groups = [[norm(w) for w in re.findall(r"[A-Za-zÄÖÜäöüß]+", g)
                   if len(w) >= 3 and norm(w) not in STOP]
                  for g in opt.split("/")]
        toks = groups[0]
        def tok_in_own(t, own, ownwords, allow_head=False):
            if t in ownwords:
                return True
            if len(t) <= 4 and t in own:
                return True
            if 5 <= len(t) <= 6 and t[:5] in own:
                return True
            if len(t) > 6 and t[:7] in own:
                return True
            forms = set(stems(t)) | {NINF.get(t, t)}
            if any(f in ownwords for f in forms):
                return True
            base = NINF.get(t, t)
            ows = set()
            for w in ownwords:
                if len(w) >= 3:
                    ows |= set(stems(w)) | {NINF.get(w, w)}
            if base in ows or t in ows or forms & ows:
                return True
            if len(t) >= 7:
                for i in range(3, len(t) - 2):
                    a, b = t[:i], t[i:]
                    if len(a) >= 3 and len(b) >= 3:
                        fa = set(stems(a)) | {NINF.get(a, a)}
                        fb = set(stems(b)) | {NINF.get(b, b)}
                        if (fa & ows) and (fb & ows):
                            return True
            if allow_head and len(t) >= 5 and any(len(w) >= 5 and w in t for w in ownwords):
                return True  # compound head: Geschenk in Geburtstagsgeschenk
            return False
        def is_pl(j):
            l = te["lines"][j]
            if l["speaker"] in tlist:
                return True
            txt = norm(l["text"])
            return any(re.search(r'\b' + re.escape(norm(t)) + r's?\b', txt) for t in tlist)
        hit = None
        for j, l in enumerate(te["lines"]):
            own = norm(l["text"])
            ownwords = set(re.findall(r"[a-zäöüß]+", own))
            if any(g and all(tok_in_own(t, own, ownwords) for t in g) for g in groups):
                if any(is_pl(x) for x in range(max(0, j-2), min(len(te["lines"]), j+3))):
                    hit = j
                    break
        if hit is None:
            iss.append(f"CONCEPT {it['person']}->{it['correct']} not found near person-lines")
        else:
            pos.append(hit)
    if pos:
        if pos[0] < 2: iss.append(f"TOO-EARLY first answer at turn {pos[0]}")
        if pos[-1] < 9: iss.append(f"TOO-COMPACT last answer at turn {pos[-1]}")
    # distractors: unassigned options mentioned (lemma match); their words are
    # booklet-given and non-essential, hence exempt from VOCAB (handled there).
    assigned = {it["correct"] for it in te["items"]}
    alltxt = norm(" ".join(l["text"] for l in te["lines"]))
    allwords = set(re.findall(r"[a-zäöüß]+", alltxt))
    nd = 0
    for o in te["options"]:
        if o["letter"] in assigned:
            continue
        toks = [norm(w) for w in re.findall(r"[A-Za-zÄÖÜäöüß]+", o["text"])
                if len(w) >= 3 and norm(w) not in STOP]
        if any(tok_in_own(t, alltxt, allwords, allow_head=True) for t in toks):
            nd += 1
    if nd < 2: iss.append(f"DISTRACTORS only {nd} (want >=2)")
    for l in te["lines"]:
        nc = l["text"].count(",")
        if nc >= 3:
            iss.append(f"COMMAS {nc} :: {l['speaker']}: {l['text'][:70]}")
        for m in re.finditer(r"\b(Ja|Nein|Genau|Super|Gut|Klar|Okay|Stimmt|Prima|Toll|Danke|Gerne|Schade)\. [A-ZÄÖÜ]", l["text"]):
            iss.append(f"PUNCT {m.group(0)}")
        for m in re.finditer(r"\. ([a-zäöüß])", l["text"]):
            iss.append(f"FRAG ...{l['text'][max(0,m.start()-20):m.start()+15]}...")
        seen_w = {}
        for w in re.findall(r"[A-Za-zÄÖÜäöüß]{4,}", norm(l["text"])):
            if w in VSTOP or w in NAMES:
                continue
            seen_w[w] = seen_w.get(w, 0) + 1
        dups = sorted(w for w, c in seen_w.items() if c > 2)
        adj = re.findall(r",\s*([a-zäöüß]{4,}),\s*\1\b", norm(l["text"]))
        dups = sorted(set(dups) | set(adj))
        if dups:
            iss.append(f"DUPINTRA {dups} :: {l['speaker']}: {l['text'][:60]}")
    tot_commas = sum(l["text"].count(",") for l in te["lines"])
    if tot_commas > 22:
        iss.append(f"COMMAS-TOTAL {tot_commas} (want <=22)")
    # VOCAB: content words must be A2 (0) or B1/allow (1); above B1 (2) forbidden.
    # Budget: max 8 level-1 words per dialogue; answer concepts must be level-0 or option text.
    if A2 and B1:
        optwords = set()
        for o in te["options"]:
            optwords.update(norm(w) for w in re.findall(r"[A-Za-zÄÖÜäöüß]+", o["text"]))
        lvl1, bad = [], []
        for l in te["lines"]:
            for w in re.findall(r"[A-Za-zÄÖÜäöüß]{4,}", l["text"]):
                wl = norm(w)
                if wl in VSTOP or wl in NAMES:
                    continue
                if wl.endswith("s") and wl[:-1] in NAMES:
                    continue  # Toms, Lisas, Annas ...
                if wl.endswith("'") or wl.endswith("’"):
                    continue
                if wl in optwords or any(wl in o for o in optwords):
                    continue  # option wording is given in the booklet
                if len(wl) >= 4 and any(len(o) >= 4 and o[:4] == wl[:4] for o in optwords):
                    continue  # inflected option word (platten/platter ...)
                lv = vocab_level(wl)
                if lv == 2:
                    bad.append(w)
                elif lv == 1:
                    lvl1.append(w)
        if bad:
            iss.append(f"VOCAB>B1 {sorted(set(bad))}")
        if len(lvl1) > 8:
            iss.append(f"VOCAB-B1-budget {len(lvl1)} (max 8): {sorted(set(lvl1))}")
    return iss

if __name__ == "__main__":
    allok = True
    for n in [int(a) for a in sys.argv[1:]]:
        iss = check(n)
        print(f"#{n}:", "OK" if not iss else iss)
        allok = allok and not iss
    sys.exit(0 if allok else 1)
