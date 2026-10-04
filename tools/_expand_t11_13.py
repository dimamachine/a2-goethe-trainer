#!/usr/bin/env python3
"""Expand Goethe A2 Hören tests 11-15 (+T1 top-ups 20/24/25). Temporary mutator."""
import json
import re
from pathlib import Path

TOOLS = Path(__file__).resolve().parent


def W(text):
    return len(re.findall(r"[A-Za-zÄÖÜäöüß]+", text))


def L(speaker, gender, text):
    return {"speaker": speaker, "gender": gender, "text": text}


def apply(n, t1=None, t2=None, t3=None, t4=None):
    path = TOOLS / f"_test{n}_data.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    teile = data["teile"]
    if t1:
        for i, text in t1.items():
            teile[0]["items"][i]["transcript"] = text
    if t2:
        teile[1]["lines"] = t2
    if t3:
        for i, lines in enumerate(t3):
            teile[2]["items"][i]["lines"] = lines
    if t4 is not None:
        teile[3]["transcript"] = t4
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    te = data["teile"]
    t1w = [W(it["transcript"]) for it in te[0]["items"]]
    t2w = sum(W(x["text"]) for x in te[1]["lines"])
    t3w = [sum(W(x["text"]) for x in it["lines"]) for it in te[2]["items"]]
    t4w = sum(W(x["text"]) for x in te[3]["transcript"])
    print(f"T{n} T1={t1w} avg={sum(t1w)/5:.0f} T2={t2w}w/{len(te[1]['lines'])}t "
          f"T3={t3w} avg={sum(t3w)/5:.0f} T4={t4w}w")


# ---------------- TEST 11 termine-und-telefon ----------------
apply(11,
      t1={2: "Hier ist der Anrufbeantworter von Doktor Klein. Wir sind im Urlaub bis zum 15. Mai. "
             "Für dringende Notfälle wenden Sie sich an Doktor Weber in der Mozartstraße 18. "
             "Für normale Termine warten Sie bitte bis zur Rückkehr. Bleiben Sie gesund und bis bald! Danke!",
          4: "Anrufbeantworter Tier-Praxis. Wir sind heute am Freitag bis 18 Uhr offen, am Samstag nur Notdienst von 10 bis 12 Uhr. "
             "Sonntag haben wir geschlossen. Wenn Sie einen Termin brauchen, rufen Sie morgen ab 8 Uhr an oder buchen Sie online. "
             "In Notfällen rufen Sie die 112! Vielen Dank für Ihr Verständnis. Danke!"},
      t3=[[L("Anruferin", "f", "Hallo, ich brauche einen Termin bei Dr. Bauer."),
           L("Sekretärin", "f", "Diese Woche oder nächste?"),
           L("Anruferin", "f", "Wenn möglich schon diese Woche."),
           L("Sekretärin", "f", "Heute um 16 Uhr ist noch frei. Oder Freitag um 9 Uhr."),
           L("Anruferin", "f", "Freitag 9 Uhr — am Nachmittag arbeite ich, das passt gut."),
           L("Sekretärin", "f", "Notiert, Freitag 9 Uhr bei Dr. Bauer. Bis dann!")],
          [L("Anrufer", "m", "Hallo, ich möchte einen Tisch reservieren."),
           L("Restaurant", "f", "Wann und für wie viele Personen?"),
           L("Anrufer", "m", "Samstagabend, 8 Personen. Geht das? Oder lieber Sonntag?"),
           L("Restaurant", "f", "Hmm, Samstagabend ist sehr voll. Können Sie Freitag oder Sonntag?"),
           L("Anrufer", "m", "Freitag wäre auch okay. Selbe Uhrzeit, etwa 19 Uhr."),
           L("Restaurant", "f", "Freitag 19 Uhr, 8 Personen, notiert. Wir freuen uns auf Sie!")],
          [L("Frau", "f", "Hallo, mein Mann hat heute einen Termin bei Ihnen — Dr. Schmidt um 14 Uhr. Kann er den verschieben?"),
           L("Sekretärin", "f", "Was ist passiert?"),
           L("Frau", "f", "Sein Auto hat eine Panne, er kommt nicht rechtzeitig."),
           L("Sekretärin", "f", "Wir können ihn um 16 Uhr nehmen. Geht das?"),
           L("Frau", "f", "16 Uhr wäre perfekt, danke. Bis später!"),
           L("Sekretärin", "f", "Gern! 16 Uhr statt 14 Uhr, notiert, tschüss!")],
          [L("Kunde", "m", "Wann ist Ihr Geschäft am Wochenende offen?"),
           L("Verkäuferin", "f", "Samstag von 9 bis 18 Uhr. Sonntag haben wir leider zu."),
           L("Kunde", "m", "Schade, ich kann nur Sonntag. Was kann ich tun?"),
           L("Verkäuferin", "f", "Wir haben einen Online-Shop, da können Sie 24 Stunden bestellen. Lieferung in zwei Tagen."),
           L("Kunde", "m", "Ah gut, dann online. Danke für die Info!")],
          [L("Anruferin", "f", "Hier Mariella. Hör mal, ich wollte fragen, ob wir den Geburtstag schon kommendes Wochenende feiern?"),
           L("Anrufer", "m", "Hmm, kommendes Wochenende ist meine Frau auf Geschäftsreise. Nächsten Monat wäre zu spät."),
           L("Anruferin", "f", "Schade, vielleicht das Wochenende danach?"),
           L("Anrufer", "m", "Das passt besser, ja. Lass uns das machen, ich freue mich!"),
           L("Anruferin", "f", "Ich auch! Das Wochenende danach feiern wir, einverstanden?")]])

# ---------------- TEST 12 tiere-und-haustiere ----------------
apply(12,
      t2=[L("Anna", "f", "Lukas, ich bin nächste Woche im Urlaub und brauche Hilfe mit den Tieren. Lass mich erzählen, wer was macht."),
          L("Lukas", "m", "Klar, erzähl mal. Du hast ja viele Tiere."),
          L("Anna", "f", "Meine Schwester Lisa kommt zweimal am Tag — sie geht mit Bruno spazieren, jeweils 30 Minuten."),
          L("Lukas", "m", "Super, und die Katze?"),
          L("Anna", "f", "Meine Mutter füttert die Katze. Sie wohnt in der Nähe, ein kurzer Weg für sie, zweimal am Tag."),
          L("Lukas", "m", "Und der Kanarienvogel?"),
          L("Anna", "f", "Mein Bruder Tim kümmert sich um den Vogel. Frisches Wasser, Vogelfutter, Käfig sauber machen."),
          L("Lukas", "m", "Und die Fische im Aquarium?"),
          L("Anna", "f", "Mein Vater übernimmt das. Er kennt sich mit Fischen aus, weil er als Kind selbst welche hatte. Das Aquarium ist groß."),
          L("Lukas", "m", "Und was wäre meine Aufgabe?"),
          L("Anna", "f", "Du machst die wichtigste Sache: die Post holen und jeden zweiten Tag nach der Wohnung schauen, ob alles in Ordnung ist."),
          L("Lukas", "m", "Das mache ich gern. Das ist meine Spezialität."),
          L("Anna", "f", "Danke, Lukas! Ohne dich wäre der Urlaub stressig."),
          L("Lukas", "m", "Gern! Grüß die Tiere von mir, und erhol dich gut!")],
      t3=[[L("Verkäufer", "m", "Welches Hundefutter möchten Sie?"),
           L("Kundin", "f", "Mein Hund ist schon alt — 12 Jahre. Kein Babywelpen-Futter mehr nötig."),
           L("Verkäufer", "m", "Für Senior-Hunde haben wir dieses spezielle Futter mit weniger Fett. Oder das normale Futter, aber kleinere Portion."),
           L("Kundin", "f", "Senior-Futter klingt besser, das nehme ich. Danke!"),
           L("Verkäufer", "m", "Gute Wahl! Soll ich es zum Auto tragen? Es ist schwer.")],
          [L("Tierarzt", "m", "Wie geht es Ihrer Katze heute?"),
           L("Besitzerin", "f", "Sie ist noch müde, aber besser als gestern."),
           L("Tierarzt", "m", "Hat sie etwas gefressen?"),
           L("Besitzerin", "f", "Heute Morgen ein bisschen Nassfutter. Trockenfutter mag sie nicht, beides schon gar nicht."),
           L("Tierarzt", "m", "Sehr gut, dass sie wieder frisst. Geben Sie ihr weiter Nassfutter, das ist leichter zu verdauen. In einer Woche kommen Sie wieder.")],
          [L("Anrufer", "m", "Hallo, ich möchte Ihnen meinen Vogel zur Pension geben für eine Woche."),
           L("Mitarbeiterin", "f", "Welche Art Vogel und für welche Woche?"),
           L("Anrufer", "m", "Ein Wellensittich. Vom 10. bis 17. Juni."),
           L("Mitarbeiterin", "f", "Das geht. 15 Euro pro Tag, also 105 Euro für die Woche."),
           L("Anrufer", "m", "Okay, ich bringe ihn am 10. vorbei. Danke, tschüss!"),
           L("Mitarbeiterin", "f", "Bis zum 10. Juni! Bringen Sie Futter mit, bitte!")],
          [L("Nachbar", "m", "Ihr Hund bellt jeden Tag stundenlang, wenn Sie nicht zu Hause sind."),
           L("Hundebesitzerin", "f", "Oh, das tut mir leid. Ich wusste das nicht. Ich ignoriere das nicht, versprochen."),
           L("Nachbar", "m", "Können Sie eine Lösung finden? Vielleicht eine Hundebetreuung tagsüber?"),
           L("Hundebesitzerin", "f", "Gute Idee, ich melde ihn ab Montag bei der Hundeschule an. Weggeben will ich ihn nicht. Danke!"),
           L("Nachbar", "m", "Super, danke! Dann ist es bald ruhig, hoffentlich.")]])

# ---------------- TEST 13 verkehr-und-stadt ----------------
apply(13,
      t1={0: "Achtung an die Fahrgäste der U-Bahn-Linie 4. Wegen Bauarbeiten zwischen Hauptbahnhof und Rathaus fahren wir heute nur bis Hauptbahnhof. "
             "Ein Ersatz-Bus fährt von dort zum Rathaus, alle 10 Minuten. Bitte warten Sie nicht, nehmen Sie den Bus. "
             "Die Linie 7 fährt normal — Sie können auch dort umsteigen. Vielen Dank!",
          1: "Hier ist der Verkehrsfunk. Auf der Stadtautobahn Richtung Süden gibt es einen schweren Unfall. Mindestens 30 Minuten Wartezeit. "
             "Wir empfehlen, über die Bahnhofstraße oder die Münchner Straße auszuweichen. "
             "Auch die Linie 8 der Straßenbahn fährt normal — kein Stau für die. Der Stau dauert noch lange, fahren Sie vorsichtig. Gute Fahrt!",
          2: "Liebe Fahrgäste, der Bus 47 fällt heute ganz aus, wegen Wartungsarbeiten. "
             "Bitte nutzen Sie statt 47 die Linie 23 — die hält direkt nebenan und fährt fast die gleiche Strecke. "
             "Nicht Linie 8 und nicht Linie 7, sondern Linie 23. Morgen läuft die Linie 47 wieder normal. "
             "Wir entschuldigen uns für die Unannehmlichkeiten. Danke!"},
      t2=[L("Tom", "m", "Lisa, wir müssen den Freunden Vorschläge machen, wie sie zur Hochzeit nach Berlin kommen können."),
          L("Lisa", "f", "Genau, jeder hat eine andere Situation. Anna hat schon entschieden — sie kommt mit dem Zug. Das ist für sie am bequemsten."),
          L("Tom", "m", "Und Markus? Er hat doch sein neues Auto."),
          L("Lisa", "f", "Markus fährt mit dem Auto. Er nimmt auch zwei andere mit, also umweltfreundlich."),
          L("Tom", "m", "Und Sara? Sie ist doch immer pragmatisch."),
          L("Lisa", "f", "Sara fliegt — vom Flughafen München direkt nach Berlin-Tegel. Sie hatte schon ein günstiges Ticket gefunden."),
          L("Tom", "m", "Was ist mit Lukas? Er hatte ja diese Reise-App entdeckt."),
          L("Lisa", "f", "Lukas nimmt einen Fernbus. Das ist die billigste Option, aber dauert lange. Er kommt also einen Tag früher."),
          L("Tom", "m", "Und wir? Wir wohnen ja in Berlin selbst."),
          L("Lisa", "f", "Wir gehen einfach zu Fuß zum Standesamt. Es sind nur 15 Minuten von uns. Und du kennst den Weg."),
          L("Tom", "m", "Stimmt, zu Fuß ist die schönste Option."),
          L("Tom", "m", "Toll! Dann kommt jeder anders, wie spannend!"),
          L("Lisa", "f", "Ja, spannend! Und nach der Hochzeit feiern wir alle zusammen!")],
      t3=[[L("Tourist", "m", "Entschuldigung, wie komme ich zum Schloss?"),
           L("Einheimischer", "m", "Mit dem Bus 8 — er fährt direkt hin. Kein Taxi nötig."),
           L("Tourist", "m", "Wie lange dauert es?"),
           L("Einheimischer", "m", "Etwa 15 Minuten. Oder zu Fuß 35 Minuten, der Weg ist schön."),
           L("Tourist", "m", "Es regnet bald, ich nehme den Bus. Danke!"),
           L("Einheimischer", "m", "Gute Fahrt! Der Bus kommt in fünf Minuten!")],
          [L("Taxifahrerin", "f", "Wohin möchten Sie?"),
           L("Fahrgast", "m", "Zum Hauptbahnhof, bitte."),
           L("Taxifahrerin", "f", "Über die Stadtmitte oder die Umgehungsstraße? Der kürzeste Weg ist Mitte, aber mit Stau. Umgehung 5 Minuten länger aber sicher schneller."),
           L("Fahrgast", "m", "Umgehung. Ich muss meinen Zug erreichen."),
           L("Taxifahrerin", "f", "Gut, dann sind wir in 12 Minuten dort. Kein Stau heute!"),
           L("Fahrgast", "m", "Perfekt! 12 Minuten reicht für meinen Zug. Danke!")],
          [L("Schalterbeamte", "m", "Eine Fahrkarte wohin?"),
           L("Reisende", "f", "Eine Tageskarte für die Stadt, bitte."),
           L("Schalterbeamte", "m", "Erwachsenenkarte 8 Euro, mit Studentenausweis 5 Euro. Familienkarte 12."),
           L("Reisende", "f", "Ich bin Studentin. Eine Karte, bitte."),
           L("Schalterbeamte", "m", "Das macht 5 Euro. Hier ist Ihre Karte!"),
           L("Reisende", "f", "Danke! 5 Euro für den ganzen Tag, super!")],
          [L("Mann", "m", "Mein Auto wurde gestohlen!"),
           L("Polizist", "m", "Wo stand es?"),
           L("Mann", "m", "Auf dem Marktplatz, vor dem Rathaus. Eigentlich verboten dort, aber kurz."),
           L("Polizist", "m", "Wann haben Sie es zuletzt gesehen?"),
           L("Mann", "m", "Heute Morgen um 9 Uhr, nicht gestern Abend. Jetzt ist es 13 Uhr, vier Stunden weg."),
           L("Polizist", "m", "Verstanden! Wir suchen sofort. Haben Sie ein Foto vom Auto?")],
          [L("Junge", "m", "Mama, wir kommen zu spät zum Kino!"),
           L("Mutter", "f", "Beruhig dich. Wir nehmen ein Taxi statt der Straßenbahn, kein Problem."),
           L("Junge", "m", "Taxi ist teurer. Zu Fuß schaffen wir es nicht mehr."),
           L("Mutter", "f", "Nur 8 Euro mehr. Los, wir schaffen den Film!"),
           L("Junge", "m", "Okay, dann Taxi! Aber beeilen wir uns!"),
           L("Mutter", "f", "Ja, los! In zehn Minuten sind wir da!")]])

print("11-13 applied")
