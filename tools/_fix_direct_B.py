#!/usr/bin/env python3
"""Top-up for direct-speech batch B (same W counter). All neutral, no assignments."""
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


# T13
for i, t in [(0, "Bequem und schnell."), (1, "Ganz umweltfreundlich."), (2, "Billig gefunden."),
             (3, "Egal, wirklich."), (4, "Ganz nah."), (5, "Von uns allen?"), (6, "Viel zu teuer."),
             (7, "Viel zu weit."), (8, "Wirklich alles."), (9, "Am Freitag schon?"), (10, "Ja, gern."),
             (12, "Bitte!"), (13, "Hoffentlich!")]:
    ext(13, i, t)
add(13, L("Tom", "m", "Noch etwas: Handys aufladen, ganz wichtig!"))
add(13, L("Lisa", "f", "Stimmt! Und Tickets ausdrucken, einverstanden?"))
# T14
for i, t in [(0, "Im Zentrum."), (1, "Wunderbar."), (2, "Gern geschehen."), (3, "Für alle gern."),
             (4, "Wirklich gern."), (5, "Bisher nicht."), (6, "Wirklich keiner."), (7, "Leider nein."),
             (8, "Wirklich nur das."), (9, "Alles organisiert."), (10, "Super Idee."), (11, "Pünktlich!"),
             (12, "Tschüss!"), (13, "Hurra!")]:
    ext(14, i, t)
add(14, L("Tante Eva", "f", "Noch etwas: Blumen besorgen wir morgen, einverstanden?"))
add(14, L("Mama", "f", "Einverstanden! Rote Rosen für Oma, schön!"))
# T16
for i, t in [(0, "Wie immer gern."), (1, "Hausgemacht lecker."), (2, "Heute frisch."), (3, "Sehr gesund."),
             (4, "Unbedingt nötig."), (5, "Jemand bitte?"), (6, "Wirklich nicht."), (7, "Ganz allein."),
             (8, "Leider nein."), (9, "Leider auch nicht."), (10, "Genug daheim."), (11, "Genau um eins?"),
             (12, "Tschüss!"), (13, "Wirklich schon!"), (14, "Unbedingt mitbringen!"), (15, "Wirklich einverstanden?")]:
    ext(16, i, t)
# T18
for i, t in [(0, "Ganz modern."), (1, "Dringend nötig."), (2, "Jeden Tag gern."), (3, "Genau richtig."),
             (4, "Ganz dringend."), (5, "Bitte melden!"), (6, "Wirklich nicht."), (7, "Nur für mich."),
             (8, "Digital immer."), (9, "Wirklich digital."), (10, "Leider nein."), (11, "Tschüss!"),
             (12, "Wirklich sehr!"), (13, "Vorfreude überall!"), (14, "Wirklich einverstanden?"), (15, "Ehrlich versprochen?")]:
    ext(18, i, t)
# T20
for i, t in [(0, "Mit viel Spaß."), (1, "Wunderbar schön."), (2, "Tolle Sprache."), (3, "Sehr spannend."),
             (4, "Wirklich schwer."), (5, "Bitte melden!"), (6, "Wirklich nur das."), (7, "Nichts anderes."),
             (8, "Schon lange."), (9, "Wirklich gern."), (10, "Gern zusammen."), (11, "Diesen Freitag?"),
             (12, "Sehr gern."), (13, "Allen zusammen!"), (14, "Ganz wichtig!"), (15, "Ja, gern!")]:
    ext(20, i, t)
# T21
for i, t in [(0, "Fahre nicht mehr."), (1, "Sehr ärgerlich."), (2, "Total schrecklich."), (3, "Jeden Morgen neu."),
             (4, "Informiert schon."), (5, "Wirklich schrecklich."), (6, "Bei mir okay."), (7, "Batterie nur leer."),
             (8, "Bei mir okay."), (9, "Egal wirklich."), (10, "Pünktlich da!"), (11, "Bis dann!"),
             (12, "Alles gut!"), (13, "Bitte doch!"), (14, "Wirklich danke!"), (15, "Ja, einverstanden!")]:
    ext(21, i, t)
# T22
for i, t in [(0, "Mit Gravur schön."), (1, "Vom Sommer her."), (2, "Aus Italien gut."), (3, "Im Sommer schön."),
             (4, "Zusammen gern."), (5, "Bitte melden!"), (6, "Nur meins!"), (7, "Nur meins!"),
             (8, "Wirklich meins."), (9, "Nur meine!"), (10, "Freust du dich?"), (11, "Bis gleich!"),
             (12, "Freue mich!"), (13, "Zusammen tschüss!"), (14, "Zusammen unterschreiben!"), (15, "Viele Grüße!")]:
    ext(22, i, t)
# T24
for i, t in [(0, "Gern zusammen?"), (5, "Wirklich aktiv!"), (10, "Wirklich alle?"), (14, "Bis gleich!")]:
    ext(24, i, t)
# T25
for i, t in [(0, "Total spannend."), (1, "Sehr lehrreich."), (2, "Zum Träumen schön."), (3, "Wirklich cool."),
             (4, "Vor dem Schlafen."), (5, "Bitte melden!"), (6, "Wirklich nur das."), (7, "Nur meine!"),
             (8, "Nur meins!"), (9, "Bei Märchen!"), (10, "Zu Hause gern?"), (11, "Tschüss!"),
             (12, "Versprochen!"), (13, "Zusammen!"), (14, "Gern tauschen!"), (15, "Bis bald!"),
             (0, "Unbedingt lesen!"), (5, "Alle lesen!")]:
    ext(25, i, t)

print("top-up B applied")
