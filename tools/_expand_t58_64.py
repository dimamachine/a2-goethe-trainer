#!/usr/bin/env python3
"""Expand Goethe A2 Hören tests 58-64 to official length. Temporary mutator."""
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


# ---------------- TEST 58 beim-friseur-und-beauty ----------------
apply(58,
      t1={0: "Liebe Kunden: Unser Friseur-Salon hat ab Mai neue Preise. Damen-Haarschnitt 35 Euro statt 30. "
             "Herren-Haarschnitt 25 Euro statt 22. Färben 70 Euro statt 65. "
             "45 Euro kostet nur das Verwöhn-Paket mit Massage, der normale Schnitt bleibt bei 35. "
             "Wir entschuldigen uns für die Erhöhung — gestiegene Kosten. Vielen Dank für Ihr Verständnis!",
          1: "Hallo Anna, hier ist Lisa. Hör mal, ich habe Termin beim Friseur am Mittwoch — möchtest du auch? "
             "Können zusammen gehen. Färben lassen, ich nehme rot. Nur schneiden wäre mir zu wenig, und nichts machen kommt nicht in Frage. "
             "Du wolltest doch was Neues? Bei Maria im Salon, Maxstraße 10. Ruf zurück, bis dann!",
          2: "Achtung Kunden: Unsere Friseurin Petra ist krank diese Woche. "
             "Sie ist nicht im Urlaub und hat nicht gekündigt, sie ist wirklich krank. "
             "Termine bei ihr werden verschoben — wir rufen alle persönlich an. "
             "Wer dringend braucht, kann zur Kollegin Sabine — gleiche Qualität, freie Termine vorhanden. "
             "Wir entschuldigen uns. Bis bald!",
          3: "Hi Markus, hier ist Tom. Mein erstes Mal beim Friseur seit einem Jahr! Haare sehr lang, fast wie Frau. "
             "Habe Termin morgen — kurz schneiden, modern. Lang lassen will ich nicht mehr, und färben auch nicht, nur kurz. "
             "Bin nervös, das letzte Mal war schrecklich. Diesmal anderer Friseur. Wünsch mir Glück!",
          4: "Liebe Damen: Im Beauty-Salon Schön bieten wir neue Behandlungen. Massage neu im Programm, Gesichtsbehandlung schon länger. "
             "Auch Maniküre und Pediküre. Aktion diese Woche: 20% auf alle Behandlungen außer Massage. "
             "Termin online buchen, bitte. Fragen Sie an der Rezeption nach Details. Wir freuen uns auf euch!"},
      t2=[L("Anna", "f", "Markus, alle machen jetzt Beauty-Sachen! Was lässt denn jeder machen?"),
          L("Markus", "m", "Lukas lässt sich rasieren, beim Barbier, klassisch mit Klinge. Sieht gut aus."),
          L("Anna", "f", "Klassisch, schön! Und Lisa? Färbt sie die Haare?"),
          L("Markus", "m", "Nein, keine Farbe. Lisa macht Maniküre, wöchentlich, sehr gepflegte Hände."),
          L("Anna", "f", "Wöchentlich, wow! Und Tom? Auch Maniküre?"),
          L("Markus", "m", "Nein, Tom geht zur Massage. Rückenschmerzen vom Büro, jede Woche eine Stunde."),
          L("Anna", "f", "Jede Woche, das hilft sicher! Und Sara?"),
          L("Markus", "m", "Sara macht eine Gesichtsbehandlung, Haut-Pflege, jeden Monat im Salon."),
          L("Anna", "f", "Jeden Monat, toll! Und Tim? Lässt er sich die Wimpern machen?"),
          L("Markus", "m", "Nein, keine Wimpern! Tim lässt sich Pediküre machen. Als Sportler sind ihm gepflegte Füße wichtig."),
          L("Anna", "f", "Pediküre für Sportler, logisch! Und Augenbrauen oder Solarium macht keiner?"),
          L("Markus", "m", "Nein, Augenbrauen zupfen mag keiner von uns, und Solarium ist ungesund."),
          L("Anna", "f", "Stimmt, Solarium ist ungesund! Sollen wir auch etwas buchen?"),
          L("Markus", "m", "Gute Idee! Ich nehme eine Massage, und du eine Gesichtsbehandlung, okay?")],
      t3=[[L("Kundin", "f", "Guten Tag! Ich möchte etwas Neues. Aber bitte nicht sehr kurz!"),
           L("Friseurin", "f", "Wie wäre es schulterlang? Drei Finger breit über die Schultern?"),
           L("Kundin", "f", "Ja, schulterlang ist gut. Mit Pony oder ohne?"),
           L("Friseurin", "f", "Mit Pony, aber kurzem Pony. Nur Spitzen schneiden wäre zu wenig."),
           L("Kundin", "f", "Gut, schulterlang mit Pony! Wann fangen wir an?")],
          [L("Kunde", "m", "Guten Tag! Was kostet Bart trimmen, nur Bart allein?"),
           L("Barbier", "m", "Zum Haarschnitt dazu 10 Euro extra. Allein kostet es 15 Euro."),
           L("Kunde", "m", "Und mit Rasur zusammen 25 Euro, oder?"),
           L("Barbier", "m", "Genau, mit klassischer Rasur 25 Euro. Was darf es sein?"),
           L("Kunde", "m", "Nur Bart trimmen für 15 Euro, bitte.")],
          [L("Mutter", "f", "Klein-Lukas, deine Haare sind zu lang! Wir gehen zum Friseur."),
           L("Lukas", "m", "Nein, ich hasse das! Bitte zu Hause selbst schneiden!"),
           L("Mutter", "f", "Zu Hause wird es schief. Oder willst du beides, halb hier, halb dort?"),
           L("Lukas", "m", "Nein! Entweder zu Hause oder gar nicht!"),
           L("Mutter", "f", "Kein Entweder-oder! Wir gehen zum Friseur, danach bekommst du Eis.")],
          [L("Frau", "f", "Guten Tag! Kann ich meinen Termin verschieben? Ich hatte Donnerstag um 15 Uhr."),
           L("Empfang", "f", "Wohin denn? Freitag oder Samstag wäre frei."),
           L("Frau", "f", "Freitag geht nicht, da arbeite ich lange."),
           L("Empfang", "f", "Dann Samstag um 14 Uhr? Da ist noch etwas frei."),
           L("Frau", "f", "Perfekt, Samstag um 14 Uhr! Vielen Dank!")],
          [L("Mann", "m", "Hat alles gut geklappt? Der Schnitt ist super! Möchten Sie Trinkgeld? Ich gebe 3 oder 5 Euro?"),
           L("Friseur", "m", "Wie Sie möchten, das ist nett! 10 Euro wäre zu viel."),
           L("Mann", "m", "Dann 5 Euro Trinkgeld, bitte schön!"),
           L("Friseur", "m", "Vielen Dank, sehr nett! Bis zum nächsten Mal!")]])

# ---------------- TEST 59 beim-friseur-maenner ----------------
apply(59,
      t1={0: "Liebe Kunden: Der Barbier-Salon Klassik öffnet ab Donnerstag. "
             "Nicht Montag und nicht Samstag, wirklich erst ab Donnerstag. "
             "Spezialist für Männer-Haarschnitt, Bart-Pflege, klassisches Rasieren. "
             "Eröffnungsangebot: 30% Rabatt erste zwei Wochen. Termin online oder telefonisch. "
             "Wir freuen uns auf erste Männer-Kunden!",
          1: "Hallo Markus, hier ist Tom. Hey, mein Bart wird zu lang. Habe Termin morgen beim Barbier, 14 Uhr. "
             "Abrasieren will ich ihn nicht, und wachsen lassen auch nicht, nur pflegen lassen. "
             "Möchtest du mitkommen? Du hast auch einen ungepflegten Bart, sage ich ehrlich. "
             "Treffen wir uns davor zum Mittagessen. Ruf zurück, bis bald!",
          2: "Achtung Kunden: Klassische Rasur mit Messer ist nur noch bei vorheriger Anmeldung. "
             "Spontan geht nicht — dauert 30 Minuten pro Person, brauchen wir Zeit. Bitte zwei Tage vorher anrufen. "
             "Normale Bart-Pflege auch spontan möglich. Haarschnitt geht immer spontan, nur die Rasur nicht. "
             "Vielen Dank für Verständnis!",
          3: "Hi Anna, hier ist Lisa. Du, mein Mann hat einen schlechten Haarschnitt bekommen — viel zu kurz! "
             "Nicht falsche Farbe und nicht falscher Stil, einfach viel zu kurz. Sieht aus wie ein Soldat. "
             "Er ist sauer auf den Friseur. Wechselt jetzt zum Barbier in der Hauptstraße — kennst du den? "
             "Soll besser sein. Was meinst du?",
          4: "Liebe Kunden: Wir bieten ab Mai ein Bart-Komplett-Paket — Rasur, Pflege-Öl, Form-Modellierung. "
             "Alles zusammen 35 Euro statt 50 wenn einzeln. 25 Euro kostet nur die kleine Pflege ohne Rasur. "
             "Auch Bart-Beratung kostenlos: welche Form passt zu welchem Gesicht? Termin nötig. Wir freuen uns!"},
      t2=[L("Anna", "f", "Markus, alle Männer haben neue Frisuren! Wer hat was? Erzähl mal!"),
          L("Markus", "m", "Lukas hat eine Glatze, selbst rasiert. Gefällt ihm, sehr praktisch."),
          L("Anna", "f", "Eine Glatze, mutig! Und Lisa? Auch kurz?"),
          L("Markus", "m", "Lisa? Du meinst sicher Lars. Lars hat einen Iro, einen auffälligen Mohawk."),
          L("Anna", "f", "Ja, sorry, Lars! Und Tom? Pferdeschwanz oder kurz?"),
          L("Markus", "m", "Kein Pferdeschwanz. Tom hat einen Mittelscheitel, klassisch, mit langen Haaren."),
          L("Anna", "f", "Klassisch, schön! Und Sven? Auch Glatze?"),
          L("Markus", "m", "Nein, Sven hat einen Dutt. Haare zusammen, sportlich und modisch."),
          L("Anna", "f", "Ein Dutt, interessant! Und Tim? Locken oder Bürstenschnitt?"),
          L("Markus", "m", "Weder Locken noch Bürstenschnitt. Tim hat einen Undercut, kurz an den Seiten, oben länger."),
          L("Anna", "f", "Undercut, cool! Und Dreadlocks hat keiner, oder?"),
          L("Markus", "m", "Nein, Dreadlocks will keiner von uns. Zu viel Arbeit, zu lang."),
          L("Anna", "f", "Verstehe! Sollen wir dir auch eine neue Frisur machen?"),
          L("Markus", "m", "Nein danke! Meine Haare bleiben so, ganz normal und langweilig.")],
      t3=[[L("Kunde", "m", "Guten Tag! Wie lange dauert es? Ich habe Eile."),
           L("Barbier", "m", "Haarschnitt 25 Minuten, mit Bart 40 Minuten. Eine Stunde brauchen wir nie."),
           L("Kunde", "m", "Dann nur Haare, bitte, ohne Bart."),
           L("Barbier", "m", "Alles klar, 25 Minuten. Nehmen Sie Platz!"),
           L("Kunde", "m", "Perfekt! In 25 Minuten bin ich wieder weg. Danke!")],
          [L("Junge", "m", "Mama, ich will nicht zum Friseur! Bitte nicht!"),
           L("Mutter", "f", "Aber Schulanfang ist bald! Du musst ordentlich aussehen."),
           L("Junge", "m", "Okay, aber nicht sehr kurz, bitte! Und färben auch nicht!"),
           L("Mutter", "f", "Versprochen, nicht kurz und kein Färben. Nur Spitzen schneiden."),
           L("Junge", "m", "Nur Spitzen? Na gut, einverstanden. Aber schnell!")],
          [L("Mann", "m", "Ich werde grau, überall! Was soll ich tun? Färben oder akzeptieren?"),
           L("Friseur", "m", "Viele färben. Schwarz oder blond? Oder dunkelbraun?"),
           L("Mann", "m", "Schwarz ist zu hart, blond passt nicht zu mir."),
           L("Friseur", "m", "Dann dunkelbraun, das sieht am natürlichsten aus."),
           L("Mann", "m", "Gut, dunkelbraun! Wann haben Sie Zeit? Morgen vielleicht?")],
          [L("Kunde", "m", "Guten Tag! Wann ist mein Termin? Freitag um 17 Uhr?"),
           L("Empfangs-Dame", "f", "Ja, Freitag 17 Uhr steht hier. Möchten Sie wechseln?"),
           L("Kunde", "m", "Geht auch Samstag? Da habe ich Zeit."),
           L("Empfangs-Dame", "f", "Samstag ist leider voll. Donnerstag wäre möglich."),
           L("Kunde", "m", "Gut, dann Donnerstag! Gleiche Uhrzeit?"),
           L("Empfangs-Dame", "f", "Ja, Donnerstag 17 Uhr. Bis dann!")],
          [L("Vater", "m", "Sohn, dein Bart muss weg vor dem Vorstellungsgespräch!"),
           L("Sohn", "m", "Aber Papa, Bart ist Trend! Nur trimmen reicht doch auch."),
           L("Vater", "m", "Trimmen reicht nicht. Das macht schlechten Eindruck beim Chef."),
           L("Sohn", "m", "Und behalten geht gar nicht? Wirklich nicht?"),
           L("Vater", "m", "Nein, also: Rasieren, bitte, noch heute!"),
           L("Sohn", "m", "Okay, okay, ich rasiere. Aber danach lasse ich ihn wieder wachsen!")]])

# ---------------- TEST 60 im-park-und-erholung ----------------
apply(60,
      t1={0: "Liebe Park-Besucher: Der Stadtpark hat neue Regeln. Hunde nur an der Leine — überall im Park, nicht nur am Spielplatz. "
             "Müll bitte in Eimer, nicht im Gras. Grillen erlaubt, aber nur am Grillplatz hinten. "
             "Also nicht überall und nicht gar nicht, nur am Grillplatz hinten. Wir wünschen einen schönen Aufenthalt!",
          1: "Hallo Lisa, hier ist Anna. Das Wetter ist super heute! Lass uns in den Park gehen — Picknick machen. "
             "Ich bringe Decke und Brote, du kannst Getränke holen. Nichts mitbringen geht nicht, wir brauchen Getränke. "
             "Treffen wir uns am Brunnen um 14 Uhr? Wenn Regen, sage ich Bescheid. Tschüs!",
          2: "Achtung Besucher: Der Spielplatz im Park ist wegen Renovierung geschlossen. "
             "Bis Juni dauert die Arbeit — neue Schaukeln, neuer Sandkasten. "
             "Der Park ist offen und das Café auch, nur der Spielplatz ist zu. "
             "Kinder können den anderen Spielplatz im West-Park benutzen. Wir entschuldigen uns für Unannehmlichkeiten. Sicherheit zuerst!",
          3: "Hi Markus, hier ist Tom. Pass auf, ich gehe heute Abend laufen im Park. "
             "Nicht spazieren und nicht Fahrrad fahren, wirklich laufen! Möchtest du mit? "
             "Ich habe Sportprogramm jeden zweiten Tag. Treffen 18 Uhr am Haupteingang. 5 Kilometer ungefähr. "
             "Wenn du nicht magst, ist okay. Aber lass mich wissen. Tschüs!",
          4: "Liebe Eltern: Im Park startet ab Mai ein Yoga-Kurs für Kinder, jeden Samstag 10 Uhr. "
             "Kostenlos, draußen unter Bäumen. Auch Kurs für Erwachsene um 11 Uhr — 10 Euro pro Stunde. "
             "Keine 20 Euro, nur 10 Euro pro Stunde für Erwachsene. "
             "Bitte mitbringen: Yoga-Matte, Wasser, bequeme Kleidung. Anmeldung nicht nötig!"},
      t2=[L("Anna", "f", "Markus, alle gehen heute in den Park! Was macht denn jeder?"),
          L("Markus", "m", "Lukas geht joggen, sportlich, 10 Kilometer jeden Tag. Wahnsinn, oder?"),
          L("Anna", "f", "Jeden Tag, wow! Und Lisa? Geht sie spazieren?"),
          L("Markus", "m", "Nein, nicht spazieren. Lisa fährt Fahrrad, entspannt, mit der Familie."),
          L("Anna", "f", "Mit der Familie, schön! Und Tom? Spielt er Fußball?"),
          L("Markus", "m", "Nein, kein Fußball. Tom liest auf einer Bank, Bücher, in einer ruhigen Ecke unter Bäumen."),
          L("Anna", "f", "Ruhig und gemütlich! Und Sara? Geht sie mit dem Hund?"),
          L("Markus", "m", "Nein, ohne Hund. Sara macht Picknick mit Freundinnen, mit Decke, Essen und Getränken."),
          L("Anna", "f", "Lecker! Und Tim? Frisbee oder Tai Chi?"),
          L("Markus", "m", "Weder noch. Tim spielt Fußball, informelle Spiele mit anderen Jungs, jeden Sonntag."),
          L("Anna", "f", "Jeden Sonntag! Und spazieren geht heute keiner?"),
          L("Markus", "m", "Doch, viele Leute spazieren. Aber von unseren Freunden geht keiner nur spazieren."),
          L("Anna", "f", "Verstehe! Dann gehen wir auch in den Park, einverstanden?"),
          L("Markus", "m", "Einverstanden! Wir nehmen Decke und Brote mit, wie Sara.")],
      t3=[[L("Tourist", "m", "Entschuldigung, wo ist der See im Park? Ist es weit?"),
           L("Mann", "m", "Geradeaus, dann links beim Café. Nicht weit, nur 5 Minuten? Nein, 10 Minuten zu Fuß."),
           L("Tourist", "m", "10 Minuten, gut. Und 20 Minuten wäre zu viel für mich."),
           L("Mann", "m", "Nein, keine 20 Minuten. Zehn Minuten, ganz gemütlich."),
           L("Tourist", "m", "Perfekt, danke! Dann gehe ich los.")],
          [L("Vater", "m", "Wo ist der Spielplatz? Bei den Schaukeln links?"),
           L("Mutter", "f", "Ja, dort. Die Kinder sind da sicher."),
           L("Vater", "m", "Ist der Boden hart oder aus Sand?"),
           L("Mutter", "f", "Weder hart noch Sand. Weicher Boden und hohe Zäune, keine Sorge."),
           L("Vater", "m", "Gut, dann spiele ich mit den Kindern. Wo sind die Bälle?")],
          [L("Frau", "f", "Guten Tag! Darf ich hier überall Fahrrad fahren?"),
           L("Wächter", "m", "Auf den Hauptwegen ja, überall leider nicht."),
           L("Frau", "f", "Auch im Gras? Das wäre schön weich."),
           L("Wächter", "m", "Nein, im Gras nicht, das ist neu. Nur auf den Wegen, das Gras ist verboten."),
           L("Frau", "f", "Verstanden! Nur Wege, kein Gras. Danke!")],
          [L("Tochter", "f", "Papa, ich habe Hunger, großen Hunger! Was gibt es am Café-Stand?"),
           L("Vater", "m", "Eis, Pommes und Wraps. Was möchtest du?"),
           L("Tochter", "f", "Kein Eis heute. Wraps oder Pommes?"),
           L("Vater", "m", "Wraps sind leider schon aus heute. Nur noch Pommes und Eis."),
           L("Tochter", "f", "Dann Pommes, bitte! Mit viel Ketchup, lecker!")],
          [L("Mann1", "m", "Wann sperrt der Park? Im Sommer um 23 Uhr?"),
           L("Wächter", "m", "Im Sommer 23 Uhr, im Winter 20 Uhr, genau."),
           L("Mann1", "m", "Und jetzt im April? Auch 20 Uhr?"),
           L("Wächter", "m", "Nein, nicht 20. Im April 21 Uhr, das ist Übergangszeit."),
           L("Mann1", "m", "21 Uhr, verstanden! Danke und tschüss!")]],
      t4=[L("Reporter", "m", "Frau Walter, was sind Ihre Aufgaben im Park?"),
          L("Walter", "f", "Ich kümmere mich um die Pflanzen und die Wege im ganzen Park. Viele Gärtner arbeiten bei mir, im Sommer auch Studenten."),
          L("Reporter", "m", "Wie viele Besucher kommen?"),
          L("Walter", "f", "Im Sommer sehr viele, im Winter viel weniger. Bei Regen fast niemand. Aber unser Park ist sehr beliebt bei Familien."),
          L("Reporter", "m", "Was sind die Probleme?"),
          L("Walter", "f", "Der Müll, ganz klar. Manche Leute werfen alles auf den Boden, Flaschen, Papier, alles. Das ärgert mich wirklich sehr."),
          L("Reporter", "m", "Welche Feste gibt es im Park? Ist im Sommer etwas los?"),
          L("Walter", "f", "Im Sommer ein großes Fest mit Musik und Essen, drei Tage lang. Auch ein Lauf geht durch den Park, im September."),
          L("Reporter", "m", "Wie sehen Sie die Zukunft?"),
          L("Walter", "f", "Parks werden immer wichtiger, nicht weniger! Die Stadt braucht Grün. Wir pflanzen jedes Jahr mehr Bäume, etwa hundert.")])

# ---------------- TEST 61 im-fitnessstudio ----------------
apply(61,
      t1={0: "Liebe Mitglieder: Unser Fitnessstudio hat ab Juni neue Öffnungszeiten. "
             "Werktags nun von 6 bis 23 Uhr, also abends länger. Nicht bis 20 und nicht bis 22, werktags bis 23 Uhr. "
             "Am Wochenende bleibt es bei 8 bis 20 Uhr. Die Sauna schließt aber immer eine Stunde früher als das Studio. "
             "Viel Spaß beim Training!",
          1: "Hallo Tom, hier ist Markus. Ich habe mich endlich im Fitnessstudio angemeldet! "
             "Aber nicht für Geräte, sondern für die Kurse — Spinning und Boxen. Sauna mag ich nicht so, ich nehme die Kurse. "
             "Möchtest du mitkommen? Erste Stunde ist gratis als Probe. Treffen wir uns Montag um 18 Uhr? Ruf zurück!",
          3: "Hi Lisa, hier ist Anna. Also, ich kündige meine Mitgliedschaft im Fitnessstudio. "
             "Nicht weil es schlecht ist — im Gegenteil. Aber ich ziehe um, zu weit weg jetzt. Zu teuer ist es nicht, wirklich nicht, nur zu weit weg nach dem Umzug. "
             "Schade, ich war gern dort. Suchst du nicht auch ein Studio? Vielleicht übernimmst du meinen Vertrag. Melde dich!"},
      t2=[L("Anna", "f", "Markus, alle gehen jetzt ins Fitnessstudio! Was macht denn jeder?"),
          L("Markus", "m", "Lukas macht Krafttraining, schwere Gewichte, große Muskeln. Typisch Lukas!"),
          L("Anna", "f", "Typisch, ja! Und Lisa? Auch Krafttraining?"),
          L("Markus", "m", "Nein, Lisa geht zum Spinning. Schnelles Radfahren mit Musik, dreimal pro Woche."),
          L("Anna", "f", "Dreimal pro Woche, sportlich! Und Tom? Auch Spinning?"),
          L("Markus", "m", "Nein, Tom macht Yoga. Entspannung gegen seinen Stress im Büro, zweimal pro Woche."),
          L("Anna", "f", "Yoga gegen Stress, gute Idee! Und Sara? Schwimmt sie noch?"),
          L("Markus", "m", "Ja, Sara schwimmt. Das Studio hat ein Becken, sie schwimmt jeden Morgen Bahnen."),
          L("Anna", "f", "Jeden Morgen, wow! Und Tim? Klettern oder Boxen?"),
          L("Markus", "m", "Tim boxt! Box-Kurs zweimal die Woche, sehr anstrengend, aber er liebt es."),
          L("Anna", "f", "Anstrengend, nichts für mich! Und Pilates oder Zumba macht keiner?"),
          L("Markus", "m", "Nein, Pilates mag keiner von uns. Zumba gibt es freitags, aber da hat keiner Zeit."),
          L("Anna", "f", "Schade! Und Laufband läuft auch keiner? Alles Kurse bei euch!"),
          L("Markus", "m", "Genau, alles Kurse! Komm doch mit, erste Stunde ist gratis, einverstanden?")],
      t3=[[L("Kundin", "f", "Guten Tag! Was kostet die Mitgliedschaft im Monat?"),
           L("Trainer", "m", "Der Basis-Tarif kostet 30 Euro, mit Kursen 45 Euro."),
           L("Kundin", "f", "Und mit Sauna? Wären das 55 Euro?"),
           L("Trainer", "m", "Genau, mit Sauna 55 Euro im Monat. Was darf es sein?"),
           L("Kundin", "f", "Ich nehme den Tarif mit Kursen für 45 Euro.")],
          [L("Mann", "m", "Entschuldigung, wo sind die Umkleidekabinen? Im ersten Stock?"),
           L("Trainerin", "f", "Nein, nicht im ersten Stock. Im Erdgeschoss, links neben der Sauna."),
           L("Mann", "m", "Und die Duschen? Im Keller vielleicht?"),
           L("Trainerin", "f", "Nein, kein Keller. Die Duschen sind gleich daneben in der Umkleide."),
           L("Mann", "m", "Alles klar! Erdgeschoss links. Vielen Dank!")],
          [L("Anfänger", "m", "Guten Tag! Ich bin neu hier. Wie oft soll ich trainieren?"),
           L("Trainer", "m", "Am Anfang dreimal die Woche, nicht jeden Tag."),
           L("Anfänger", "m", "Nicht jeden Tag? Wirklich nicht?"),
           L("Trainer", "m", "Nein, der Körper braucht Pausen. Einmal die Woche wäre zu wenig, dreimal ist perfekt."),
           L("Anfänger", "m", "Gut, dreimal die Woche! Ab Montag geht es los!")],
          [L("Frau", "f", "Guten Tag! Wann ist der Zumba-Kurs? Montags?"),
           L("Rezeption", "f", "Nein, nicht montags. Dienstags und donnerstags um 19 Uhr, mit Trainerin Julia."),
           L("Frau", "f", "Und freitags? Da hätte ich Zeit."),
           L("Rezeption", "f", "Freitags gibt es leider nur Pilates am Abend, kein Zumba."),
           L("Frau", "f", "Schade! Dann komme ich dienstags und donnerstags. Bis dann, danke!")],
          [L("Mitglied", "m", "Guten Tag! Mein Schließfach geht nicht auf. Nummer 42."),
           L("Trainerin", "f", "Nummer 42, alles klar. Ist sonst alles okay? Dusche warm, Geräte gut?"),
           L("Mitglied", "m", "Ja, Dusche warm und Geräte gut. Nur das Fach klemmt."),
           L("Trainerin", "f", "Gut, ich hole den Schlüssel. Einen Moment, bitte!"),
           L("Mitglied", "m", "Danke! Hoffentlich geht es schnell, ich habe Kurs.")]])

# ---------------- TEST 62 auf-dem-wochenmarkt ----------------
apply(62,
      t1={0: "Liebe Marktbesucher: Der Wochenmarkt findet ab April nicht mehr nur am Samstag statt, sondern auch mittwochs. "
             "Mittwochs aber kleiner — nur Obst, Gemüse und Blumen. Nur Fisch gibt es nie, mittwochs nur Obst, Gemüse und Blumen. "
             "Samstags wie immer das volle Angebot mit Käse, Fisch und Fleisch. Wir freuen uns auf euch!",
          1: "Hallo Mama, hier ist Anna. Ich bin auf dem Markt. Die Erdbeeren sind heute super günstig, eine Schale nur 2 Euro. "
             "Soll ich zwei nehmen? Und der Spargel ist auch da, aber teuer. Blumen kaufe ich nicht, nur Erdbeeren. "
             "Sag mir bitte schnell Bescheid, sonst sind die Erdbeeren weg. Tschüs!",
          2: "Achtung Kunden: Unser Fischstand bleibt heute geschlossen. Der Lieferwagen hatte eine Panne, leider kein frischer Fisch. "
             "Ab nächstem Samstag sind wir wieder da. Der Gemüsestand ist offen, nur der Fisch fehlt heute. "
             "Der Käsestand nebenan ist normal geöffnet. Wir bitten um Entschuldigung und danken für Ihr Verständnis!",
          3: "Hi Tom, hier ist Markus. Ich mache morgen ein großes Essen und brauche Hilfe beim Einkaufen auf dem Markt. "
             "Ich brauche frisches Gemüse und Kräuter — nicht aus dem Supermarkt, sondern vom Bauern direkt. "
             "Kein Fleisch und kein Brot, nur Gemüse und Kräuter. Kommst du mit um 9 Uhr? Der Markt ist früh am besten!",
          4: "Liebe Besucher: Am letzten Samstag im Monat gibt es ein Markt-Fest. "
             "Viele Stände bieten Kostproben gratis an, dazu Live-Musik. Für Kinder gibt es ein Karussell. Der Eintritt ist frei. "
             "Keine 5 Euro und keine 2 Euro, der Eintritt ist wirklich frei. "
             "Kommen Sie vorbei und probieren Sie regionale Produkte! Wir freuen uns!"},
      t2=[L("Anna", "f", "Markus, jeder kauft etwas anderes auf dem Markt! Was holt denn jeder?"),
          L("Markus", "m", "Lukas kauft immer frischen Fisch. Er kocht gern am Wochenende, tolle Rezepte."),
          L("Anna", "f", "Tolle Rezepte, lecker! Und Lisa? Auch Fisch?"),
          L("Markus", "m", "Nein, Lisa nimmt Blumen mit. Jeden Samstag ein frischer Strauß für die Wohnung."),
          L("Anna", "f", "Ein frischer Strauß, schön! Und Tom? Kauft er Eier?"),
          L("Markus", "m", "Eier auch, aber vor allem Käse. Tom liebt den Käse, er probiert immer verschiedene Sorten."),
          L("Anna", "f", "Verschiedene Sorten, interessant! Und Sara? Gemüse oder Obst?"),
          L("Markus", "m", "Sara kauft Obst, vor allem Beeren und Äpfel, direkt vom Bauern. Gemüse hat sie im Garten."),
          L("Anna", "f", "Im Garten, praktisch! Und Tim? Brot oder Honig?"),
          L("Markus", "m", "Tim holt Honig, vom Imker, immer ein großes Glas. Brot backt er selbst."),
          L("Anna", "f", "Selbst gebackenes Brot, wow! Und Fleisch und Wurst kauft keiner?"),
          L("Markus", "m", "Nein, Fleisch und Wurst diesmal nicht. Heute nur Fisch, Käse, Obst und Honig."),
          L("Anna", "f", "Alles frisch und regional! Gehen wir Samstag zusammen hin?"),
          L("Markus", "m", "Gute Idee! Um neun am Eingang, mit Fahrrad und Korb, einverstanden?")],
      t3=[[L("Kundin", "f", "Guten Tag! Was kostet das Kilo Tomaten?"),
           L("Händler", "m", "Normale 3 Euro 50, Bio-Tomaten 4 Euro. Zwei Kilo kosten 7 Euro 50."),
           L("Kundin", "f", "Dann ein Kilo Bio für 4 Euro, bitte."),
           L("Händler", "m", "Gern! Macht 4 Euro. Sonst noch etwas?"),
           L("Kundin", "f", "Nein danke, das ist alles. Tschüss!")],
          [L("Mann", "m", "Guten Tag! Sind die Äpfel aus der Region?"),
           L("Bäuerin", "f", "Ja, vom Hof gleich nebenan. Frisch von gestern!"),
           L("Mann", "m", "Und die Orangen? Auch aus der Region?"),
           L("Bäuerin", "f", "Die nicht, die kommen aus Spanien. Italien haben wir selten."),
           L("Mann", "m", "Gut, dann nehme ich zwei Kilo Äpfel aus der Region.")],
          [L("Frau", "f", "Guten Tag! Haben Sie noch Spargel? Weißen oder grünen?"),
           L("Händler", "m", "Der weiße ist leider aus. Nur noch grüner Spargel da."),
           L("Frau", "f", "Schade! Ganz ohne Spargel will ich nicht gehen."),
           L("Händler", "m", "Dann nehmen Sie grünen, der schmeckt auch gut. 5 Euro das Bund."),
           L("Frau", "f", "Gut, dann ein Bund grünen Spargel, bitte!")],
          [L("Kunde", "m", "Guten Tag! Wann bauen Sie morgens auf? Um 7 Uhr?"),
           L("Händlerin", "f", "Ja, wir sind ab 7 Uhr da. Um 12 Uhr ist am meisten los."),
           L("Kunde", "m", "Und wann ist Schluss? Wann packen Sie zusammen?"),
           L("Händlerin", "f", "Um 14 Uhr packen wir zusammen. Dann ist der Markt zu Ende."),
           L("Kunde", "m", "Verstanden, bis 14 Uhr! Danke und tschüss!")],
          [L("Tochter", "f", "Papa, darf ich den Honig probieren? Bitte!"),
           L("Vater", "m", "Frag den Imker. Und die Marmelade dort sieht auch gut aus."),
           L("Imker", "m", "Klar, hier ein Löffel Blütenhonig für dich!"),
           L("Tochter", "f", "Mmm, lecker! Den Honig nehmen wir, keine Marmelade!"),
           L("Vater", "m", "Und Käse nehmen wir auch noch mit. Zahlt der Papa.")]],
      t4=[L("Reporter", "m", "Frau Hofer, was verkaufen Sie auf dem Markt?"),
          L("Hofer", "f", "Alles von meinem eigenen Hof, nur das. Gemüse, Salate und im Sommer auch Beeren. Nichts dazu gekauft, alles selbst angebaut."),
          L("Reporter", "m", "Wie sieht Ihr Tag aus?"),
          L("Hofer", "f", "Sehr früh, wirklich. Ich stehe um vier Uhr auf, nicht erst um sieben, und fahre in die Stadt. Um sechs baue ich den Stand auf."),
          L("Reporter", "m", "Warum kaufen die Leute bei Ihnen?"),
          L("Hofer", "f", "Wegen der Frische, ganz klar. Mein Gemüse ist von gestern, nicht von letzter Woche wie im Supermarkt. Das schmeckt man."),
          L("Reporter", "m", "Ist es schwer, von einem kleinen Hof zu leben?"),
          L("Hofer", "f", "Ja, das ist es, sehr schwer. Ohne den Markt würden wir es nicht schaffen, das sage ich ehrlich. Der Hof allein reicht nicht."),
          L("Reporter", "m", "Was wünschen Sie sich für die Zukunft?"),
          L("Hofer", "f", "Dass mehr junge Leute wieder auf dem Markt einkaufen. Sie kochen wieder mehr selbst, das sehe ich. Das freut mich.")])

# ---------------- TEST 63 in-der-autowerkstatt ----------------
apply(63,
      t1={1: "Hallo Tom, hier ist Markus. Mein Auto macht ein komisches Geräusch beim Bremsen. "
             "Beim Starten ist alles normal, und beim Parken auch, nur beim Bremsen kracht es. "
             "Ich traue mich nicht mehr zu fahren. Kennst du eine gute Werkstatt? Nicht zu teuer, aber ehrlich. "
             "Die letzte hat mich abgezockt. Ruf mich an, ich brauche bald einen Termin. Danke!",
          2: "Achtung Kunden: Unsere Werkstatt macht vom 1. bis 14. August Betriebsferien. "
             "In dringenden Fällen — Panne oder Unfall — rufen Sie den Notdienst an, die Nummer steht an der Tür. "
             "Reifen wechseln geht vorher noch, nur in den Ferien nicht. "
             "Normale Termine wie Inspektion bitte erst ab dem 15. August. Wir wünschen schöne Ferien!",
          3: "Hi Lisa, hier ist Anna. Hör mal, mein Auto ist in der Werkstatt, dauert zwei Tage. "
             "Nicht einen Tag und keine Woche, genau zwei Tage. "
             "Kannst du mich morgen zur Arbeit fahren? Oder soll ich den Bus nehmen? "
             "Die Werkstatt bietet auch einen Ersatzwagen, aber der kostet extra. Sag mir Bescheid, was einfacher ist. Danke dir!",
          4: "Liebe Kunden: Ab Oktober bieten wir den Reifenwechsel im Paket an. "
             "Wechsel plus Einlagerung der Sommerreifen kostet zusammen 80 Euro. Nur der Wechsel allein 40 Euro. "
             "Keine 120 Euro, nur 80 Euro mit Einlagerung. "
             "Bitte buchen Sie früh einen Termin — im Herbst ist immer viel los. Wir freuen uns auf Sie!"},
      t2=[L("Anna", "f", "Markus, alle haben Probleme mit dem Auto! Was ist bei wem los?"),
          L("Markus", "m", "Bei Lukas ist die Batterie leer. Morgens springt das Auto nicht an, schrecklich."),
          L("Anna", "f", "Schrecklich, ja! Und Lisa? Springt ihr Auto an?"),
          L("Markus", "m", "Der Motor springt an, aber Lisa hat einen platten Reifen. Gestern über einen Nagel gefahren."),
          L("Anna", "f", "Über einen Nagel, ärgerlich! Und Tom? Auch Reifen?"),
          L("Markus", "m", "Nein, bei Tom funktioniert die Bremse nicht richtig. Gefährlich, er muss sofort in die Werkstatt."),
          L("Anna", "f", "Sofort, ja! Und Sara? Auch Bremse?"),
          L("Markus", "m", "Nein, Saras Auto verliert Öl. Jeden Morgen ein Fleck unter dem Wagen."),
          L("Anna", "f", "Ein Fleck, nicht gut! Und Tim? Verliert er auch Öl?"),
          L("Markus", "m", "Nein, bei Tim ist die Klimaanlage kaputt. Im Sommer schrecklich heiß im Auto."),
          L("Anna", "f", "Heiß im Sommer, arm! Und Licht und Scheibenwischer sind okay bei allen?"),
          L("Markus", "m", "Ja, Licht geht überall, Scheibenwischer auch. Nur der Auspuff von meinem Auto kracht ein bisschen."),
          L("Anna", "f", "Dein Auspuff auch! Dann fahren wir alle zusammen in die Werkstatt."),
          L("Markus", "m", "Gute Idee! Morgen um acht bei Müller, alle zusammen, einverstanden?")],
      t3=[[L("Kundin", "f", "Guten Tag! Wann ist mein Auto fertig? Um 12 Uhr?"),
           L("Mechaniker", "m", "Heute Nachmittag um 15 Uhr. Um 12 Uhr schaffen wir es nicht."),
           L("Kundin", "f", "Schade! Geht es nicht früher? Morgen wäre zu spät für mich."),
           L("Mechaniker", "m", "Nein, früher geht nicht. Wir brauchen das Ersatzteil, es kommt um zwei."),
           L("Kundin", "f", "Gut, dann komme ich um 15 Uhr. Bis später!")],
          [L("Mann", "m", "Guten Tag! Was kostet die Inspektion? Die große?"),
           L("Mechanikerin", "f", "Die kleine kostet 120 Euro, die große 250 Euro. 200 Euro gibt es nicht."),
           L("Mann", "m", "250 Euro, viel Geld! Welche brauche ich denn?"),
           L("Mechanikerin", "f", "Bei Ihrem alten Auto die große, sicher."),
           L("Mann", "m", "Na gut, dann die große für 250 Euro.")],
          [L("Kunde", "m", "Mein Auto zieht nach rechts. Ist es der Motor oder die Bremse?"),
           L("Mechaniker", "m", "Weder Motor noch Bremse. Die Spur muss eingestellt werden."),
           L("Kunde", "m", "Ist das schlimm? Teuer?"),
           L("Mechaniker", "m", "Nein, in einer Stunde erledigt. Kostet nur 50 Euro."),
           L("Kunde", "m", "Gut, dann machen Sie die Spur, bitte. Ich warte hier.")],
          [L("Frau", "f", "Guten Tag! Kann ich einen Ersatzwagen bekommen? Was kostet er pro Tag?"),
           L("Mechaniker", "m", "Ja, einen kleinen für 25 Euro am Tag. 15 Euro gibt es leider nicht."),
           L("Frau", "f", "Und einen größeren? Für 35 Euro vielleicht?"),
           L("Mechaniker", "m", "Nein, das ist schon der günstigste. Größere haben wir nicht frei."),
           L("Frau", "f", "Gut, dann den kleinen für 25 Euro, bitte!")],
          [L("Kunde", "m", "Macht ihr auch den TÜV? Wann kommt der Prüfer?"),
           L("Mechanikerin", "f", "Ja, der Prüfer kommt mittwochs. Nicht montags und nicht freitags."),
           L("Kunde", "m", "Mittwoch passt mir nicht. Brauche ich einen Termin?"),
           L("Mechanikerin", "f", "Ja, unbedingt. Ich trage Sie für nächsten Mittwoch ein."),
           L("Kunde", "m", "Gut, nächsten Mittwoch! Um wie viel Uhr?"),
           L("Mechanikerin", "f", "Um 10 Uhr. Bringen Sie die Papiere mit!")]],
      t4=[L("Reporterin", "f", "Herr Wolf, wie lange arbeiten Sie schon als Mechaniker?"),
          L("Wolf", "m", "Schon seit zwanzig Jahren, ja. Ich repariere jeden Tag Autos, alles Mögliche. Die Arbeit macht mir Spaß, immer noch."),
          L("Reporterin", "f", "Was reparieren Sie am häufigsten?"),
          L("Wolf", "m", "Meistens Bremsen und Reifen, das ist Standard. Fenster fast nie, vielleicht zweimal im Jahr. Im Winter sind oft die Batterien leer."),
          L("Reporterin", "f", "Müssen die Kunden lange warten?"),
          L("Wolf", "m", "Manchmal ja, einen Tag oder zwei. Aber bei einem Notfall helfe ich sofort, da warte ich nicht. Sicherheit zuerst."),
          L("Reporterin", "f", "Wie können die Kunden Geld sparen?"),
          L("Wolf", "m", "Sie sollen früh kommen, nicht erst spät. Ein kleines Problem ist billig, ein großes ist teuer. Das sage ich immer."),
          L("Reporterin", "f", "Was wünschen Sie sich von den Kunden?"),
          L("Wolf", "m", "Dass sie mir vertrauen. Ich zeige ihnen immer die kaputten Teile, ganz offen. Ich bin ehrlich, das ist mein Prinzip.")])

# ---------------- TEST 64 im-reisebuero ----------------
apply(64,
      t1={0: "Guten Tag, hier ist das Reisebüro Sonnenschein. Ihre Buchung nach Italien ist bestätigt. "
             "Aber Achtung: Der Flug geht nicht um 10 Uhr, sondern wurde auf 14 Uhr verschoben. "
             "Nicht um 17 Uhr, wirklich um 14 Uhr. Das Hotel und alles andere bleibt gleich. "
             "Bitte am Flughafen drei Stunden vorher da sein. Schöne Reise!",
          1: "Hallo Lisa, hier ist Anna. Ich war im Reisebüro und habe einen tollen Last-Minute-Urlaub gefunden. "
             "Eine Woche Griechenland, nur 400 Euro mit Flug und Hotel. Nicht Italien und nicht Spanien, wirklich Griechenland! "
             "Aber ich will nicht allein fahren. Hast du Lust und Zeit nächste Woche? Sag schnell Bescheid, das Angebot ist begrenzt!",
          2: "Achtung Kunden: Wegen eines Streiks bei der Fluggesellschaft fallen am Freitag viele Flüge aus. "
             "Wenn Sie am Freitag fliegen, rufen Sie uns bitte heute noch an. "
             "Fahren Sie nicht zum Flughafen und warten Sie nicht, rufen Sie heute an! "
             "Wir suchen eine andere Verbindung für Sie. Buchungen für andere Tage sind nicht betroffen. Danke für Ihr Verständnis!",
          3: "Hi Markus, hier ist Tom. Hey, ich plane eine Rundreise durch Deutschland mit dem Zug — keine Flüge, ist mir zu stressig. "
             "Nicht mit dem Flugzeug und nicht mit dem Auto, nur mit dem Zug. "
             "Das Reisebüro hat mir ein Bahn-Ticket für vier Wochen empfohlen. Möchtest du mit? "
             "Wir könnten viele Städte sehen. Überleg es dir, ruf zurück!",
          4: "Liebe Kunden: Wer früh bucht, spart Geld. Bei Buchung bis Ende Januar gibt es auf alle Sommerreisen 15 Prozent Frühbucherrabatt. "
             "Keine 10 und keine 20 Prozent, genau 15 Prozent. "
             "Außerdem ist die Reiserücktrittsversicherung kostenlos dabei. "
             "Kommen Sie vorbei und planen Sie schon jetzt Ihren Traumurlaub! Wir beraten Sie gern."},
      t2=[L("Anna", "f", "Markus, alle fahren dieses Jahr weg! Was hat denn jeder gebucht?"),
          L("Markus", "m", "Lukas macht einen Strandurlaub. Nur Sonne, Meer und Faulenzen, zwei Wochen."),
          L("Anna", "f", "Zwei Wochen Faulenzen, schön! Und Lisa? Auch Strand?"),
          L("Markus", "m", "Nein, Lisa bucht eine Kreuzfahrt. Mit dem Schiff durch das Mittelmeer, sieben Tage."),
          L("Anna", "f", "Sieben Tage Schiff, toll! Und Tom? Camping oder was?"),
          L("Markus", "m", "Kein Camping. Tom macht eine Städtereise, Museen, Kultur, viele alte Gebäude."),
          L("Anna", "f", "Kultur, interessant! Und Sara? Wellness-Urlaub vielleicht?"),
          L("Markus", "m", "Nein, kein Wellness. Sara fährt zum Wandern in die Berge, Natur und frische Luft."),
          L("Anna", "f", "Frische Luft, gesund! Und Tim? Auch Berge?"),
          L("Markus", "m", "Nein, Tim macht eine Safari in Afrika. Sein großer Traum, wilde Tiere sehen."),
          L("Anna", "f", "Wilde Tiere, Wahnsinn! Und Skiurlaub oder Fahrradtour macht keiner?"),
          L("Markus", "m", "Nein, Skiurlaub im Sommer geht nicht. Und Fahrradtour will keiner von uns."),
          L("Anna", "f", "Stimmt, im Sommer kein Ski! Und wir? Fahren wir auch weg?"),
          L("Markus", "m", "Ja! Wir machen Strandurlaub wie Lukas, einverstanden? Ich buche heute!")],
      t3=[[L("Kundin", "f", "Guten Tag! Was kostet die Reise pro Person im Doppelzimmer?"),
           L("Berater", "m", "Im Doppelzimmer 600 Euro, im Einzelzimmer 750 Euro. 650 Euro gibt es nicht."),
           L("Kundin", "f", "750 Euro allein? Das ist viel. Gibt es Rabatt?"),
           L("Berater", "m", "Leider nein. Einzelzimmer mit Zuschlag, genau 750 Euro."),
           L("Kundin", "f", "Na gut, dann Einzelzimmer für 750 Euro.")],
          [L("Mann", "m", "Guten Tag! Ist das Frühstück im Preis dabei?"),
           L("Beraterin", "f", "Ja, Frühstück ist inklusive. Aber nur das Frühstück, nichts anderes."),
           L("Mann", "m", "Und das Abendessen? Ist das auch dabei?"),
           L("Beraterin", "f", "Nein, das kostet extra, 20 Euro pro Tag. Mittagessen auch extra."),
           L("Mann", "m", "Verstanden, nur Frühstück! Das reicht mir.")],
          [L("Frau", "f", "Guten Tag! Brauche ich ein Visum für die Türkei?"),
           L("Berater", "m", "Nein, unbedingt kein Visum. Der Reisepass reicht völlig."),
           L("Frau", "f", "Wirklich nicht? Und wie lange darf ich bleiben?"),
           L("Berater", "m", "Bis zu 90 Tage ohne Visum, ganz legal."),
           L("Frau", "f", "90 Tage, das reicht völlig! Vielen Dank für die Auskunft!")],
          [L("Kunde", "m", "Guten Tag! Wann ist mein gebuchter Rückflug? Samstag?"),
           L("Beraterin", "f", "Am Sonntag um 18 Uhr. Nicht Samstag, wirklich Sonntag."),
           L("Kunde", "m", "Geht auch ein Tag später, also Montag?"),
           L("Beraterin", "f", "Ja, Montag geht auch, aber 50 Euro mehr."),
           L("Kunde", "m", "Nein, dann bleibe ich bei Sonntag um 18 Uhr. Danke!")],
          [L("Kundin", "f", "Guten Tag! Ich möchte eine Reise stornieren, nicht buchen."),
           L("Berater", "m", "Oh! Haben Sie eine Versicherung? Eine Reiserücktrittsversicherung?"),
           L("Kundin", "f", "Ja, die habe ich. Verlängern will ich sie nicht, wirklich stornieren."),
           L("Berater", "m", "Gut, dann bekommen Sie das Geld zurück. Kommen Sie morgen vorbei."),
           L("Kundin", "f", "Morgen? Geht auch heute? Ich habe Zeit."),
           L("Berater", "m", "Heute geht auch. Bringen Sie die Papiere mit!")]],
      t4=[L("Reporter", "m", "Frau Sommer, warum geht man noch ins Reisebüro?"),
          L("Sommer", "f", "Wegen der persönlichen Beratung, ganz klar. Im Internet ist man allein mit tausend Angeboten. Bei uns hilft ein Mensch, der alles kennt."),
          L("Reporter", "m", "Welche Reiseziele sind beliebt?"),
          L("Sommer", "f", "Spanien und Italien immer, das sind Klassiker. Aber auch ferne Länder wie Thailand kommen wieder, nach Corona besonders."),
          L("Reporter", "m", "Was ist der häufigste Fehler?"),
          L("Sommer", "f", "Die Leute buchen zu spät, das ist der Fehler. Dann ist alles teuer und voll. Wer früh bucht, spart Geld, manchmal die Hälfte."),
          L("Reporter", "m", "Reisen Sie selbst gern?"),
          L("Sommer", "f", "Ja, sehr, ich liebe Reisen. Am liebsten dorthin, wo wenige Touristen sind. Kleine Dörfer, Natur, Ruhe."),
          L("Reporter", "m", "Was raten Sie für die nächste Reise?"),
          L("Sommer", "f", "Probieren Sie etwas Neues, nicht immer das Gleiche. Und nehmen Sie nicht zu viel Gepäck mit, ein Koffer reicht.")])

print("58-64 applied")
