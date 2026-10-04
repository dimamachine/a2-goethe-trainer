"""Verify rewritten T2 dialogues: LEN/TURNS/ORDER/OWN/PUNCT/FRAG. Usage: python3 tools/_checkT2.py 1 3 4 ..."""
import json, re, sys

def W(t): return len(re.findall(r"[A-Za-zÄÖÜäöüß]+", t))
def norm(s): return s.lower().replace("ä","a").replace("ö","o").replace("ü","u").replace("ß","ss")
STOP = {'eine','einen','einem','einer','eines','und','fuer','mit','die','der','das','den','dem',
        'vom','beim','sich','macht','geht','kauft','bringt','alle','einem','einer','eines',
        'wird','werde','werden','haben','hat','habe','sind','ist','bin','tut','mache'}

def person_tag(p, tags=None):
    full = p.split("(")[0].strip()
    if tags and full in tags:
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
    if not (160 <= tot <= 220): iss.append(f"LEN {tot}")
    if not (12 <= len(te["lines"]) <= 16): iss.append(f"TURNS {len(te['lines'])}")
    seen = []
    for l in te["lines"]:
        if l["speaker"] not in seen: seen.append(l["speaker"])
    spk = set(l["speaker"] for l in te["lines"])
    exp = []
    pair_tags = {}
    for i in te["items"]:
        p = i["person"]
        if " und " in person_tag(p, spk):
            pt = person_tag(p, spk).split(" und ")
            exp.extend(pt)
            pair_tags[p] = pt
        else:
            exp.append(person_tag(i["person"], spk))
    if seen != exp: iss.append(f"ORDER {seen} vs {exp}")
    for it in te["items"]:
        p = it["person"]
        pt = pair_tags.get(p, [person_tag(p, spk)])
        opt = next(o["text"] for o in te["options"] if o["letter"] == it["correct"])
        toks = [norm(w) for w in re.findall(r"[A-Za-zÄÖÜäöüß]+", opt)
                if len(w) > 3 and norm(w) not in STOP]
        own = norm(" ".join(l["text"] for l in te["lines"] if l["speaker"] in pt))
        miss = [t for t in toks if t[:3] not in own]
        if miss: iss.append(f"OWN {it['person']}->{it['correct']} miss {miss}")
    for l in te["lines"]:
        for m in re.finditer(r"\b(Ja|Nein|Genau|Super|Gut|Klar|Okay|Stimmt|Prima|Toll|Danke|Gerne|Schade)\. [A-ZÄÖÜ]", l["text"]):
            if "tanke ich Super" not in l["text"]: iss.append(f"PUNCT {m.group(0)}")
        for m in re.finditer(r"\. ([a-zäöüß])", l["text"]):
            iss.append(f"FRAG ...{l['text'][max(0,m.start()-20):m.start()+15]}...")
    return iss

if __name__ == "__main__":
    allok = True
    for n in [int(a) for a in sys.argv[1:]]:
        iss = check(n)
        print(f"#{n}:", "OK" if not iss else iss)
        allok = allok and not iss
    sys.exit(0 if allok else 1)
