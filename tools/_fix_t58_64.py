#!/usr/bin/env python3
"""Top-up pass for tests 58-64 (same W counter as _expand scripts)."""
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


def add_turn(n, item, line):
    p, d = load(n)
    d["teile"][1]["lines"].append(line)
    save(p, d)


def add_t3_turn(n, item, line):
    p, d = load(n)
    d["teile"][2]["items"][item]["lines"].append(line)
    save(p, d)


def extend_turn(n, turn, extra):
    p, d = load(n)
    d["teile"][1]["lines"][turn]["text"] += " " + extra
    save(p, d)


def extend_t3(n, item, turn, extra):
    p, d = load(n)
    d["teile"][2]["items"][item]["lines"][turn]["text"] += " " + extra
    save(p, d)


def extend_t4(n, turn, extra):
    p, d = load(n)
    d["teile"][3]["transcript"][turn]["text"] += " " + extra
    save(p, d)


# ---- T1 ----
pad_t1(59, 0, "Kommen Sie vorbei, wir beraten gern!")
pad_t1(59, 4, "Fragen Sie uns, wir helfen gern!")
pad_t1(61, 2, "Vielen Dank für Ihr Verständnis und viel Spaß beim Training!")
pad_t1(61, 4, "Rufen Sie an oder kommen Sie vorbei, wir beraten Sie gern!")

# ---- T2 closers ----
add_turn(58, None, L("Anna", "f", "Dann buche ich uns gleich Termine für Samstag, einverstanden?"))
add_turn(58, None, L("Markus", "m", "Einverstanden! Samstag um elf, ich freue mich schon!"))
extend_turn(59, 1, "und billig.")
add_turn(59, None, L("Anna", "f", "Interessant! Und du bleibst bei deiner Frisur, wirklich?"))
add_turn(59, None, L("Markus", "m", "Ja, wirklich! Aber dich begleite ich zum Barbier, einverstanden?"))
extend_turn(59, 9, "Sieht cool aus, finde ich.")
extend_turn(59, 11, "und zu teuer.")
add_turn(60, None, L("Anna", "f", "Toll! Dann sehen wir uns Samstag im Park, einverstanden?"))
add_turn(60, None, L("Markus", "m", "Einverstanden! Ich bringe Decke und Brote mit, du Getränke!"))
add_turn(61, None, L("Anna", "f", "Super! Dann komme ich Montag zum Training, einverstanden?"))
add_turn(61, None, L("Markus", "m", "Einverstanden! Um 18 Uhr an der Rezeption, bis dann!"))
add_turn(62, None, L("Anna", "f", "Perfekt! Bis Samstag um neun am Eingang!"))
add_turn(64, None, L("Anna", "f", "Schön! Und unsere Reise buchen wir heute Abend, einverstanden?"))
add_turn(64, None, L("Markus", "m", "Einverstanden! Ich hole die Kataloge, du machst Kaffee!"))

# ---- T3 ----
# 58
extend_t3(58, 1, 1, "ganz schnell.")
extend_t3(58, 1, 3, "heute")
add_t3_turn(58, 1, L("Barbier", "m", "Gern! Nehmen Sie Platz, es geht sofort los!"))
extend_t3(58, 3, 3, "am Nachmittag.")
extend_t3(58, 3, 4, "und tschüss!")
add_t3_turn(58, 4, L("Friseur", "m", "Danke schön! Und bis zum nächsten Mal in vier Wochen!"))
# 59
extend_t3(59, 0, 1, "ganze")
extend_t3(59, 0, 3, "bitte")
extend_t3(59, 0, 4, "Vielen Dank!")
add_t3_turn(59, 0, L("Barbier", "m", "So, fertig! Sehen Sie gut aus, bis zum nächsten Mal!"))
extend_t3(59, 1, 1, "nächste Woche!")
extend_t3(59, 1, 4, "Mama!")
extend_t3(59, 2, 0, "wirklich!")
extend_t3(59, 2, 4, "am Abend?")
extend_t3(59, 3, 1, "im Buch.")
extend_t3(59, 3, 4, "wie Freitag?")
extend_t3(59, 3, 5, "tschüss!")
# 60
extend_t3(60, 1, 4, "Mama?")
extend_t3(60, 2, 4, "und tschüss!")
extend_t3(60, 3, 1, "mein Schatz?")
extend_t3(60, 3, 3, "heute.")
extend_t3(60, 4, 0, "oder?")
extend_t3(60, 4, 1, "so ist es.")
extend_t3(60, 4, 3, "im Frühling.")
extend_t3(60, 4, 4, "schönen Abend!")
add_t3_turn(60, 4, L("Wächter", "m", "Gern! Und kommen Sie morgen wieder, bei schönem Wetter!"))
# 61
extend_t3(61, 0, 1, "pro Monat.")
extend_t3(61, 0, 3, "heute")
extend_t3(61, 0, 4, "Ab wann gilt er?")
extend_t3(61, 1, 3, "hier.")
extend_t3(61, 1, 4, "und tschüss!")
# 62
extend_t3(62, 0, 3, "Schönes?")
extend_t3(62, 0, 4, "für heute.")
add_t3_turn(62, 0, L("Kundin", "f", "Ach ja, noch ein Bund Petersilie dazu, bitte!"))
extend_t3(62, 1, 1, "sehr lecker!")
extend_t3(62, 1, 4, "Danke!")
extend_t3(62, 4, 1, "oder?")
extend_t3(62, 4, 4, "heute.")
# 63
extend_t3(63, 1, 2, "wirklich?")
extend_t3(63, 1, 4, "Wann kann ich kommen?")
extend_t3(63, 2, 4, "im Café.")
# 64
extend_t3(64, 0, 2, "Geld.")
extend_t3(64, 0, 4, "So ist es.")
extend_t3(64, 1, 1, "im Preis.")
extend_t3(64, 1, 3, "und Person.")
extend_t3(64, 1, 4, "völlig aus.")
extend_t3(64, 2, 2, "dort")
extend_t3(64, 2, 3, "und einfach.")
extend_t3(64, 2, 4, "tschüss!")
extend_t3(64, 3, 1, "geht es los.")
extend_t3(64, 3, 3, "Überlegen Sie es sich.")
extend_t3(64, 3, 4, "schön!")

# ---- T4 ----
# 60 Walter
extend_t4(60, 1, "Im Winter sind wir weniger Leute.")
extend_t4(60, 3, "Am Sonntag kommen die meisten.")
extend_t4(60, 5, "Wir stellen mehr Eimer auf.")
extend_t4(60, 7, "Alle dürfen mitmachen, auch Kinder.")
extend_t4(60, 9, "Grün ist gesund für alle.")
# 62 Hofer
extend_t4(62, 1, "Keine Chemie, alles natürlich.")
extend_t4(62, 3, "pünktlich um sieben geht es los.")
extend_t4(62, 5, "Das schmeckt man sofort.")
extend_t4(62, 7, "Der Hof allein reicht nicht zum Leben.")
extend_t4(62, 9, "Das freut mich sehr.")
# 63 Wolf
extend_t4(63, 0, "Schon lange, oder?")
extend_t4(63, 1, "Ich lerne jeden Tag etwas Neues.")
extend_t4(63, 2, "Bremsen oder Motor?")
extend_t4(63, 5, "Das geht schnell.")
extend_t4(63, 7, "da warte ich nicht lange.")
extend_t4(63, 8, "Haben Sie Tipps?")
extend_t4(63, 11, "und dauert lange.")
extend_t4(63, 13, "seit zwanzig Jahren.")
# 64 Sommer
extend_t4(64, 0, "Ist Internet nicht billiger?")
extend_t4(64, 1, "der alles kennt und ehrlich berät.")
extend_t4(64, 2, "Wohin fahren die Deutschen?")
extend_t4(64, 5, "Die Leute wollen wieder weit weg.")
extend_t4(64, 7, "Das sage ich allen Kunden.")
extend_t4(64, 9, "kein Stress.")
extend_t4(64, 11, "Zwei Koffer braucht kein Mensch.")

print("top-up 58-64 applied")
