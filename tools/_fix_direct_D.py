#!/usr/bin/env python3
"""Top-up for direct-speech batch D. Neutral elaborations only."""
import json
from pathlib import Path

TOOLS = Path(__file__).resolve().parent


def load(n):
    p = TOOLS / f"_test{n}_data.json"
    return p, json.loads(p.read_text(encoding="utf-8"))


def save(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ext(n, idx, extra):
    p, d = load(n)
    d["teile"][1]["lines"][idx]["text"] += " " + extra
    save(p, d)


# T38 (+7)
for i, t in [(0, "Bunte Autos!"), (1, "Wunderschön!"), (2, "Riesig grün!"), (4, "Zum Vorlesen gern!"),
             (11, "Wirklich gern!"), (15, "Bunt und schön!")]:
    ext(38, i, t)
# T39 (+8)
for i, t in [(0, "Wunderbar weit!"), (1, "Tolles Musical!"), (2, "Wirklich schön!"), (4, "Total spannend!"),
             (11, "Wirklich gern!"), (15, "Niemals vergessen!")]:
    ext(39, i, t)
# T40 (+16)
for i, t in [(0, "Mit viel Spaß!"), (1, "Total nass!"), (2, "Richtig ruhig!"), (3, "Wie früher!"),
             (4, "Viele Fische!"), (5, "Bitte melden!"), (7, "Wirklich nur das."), (9, "Nur meins!"),
             (10, "Bitte melden!"), (12, "Unbedingt!"), (15, "Unbedingt wichtig!")]:
    ext(40, i, t)
# T41 (+11)
for i, t in [(0, "Mit viel Spaß!"), (1, "Seit Jahren schon!"), (2, "Jede Woche!"),
             (3, "Mit allen!"), (4, "Schon gewonnen!"), (10, "Wirklich Wahnsinn!"),
             (11, "Warme Sachen!"), (15, "Sehr wichtig!")]:
    ext(41, i, t)
# T42 (+25)
for i, t in [(0, "Wunderschön glänzend!"), (1, "Selbst gelesen gern!"), (2, "Gut gemerkt wirklich!"),
             (3, "Riesig duftend!"), (4, "Lecker belgisch!"), (5, "Bitte melden?"),
             (6, "Wirklich nur das."), (7, "Bleibe dabei!"), (8, "Nur meine!"),
             (9, "Nur meine!"), (10, "Nur meiner!"), (11, "Alle zusammen!"),
             (12, "Wirklich sehr!"), (14, "Wirklich pünktlich!"), (15, "Unbedingt schön!")]:
    ext(42, i, t)
# T43 (+18)
for i, t in [(0, "Traumhaft schnell!"), (1, "Umweltfreundlich toll!"), (2, "Drei Kinder Platz!"),
             (3, "Stadtflitzer süß!"), (4, "Bequem weit!"), (5, "Bitte melden?"),
             (6, "Wirklich nur der."), (7, "Bleibe dabei!"), (8, "Nur meiner!"),
             (9, "Nur meiner!"), (10, "Nur meiner!"), (15, "Jeder einen!")]:
    ext(43, i, t)
# T44 (+14)
for i, t in [(0, "Seit Jahren laut!"), (1, "Jeden Abend schön!"), (2, "Sehr stilvoll!"),
             (4, "Oft live!"), (5, "Bitte melden?"), (7, "Bleibe dabei!"),
             (8, "Nur meiner!"), (9, "Nur meiner!"), (10, "Nur meiner!"), (15, "Bitte wirklich!")]:
    ext(44, i, t)
# T45 (+12)
for i, t in [(0, "Seit Jahren Fan!"), (1, "Sehr bunt!"), (2, "Total toll!"),
             (3, "Seit Jahren schon!"), (4, "Super spannend!"), (5, "Bitte melden?"),
             (7, "Bleibe dabei!"), (9, "Nur meine!"), (15, "Unbedingt hingehen!")]:
    ext(45, i, t)
# T46 (+22)
for i, t in [(0, "Freunde wichtig!"), (1, "Total aufregend!"), (2, "Leider krank!"),
             (3, "Super live!"), (4, "Drei Tage lang!"), (5, "Bitte melden?"),
             (6, "Wirklich nur das."), (7, "Bleibe dabei!"), (8, "Nur meine!"),
             (9, "Nur meiner!"), (10, "Nur meiner!"), (12, "Aus jeder Stadt!"),
             (13, "Euch allen!"), (15, "Sehr wichtig!")]:
    ext(46, i, t)
# T47 (+26)
for i, t in [(0, "Zum Verkaufen toll!"), (1, "Mit Liebe!"), (2, "Jede Woche neu!"),
             (3, "Mit allem dran!"), (4, "Sehr ehrgeizig!"), (5, "Bitte melden?"),
             (6, "Wirklich nur die."), (7, "Bleibe dabei!"), (8, "Nur meine!"),
             (9, "Nur meine!"), (10, "Nur meine!"), (11, "Alle zusammen!"),
             (12, "Fünf Minuten!"), (14, "Geht weiter!"), (15, "Sehr wichtig!")]:
    ext(47, i, t)

print("top-up D applied")
