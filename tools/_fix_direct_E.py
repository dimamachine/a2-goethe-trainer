#!/usr/bin/env python3
"""Top-up for direct-speech batch E. Self-reinforcing tails only."""
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
 48: [(0, "Würstchen und Steaks lecker!"), (1, "Zwei Kästen voll!"), (2, "Noch warm frisch!"),
      (3, "Paprika rot!"), (4, "Eis kalt!"), (15, "Jeder seine eigenen!")],
 49: [(0, "Mit der Klasse schön!"), (1, "Musik wunderbar!"), (2, "Mit Freunden lustig!"),
      (3, "Mit Mutter gern!"), (4, "Freue mich riesig!"), (15, "Gut aufpassen wirklich!")],
 50: [(0, "Sehr lieb brav!"), (1, "Schläft viel!"), (2, "Mit Rad schnell!"),
      (3, "Bunt und ruhig!"), (4, "Hallo und Tschüss lustig!"), (15, "Für alle Tiere gern!")],
 51: [(0, "Seit letztem Jahr schon!"), (1, "Beim Sport super!"), (2, "Abends am Sofa!"),
      (3, "Sommer und Winter!"), (4, "Laser bald!"), (11, "In der Stadt zentral!"),
      (15, "Unbedingt mitnehmen!"), (5, "Bitte melden gern!")],
 52: [(0, "Heiß und gut!"), (1, "Ausdauer pur!"), (2, "Immer wieder!"),
      (3, "Mutig und toll!"), (4, "Warm gemütlich!"), (11, "Mit Badesachen!"),
      (15, "Zwei Stück unbedingt!"), (5, "Bitte melden gern!")],
 53: [(0, "Den ganzen Abend lang!"), (1, "Für die Tische schön!"), (2, "Den ganzen Tag!"),
      (3, "Mit Erdbeeren süß!"), (4, "Lustig und kurz!"), (15, "Unbedingt fröhlich!"),
      (5, "Bitte melden gern!")],
 54: [(0, "Klassisch schick!"), (1, "Leicht und modern!"), (2, "Steht mir gut!"),
      (3, "Mutig und lustig!"), (4, "Cool und groß!"), (11, "Um vier Uhr!"),
      (15, "Unbedingt dabei!"), (5, "Bitte melden gern!")],
 55: [(0, "Schon immer treu!"), (1, "Stimmung super!"), (2, "Seit Kindheit treu!"),
      (3, "Meine Stadt stolz!"), (4, "Für immer treu!"), (11, "Bei mir daheim!"),
      (15, "Jeder eine Tüte!"), (5, "Bitte melden gern!")],
 56: [(0, "Zwei Stück frisch!"), (1, "Warm und weich!"), (2, "Ein ganzes Leib!"),
      (3, "Zum Kaffee süß!"), (4, "Zwei Stück süß!"), (5, "Bitte melden gern!"),
      (6, "Wirklich nur die!"), (7, "Bleibe dabei gern!"), (8, "Nur meine!"),
      (9, "Nur meine!"), (10, "Nur meine!"), (11, "Wirklich gern!"),
      (12, "Weiterhin gern!"), (15, "Gleiche Zeit gern!")],
 57: [(0, "Zentral und billig!"), (1, "Ruhig allein!"), (2, "Für uns fünf!"),
      (3, "Hell und modern!"), (4, "Für immer fest!"), (11, "In die Gruppe schnell!"),
      (15, "Morgen früh gern!"), (5, "Bitte melden gern!")],
 58: [(0, "Mit Klinge scharf!"), (1, "Gepflegte Hände!"), (2, "Jede Woche fest!"),
      (3, "Jeden Monat!"), (4, "Gepflegte Füße!"), (11, "Mit Kuchen süß!"),
      (15, "Unbedingt ehrlich!"), (5, "Bitte melden gern!"), (6, "Wirklich nur die!"),
      (9, "Nur meine!")],
 59: [(0, "Selbst rasiert glatt!"), (1, "Hoch und stark!"), (2, "Lang und klassisch!"),
      (3, "Modisch praktisch!"), (4, "Oben länger!"), (11, "Um sieben Uhr!"),
      (15, "Alle zusammen gern!"), (5, "Bitte melden gern!"), (6, "Wirklich nur der!")],
 60: [(0, "Jeden Tag fit!"), (1, "Mit Familie schön!"), (2, "Ruhig lesen!"),
      (3, "Essen lecker!"), (4, "Jeden Sonntag!"), (11, "Mit Decke weich!"),
      (15, "Hoffentlich Sonne!"), (5, "Bitte melden gern!"), (6, "Wirklich nur das!")],
 61: [(0, "Schwere Gewichte!"), (1, "Mit Musik schnell!"), (2, "Gegen Stress gut!"),
      (3, "Bahnen täglich!"), (4, "Sehr anstrengend!"), (11, "Mit Handtuch trocken!"),
      (15, "Unbedingt trinken!"), (5, "Bitte melden gern!"), (6, "Wirklich nur das!"),
      (7, "Bleibe dabei gern!"), (9, "Nur meine!"), (10, "Nur meine!"),
      (2, "Im Büro entspannt!"), (3, "Im Becken morgens!")],
 62: [(0, "Frisch vom Kutter!"), (1, "Jeden Samstag neu!"), (2, "Verschieden lecker!"),
      (3, "Vom Bauern frisch!"), (4, "Großes Glas voll!"), (11, "Mit Korb praktisch!"),
      (15, "Unbedingt mitnehmen!"), (5, "Bitte melden gern!"), (6, "Wirklich nur die!"),
      (9, "Nur meiner!"), (10, "Nur meiner!"), (2, "Immer gern!")],
 63: [(0, "Morgens nichts los!"), (1, "Nagel drin blöd!"), (2, "Sofort nötig!"),
      (3, "Jeden Morgen!"), (4, "Schrecklich heiß!")],
 64: [(0, "Sonne und Meer!"), (1, "Sieben Tage lang!"), (2, "Alte Gebäude!"),
      (3, "Frische Luft!"), (4, "Großer Traum!"), (11, "Mit allen Bildern!"),
      (15, "Unbedingt einpacken!"), (5, "Bitte melden gern!")],
}

for n, jobs in JOBS.items():
    for idx, t in jobs:
        ext(n, idx, t)

print("top-up E applied")
