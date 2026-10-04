#!/usr/bin/env python3
"""Top-up for direct-speech batch C. Statement elaborations, no reassignments."""
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


# T26
for i, t in [(0, "Kurz und modern, beim besten Friseur der Stadt."), (1, "Mit rotem Lack."),
             (2, "Hoffentlich hilft es gut."), (3, "Lange und schön."), (4, "Eine ganze Stunde."),
             (5, "Bitte melden?"), (8, "Nur das."), (9, "Nur die."), (14, "Alle zusammen!")]:
    ext(26, i, t)
# T27
for i, t in [(0, "Direkt am Strand."), (1, "Zusammen, super."), (2, "Mit Balkon."), (3, "Mit Lagerfeuer."),
             (4, "Gemütlich und ruhig."), (5, "Bitte melden?"), (6, "Wirklich nur Hotel."),
             (7, "Nur die."), (8, "Nur die."), (9, "Nur das."), (10, "Ganz früh?"),
             (11, "Bis Samstag!"), (12, "Zusammen!"), (13, "Gute Reise!"), (14, "Unbedingt!"), (15, "Wirklich.")]:
    ext(27, i, t)
# T28
for i, t in [(0, "Aus Berlin."), (1, "Ärgerlich."), (2, "Von meiner Freundin."), (3, "Nach Wochen."),
             (4, "Spannend, wirklich."), (5, "Bitte melden?"), (6, "Nur die."), (7, "Nur die."),
             (8, "Nur die."), (9, "Nur das."), (10, "Heute?"), (11, "Feierabend!"),
             (12, "Bis dann!"), (13, "Erholt euch!"), (14, "Schönes Wochenende!"), (15, "Bitte!")]:
    ext(28, i, t)
# T29
for i, t in [(0, "Jeden Donnerstag."), (1, "Jede Woche."), (2, "Aber toll."),
             (3, "Premiere."), (4, "Endlich."), (5, "Bitte melden?"), (6, "Wirklich nur Chor."),
             (7, "Nur der."), (8, "Nur das."), (9, "Nur die."), (10, "Um drei?"),
             (11, "Bis dann!"), (12, "Sehr!"), (13, "Bis Sonntag!"), (15, "Bis Sonntag alle!")]:
    ext(29, i, t)
# T30
for i, t in [(0, "Endlich fertig."), (1, "Dringend."), (2, "Zwei Stunden."),
             (3, "Endlich genehmigt."), (4, "Bestanden."), (5, "Bitte melden?"),
             (6, "Wirklich nur das."), (7, "Nur das."), (8, "Nur die."), (9, "Nur der."),
             (10, "Pünktlich?"), (11, "Bis heute Abend!"), (13, "Ihr Lieben!")]:
    ext(30, i, t)
# T31
for i, t in [(0, "Eine Stunde."), (1, "Hurra."), (2, "Super."),
             (3, "Wirklich."), (4, "Leider wahr."), (5, "Bitte melden?"), (6, "Wirklich nur die."),
             (7, "Nur die."), (8, "Nur die."), (9, "Wirklich."), (10, "Alle?"),
             (11, "Wirklich immer."), (12, "Tschüss!"), (13, "Euch auch!"), (14, "Bis bald!")]:
    ext(31, i, t)
# T32
for i, t in [(0, "Jeden Morgen früh."), (1, "Jeden Dienstag fest."), (2, "Klasse!"),
             (3, "Mit Lehrer."), (4, "Herrlich."), (5, "Immer."), (6, "Wirklich nur die."),
             (7, "Nur die."), (8, "Nur die."), (9, "Nur der."), (10, "Alle da?"),
             (11, "Bis gleich!"), (12, "Alle Bahnen!"), (13, "Viel Spaß!"), (14, "Bis gleich!"), (15, "Unbedingt!")]:
    ext(32, i, t)
# T33
for i, t in [(0, "Große, für alle."), (1, "Frisch."), (2, "Super."),
             (3, "Gemütlich."), (4, "Dicke."), (5, "Bitte melden?"), (6, "Wirklich nur das."),
             (7, "Nur der."), (8, "Nur die."), (9, "Oder?"), (10, "Freitag?"),
             (11, "Wirklich, los!"), (12, "Sehr!"), (13, "Bis Freitag!"), (14, "Bis dann!"), (15, "Bitte!")]:
    ext(33, i, t)
# T34
for i, t in [(0, "Plötzlich."), (1, "Wirklich."), (2, "Schatz?"),
             (3, "Leider."), (4, "Gott sei Dank."), (5, "Alles gut."), (6, "Bitte melden?"),
             (7, "Nur das."), (8, "Nur die."), (9, "Nur das!"), (10, "Hurra."),
             (11, "Alle?"), (12, "Bitte!"), (13, "Tschüss!"), (14, "Euch auch!"), (15, "Bis bald!")]:
    ext(34, i, t)
# T36
for i, t in [(0, "Toll."), (1, "Wirklich."), (2, "Sehr."),
             (3, "Schön."), (4, "Interessant."), (5, "Bitte melden?"), (6, "Wirklich nur das."),
             (7, "Nur das."), (8, "Nur die."), (9, "Nur die."), (10, "Pünktlich?"),
             (11, "Bis dann!"), (12, "Allen!"), (13, "Bis morgen!"), (14, "Tschüss!")]:
    ext(36, i, t)

print("top-up C applied")
