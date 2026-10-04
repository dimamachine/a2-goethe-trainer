#!/usr/bin/env python3
"""Top-up for direct-speech batch F1. Self-reinforcing tails only."""
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


JOBS = {
 65: [(0, "Schnell und leicht!"), (1, "Überall dabei!"), (2, "Fürs Wohnzimmer groß!"),
      (3, "Mit viel Zoom!"), (4, "Super Grafik!"), (11, "In die Stadt!"),
      (15, "Unbedingt vergleichen!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (9, "Nur meine!")],
 66: [(0, "Im Bad tropfend!"), (1, "In der Küche dunkel!"), (2, "Neu und hell!"),
      (3, "Klemmt leider!"), (4, "Nach dem Sturm!"), (15, "Genau schauen!"),
      (5, "Bitte melden?")],
 67: [(0, "Groß und laut!"), (1, "Ganz viele!"), (2, "Sehr lustig!"),
      (3, "Ruhig schön!"), (4, "Beeindruckend groß!"), (11, "Mit Jahreskarten!"),
      (15, "Alle mitbringen!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (9, "Nur meine!"), (10, "Nur meine!"), (12, "Uns allen!")],
 68: [(0, "Mit Pommes lecker!"), (1, "Frisch und gesund!"), (2, "Mit Tomatensoße!"),
      (3, "Als Vorspeise!"), (4, "Mit Kartoffeln!"), (11, "Mit Kuchen?"),
      (15, "Gleiche Zeit!"), (5, "Bitte melden?"), (6, "Wirklich nur der!"),
      (7, "Bleibe dabei!"), (8, "Nur meine!"), (9, "Nur meine!"),
      (10, "Nur meine!"), (12, "Ihr Lieben!")],
 69: [(0, "Rot leuchtend!"), (1, "Gestern im Bus!"), (2, "Mit Karten voll!"),
      (3, "Nichts sehen!"), (4, "Haus und Fahrrad!"), (11, "Mit Ausweis!"),
      (15, "Namen drauf!"), (5, "Bitte melden?"), (6, "Wirklich nur das!")],
 70: [(0, "Vollkasko gut!"), (1, "Möbel sicher!"), (2, "Unterwegs sicher!"),
      (3, "Ganz normal!"), (4, "Finde ich wichtig!"), (11, "Ganz genau?"),
      (15, "Ordentlich ablegen!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (7, "Bleibe dabei!"), (8, "Nur meine!"), (9, "Nur meine!"),
      (10, "Nur meine!"), (12, "Ihr Lieben!"), (14, "Gut versichert!")],
 71: [(0, "Fürs Wohnzimmer!"), (1, "Balkon grün!"), (2, "Fürs Regal!"),
      (3, "Modern blau!"), (4, "Schreibtisch hell!"), (11, "Mit Auto!"),
      (15, "Unbedingt aufheben!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (7, "Bleibe dabei!"), (8, "Nur meine!"), (9, "Nur meine!"),
      (10, "Nur meine!"), (14, "Pünktlich da!"), (12, "Uns allen!"), (3, "Bad modern!")],
 72: [(0, "Alles sortiert!"), (1, "Fürs Taschengeld!"), (2, "Gute Erde!"),
      (3, "Mit Beuteln!"), (4, "Regelmäßig hin!"), (11, "Unbedingt mitmachen!"),
      (15, "Alle mitmachen!"), (5, "Bitte melden?"), (6, "Wirklich nur das!"),
      (7, "Bleibe dabei!"), (8, "Aufgabe klar!"), (9, "Nur meiner!"),
      (10, "Nur meiner!"), (12, "Ihr Lieben!"), (14, "Umweltfreundlich!"), (2, "Garten gut!")],
 73: [(0, "Groß und treu!"), (1, "Zum Kuscheln weich!"), (2, "Für die Kinder!"),
      (3, "Fürs Wohnzimmer!"), (4, "Im Käfig klein!"), (11, "Mit Boxen!"),
      (15, "Gleich morgen!"), (5, "Bitte melden?"), (6, "Wirklich nur die!")],
 74: [(0, "Heiß und süß!"), (1, "Viele Tüten!"), (2, "Zwei Stück!"),
      (3, "Wunderschön laut!"), (4, "Juhu hoch!"), (11, "Mit Mützen!"),
      (15, "Unbedingt warm!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (7, "Bleibe dabei!"), (8, "Nur meine!"), (9, "Nur meine!"), (10, "Nur meine!")],
 75: [(0, "Dunkelblau festlich!"), (1, "Für die Feier!"), (2, "Fleck drauf blöd!"),
      (3, "Zum Waschen groß!"), (4, "Fünf Stück weiß!"), (11, "Mit Zetteln!"),
      (15, "Unbedingt aufheben!"), (5, "Bitte melden?"), (6, "Wirklich nur das!"),
      (7, "Bleibe dabei!"), (8, "Nur meine!"), (9, "Nur meine!"),
      (10, "Nur meiner!"), (14, "Pünktlich da!")],
 76: [(0, "Spannend bis zum Ende!"), (1, "Romantisch verträumt!"), (2, "Über Geschichte wahr!"),
      (3, "Zum Nachkochen lecker!"), (4, "Viele Helden bunt!"), (11, "Mit Kuchen süß!"),
      (15, "Gratis dazu!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (7, "Bleibe dabei!"), (8, "Nur meine!"), (9, "Nur meine!"),
      (10, "Nur meine!"), (14, "Viel Spaß!")],
}

for n, jobs in JOBS.items():
    for idx, t in jobs:
        ext(n, idx, t)

print("top-up F1 applied")
