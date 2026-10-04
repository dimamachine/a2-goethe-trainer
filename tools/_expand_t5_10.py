#!/usr/bin/env python3
"""Expand Goethe A2 Hören tests 5-10 to official length. Temporary mutator."""
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


# ---------------- TEST 5 wohnen-und-umzug ----------------
apply(5,
      t1={2: "Suchen Sie eine schöne Wohnung in Bestlage? Wir haben gerade eine 3-Zimmer-Wohnung im Stadtzentrum, "
             "75 Quadratmeter, mit Balkon. Die Miete ist 1.200 Euro warm, das ist sehr fair für die Lage. "
             "Besichtigung am Samstag um 14 Uhr. Bitte vorher anrufen, weil wir nur 10 Interessenten reinlassen. "
             "Rufen Sie heute noch an! Tel. 089 / 123 456."},
      t3=[[L("Vermieter", "m", "Sie interessieren sich für die Wohnung?"),
           L("Interessentin", "f", "Ja, sehr, wie hoch ist die Miete?"),
           L("Vermieter", "m", "850 Euro kalt. Plus Nebenkosten 150 Euro — also 1.000 Euro warm."),
           L("Interessentin", "f", "Verstehe, und Heizkosten?"),
           L("Vermieter", "m", "Die Heizkosten sind schon in den 150 Euro Nebenkosten enthalten."),
           L("Interessentin", "f", "Gut, wie hoch ist die Kaution?"),
           L("Vermieter", "m", "Drei Monatsmieten, also 2.550 Euro. Fragen Sie, wenn etwas unklar ist.")],
          [L("Mitarbeiterin", "f", "Stadtwerke München, guten Tag."),
           L("Kunde", "m", "Hallo, ich bin gerade umgezogen und möchte den Strom anmelden."),
           L("Mitarbeiterin", "f", "Ihre alte Adresse und die neue, bitte."),
           L("Kunde", "m", "Alte Adresse: Goethestraße 5. Neue Adresse: Bahnhofstraße 27, Wohnung 3B."),
           L("Mitarbeiterin", "f", "Notiert, Sie bekommen einen Vertrag in zwei Tagen per Post. Bitte unterschreiben und uns zurückschicken, danke!")],
          [L("Kunde", "m", "Ich brauche ein neues Bett. Was haben Sie?"),
           L("Verkäuferin", "f", "Welche Größe? Einzelbett 90, Doppelbett 140 oder King-size 180 breit?"),
           L("Kunde", "m", "Doppelbett, also 140."),
           L("Verkäuferin", "f", "Wir haben eines aus Holz für 450 Euro. Oder ein modernes weißes für 650 Euro, sehr schön."),
           L("Kunde", "m", "Ich nehme das aus Holz. Holz hält länger als Lack, finde ich.")]])

# ---------------- TEST 6 beim-arzt-und-in-der-apotheke ----------------
apply(6,
      t1={3: "Krankenhaus-Information für alle Besucher. Die Besuchszeit dauert bis 19 Uhr. "
             "Bitte bringen Sie keine Blumen mit — wegen Allergien sind die in unserem Haus verboten. "
             "Kuchen und Obst sind erlaubt, aber bitte fragen Sie vorher die Pflege, ob der Patient das essen darf. "
             "Vielen Dank. Gute Besserung!"},
      t3=[[L("Arzt", "m", "Was tut weh?"),
           L("Patient", "m", "Mein Hals. Und ich habe Husten. Der Magen ist okay."),
           L("Arzt", "m", "Fieber auch?"),
           L("Patient", "m", "Nein, kein Fieber. Aber starker Husten, vor allem nachts."),
           L("Arzt", "m", "Ich verschreibe Ihnen einen Hustensaft. Trinken Sie viel warmen Tee, das hilft auch. Und bleiben Sie zwei Tage im Bett.")],
          [L("Apothekerin", "f", "Sie haben das Rezept dabei, oder?"),
           L("Kunde", "m", "Ja, hier. Aber kostet das viel?"),
           L("Apothekerin", "f", "Mit Rezept zahlen Sie nur 5 Euro Eigenanteil. Ohne Rezept wären es 28 Euro."),
           L("Kunde", "m", "Gut, dass ich das Rezept dabei habe. 23 Euro wären zu viel."),
           L("Apothekerin", "f", "Genau, hier sind die Medikamente. Gute Besserung!"),
           L("Kunde", "m", "Danke! Tschüss und schönen Tag!")],
          [L("Patientin", "f", "Ich möchte einen Termin für meinen Sohn."),
           L("Arzthelferin", "f", "Was hat er denn?"),
           L("Patientin", "f", "Er hat sich am Bein verletzt beim Fußball."),
           L("Arzthelferin", "f", "Wir haben heute um 11 Uhr noch frei, oder morgen um 9. Heute ist besser für eine Sportverletzung. Nächste Woche wäre zu spät."),
           L("Patientin", "f", "Dann heute um 11. Danke, bis später!")],
          [L("Krankenschwester", "f", "Sie kommen zur Untersuchung, ja? Zur Blutuntersuchung?"),
           L("Patient", "m", "Ja, eine Blutuntersuchung."),
           L("Krankenschwester", "f", "Sie sind nüchtern, hoffe ich?"),
           L("Patient", "m", "Ich habe heute Morgen einen Kaffee getrunken. Keinen Tee und kein Wasser, nur Kaffee."),
           L("Krankenschwester", "f", "Hmm, eigentlich auch kein Kaffee. Aber meistens geht das, wir machen es trotzdem.")],
          [L("Kollegin", "f", "Ich brauche ein Aspirin. Hast du eins? Oder ein Glas Wasser?"),
           L("Kollege", "m", "Kopfschmerzen? Seit wann?"),
           L("Kollegin", "f", "Schrecklich. Schon seit heute Morgen, es wird schlimmer."),
           L("Kollege", "m", "Aspirin habe ich nicht, aber Paracetamol. Hilft auch gut."),
           L("Kollegin", "f", "Gib her, danke! Wasser hole ich mir selbst."),
           L("Kollege", "m", "Hier, Paracetamol. Gute Besserung, ruh dich aus!")]])

# ---------------- TEST 7 im-buero-und-arbeitsleben ----------------
apply(7,
      t1={0: "Liebe Kolleginnen und Kollegen, die Mitarbeiter-Versammlung am Mittwoch verschiebt sich auf Donnerstag, gleiche Uhrzeit, 14 Uhr. "
             "Der Konferenzraum 12 ist leider belegt — wir treffen uns deshalb in Raum 8 im zweiten Stock. "
             "Nicht Raum 12 und nicht Raum 8 im dritten Stock, sondern Raum 8 im zweiten Stock. "
             "Wer nicht kommen kann, schickt bitte eine E-Mail. Anwesenheit ist aber wichtig.",
          1: "Hallo Frau Schmidt, hier ist Personalbüro Müller. Ihr Vorstellungsgespräch am Freitag um 10 Uhr ist bestätigt. "
             "Bitte bringen Sie alle Unterlagen mit: Lebenslauf, Zeugnisse, Empfehlungsschreiben. "
             "Nur den Lebenslauf brauchen wir nicht, bitte alle Unterlagen. "
             "Sie treffen sich zuerst mit Herrn Krüger, dem Chef der Abteilung. Das Gespräch dauert etwa eine Stunde. Viel Erfolg!",
          3: "Achtung an alle Mitarbeiter im Bürogebäude. Heute Abend wird ab 19 Uhr im ganzen Haus die Reinigung gemacht. "
             "Bitte lassen Sie keine wichtigen Dokumente auf den Schreibtischen liegen. Auch persönliche Sachen sollten Sie wegräumen. "
             "Die Reinigung dauert bis etwa 23 Uhr. Vielen Dank für Ihre Mitarbeit und einen schönen Abend!",
          4: "Hallo zusammen, der Drucker im dritten Stock ist seit heute Morgen kaputt. "
             "Wir warten auf den Techniker, der kommt erst am Donnerstag, bitte haben Sie Geduld. "
             "Bitte nutzen Sie bis dahin den Drucker im Erdgeschoss oder im fünften Stock. "
             "Wir entschuldigen uns für die Unannehmlichkeiten."},
      t2=[L("Anna", "f", "Markus, die Sommer-Feier braucht jetzt eine klare Planung. Wer macht was?"),
          L("Markus", "m", "Ich habe schon mit allen gesprochen. Jonas kümmert sich um die Location — er kennt eine schöne Halle, die noch frei ist."),
          L("Anna", "f", "Super, und das Essen?"),
          L("Markus", "m", "Lisa hat das übernommen. Sie organisiert einen Catering-Service mit warmen Speisen für 50 Personen."),
          L("Anna", "f", "Klasse. Was ist mit der Musik?"),
          L("Markus", "m", "Robert bringt die Anlage und macht den ganzen Abend DJ. Er hat das schon mehrfach bei Familienfesten gemacht."),
          L("Anna", "f", "Toll, wer schickt die Einladungen?"),
          L("Markus", "m", "Das mache ich. Ich habe schon ein Template vorbereitet. Die schicke ich morgen raus."),
          L("Anna", "f", "Und die Getränke?"),
          L("Markus", "m", "Tanja war erst skeptisch, aber jetzt hat sie zugesagt. Sie holt Bier, Wein und Limonade beim Großmarkt."),
          L("Anna", "f", "Und die Dekoration?"),
          L("Markus", "m", "Da habe ich an Sara gedacht. Aber sie hat keine Zeit, sie muss in die Konferenz. Vielleicht machst du das, Anna?"),
          L("Anna", "f", "Klar, ich kümmere mich um die Dekoration. Tische, Blumen, Lichter — das organisiere ich."),
          L("Markus", "m", "Dann sind wir startklar! Die Feier wird super für alle, bis Samstag!")],
      t3=[[L("Chefin", "f", "Können Sie heute länger bleiben? Wir haben viel zu tun."),
           L("Mitarbeiter", "m", "Wie lange denn?"),
           L("Chefin", "f", "Bis 20 Uhr wäre super, oder wenigstens bis 19 Uhr."),
           L("Mitarbeiter", "m", "20 Uhr geht nicht, ich habe einen Arzttermin um 19 Uhr. Aber bis 18 Uhr 30 kann ich bleiben, einverstanden?"),
           L("Chefin", "f", "Okay, das passt schon. Danke, bis morgen!"),
           L("Mitarbeiter", "m", "Danke! Dann arbeite ich bis halb sieben, tschüss!")],
          [L("Kollege", "m", "Wo ist der Konferenzraum 5?"),
           L("Kollegin", "f", "Im dritten Stock, nicht im ersten und nicht im fünften. Mit dem Aufzug, dann rechts."),
           L("Kollege", "m", "Ah, dort wo der große Kaffeeautomat steht?"),
           L("Kollegin", "f", "Genau, direkt daneben. Erst aber durch die Tür mit dem grünen Schild, dann links."),
           L("Kollege", "m", "Alles klar, dritter Stock, grünes Schild! Vielen Dank!")],
          [L("Sekretärin", "f", "Sie möchten Urlaub einreichen?"),
           L("Mitarbeiter", "m", "Ja, im Juli. Zwei Wochen wären gut."),
           L("Sekretärin", "f", "Wann genau? Vom 1. bis 14.? Oder vom 15. bis 28.? Im August ist leider alles voll."),
           L("Mitarbeiter", "m", "Vom 15. bis 28. — meine Frau hat dann auch Urlaub."),
           L("Sekretärin", "f", "Notiert, Sie bekommen die Bestätigung per E-Mail. Schönen Urlaub!"),
           L("Mitarbeiter", "m", "Danke! Vom 15. bis 28. Juli, ich freue mich schon!")],
          [L("Bewerberin", "f", "Wie viele Stunden pro Woche wäre das?"),
           L("Chef", "m", "Wir bieten Vollzeit mit 40 Stunden. 20 Stunden geht leider nicht. Aber Teilzeit mit 30 ist auch möglich, wenn Sie das wünschen."),
           L("Bewerberin", "f", "30 Stunden wäre besser für mich. Wegen der Kinder."),
           L("Chef", "m", "Kein Problem, wir machen 30 Stunden. Willkommen im Team!"),
           L("Bewerberin", "f", "Vielen Dank! 30 Stunden ab Montag, ich freue mich!")],
          [L("Praktikant", "m", "Was soll ich heute machen?"),
           L("Chefin", "f", "Bitte sortiere die Akten im Schrank links und mache eine Liste."),
           L("Praktikant", "m", "Soll ich auch die E-Mails beantworten?"),
           L("Chefin", "f", "Nein, das mache ich selbst. Konzentrierst du dich auf die Akten, bitte?"),
           L("Praktikant", "m", "Alles klar, Akten sortieren! Und Telefon-Anrufe mache ich nicht, oder?"),
           L("Chefin", "f", "Genau, keine Anrufe heute. Nur Akten sortieren, danke!")]])

# ---------------- TEST 8 urlaub-und-reisen-planen ----------------
apply(8,
      t1={3: "Liebe Hotelgäste, eine Information für Ihren Aufenthalt. "
             "Das Frühstück gibt es ab morgen erst um 8 Uhr statt um 7 Uhr — wegen einer Personalumstellung. "
             "Auch das Schwimmbad ist heute Nachmittag von 14 bis 17 Uhr geschlossen, eine Reinigungsarbeit. "
             "Wir entschuldigen uns für die Unannehmlichkeiten. Morgen ist alles wieder normal."},
      t2=[L("Anna", "f", "Markus, der Urlaub im August muss jetzt geplant werden. Was hat jeder gesagt?"),
          L("Markus", "m", "Mama bucht das Hotel. Sie kennt einen Ort am Bodensee, wo sie schon mal war. Mit Seeblick!"),
          L("Anna", "f", "Super, und die Anreise?"),
          L("Markus", "m", "Papa fährt uns mit dem Auto. Er hat sich angeboten, das große Auto zu nehmen, mit Dachbox."),
          L("Anna", "f", "Und die Aktivitäten — Tagesausflüge?"),
          L("Markus", "m", "Lisa hat sich darum gekümmert. Sie hat einen ganzen Plan gemacht: Schwimmen, Wandern, ein Museum."),
          L("Anna", "f", "Lisa ist immer so organisiert. Was machen wir mit dem Essen?"),
          L("Markus", "m", "Tante Eva übernimmt das. Sie kocht uns einmal pro Tag eine warme Mahlzeit, das ist günstiger als Restaurants."),
          L("Anna", "f", "Wunderbar! Was ist mit dem Hund? Wir nehmen Bello mit?"),
          L("Markus", "m", "Genau, mein Bruder Tim sorgt für Bello — Futter, Spaziergänge, alles. Er hat mit Hunden Erfahrung."),
          L("Anna", "f", "Und was mache ich? Ich möchte auch helfen."),
          L("Markus", "m", "Machst du die Fotos? Dokumentierst alles, für später und für Oma."),
          L("Anna", "f", "Foto-Job ist mir lieb. Mache ich gern.")],
      t3=[[L("Mitarbeiter", "m", "Wohin möchten Sie reisen?"),
           L("Kundin", "f", "Wir hatten zwischen Spanien und Italien überlegt. Griechenland war zu teuer."),
           L("Mitarbeiter", "m", "Spanien ist im Juni günstiger. Italien dafür im Mai, aber Mai geht nicht."),
           L("Kundin", "f", "Wir fahren im Juni — also Spanien."),
           L("Mitarbeiter", "m", "Sehr gut. Ich zeige Ihnen Angebote für Spanien im Juni."),
           L("Kundin", "f", "Danke! Spanien im Juni, wir freuen uns schon!")],
          [L("Rezeption", "f", "Wie lange möchten Sie bleiben? Und wie viele Personen?"),
           L("Gast", "m", "Drei Nächte, ab Freitag. Zwei Personen, ohne Kinder."),
           L("Rezeption", "f", "Doppelzimmer oder Familienzimmer? Einzelzimmer haben wir auch frei."),
           L("Gast", "m", "Doppelzimmer reicht — meine Kinder kommen nicht mit. Kein Familienzimmer nötig."),
           L("Rezeption", "f", "Notiert. 360 Euro insgesamt. Möchten Sie mit Frühstück?"),
           L("Gast", "m", "Ja, mit Frühstück bitte! Dann bis Freitag, danke!")],
          [L("Reiseberater", "m", "Welches Verkehrsmittel bevorzugen Sie?"),
           L("Kundin", "f", "Hmm. Auto wäre flexibel, aber die Strecke ist lang."),
           L("Reiseberater", "m", "Flug ist schneller und nicht viel teurer als Bahn."),
           L("Kundin", "f", "Dann nehme ich den Flug. Schneller ist mir wichtiger als flexibel."),
           L("Reiseberater", "m", "Gute Wahl! Soll ich gleich buchen? Der Flug geht täglich."),
           L("Kundin", "f", "Ja, bitte buchen! Vielen Dank und tschüss!")],
          [L("Reisende", "f", "Mein Koffer ist nicht angekommen!"),
           L("Mitarbeiterin", "f", "Aus welcher Stadt sind Sie gekommen?"),
           L("Reisende", "f", "Berlin. Flug LH 254."),
           L("Mitarbeiterin", "f", "Moment, ich prüfe. Ja, Ihr Koffer ist noch in Frankfurt. Wir bringen ihn morgen zu Ihrem Hotel."),
           L("Reisende", "f", "Danke! Wann kommt er genau? Morgen früh?"),
           L("Mitarbeiterin", "f", "Morgen früh um neun, direkt zu Ihrem Hotel. Entschuldigung!")],
          [L("Kundin", "f", "Können wir die Reise stornieren?"),
           L("Mitarbeiterin", "f", "Sie wollten in zwei Wochen abreisen, oder?"),
           L("Kundin", "f", "Genau, mein Mann ist plötzlich krank geworden."),
           L("Mitarbeiterin", "f", "Mit Krankheits-Schein bekommen Sie 90 Prozent zurück. Ohne Schein nur 50. Ganz ohne Grund gäbe es nichts zurück."),
           L("Kundin", "f", "Ein Schein ist kein Problem. Ich bringe ihn morgen vorbei."),
           L("Mitarbeiterin", "f", "Perfekt! Dann bekommen Sie 90 Prozent zurück. Bis morgen!")]])

# ---------------- TEST 9 sport-und-fitness ----------------
apply(9,
      t1={0: "Hallo Mitglieder vom Fitnessstudio Aktiv, eine wichtige Information: Der Gruppen-Kurs Spinning am Mittwochabend fällt diese Woche aus, weil der Trainer krank ist. "
             "Statt Spinning bieten wir Yoga in derselben Zeit an. Alle Kurse fallen nicht aus, und die Trainer bleiben auch. "
             "Wer Interesse hat, bitte am Empfang anmelden. Die anderen Kurse laufen normal weiter.",
          1: "Achtung an alle Schwimmer im Hallenbad. Das Schwimmbad schließt heute schon um 18 Uhr, statt um 22 Uhr. "
             "Wegen einer Veranstaltung am Abend können wir das Bad nicht länger offen halten. "
             "Morgen sind wir wieder zu den normalen Zeiten geöffnet. Wir bitten um Ihr Verständnis. Vielen Dank!",
          2: "Hi Anna, hier ist Trainer Marco. Dein Tennis-Termin morgen um 17 Uhr passt nicht mehr — der Platz ist gebucht. "
             "Ich biete dir 16 Uhr oder 19 Uhr an, beide gehen. Vielleicht ist 16 Uhr besser, weil du danach noch Zeit hast. "
             "Schreib mir kurz, was du nimmst. Danke!"},
      t2=[L("Lukas", "m", "Anna, was hast du diese Woche für Sport geplant?"),
          L("Anna", "f", "Eine Menge! Am Montag mache ich Krafttraining — den ganzen Körper. Das ist meine wichtigste Stunde."),
          L("Lukas", "m", "Krafttraining! Toll, was am Dienstag?"),
          L("Anna", "f", "Dienstag gehe ich schwimmen — eine Stunde im Hallenbad nach der Arbeit."),
          L("Lukas", "m", "Schwimmen? Schön, und Mittwoch?"),
          L("Anna", "f", "Mittwoch ist mein Ruhetag. Da macht meine Schwester einen Yoga-Kurs, aber ich brauche eine Pause. Donnerstag geht es weiter."),
          L("Lukas", "m", "Verstehe, donnerstag?"),
          L("Anna", "f", "Donnerstag habe ich einen festen Termin: Pilates mit meiner Freundin Lisa. Wir machen das schon seit einem Jahr zusammen."),
          L("Lukas", "m", "Schön, freitag?"),
          L("Anna", "f", "Freitag — Joggen, früh am Morgen vor der Arbeit. Eine Stunde im Park, bei jedem Wetter."),
          L("Lukas", "m", "Und am Wochenende?"),
          L("Anna", "f", "Samstag fahre ich Fahrrad mit meinen Eltern, ein langer Ausflug aufs Land. Sonntag mache ich Yoga zu Hause, ganz für mich allein."),
          L("Lukas", "m", "Wow, du machst wirklich sehr viel. Beeindruckend! Gehen wir Sonntag zusammen joggen?"),
          L("Anna", "f", "Sonntag joggen? Gern! Um neun im Park, einverstanden?")],
      t3=[[L("Verkäufer", "m", "Welche Schuhe brauchen Sie?"),
           L("Kundin", "f", "Laufschuhe. Ich gehe joggen, aber im Wald, mit unebenem Boden."),
           L("Verkäufer", "m", "Dann brauchen Sie Trail-Schuhe, nicht normale Laufschuhe und keine Tennis-Schuhe. Die haben bessere Sohlen."),
           L("Kundin", "f", "Verstehe, ich nehme die. Haben Sie Größe 38?"),
           L("Verkäufer", "m", "Größe 38 haben wir da. Möchten Sie sie anprobieren?")],
          [L("Trainerin", "f", "Was möchten Sie heute machen?"),
           L("Schüler", "m", "Mein Rücken tut weh seit gestern. Vielleicht keine starken Übungen heute."),
           L("Trainerin", "f", "Dann machen wir Dehnübungen und etwas Yoga. Keine Gewichte und kein Spinning heute."),
           L("Schüler", "m", "Perfekt, das tut mir gut. Danke schön!"),
           L("Trainerin", "f", "Gern! Und Spinning machen wir ein anderes Mal, einverstanden?")],
          [L("Empfang", "f", "Sie möchten Mitglied werden?"),
           L("Kunde", "m", "Ja, wie viel kostet das?"),
           L("Empfang", "f", "Monatsmitgliedschaft 39 Euro, Jahresmitgliedschaft 35 Euro pro Monat. Studenten zahlen 25."),
           L("Kunde", "m", "Ich bin Student. Aber Jahres ist mir zu lang. Monatlich, bitte."),
           L("Empfang", "f", "Mit Studentenausweis. 25 Euro pro Monat, das ist günstig."),
           L("Kunde", "m", "Gut, hier ist mein Ausweis. Wo unterschreibe ich?")],
          [L("Trainer", "m", "Wie war das Training?"),
           L("Spielerin", "f", "Anstrengend. Aber gut."),
           L("Trainer", "m", "Wir haben heute das nächste Spiel am Samstag um 15 Uhr. Bist du dabei?"),
           L("Spielerin", "f", "Samstag um 15 Uhr — leider nicht. Mein Bruder hat Hochzeit."),
           L("Trainer", "m", "Schade, aber Hochzeit ist Hochzeit. Viel Spaß am Samstag!"),
           L("Spielerin", "f", "Danke! Nächstes Spiel bin ich wieder dabei, versprochen!")],
          [L("Vater", "m", "Mama, willst du Sport mit mir machen?"),
           L("Tochter", "f", "Hmm, was?"),
           L("Vater", "m", "Ich gehe joggen. Oder ein Spaziergang, wenn du nicht laufen willst."),
           L("Tochter", "f", "Spaziergang ist gut. Joggen schaffe ich nicht mehr, Fahrrad auch nicht."),
           L("Vater", "m", "Gut, Spaziergang! Um drei am See, einverstanden?"),
           L("Tochter", "f", "Einverstanden! Bis drei, ich freue mich!")]])

# ---------------- TEST 10 einkaufen-und-geschaefte ----------------
apply(10,
      t1={0: "Liebe Kunden, herzlich willkommen im Supermarkt Frischeparadies. Heute haben wir besondere Angebote: "
             "Erdbeeren ein Kilo nur 2,99 Euro, Milch im Drei-Liter-Pack 4,50 Euro. "
             "Außerdem ist heute Sonderaktion bei Wein — jede dritte Flasche kostenlos. Nicht 50 Prozent auf alles, nur jede dritte Flasche Wein gratis. "
             "Die Aktion gilt nur bis 20 Uhr. Genießen Sie Ihren Einkauf! Viel Spaß beim Einkaufen!",
          1: "Hallo Schatz, hier ist Mama. Kannst du beim Einkaufen heute noch Brot und Milch mitbringen? "
             "Brot vom Bäcker, nicht vom Supermarkt — das schmeckt besser. Egal woher die Milch kommt, aber Brot bitte vom Bäcker. "
             "Auch noch Tomaten, wenn die schön aussehen. Bis später! Danke!",
          2: "Sehr geehrte Kunden, die Kasse 5 ist leider kaputt — bitte gehen Sie zur Kasse 3 oder 7. "
             "Wir entschuldigen uns für die Wartezeit. Wir bitten Kunden mit großem Einkauf, die Kasse 3 zu nutzen, weil die schneller ist. "
             "Kunden mit wenigen Artikeln können auch die Express-Kasse 7 nutzen. Danke!",
          3: "Hallo Frau Wagner, hier ist Schuhgeschäft Lauffit. Die Schuhe, die Sie bestellt haben, sind angekommen — aber in der falschen Größe. "
             "Statt 38 ist die Größe 39 da. Sie haben richtig bestellt, Frau Wagner, das war unser Fehler. "
             "Wir bestellen jetzt nochmal die richtige Größe. Es dauert noch eine Woche. Tut uns leid für die Wartezeit.",
          4: "Achtung an alle Kunden im Einkaufszentrum. Heute schließen wir schon um 18 Uhr statt um 22 Uhr, weil eine private Veranstaltung stattfindet. "
             "Letzter Einlass ist um 17 Uhr 30. Morgen sind wir wieder zu normalen Zeiten geöffnet. "
             "Vielen Dank für Ihr Verständnis und einen schönen Einkauf. Bitte kommen Sie morgen wieder!"},
      t2=[L("Mara", "f", "Felix, ich habe Anna gefragt, was alle für die Einweihung mitbringen. Lass mich erzählen."),
          L("Felix", "m", "Erzähl mal. Wir brauchen viel."),
          L("Mara", "f", "Anna kauft die Blumen — sie hat einen schönen Floristen in der Nähe gefunden. Ein großer Strauß für die Wohnzimmer-Vase."),
          L("Felix", "m", "Schön, und der Wein?"),
          L("Mara", "f", "Markus kümmert sich um Wein und Sekt. Er kennt einen guten Laden mit fairen Preisen."),
          L("Felix", "m", "Und Brot, Käse — die Snacks?"),
          L("Mara", "f", "Lisa macht das Buffet. Sie kauft alles: Käse, Brot, Oliven, kleine Salate."),
          L("Felix", "m", "Lisa ist immer so zuverlässig. Was ist mit der Musik?"),
          L("Mara", "f", "Tom organisiert die Musik. Er hat eine gute Musik-Sammlung auf seinem Handy."),
          L("Felix", "m", "Und Eis als Dessert?"),
          L("Mara", "f", "Eis bringt Sara mit. Sie holt es am Tag der Party — etwa drei Sorten."),
          L("Felix", "m", "Wunderbar! Was machen wir dann?"),
          L("Mara", "f", "Wir putzen die Wohnung und stellen alles bereit. Das ist eigentlich die ganze Arbeit."),
          L("Felix", "m", "Klingt gut, dann sind wir vorbereitet. Bis Samstag!"),
          L("Mara", "f", "Bis Samstag! Ich kaufe noch Servietten und Kerzen dazu."),
          L("Felix", "m", "Perfekt! Dann wird die Einweihung super, ich freue mich!")],
      t3=[[L("Verkäuferin", "f", "Was suchen Sie?"),
           L("Kunde", "m", "Eine Hose. Größe 32. Für die Arbeit, nichts Sportliches."),
           L("Verkäuferin", "f", "Welche Farbe? Wir haben Blau, Schwarz und Beige."),
           L("Kunde", "m", "Schwarz ist mir zu klassisch. Beige? Hmm, die könnte gut sein, oder?"),
           L("Verkäuferin", "f", "Hier ist die beige Hose in Größe 32. Möchten Sie sie anprobieren?"),
           L("Kunde", "m", "Perfekt, die nehme ich in Größe 32. Danke schön!")],
          [L("Bäcker", "m", "Was darf es sein?"),
           L("Kundin", "f", "Ein Vollkornbrot, bitte. Und zwei Croissants."),
           L("Bäcker", "m", "Tut mir leid, Croissants sind aus. Aber wir haben Brötchen — Mohn, Sesam oder Käse."),
           L("Kundin", "f", "Dann zwei Sesambrötchen statt der Croissants."),
           L("Bäcker", "m", "Sehr gut. Das macht 3 Euro 20, bitte."),
           L("Kundin", "f", "Hier bitte! Und Mohnbrötchen nehme ich nächstes Mal. Tschüss!")],
          [L("Kassiererin", "f", "Das macht 47 Euro 50."),
           L("Kunde", "m", "Kann ich mit Karte zahlen?"),
           L("Kassiererin", "f", "Ja, oder mit dem Handy. Bar geht ab heute leider nicht mehr, nur Karte oder Handy."),
           L("Kunde", "m", "Mit Karte, dann. Geht das hier vorne?"),
           L("Kassiererin", "f", "Ja, hier vorne bitte. Stecken oder kontaktlos?"),
           L("Kunde", "m", "Kontaktlos mit dem Handy, so modern! Danke, tschüss!")],
          [L("Kundin", "f", "Ich möchte diese Schuhe umtauschen — sie passen nicht."),
           L("Verkäuferin", "f", "Haben Sie den Bon?"),
           L("Kundin", "f", "Ja, hier."),
           L("Verkäuferin", "f", "Sie können das Geld zurück haben oder ein neues Paar in Ihrer Größe wählen."),
           L("Kundin", "f", "Geld zurück, bitte. Mir gefällt das Modell nicht so gut."),
           L("Verkäuferin", "f", "Schade! Hier ist Ihr Geld. Bis zum nächsten Mal!")],
          [L("Kunde", "m", "Haben Sie das Buch ‚Die Welt von gestern‘?"),
           L("Verkäuferin", "f", "Moment, ich schaue. Ja, einmal vorrätig. 18 Euro."),
           L("Kunde", "m", "Im Internet finde ich es für 14 Euro."),
           L("Verkäuferin", "f", "Wir können leider den Preis nicht senken. Aber wir geben ein Lesezeichen kostenlos dazu."),
           L("Kunde", "m", "Okay, ich nehme das Buch hier. 18 Euro, stimmt so.")]])

print("5-10 applied")
