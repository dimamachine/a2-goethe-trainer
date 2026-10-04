#!/usr/bin/env python3
"""Top-up for direct-speech batch F3. Self-reinforcing tails only."""
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
 89: [(0, "Schon beschriftet!"), (1, "Die Treppe runter!"), (2, "Kein Problem!"),
      (3, "Mit Werkzeug!"), (4, "Für alle!"), (11, "Mit Handschuhen!"),
      (15, "Unbedingt vorsichtig!"), (5, "Bitte melden?"), (6, "Wirklich nur das!")],
 90: [(0, "Rot schnell!"), (1, "Blau bequem!"), (2, "Für den Winter!"),
      (3, "Braun fest!"), (4, "Für den Verein!"), (11, "Mit Beratung!"),
      (15, "Unbedingt aufheben!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (9, "Nur meine!"), (10, "Nur meiner!"), (7, "Bleibe dabei!"),
      (8, "Nur meine!"), (14, "Pünktlich da!")],
 91: [(0, "Nachts schlimm!"), (1, "Seit gestern!"), (2, "Nach der Arbeit!"),
      (3, "Kleiner Sturz!"), (4, "Jeden Tag!"), (11, "Mit Rezept!"),
      (15, "Unbedingt lesen!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (9, "Nur meine!"), (10, "Nur meiner!"), (7, "Bleibe dabei!")],
 92: [(0, "Dunkel und lecker, wunderbar!"), (1, "Fruchtig und frisch, toll!"),
      (2, "Klassisch mit Sahne!"), (3, "Sauer und frisch!"), (4, "Nussig und grün!"),
      (11, "Einverstanden gern!"), (15, "Gleiche Zeit morgen!"), (5, "Bitte melden?"),
      (6, "Wirklich nur die!"), (9, "Nur meine!"), (10, "Nur meiner!"),
      (7, "Bleibe dabei!"), (8, "Nur meine!")],
 93: [(0, "Routine wichtig!"), (1, "Hoch leider!"), (2, "Alles normal!"),
      (3, "Juckt leider!"), (4, "Weint viel!"), (11, "Mit Spielzeug!"),
      (15, "Unbedingt dabei!"), (5, "Bitte melden?"), (6, "Wirklich nur das!"),
      (9, "Nur unsere!"), (10, "Nur unsere!"), (7, "Bleibe dabei!"), (8, "Nur meine!")],
 94: [(0, "Voll Super!"), (1, "Glänzend sauber!"), (2, "Für Urlaub wichtig!"),
      (3, "Für unterwegs!"), (4, "Beides schnell!"), (11, "Getankt und fertig!"),
      (15, "Fürs Fahrtenbuch!"), (5, "Bitte melden?"), (6, "Wirklich nur das!"),
      (9, "Nur meiner!"), (10, "Nur meiner!")],
 95: [(0, "Nach dem Schlamm!"), (1, "Für den Sommer!"), (2, "Auf dem Boden!"),
      (3, "Jeden Tag!"), (4, "Sanft und gut!"), (11, "Mit Hunden!"),
      (15, "Unbedingt mitnehmen!"), (5, "Bitte melden?"), (6, "Wirklich nur der!"),
      (9, "Nur unsere!")],
 96: [(0, "Weiß und rosa!"), (1, "Bunt gemischt!"), (2, "Grün und leicht!"),
      (3, "Bei Nachbarin lieb!"), (4, "Ruhig und würdevoll!"), (15, "Frisch halten!")],
 97: [(0, "Zu lang leider!"), (1, "Perfekt sitzen!"), (2, "An der Jacke!"),
      (3, "Fast unsichtbar!"), (4, "Am Mantel!"), (11, "Mit Zetteln!"),
      (15, "Geduld haben!"), (5, "Bitte melden?"), (6, "Wirklich nur das!"),
      (9, "Nur meiner!"), (10, "Nur meiner!"), (7, "Bleibe dabei!")],
 98: [(0, "Heiß und gut!"), (1, "Eine Stunde!"), (2, "Am Morgen!"),
      (3, "Frisch und rosig!"), (4, "Entspannt toll!"), (11, "Im Restaurant!"),
      (15, "Unbedingt mitnehmen!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (9, "Nur meine!"), (10, "Nur meiner!"), (7, "Bleibe dabei!")],
 99: [(0, "Fließend üben!"), (1, "Für den Urlaub!"), (2, "Schwierig gut!"),
      (3, "Mit Liedern!"), (4, "Wichtig sehr!")],
 100: [(0, "In München!"), (1, "Ab August!"), (2, "Ein Jahr!"),
      (3, "Erst mal!"), (4, "Helfen gern!"), (11, "Mit Eltern!"),
      (15, "Unbedingt so!"), (5, "Bitte melden?"), (6, "Wirklich nur die!")],
}

for n, jobs in JOBS.items():
    for idx, t in jobs:
        ext(n, idx, t)

print("top-up F3 applied")
