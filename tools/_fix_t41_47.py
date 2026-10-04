#!/usr/bin/env python3
"""Top-up pass for tests 41-47 (same W counter as _expand scripts)."""
import json
from pathlib import Path

TOOLS = Path(__file__).resolve().parent


def load(n):
    p = TOOLS / f"_test{n}_data.json"
    return p, json.loads(p.read_text(encoding="utf-8"))


def save(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def L(speaker, gender, text):
    return {"speaker": speaker, "gender": gender, "text": text}


def pad_t1(n, idx, extra):
    p, d = load(n)
    d["teile"][0]["items"][idx]["transcript"] += " " + extra
    save(p, d)


def add_turn(n, teil, item, line):
    p, d = load(n)
    if teil == 2:
        d["teile"][1]["lines"].append(line)
    else:
        d["teile"][2]["items"][item]["lines"].append(line)
    save(p, d)


def extend_turn(n, teil, item, turn, extra):
    p, d = load(n)
    if teil == 2:
        d["teile"][1]["lines"][turn]["text"] += " " + extra
    else:
        d["teile"][2]["items"][item]["lines"][turn]["text"] += " " + extra
    save(p, d)


# #41
pad_t1(41, 0, "Bitte bleiben Sie im Hotel und warten Sie auf morgen.")
pad_t1(41, 2, "Fahren Sie bitte nur mit Helm und langsam.")
add_turn(41, 3, 3, L("Skifahrer2", "m", "Einverstanden! Bis später am Lift, viel Spaß!"))
# #42
pad_t1(42, 2, "Parkplätze gibt es hinter dem Restaurant.")
# #43
pad_t1(43, 3, "Danke für Ihr Verständnis!")
extend_turn(43, 2, None, 13, "Nächste Woche Samstag um zehn bei mir.")
add_turn(43, 3, 0, L("Kundin", "f", "Gut, dann tanke ich Super. Mit Karte, bitte, und tschüss!"))
extend_turn(43, 3, 1, 4, "Ich freue mich schon!")
# #44
pad_t1(44, 2, "Bei Fragen rufen Sie bitte im Sekretariat an.")
extend_turn(44, 2, None, 13, "Ich bringe Chips und Getränke mit.")
extend_turn(44, 2, None, 11, "beim Grillen")
add_turn(44, 2, None, L("Anna", "f", "Super! Ich freue mich schon auf Samstag!"))
extend_turn(44, 3, 0, 4, "für Samstag")
extend_turn(44, 3, 1, 5, "Du wirst sehen, es macht Spaß!")
# #45
pad_t1(45, 0, "Vielen Dank für Ihren Besuch!")
pad_t1(45, 3, "Wir sehen uns morgen!")
extend_turn(45, 2, None, 13, "Und danach trinken wir Kaffee im Museums-Café.")
extend_turn(45, 2, None, 12, "Das wird ein langer Tag.")
extend_turn(45, 3, 0, 1, "auch nicht am Sonntag")
extend_turn(45, 3, 1, 4, "Sport ist gesund,")
extend_turn(45, 3, 2, 4, "es gibt viel zu sehen!")
extend_turn(45, 3, 3, 4, "Wo geht es los?")
# #46
pad_t1(46, 0, "Bitte beeilen Sie sich ein bisschen.")
extend_turn(46, 2, None, 1, "Er freut sich schon sehr darauf.")
extend_turn(46, 2, None, 5, "Er bleibt das ganze Wochenende dort.")
extend_turn(46, 2, None, 9, "Er nimmt den ICE am Morgen.")
extend_turn(46, 2, None, 13, "Ich kaufe Chips dazu.")
extend_turn(46, 3, 0, 0, "für morgen")
extend_turn(46, 3, 0, 3, "viel billiger")
extend_turn(46, 3, 0, 4, "Auf Wiedersehen!")
extend_turn(46, 3, 1, 4, "für die Auskunft!")
extend_turn(46, 3, 3, 4, "Bis später!")
# #47
pad_t1(47, 1, "Das Angebot gilt nur diese Woche.")
pad_t1(47, 3, "Vielen Dank für Ihre Aufmerksamkeit!")
extend_turn(47, 2, None, 13, "Bis später am Abend!")
extend_turn(47, 3, 0, 3, "und Garantie")
extend_turn(47, 3, 1, 4, "Danke, Mama!")
extend_turn(47, 3, 3, 4, "und der Rücken auch!")

print("top-up applied")
