#!/usr/bin/env python3
"""Top-up for direct-speech batch A (same W counter)."""
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


def ext(n, idx, extra):
    p, d = load(n)
    d["teile"][1]["lines"][idx]["text"] += " " + extra
    save(p, d)


def add(n, line):
    p, d = load(n)
    d["teile"][1]["lines"].append(line)
    save(p, d)


# T1 +3
ext(1, 14, "Pünktlich um neun!")
# T4 +17
ext(4, 1, "Wirklich gut.")
ext(4, 5, "Für die Pause?")
add(4, L("Tobias", "m", "Alles klar! Dann lernen wir morgen alles zusammen, einverstanden?"))
# T5 +10 (152->162)
ext(5, 13, "Ganz sicher!")
add(5, L("Anna", "f", "Genau! Danke euch allen, ihr seid super!"))
# T6 +35
ext(6, 0, "Dringend nötig.")
ext(6, 2, "Herrlich.")
ext(6, 4, "Wirklich.")
ext(6, 5, "Jemand?")
ext(6, 7, "Oder nicht?")
ext(6, 9, "Von uns?")
ext(6, 10, "Nichts anderes.")
ext(6, 12, "Gemütlich.")
ext(6, 13, "Schon sehr!")
add(6, L("Mama", "f", "Noch etwas: Nach dem Wellness trinken wir Kaffee zusammen, einverstanden?"))
add(6, L("Papa", "m", "Einverstanden! Kaffee und Kuchen nach der Sauna, perfekt!"))
# T7 +25
ext(7, 1, "Super.")
ext(7, 2, "Lecker.")
ext(7, 3, "Versprochen.")
ext(7, 4, "Günstig und gut.")
ext(7, 13, "Tschüss!")
add(7, L("Lisa", "f", "Alles klar! Dann feiern wir Freitag alle zusammen, einverstanden?"))
add(7, L("Tanja", "f", "Einverstanden! Es wird die beste Feier des Sommers!"))
# T8 +33
ext(8, 0, "Mit Seeblick.")
ext(8, 1, "Für alle.")
ext(8, 2, "Ist organisiert.")
ext(8, 3, "Viel günstiger.")
ext(8, 4, "Wirklich.")
ext(8, 8, "Nein.")
ext(8, 10, "Pünktlich um sieben?")
ext(8, 11, "Bis Samstag!")
ext(8, 12, "Schon sehr!")
ext(8, 13, "Super!")
add(8, L("Mama", "f", "Noch etwas: Badesachen nicht vergessen, für den See!"))
add(8, L("Papa", "m", "Stimmt! Und Sonnencreme auch, ganz wichtig!"))
# T10 +31
ext(10, 0, "Schöne bunte.")
ext(10, 1, "An der Ecke.")
ext(10, 2, "Ganz frisch.")
ext(10, 3, "Super.")
ext(10, 4, "Wirklich.")
ext(10, 10, "Oder?")
ext(10, 12, "Um sieben?")
add(10, L("Anna", "f", "Noch etwas: Bringt gute Laune mit, ganz viel!"))
add(10, L("Markus", "m", "Immer! Und Hunger mitbringen, es gibt viel Essen!"))
# T11 +19
ext(11, 4, "Sehr gern.")
ext(11, 13, "Zusammen!")
add(11, L("Vater", "m", "Noch etwas: Pässe nicht vergessen, ganz wichtig!"))
add(11, L("Mutter", "f", "Stimmt! Und die Tickets auch, alles einpacken!"))
# T12 +22
ext(12, 0, "Morgens und abends.")
ext(12, 4, "Pünktlich.")
ext(12, 10, "Wirklich nicht!")
add(12, L("Mutter", "f", "Noch etwas: Ruf an, wenn etwas ist, ja?"))
add(12, L("Lisa", "f", "Klar, ich rufe jeden Tag an, versprochen!"))

print("top-up A applied")
