#!/usr/bin/env python3
"""Expand Goethe A2 Hören tests 14-15 (+T1 top-ups 20/24/25). Temporary mutator."""
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


# ---------------- TEST 14 familienfeste ----------------
apply(14,
      t1={1: "Hallo Sabine, hier ist Mama. Hey, Omas Geburtstag am Sonntag — Tante Eva kann doch nicht kommen, weil ihr Sohn krank wurde. "
             "Aber Onkel Karl kommt, das ist eine Überraschung für Oma. Kein neues Geschenk, Onkel Karl selbst ist die Überraschung. "
             "Bitte sag noch nichts, das ist ein Geheimnis. Komm bitte pünktlich um 14 Uhr. Danke!",
          2: "Hier ist die Konditorei Süßgebäck. Ihr Hochzeitskuchen ist bestellt: drei Stockwerke, weiße Schokolade mit Erdbeeren. "
             "Lieferung am Samstag um 14 Uhr direkt zum Festsaal. Nicht Sonntag früh, sondern Samstag um 14 Uhr. "
             "Falls es Probleme gibt, rufen Sie uns bis Freitagabend zurück. Ansonsten — wir freuen uns auf Ihren großen Tag. Danke!"},
      t2=[L("Anna", "f", "Markus, die Goldene Hochzeit von Oma und Opa kommt bald. Wir müssen alles planen."),
          L("Markus", "m", "Stimmt, wer kümmert sich um was in der Familie? Alles muss perfekt sein."),
          L("Anna", "f", "Tante Eva organisiert die Location — sie hat schon einen schönen Saal reserviert, mit Garten."),
          L("Markus", "m", "Super, und das Essen?"),
          L("Anna", "f", "Mama kocht das Hauptessen. Sie hat ein altes Familienrezept, das Oma lieben wird."),
          L("Markus", "m", "Klingt nach einer schönen Idee. Wer fotografiert?"),
          L("Anna", "f", "Papa hat eine gute Kamera. Er macht die Fotos und filmt auch ein paar Momente."),
          L("Markus", "m", "Und die Musik?"),
          L("Anna", "f", "Mein Bruder Lukas. Er ist ja Musiker und spielt Klavier — auch Lieder, die unsere Großeltern lieben."),
          L("Markus", "m", "Toll, was ist mit den Reden? Jemand muss eine schöne Rede halten."),
          L("Anna", "f", "Onkel Robert macht die Rede. Er ist der älteste Sohn und kennt die Geschichte am besten."),
          L("Markus", "m", "Und was machen wir?"),
          L("Anna", "f", "Wir kümmern uns um das Geschenk und die Einladungen. Eine schöne Karte und ein Geschenk haben wir schon."),
          L("Markus", "m", "Perfekt! Klingt nach einem schönen Plan. Oma und Opa werden sich freuen!")],
      t3=[[L("Mutter", "f", "Was wünschst du dir zum Geburtstag?"),
           L("Kind", "m", "Ich möchte ein neues Fahrrad."),
           L("Mutter", "f", "Ein Fahrrad ist viel Geld. Vielleicht ein kleineres Geschenk? Aber nichts wäre zu wenig."),
           L("Kind", "m", "Dann ein Skateboard? Das wollte ich auch schon lange."),
           L("Mutter", "f", "Skateboard geht. Ich kaufe eins. Aber erst zum Geburtstag!"),
           L("Kind", "m", "Juhu, Skateboard! Danke, Mama, du bist die Beste!")],
          [L("Frau", "f", "Mein Mann hat morgen Geburtstag. Was kann ich kochen?"),
           L("Freundin", "f", "Sein Lieblingsessen ist Schnitzel, oder?"),
           L("Frau", "f", "Genau, aber Schnitzel mache ich oft. Ins Restaurant gehen wäre teuer. Vielleicht etwas Neues?"),
           L("Freundin", "f", "Lasagne ist immer gut für Geburtstage."),
           L("Frau", "f", "Lasagne kocht meine Schwiegermutter ständig. Ich mache Schnitzel — das ist sein Liebling, fertig."),
           L("Freundin", "f", "Gute Wahl! Schnitzel mit Kartoffelsalat, lecker!")],
          [L("Anrufer", "m", "Ich bestelle Blumen zur Hochzeit."),
           L("Floristin", "f", "Welche Farben?"),
           L("Anrufer", "m", "Weiß und rosa. Das ist klassisch."),
           L("Floristin", "f", "Wir können auch lila oder gelb anbieten, oder rote Rosen, falls Sie etwas Modernes möchten."),
           L("Anrufer", "m", "Nein, weiß und rosa bleibt — die Braut hat das so gewünscht, basta."),
           L("Floristin", "f", "Verstanden, weiß und rosa! Lieferung am Freitag, einverstanden?")],
          [L("Vater", "m", "Tochter, kommst du zur Familienfeier am Samstag?"),
           L("Tochter", "f", "Eigentlich habe ich schon einen Termin mit Freunden. Beides geht leider nicht."),
           L("Vater", "m", "Oma wird sehr traurig sein. Sie kommt extra aus Hamburg."),
           L("Tochter", "f", "Okay, dann verschiebe ich die Freunde. Oma ist wichtiger, sie freut sich."),
           L("Vater", "m", "Danke, mein Schatz! Oma wird so glücklich sein!")],
          [L("Mann", "m", "Wir machen unseren Hochzeitstag dieses Jahr besonders."),
           L("Frau", "f", "Was hast du geplant? Restaurant?"),
           L("Mann", "m", "Nein, etwas Besseres als Restaurant. Und nicht zu Hause, wirklich weg!"),
           L("Frau", "f", "Oh, das ist wundervoll! Paris, wirklich? Ich freue mich!"),
           L("Mann", "m", "Ja, Paris! Zwei Nächte, Hotel mit Frühstück, alles gebucht!"),
           L("Frau", "f", "Wunderbar! Unser Hochzeitstag in Paris, wie romantisch!")]])

# ---------------- TEST 15 kino-theater-und-konzert ----------------
apply(15,
      t1={0: "Achtung, liebe Kinobesucher: Wegen technischer Probleme verschiebt sich der Film ‚Sommerträume‘ um 30 Minuten. "
             "Statt 20 Uhr startet er erst um 20 Uhr 30. Nicht erst morgen, heute um 20 Uhr 30. "
             "Für die Wartezeit bietet die Kino-Bar Getränke zum halben Preis. "
             "Falls Sie nicht warten können, geben wir Ihnen das Geld zurück. Danke!",
          1: "Hallo Schatz, hier ist Tom. Die Theaterkarten für Samstag — du hast Recht, das Stück ist abgesagt. "
             "Aber gleichzeitig gibt es eine andere Vorstellung im selben Theater — ‚Faust‘ um 19 Uhr 30. "
             "Soll ich die Karten umtauschen oder lieber Geld zurück? Ich hole dich ab, du musst nicht allein nach Hause. "
             "Sag Bescheid bis heute Abend. Danke!",
          2: "Liebe Konzertbesucher, das Konzert beginnt pünktlich um 20 Uhr. "
             "Bitte schalten Sie Ihre Handys aus, nicht nur lautlos — wirklich aus, weil das Signal die Mikrofone stört. "
             "Fotos und Videos sind in der Pause erlaubt, während des Konzerts streng verboten. "
             "Wir wünschen Ihnen einen schönen Abend. Danke!",
          3: "Anrufbeantworter des Stadttheaters. Wir sind heute, Montag, geschlossen. Dienstag bis Sonntag sind wir von 10 bis 19 Uhr erreichbar. "
             "Für Karten-Buchungen besuchen Sie unsere Webseite — das ist 24 Stunden möglich. "
             "Bei dringenden Fragen schreiben Sie eine E-Mail. Wir freuen uns auf Ihren Besuch von Dienstag bis Sonntag! Bis morgen!"},
      t2=[L("Anna", "f", "Markus, du hattest die Idee, jede Woche etwas Kulturelles zu machen. Lass uns das jetzt festlegen."),
          L("Markus", "m", "Gut, in der ersten Woche gehen wir ins Kino — ‚Sommerträume‘, der neue Film, am Freitag."),
          L("Anna", "f", "Wunderbar, was in der zweiten Woche?"),
          L("Markus", "m", "Theater! Faust im Stadttheater. Ich habe schon Karten."),
          L("Anna", "f", "Und dritte Woche?"),
          L("Markus", "m", "Da gibt es ein Klassik-Konzert in der Philharmonie. Mozart, mein Lieblingskomponist."),
          L("Anna", "f", "Schön! Was kommt in Woche vier?"),
          L("Markus", "m", "Eine Kunstausstellung. Die neue moderne Ausstellung im Museum am Stadtpark, mit Führung."),
          L("Anna", "f", "Und die letzte Woche?"),
          L("Markus", "m", "Da besuchen wir das Filmfestival am Stadtrand. Mehrere Filme zur Auswahl, den ganzen Tag."),
          L("Anna", "f", "Klingt nach einem schönen Monat. Was machen wir mit Oper? Das wollten wir auch mal."),
          L("Markus", "m", "Oper diesmal nicht — die Saison startet erst im Herbst. Aber im nächsten Jahr."),
          L("Anna", "f", "Okay, dann ist Oper für später. Ich freue mich auf den Monat!"),
          L("Anna", "f", "Oper also später! Sollen wir Freunde einladen, zu zweit ist schöner?"),
          L("Markus", "m", "Gute Idee! Lisa und Tom kommen mit, ich frage sie heute!")],
      t3=[[L("Kunde", "m", "Eine Karte für den Film ‚Sommerträume‘."),
           L("Verkäuferin", "f", "Welche Vorstellung? 18 Uhr, 20 Uhr 30 oder 22 Uhr 45? Spät wird es auch."),
           L("Kunde", "m", "20 Uhr 30 wäre gut. Nicht 18 Uhr, zu früh."),
           L("Verkäuferin", "f", "Reihe? Vorne, Mitte oder hinten? Hinten ist fast voll."),
           L("Kunde", "m", "Mitte, bitte. Ist noch etwas frei?"),
           L("Verkäuferin", "f", "Ja, Mitte ist frei. Viel Spaß beim Film um 20 Uhr 30!")],
          [L("Frau", "f", "Welches Buch möchtest du lesen?"),
           L("Mann", "m", "Etwas Spannendes. Krimi vielleicht?"),
           L("Frau", "f", "Hier — ‚Der schwarze Schatten‘. Sehr gut bewertet."),
           L("Mann", "m", "Hmm, mir ist Krimi heute zu dunkel. Beide nehmen wäre zu viel."),
           L("Frau", "f", "‚Sommer in Paris‘ — eine leichte Komödie. Perfekt für den Urlaub."),
           L("Mann", "m", "Genau das brauche ich. Das nehme ich. Danke!")],
          [L("Mitarbeiterin", "f", "Konzerthaus, guten Abend."),
           L("Anrufer", "m", "Hallo, ich möchte 2 Karten für das Klassikkonzert am Freitag."),
           L("Mitarbeiterin", "f", "Welcher Bereich? Parkett, erster Rang oder zweiter Rang?"),
           L("Anrufer", "m", "Erster Rang, falls noch frei."),
           L("Mitarbeiterin", "f", "Frei ist da nichts mehr. Aber Parkett oder zweiter Rang gibt es noch, beide gut."),
           L("Anrufer", "m", "Parkett dann, näher dran. Danke schön!")],
          [L("Vater", "m", "Was möchtest du heute machen?"),
           L("Sohn", "m", "Ins Kino gehen!"),
           L("Vater", "m", "Im Kino läuft kein Kinderfilm gerade, nur Theater für Erwachsene. Aber das neue Museum hat eine Kinder-Ausstellung."),
           L("Sohn", "m", "Museum klingt langweilig. Kino wäre besser, oder?"),
           L("Vater", "m", "Es ist eine interaktive Ausstellung — du kannst alles anfassen und mitmachen, versprochen."),
           L("Sohn", "m", "Okay, dann Museum! Das wird toll, Papa!")],
          [L("Anrufer", "m", "Ich habe Karten für das Konzert morgen, aber ich kann nicht kommen."),
           L("Mitarbeiterin", "f", "Möchten Sie das Geld zurück oder Karten für eine andere Vorstellung?"),
           L("Anrufer", "m", "Geld zurück wäre besser. Ich weiß nicht, wann ich Zeit habe."),
           L("Mitarbeiterin", "f", "Wir können das Geld zurückgeben, abzüglich 5 Euro Bearbeitungsgebühr pro Karte. So sind die Regeln.")]])

# ---------------- T1 top-ups 20/24/25 ----------------
apply(20,
      t1={0: "Liebe Schüler der Sprachschule Aktiv, eine Information für unsere A2-Klasse: Unser Kursraum ändert sich. "
             "Statt Raum 102 sind wir ab Montag in Raum 205 — eine Etage höher. "
             "Der Lehrer bleibt gleich, nur der Raum ändert sich. Das Klassenzimmer ist größer und heller. "
             "Die Zeit bleibt gleich: Montag und Mittwoch von 18 bis 20 Uhr. Vielen Dank!"})
apply(24,
      t1={0: "Liebe Eltern, der Kindergarten Sonnenschein hat ab nächster Woche neue Öffnungszeiten. "
             "Statt 7 bis 16 Uhr sind wir nun von 7 Uhr 30 bis 17 Uhr offen. "
             "Nicht den ganzen Tag, nur bis 17 Uhr. Mehr Zeit am Nachmittag, also. Aber wir öffnen 30 Minuten später am Morgen. "
             "Bitte planen Sie das in Ihren Alltag ein. Danke!",
          3: "Achtung an alle Eltern: Am Donnerstag fällt der Schulunterricht aus, wegen Lehrerkonferenz. "
             "Die Kinder kommen erst am Freitag wieder. "
             "Wenn Sie keine Kinderbetreuung haben, bietet die Schule eine Notfall-Betreuung an — von 8 bis 13 Uhr. "
             "Es gibt also nicht gar nichts, die Betreuung ist da. Bitte melden Sie sich vorab im Sekretariat an. Danke!",
          4: "Hallo Tom, hier ist Sara. Mein Sohn Lukas möchte mit deinem Sohn am Wochenende Fußball spielen. "
             "Nicht Spielzeug tauschen und keine Hausaufgaben, wirklich Fußball spielen! "
             "Können sie sich bei uns treffen, am Samstagnachmittag um 14 Uhr? Wir haben ja einen Garten. "
             "Lukas freut sich schon. Wenn das nicht klappt, finden wir einen anderen Termin. Danke!"})
apply(25,
      t1={0: "Liebe Bibliotheksbesucher, eine Information für Sie: Wir sind ab Montag bis 22 Uhr offen, statt bis 20 Uhr. "
             "Mehr Zeit für Sie zum Lesen oder Studieren. Am Wochenende bleiben die Zeiten gleich: Samstag bis 18 Uhr, Sonntag geschlossen. "
             "Bitte beachten Sie die längeren Öffnungszeiten unter der Woche. Danke!",
          1: "Hallo Frau Wagner, hier ist die Stadtbibliothek. Das Buch, das Sie vorbestellt haben — ‚Der Steppenwolf‘ von Hermann Hesse — ist eingetroffen. "
             "Bitte holen Sie es innerhalb von 7 Tagen ab. Nicht 3 Tage und kein Monat, genau 7 Tage. "
             "Danach wird es dem nächsten Interessenten gegeben. Wir haben aktuell 5 weitere Personen, die darauf warten. Danke!",
          3: "Liebe Mitglieder der Buchclub-Gruppe, das nächste Treffen am 15. März wird in einem Café statt in der Bibliothek stattfinden. "
             "Im Café Buchstabe, Königstraße 12, ab 19 Uhr. Wir besprechen das neue Buch ‚Drei‘ von Dror Mishani. "
             "Wer das Buch noch nicht gelesen hat — bitte vorher beenden. Danke!"})

print("14-15 applied")
