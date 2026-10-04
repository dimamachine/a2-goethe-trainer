#!/usr/bin/env python3
"""Top-up for direct-speech batch F2. Self-reinforcing tails only."""
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
 77: [(0, "Anzeige wichtig!"), (1, "Mit Fotos!"), (2, "Viel Geld!"),
      (3, "Nachts laut!"), (4, "Vor dem Urlaub!"), (11, "Im Café!"),
      (15, "Unbedingt wachsam!")],
 78: [(0, "Heiße Rhythmen!"), (1, "Mit meinem Mann!"), (2, "Mit den Jüngeren!"),
      (3, "Begeistert sehr!"), (4, "Reicht mir völlig!"), (11, "Mit Musik!"),
      (15, "Glatte Sohle!"), (5, "Bitte melden?"), (6, "Wirklich nur der!"),
      (9, "Nur meine!"), (10, "Nur meiner!"), (7, "Bleibe dabei!")],
 79: [(0, "Neue Stelle!"), (1, "Mit allem!"), (2, "So süß klein!"),
      (3, "Dringend nötig!"), (4, "Sitzt still!"), (11, "Mit Kaffee danach!"),
      (15, "Beste Seite!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (9, "Nur meiner!"), (10, "Nur meiner!"), (7, "Bleibe dabei!")],
 80: [(0, "Viel laufen!"), (1, "Schick elegant!"), (2, "Fest und gut!"),
      (3, "Bequem weich!"), (4, "Pflicht wichtig!"), (11, "Vorm Geschäft!"),
      (15, "Unbedingt notieren!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (7, "Bleibe dabei!"), (8, "Nur meine!"), (9, "Nur meine!"),
      (10, "Nur meiner!"), (14, "Pünktlich da!"), (12, "Uns allen!")],
 81: [(0, "Spanisch lernen!"), (1, "Lecker italienisch!"), (2, "Nützlich sehr!"),
      (3, "Kreativ malen!"), (4, "Super entspannt!"), (11, "Mit Anmeldeformular!"),
      (15, "Kursgebühr zahlen!"), (5, "Bitte melden?"), (6, "Wirklich nur das!"),
      (9, "Nur meine!"), (10, "Nur meiner!"), (7, "Bleibe dabei!"),
      (8, "Nur meine!"), (14, "Pünktlich da!")],
 82: [(0, "Billig und wendig!"), (1, "Am Wochenende!"), (2, "Im Sommer!"),
      (3, "Gepäck viel!"), (4, "Freiheit toll!"), (11, "Mit Führerschein!"),
      (15, "Unbedingt voll!"), (5, "Bitte melden?"), (6, "Wirklich nur der!"),
      (9, "Nur meiner!")],
 83: [(0, "Nervig sehr!"), (1, "Juckt sehr!"), (2, "Routine jährlich!"),
      (3, "Creme viel!"), (4, "Rot und heiß!"), (11, "Mit Zeitschriften!"),
      (15, "Wirklich nicht kratzen!"), (5, "Bitte melden?"), (6, "Wirklich nur der!"),
      (9, "Nur meine!"), (10, "Nur meiner!"), (7, "Bleibe dabei!"),
      (8, "Nur meine!"), (14, "Daumen drücken!")],
 84: [(0, "Zu Fuß gern!"), (1, "Den ganzen Tag!"), (2, "Eine Stunde!"),
      (3, "Tolle Sicht!"), (4, "Lecker essen!"), (11, "Mit Fotos!"),
      (15, "Unbedingt mitnehmen!"), (5, "Bitte melden?"), (6, "Wirklich nur das!")],
 85: [(0, "Seit einem Jahr!"), (1, "Jeden Tag!"), (2, "Mit Band!"),
      (3, "Wunderschön!"), (4, "Toll laut!"), (11, "Mit Noten!"),
      (15, "Unbedingt stimmen!"), (5, "Bitte melden?"), (6, "Wirklich nur das!"),
      (9, "Nur meine!"), (10, "Nur meiner!"), (7, "Bleibe dabei!"),
      (8, "Nur meine!"), (12, "Uns allen!"), (13, "Zusammen!"),
      (14, "Pünktlich da!"), (3, "Im Orchester schön!"), (4, "Jazz toll!"), (0, "Gern laut!")],
 86: [(0, "Im Büro viel!"), (1, "Seit letzter Woche!"), (2, "Nach dem Umzug!"),
      (3, "Vom Kissen wohl!"), (4, "Beim Laufen!"), (11, "Zehn Minuten!"),
      (15, "Unbedingt einhalten!"), (5, "Bitte melden?"), (6, "Wirklich nur das!"),
      (9, "Nur meiner!"), (10, "Nur meiner!"), (7, "Bleibe dabei!"), (8, "Nur meine!")],
 87: [(0, "Mit Schienen lang!"), (1, "Für meine Nichte!"), (2, "Für meinen Sohn!"),
      (3, "Lustig spielen!"), (4, "Zum Liebhaben weich!"), (11, "Mit Geschenkpapier!"),
      (15, "Unbedingt aufheben!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (9, "Nur meiner!")],
 88: [(0, "Jacke und Hose!"), (1, "Drei Romane!"), (2, "Kabellos gut!"),
      (3, "Regal und Stuhl!"), (4, "Frisch geliefert!"), (11, "Morgen zur Post!"),
      (15, "Online anmelden!"), (5, "Bitte melden?"), (6, "Wirklich nur die!"),
      (9, "Nur meine!"), (10, "Nur meiner!"), (7, "Bleibe dabei!")],
}

for n, jobs in JOBS.items():
    for idx, t in jobs:
        ext(n, idx, t)

print("top-up F2 applied")
