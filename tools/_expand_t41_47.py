#!/usr/bin/env python3
"""Expand Goethe A2 Hören tests 41-47 to official length. Temporary mutator."""
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


# ---------------- TEST 41 winter-und-skifahren ----------------
apply(41,
      t1={1: "Hallo Markus, hier ist Tom. Ich habe meine Skier vergessen — kannst du mir deine leihen? "
             "Im Geschäft kosten sie 30 Euro pro Tag, für eine Woche viel zu teuer. "
             "Deine alten Skier passen mir vielleicht. Einen Schlitten habe ich schon, aber damit fahre ich nicht gern. "
             "Bring die Skier morgen mit, wenn du kommst, okay? Danke!",
          3: "Hi Lisa, hier ist Anna. Hör mal, ich habe mir das Bein gebrochen beim Skifahren! "
             "Bin im Krankenhaus, Gipsbein für 6 Wochen. Zum Glück nur das Bein, nicht der Arm, und keine Erkältung dazu. "
             "Der Skiurlaub ist zu Ende. Komm mich bitte besuchen, Besuch wäre schön. "
             "Markus ist auch hier. Krankenhaus Innsbruck, Zimmer 304.",
          4: "Liebe Gäste des Hotel Bergblick: Die Skischule bietet jetzt neue Kurse an. "
             "Anfänger-Kurs morgen 9 Uhr, Mittelstufe 11 Uhr, Fortgeschrittene 14 Uhr. "
             "Der Kurs um 9 Uhr ist fast voll, also bitte schnell anmelden. "
             "Treffpunkt unten am Lift. Anmeldung an der Hotelrezeption. "
             "Preis 50 Euro pro Tag inklusive Mittagessen. Wir freuen uns!"},
      t2=[L("Anna", "f", "Markus, es ist endlich Winter! Was machen unsere Freunde eigentlich im Schnee? Erzähl mal."),
          L("Markus", "m", "Also, Lukas geht Snowboarden. Er hat sich extra ein neues Board gekauft, ziemlich teuer."),
          L("Anna", "f", "Cool! Und Lisa? Fährt sie noch Ski?"),
          L("Markus", "m", "Ja, Lisa fährt Ski, schon seit Kindheit, und sehr gut. Blaue und rote Pisten, keine schwarzen."),
          L("Anna", "f", "Verstehe. Und Tom? Der war doch nie ein Skifahrer, oder?"),
          L("Markus", "m", "Genau, Tom geht Schlittschuhlaufen, er liebt die Eisbahn in der Stadt. Zweimal pro Woche."),
          L("Anna", "f", "Zweimal pro Woche, wow! Und was macht Sara mit den Kindern?"),
          L("Markus", "m", "Sara fährt Schlitten mit ihren Kindern, am kleinen Hügel hinter dem Haus. Sportlichen Ehrgeiz hat sie nicht."),
          L("Anna", "f", "Klingt gemütlich. Und Tim? Immer noch Eishockey?"),
          L("Markus", "m", "Ja, Tim spielt Eishockey im Verein, und sie haben schon ein paar Turniere gewonnen."),
          L("Anna", "f", "Toll! Und du? Skispringen oder Langlauf wie früher?"),
          L("Markus", "m", "Nein, Skispringen ist mir zu gefährlich, und für Langlauf habe ich keine Zeit. Ich fahre nur ein bisschen Ski, ganz ruhig."),
          L("Anna", "f", "Dann gehen wir Samstag zusammen? Ich muss mir nur noch Skier leihen."),
          L("Markus", "m", "Gute Idee, am Samstag um zehn am Lift. Aber Eisklettern machen wir nicht, das ist Wahnsinn.")],
      t3=[[L("Kunde", "m", "Guten Tag! Was kostet ein Lift-Ticket für einen Tag? Wir sind eine Familie mit zwei Kindern."),
           L("Verkäuferin", "f", "Erwachsene zahlen 45 Euro, Kinder bis 14 Jahre 25 Euro. Zusammen wären das 140 Euro."),
           L("Kunde", "m", "140 Euro ist viel. Gibt es eine Familienkarte, vielleicht für 100 Euro?"),
           L("Verkäuferin", "f", "Für 100 Euro leider nicht, aber die Familienkarte kostet 120 Euro statt 140. Sie sparen 20 Euro."),
           L("Kunde", "m", "Gut, dann nehmen wir die Familienkarte für 120 Euro. Danke!")],
          [L("Skifahrerin", "f", "Guten Tag! Können Sie meine Skier reparieren? Die Bindung ist locker."),
           L("Techniker", "m", "Kein Problem, das geht schnell. In 15 Minuten schaffe ich es nicht, aber in 30 Minuten ja."),
           L("Skifahrerin", "f", "30 Minuten ist okay. Und was kostet das?"),
           L("Techniker", "m", "25 Euro. Eine Stunde dauert es sicher nicht, keine Sorge."),
           L("Skifahrerin", "f", "Gut, dann warte ich hier im Café. Bis gleich!")],
          [L("Mutter", "f", "Tim, es ist minus 10 Grad! Ziehst du die Mütze und den Schal an?"),
           L("Tim", "m", "Mama, mir ist nicht kalt. Der Schal kratzt so."),
           L("Mutter", "f", "Bitte beides, sonst wirst du krank!"),
           L("Tim", "m", "Okay, die Mütze ja, aber den Schal lasse ich hier."),
           L("Mutter", "f", "Na gut, aber die Mütze bleibt auf dem Kopf, versprochen?"),
           L("Tim", "m", "Versprochen! Tschüss, Mama!")],
          [L("Skifahrer1", "m", "Guten Morgen! Welche Piste fahren wir zuerst?"),
           L("Skifahrer2", "m", "Schwarz ist mir zu schwer heute, da habe ich Angst."),
           L("Skifahrer1", "m", "Gut, dann rot? Die rote Piste ist schön lang."),
           L("Skifahrer2", "m", "Rot ist okay, aber zum Warmwerden fahren wir erst blau, einverstanden?"),
           L("Skifahrer1", "m", "Einverstanden! Erst blau, dann rot. Viel Spaß!")],
          [L("Vater", "m", "Sara, möchtest du in die Skischule oder lieber mit uns Eltern fahren?"),
           L("Sara", "f", "In die Skischule! Da sind andere Kinder, das macht mehr Spaß."),
           L("Vater", "m", "Sicher? Wir zeigen dir auch gerne alles. Oder möchtest du Schlitten fahren?"),
           L("Sara", "f", "Nein, kein Schlitten. Ich will Ski lernen, mit Kindern zusammen."),
           L("Vater", "m", "Gut, dann melde ich dich an. Viel Spaß in der Skischule!")]])

# ---------------- TEST 42 geburtstag-und-geschenke ----------------
apply(42,
      t1={0: "Hallo Lisa, hier ist Anna. Der Geburtstag von Tom ist nächste Woche. "
             "Wir wollen ein Geschenk zusammen kaufen — was meinst du? Tom liebt ja Bücher. "
             "Oder vielleicht ein Konzert-Ticket? Eine CD hat er schon so viele. "
             "Eigentlich am besten Bücher, das ist sicher. Ruf zurück, dann gehen wir shoppen.",
          1: "Hi Markus, hier ist Sara. Mein Geburtstag ist am Samstag. Ich mache eine Party bei mir zu Hause, ab 19 Uhr. "
             "Bring bitte etwas zum Trinken mit, Essen mache ich selbst. Geschenke braucht ihr nicht mitbringen. "
             "Komm in normaler Kleidung, kein Anzug. Lass mich wissen, ob du kommst.",
          2: "Achtung, eine Erinnerung: Klein-Max wird am Sonntag fünf Jahre alt! "
             "Wir feiern im Restaurant Sonnenblume um 14 Uhr, die Feier dauert bis 17 Uhr. "
             "Kinder spielen draußen im Garten. Bitte keine Geschenke aus Plastik — Max hat schon zu viele Spielsachen. "
             "Bücher oder Kleidung sind willkommen.",
          3: "Liebe Tante Else, hier ist Anna. Dein Geburtstag — 70 Jahre, große Sache! "
             "Nicht 60 und noch nicht 80, genau richtig zum Feiern! "
             "Wir kommen alle: ich, Markus, die Kinder, sogar Onkel Hans aus Hamburg. "
             "Brauchst du Hilfe mit dem Essen? Wir können gerne kochen. Ruf an, sag was nötig ist. Bis Samstag, freue mich!",
          4: "Hallo Lisa, hier ist Mama. Hey, Papa hat doch Geburtstag morgen. Was schenken wir ihm? "
             "Eine Krawatte hat er schon zu viele. Ein Buch hat er schon selber gekauft. "
             "Ich denke, eine schöne Uhr wäre perfekt. Im Geschäft in der Stadt gibt es schöne Uhren. "
             "Was meinst du? Ruf bitte zurück."},
      t2=[L("Anna", "f", "Markus, schau mal, ich habe so viele Geschenke bekommen! Alles liegt noch auf dem Tisch."),
          L("Markus", "m", "Wow, cool! Von wem ist denn das schöne Halsband aus Silber?"),
          L("Anna", "f", "Von Lukas, er weiß genau, ich liebe Silberschmuck. Passt perfekt, oder?"),
          L("Markus", "m", "Sehr schön! Und das Buch da, dieser dicke Krimi?"),
          L("Anna", "f", "Das hat mir Lisa geschenkt. Sie hat ihn selbst gelesen und super gefunden."),
          L("Markus", "m", "Nett! Und das Parfüm? Riecht gut."),
          L("Anna", "f", "Das ist von Tom, mein Lieblingsparfüm. Er hat es sich gemerkt, stell dir vor!"),
          L("Markus", "m", "Toll! Eine Konzertkarte hast du nicht bekommen? Du gehst doch so gern ins Konzert."),
          L("Anna", "f", "Nein, leider keine Konzertkarte. Aber schau, die Blumen! Ein großer Strauß mit 30 roten Rosen."),
          L("Markus", "m", "30 Rosen, Wahnsinn! Von Sara, oder?"),
          L("Anna", "f", "Ja, von Sara. Und die Schokolade ist von Tim, eine Riesen-Box aus Belgien."),
          L("Markus", "m", "Belgische Schokolade, lecker! Und Wein oder Geld gab es nicht?"),
          L("Anna", "f", "Nein, kein Wein und kein Geld. Aber ich freue mich über alles, wirklich!"),
          L("Markus", "m", "Das glaube ich! Komm, wir machen Kaffee, und du zeigst mir alles noch einmal.")],
      t3=[[L("Kundin", "f", "Guten Tag! Ich suche ein Geschenk für meine 16-jährige Tochter."),
           L("Verkäufer", "m", "Wie wäre es mit Schmuck? Oder ein schönes Parfüm?"),
           L("Kundin", "f", "Schmuck hat sie schon genug. Und Parfüm mag sie gar nicht. Vielleicht ein nettes Top?"),
           L("Verkäufer", "m", "Gute Idee! Wir haben tolle neue Tops da. Welche Größe?"),
           L("Kundin", "f", "Größe 38, bitte. Das Top gefällt ihr sicher.")],
          [L("Sohn", "m", "Mama, was wünschst du dir zum Geburtstag? Ein Geschenk?"),
           L("Mutter", "f", "Nichts Materielles, mein Schatz. Lieber ein gemeinsames Essen im Restaurant."),
           L("Sohn", "m", "Oder ich koche selbst für dich? Das wäre billiger."),
           L("Mutter", "f", "Nein, du kochst sowieso nie, das dauert zu lange. Gehen wir ins Restaurant!"),
           L("Sohn", "m", "Gut, dann lade ich dich am Samstag ins Restaurant ein.")],
          [L("Vater", "m", "Lukas wird 10 Jahre alt. Welchen Kuchen backen wir?"),
           L("Mutter", "f", "Schokolade oder Erdbeere? Was meinst du?"),
           L("Vater", "m", "Schokolade hatte er letztes Jahr. Lieber etwas Neues."),
           L("Mutter", "f", "Vanille mag er nicht so. Dann nehmen wir Erdbeere, einverstanden?"),
           L("Vater", "m", "Einverstanden! Ich kaufe morgen frische Erdbeeren auf dem Markt, und wir backen zusammen.")],
          [L("Lisa", "f", "Tom, danke für die Einladung zur Party am Samstag!"),
           L("Tom", "m", "Bitte! Kommst du? Es wird lustig."),
           L("Lisa", "f", "Eigentlich ja, aber meine Mutter ist plötzlich krank geworden."),
           L("Tom", "m", "Oh, das tut mir leid. Dann kommst du später nach, oder?"),
           L("Lisa", "f", "Nein, das geht leider nicht. Aber ich schicke dein Geschenk per Post, versprochen!"),
           L("Tom", "m", "Verstehe, kein Problem. Gute Besserung für deine Mutter!")],
          [L("Anna", "f", "Wo machen wir Saras Geburtstag? Hast du eine Idee?"),
           L("Markus", "m", "Im Restaurant? Oder lieber zu Hause bei uns?"),
           L("Anna", "f", "Das Restaurant ist zu teuer, und zu Hause ist zu wenig Platz."),
           L("Markus", "m", "Dann machen wir ein Picknick im Park! Das ist kostenlos und draußen."),
           L("Anna", "f", "Gute Idee! Im Park, wenn das Wetter gut ist. Ich bringe Kuchen mit.")]],
      t4=[L("Reporter", "m", "Frau Klingmann, Sie planen seit 15 Jahren Geburtstagspartys. Wie sind Sie zu diesem Beruf gekommen?"),
          L("Klingmann", "f", "Ich habe schon als Studentin gerne Partys für Freunde organisiert. Dann hat mich eine Bekannte gefragt — die Tochter wurde 18, große Party. Ich habe alles geplant, war ein Erfolg. Daraus wurde mein Geschäft."),
          L("Reporter", "m", "Welche Partys planen Sie am häufigsten?"),
          L("Klingmann", "f", "Kinder-Geburtstage am meisten, etwa die Hälfte. Dann 18. und 50. Geburtstage — runde Zahlen. Hochzeiten mache ich auch, aber das ist anders, viel mehr Stress."),
          L("Reporter", "m", "Was kostet eine Party im Durchschnitt?"),
          L("Klingmann", "f", "Sehr unterschiedlich, kleine Kinder-Party 300 Euro. Größere Erwachsenen-Feiern 2000 bis 5000 Euro. Manche Kunden geben aber auch 10.000 Euro aus — sehr exklusiv. Das ist aber selten."),
          L("Reporter", "m", "Was ist der häufigste Wunsch?"),
          L("Klingmann", "f", "Ein Thema — Märchen für Kinder, 80er-Jahre für Erwachsene, irgendwas Spezielles. Standard-Party will keiner mehr. Auch DIY-Elemente sind beliebt — Bastel-Tisch für Kinder, zum Beispiel."),
          L("Reporter", "m", "Wenn Sie selbst Geburtstag haben? Planen Sie da eine große Feier?"),
          L("Klingmann", "f", "Nein, wirklich nicht. Keine große Feier, keine 100 Gäste. Beruflich habe ich genug Partys. Privat bin ich mit Familie im Restaurant — einfach. Wir essen, lachen, mehr nicht.")])

# ---------------- TEST 43 reise-mit-dem-auto ----------------
apply(43,
      t1={0: "Achtung Autofahrer auf der A8: Wir haben einen Stau auf 15 Kilometer wegen eines Unfalls. "
             "Die linke Spur ist gesperrt. Bitte mit 50 km/h fahren. "
             "Bitte bleiben Sie nicht auf der A8 stehen, wir empfehlen die Ausfahrt Ulm — über die Landstraße kommt ihr 30 Minuten schneller voran. "
             "Und machen Sie später eine Pause an der Raststätte.",
          1: "Hallo Lisa, hier ist Anna. Du, ich stehe im Stau auf der Autobahn. Komme später, etwa 18 Uhr statt 17. Sorry! "
             "Spätestens um 19 Uhr bin ich sicher da, versprochen. "
             "Bitte fang ohne mich mit dem Essen an. Tom kommt pünktlich. Ich rufe wieder an, wenn ich näher bin. Bis später, freu mich!",
          2: "Hi Markus, mein Auto ist kaputt. Die Batterie ist tot — heute Morgen wollte ich starten, nichts. "
             "Der Motor ist in Ordnung und die Reifen sind neu, nur die Batterie ist tot. "
             "Kannst du mich am Bahnhof abholen um 15 Uhr? Nehme den Zug ins Büro. "
             "Sonst muss ich Taxi nehmen, viel zu teuer. Ruf bitte zurück, danke!",
          3: "Liebe Kunden des Park-Hauses Sonne: Ab Montag haben wir neue Preise. Stunde 3 Euro statt 2 Euro 50. "
             "Tagesticket 25 Euro statt 22. Monatskarte 200 Euro statt 180. Wer länger als eine Woche parkt, zahlt pauschal 30 Euro extra. "
             "Wir entschuldigen uns für die Erhöhung — wegen steigender Kosten unvermeidlich. Vielen Dank.",
          4: "Hallo Tom, hier ist Vater. Ich brauche das Auto morgen — habe Termin beim Arzt. "
             "Nicht zum Einkaufen und nicht für deine Treffen mit Freunden, nur für den Arzt. "
             "Du musst mit dem Bus fahren ins Büro, sorry. Oder Fahrrad, falls Wetter gut ist. "
             "Auf jeden Fall: Auto bleibt bei mir. Frag bitte nicht. Ruf zurück, wenn Probleme."},
      t2=[L("Anna", "f", "Markus, hast du gehört? Alle haben dieses Jahr neue Autos gekauft! Erzähl mal."),
          L("Markus", "m", "Ja! Lukas hat einen BMW gekauft, sportlich und schnell. Sein Traum schon lange."),
          L("Anna", "f", "Ein BMW, nicht schlecht! Und Lisa?"),
          L("Markus", "m", "Lisa fährt jetzt einen Tesla, ein Elektroauto. Sehr modern und umweltfreundlich."),
          L("Anna", "f", "Ein Tesla, cool! Und Tom? Der braucht doch viel Platz."),
          L("Markus", "m", "Genau, Tom hat einen VW Bus für Familienreisen mit drei Kindern. Praktisch, oder?"),
          L("Anna", "f", "Sehr praktisch! Und Sara? Fährt sie noch den alten Ford?"),
          L("Markus", "m", "Nein, kein Ford mehr. Sara hat jetzt einen Mini Cooper, klein und süß, perfekt für die Stadt."),
          L("Anna", "f", "Süß! Und Tim? Immer noch Audi oder Opel?"),
          L("Markus", "m", "Weder Audi noch Opel. Tim hat sich einen Mercedes geleistet, fürs Geschäftsleben, repräsentativ."),
          L("Anna", "f", "Ein Mercedes, wow! Und Porsche fährt keiner, oder?"),
          L("Markus", "m", "Nein, Porsche ist zu teuer für uns alle. Vielleicht später einmal."),
          L("Anna", "f", "Und du? Bleibst du bei deinem alten Auto?"),
          L("Markus", "m", "Ja, meins fährt noch gut. Aber am Wochenende waschen wir alle Autos zusammen, okay?")],
      t3=[[L("Kundin", "f", "Guten Tag! Volltanken, bitte."),
           L("Tankwart", "m", "Gerne! Diesel oder Super? Wir haben auch Strom für Elektroautos."),
           L("Kundin", "f", "Super, bitte. Kein Diesel, ich fahre Benziner."),
           L("Tankwart", "m", "Alles klar, Super! Das macht 75 Euro 50, bitte."),
           L("Kundin", "f", "Mit Karte, bitte. Und die Scheiben kurz putzen? Danke!")],
          [L("Fahrerin", "f", "Wie lange dauert die Fahrt nach München ohne Pausen?"),
           L("Beifahrer", "m", "Ohne Stau etwa 3 Stunden, ganz direkt."),
           L("Fahrerin", "f", "Und mit Pausen? Vier Stunden oder fünf?"),
           L("Beifahrer", "m", "Mit einer Pause vier Stunden. Fünf Stunden brauchen wir sicher nicht."),
           L("Fahrerin", "f", "Gut, dann fahren wir direkt. In drei Stunden sind wir da!")],
          [L("Vater", "m", "Lukas, bitte schnall dich an, wir fahren los!"),
           L("Lukas", "m", "Papa, es ist doch nicht weit. Muss das sein?"),
           L("Vater", "m", "Ja, immer! Wir steigen jetzt nicht mehr aus, der Gurt bleibt an. Sicherheit zuerst!"),
           L("Lukas", "m", "Okay, okay, ich tu es ja schon. Brauche ich auch einen Helm?"),
           L("Vater", "m", "Nein, Helm nur fürs Fahrrad. Der Gurt reicht im Auto.")],
          [L("Werkstattmeisterin", "f", "Guten Tag! Ihr Auto ist fertig, neue Bremsen, Service erledigt."),
           L("Kunde", "m", "Schön! Wie viel kostet das? 500 Euro?"),
           L("Werkstattmeisterin", "f", "Leider mehr, 650 Euro. Die alten Bremsen waren schlimmer als gedacht."),
           L("Kunde", "m", "650 Euro! Und 750 wären es nicht, oder?"),
           L("Werkstattmeisterin", "f", "Nein, keine 750. Genau 650 Euro, mit Rechnung."),
           L("Kunde", "m", "Okay, Sicherheit zählt. Hier ist meine Karte.")],
          [L("Tochter", "f", "Papa, fährst du mich heute mit dem Auto zur Schule?"),
           L("Vater", "m", "Heute kann ich leider nicht. Nimm den Bus oder das Fahrrad."),
           L("Tochter", "f", "Das Fahrrad geht nicht, es regnet. Und der Bus dauert so lange."),
           L("Vater", "m", "Trotzdem, heute musst du den Bus nehmen. Morgen fahre ich dich wieder."),
           L("Tochter", "f", "Na gut, dann nehme ich den Bus. Tschüss, Papa!")]])

# ---------------- TEST 44 musik-und-konzerte ----------------
apply(44,
      t1={0: "Liebe Konzert-Besucher: Das Rock-Konzert mit der Band Silbermond ist verschoben! "
             "Wegen Krankheit der Sängerin neuer Termin: Samstag, 15. März, 20 Uhr, gleicher Ort. "
             "Es ist nicht abgesagt, es findet nur später statt, also fast wie geplant. "
             "Tickets bleiben gültig. Wer nicht kommen kann, bekommt sein Geld zurück. "
             "Wir entschuldigen uns für die Umstände.",
          1: "Hallo Tom, hier ist Lisa. Ich habe zwei Karten für das Jazz-Konzert am Freitag — meine Schwester kann nicht. "
             "Möchtest du mit? Eintritt ist gratis für dich, ich lade dich ein. "
             "Verkaufen will ich die Karten nicht, und verschenken auch nicht an Fremde, ich lade dich ein. "
             "Ruf bitte zurück bis morgen. Sonst frage ich Anna. Würde mich freuen!",
          2: "Achtung Musik-Schüler: Der Klavier-Unterricht morgen fällt aus. Lehrer Schmidt ist krank. "
             "Neuer Termin: nächsten Mittwoch um 16 Uhr, gleicher Raum. "
             "Wer einen anderen Lehrer sucht, soll bitte bei der Schule anrufen für einen anderen Termin. "
             "Hausaufgaben bitte trotzdem machen für nächstes Mal.",
          3: "Hi Markus, ich habe ein neues Instrument gekauft! Schon immer wollte ich Gitarre spielen, jetzt ist es so weit. "
             "Kein Klavier und keine Geige, eine Gitarre musste es sein. "
             "Habe einen guten Lehrer gefunden — Privat-Unterricht, einmal die Woche. Sehr nett. "
             "Du musst kommen und zuhören. Ehrlich, du wirst lachen, ich bin noch schlecht!",
          4: "Liebe Hörer, in der Mediathek finden Sie ab heute neue klassische Musik kostenlos: "
             "Beethoven Symphonien, Mozart Konzerte, Bach Klavierwerke. Auch moderne Komponisten wie Glass sind dabei. "
             "Login mit Ihrer Bibliotheks-Karte. Nicht unbegrenzt und keine zehn Alben, genau fünf Alben pro Monat. "
             "Viel Spaß beim Hören!"},
      t2=[L("Anna", "f", "Markus, was hört eigentlich jeder für Musik? Erzähl mal!"),
          L("Markus", "m", "Lukas liebt Rock-Musik, laut und hart, AC/DC und so, schon seit der Schule."),
          L("Anna", "f", "Typisch Lukas! Und Lisa? Immer noch Klassik?"),
          L("Markus", "m", "Ja, Lisa hört nur klassische Musik, Beethoven, Mozart, Bach, jeden Abend."),
          L("Anna", "f", "Jeden Abend, schön! Und Tom? Jazz oder eher Pop?"),
          L("Markus", "m", "Tom mag Jazz, Improvisationen und Saxophon-Solos. Pop hört er fast nie."),
          L("Anna", "f", "Verstehe. Und Sara? Die tanzt doch immer mit Kopfhörern."),
          L("Markus", "m", "Genau, Sara liebt Hip-Hop, Rapper und Beats, überall mit Kopfhörern."),
          L("Anna", "f", "Und Tim? Geht er noch oft zu Festivals?"),
          L("Markus", "m", "Ja, Tim hört nur Elektro, Techno und House. Nächstes Wochenende wieder Festival."),
          L("Anna", "f", "Cool! Und Country oder Volksmusik hört keiner von euch?"),
          L("Markus", "m", "Nein, Country mag keiner, und Volksmusik auch nicht. Reggae manchmal im Sommer, aber selten."),
          L("Anna", "f", "Dann machen wir am Samstag eine Party bei mir, und jeder bringt seine Lieblingsmusik mit!"),
          L("Markus", "m", "Gute Idee! Aber bitte kein Reggae die ganze Nacht, einverstanden?")],
      t3=[[L("Kundin", "f", "Guten Tag! Ich suche zwei Karten für Beethoven am Samstag."),
           L("Verkäufer", "m", "Vorne ist leider alles ausverkauft. Mittlere Plätze gibt es auch keine mehr."),
           L("Kundin", "f", "Schade! Was haben Sie denn noch?"),
           L("Verkäufer", "m", "Nur noch hintere Plätze für 25 Euro pro Karte."),
           L("Kundin", "f", "Gut, dann nehme ich zwei hintere Plätze. Danke!")],
          [L("Sohn", "m", "Mama, ich möchte ein Instrument lernen!"),
           L("Mutter", "f", "Schön! Welches denn? Gitarre oder Schlagzeug?"),
           L("Sohn", "m", "Schlagzeug! Das ist laut und cool!"),
           L("Mutter", "f", "Zu laut für die Wohnung! Wie wäre es mit Klavier?"),
           L("Sohn", "m", "Na gut, dann lerne ich Klavier. Ab wann?"),
           L("Mutter", "f", "Ab Montag, ich melde dich heute noch an.")],
          [L("Junge", "m", "Papa, wann ist das Konzert heute Abend?"),
           L("Vater", "m", "Um 19 Uhr. Freust du dich schon?"),
           L("Junge", "m", "Ja! Wo ist es, im Stadion oder in der Halle?"),
           L("Vater", "m", "Weder noch, es ist Open Air im Stadtpark."),
           L("Junge", "m", "Cool, im Park! Darf ich Freunde mitbringen?"),
           L("Vater", "m", "Klar, frag sie schnell. Wir gehen um halb sieben los.")],
          [L("Anna", "f", "Markus, hörst du morgens gerne Radio in der Küche?"),
           L("Markus", "m", "Nein, Radio mag ich nicht. Ich höre lieber Streaming, Spotify."),
           L("Anna", "f", "Kostenlos oder bezahlt? Da gibt es doch Werbung."),
           L("Markus", "m", "Premium, für 10 Euro im Monat. Ganz ohne Werbung."),
           L("Anna", "f", "Verstehe! Und CDs hast du gar keine mehr?"),
           L("Markus", "m", "Doch, ein paar alte CDs im Regal, aber ich höre sie nie.")],
          [L("Verkäuferin", "f", "Guten Tag! Suchen Sie eine Schallplatte oder eine CD?"),
           L("Kunde", "m", "Eine Schallplatte, bitte. Ich habe einen Plattenspieler von meinem Opa."),
           L("Verkäuferin", "f", "Schön! Welcher Künstler soll es sein? Auch ein Buch über Musik?"),
           L("Kunde", "m", "Nein, kein Buch, nur die Platte. Haben Sie Beatles?"),
           L("Verkäuferin", "f", "Ja, hier bitte. Das macht 20 Euro.")]])

# ---------------- TEST 45 im-museum ----------------
apply(45,
      t1={0: "Liebe Museums-Besucher: Das Naturkunde-Museum hat ab Montag neue Öffnungszeiten. "
             "Wir sind nicht mehr Montag bis Sonntag offen, sondern Dienstag bis Sonntag, jeweils 10 bis 18 Uhr. "
             "Nicht Sonntag und nicht Mittwoch, nur Montag ist Ruhetag. "
             "Eintritt 8 Euro für Erwachsene. Kinder unter 12 sind frei.",
          1: "Hallo Lisa, hier ist Anna. Pass auf, das neue Kunst-Museum in der Stadt eröffnet am Samstag! "
             "Es schließt nicht und ist nicht umgezogen, es ist ganz neu! "
             "Eintritt ist die erste Woche frei. Lass uns hingehen, vielleicht Samstag oder Sonntag. "
             "Wir können auch ins Café danach. Ruf mich an, wir machen Termin. Bis bald!",
          2: "Achtung Besucher: Im Saal 7, der ägyptischen Sammlung, ist die Klimaanlage kaputt. "
             "Es ist sehr warm dort heute. Die Beleuchtung geht noch, und der Saal ist nicht gesperrt. "
             "Wir empfehlen einen kurzen Besuch oder zuerst andere Räume. Reparatur kommt morgen. "
             "Wir entschuldigen uns. Saal 7 bleibt geöffnet, aber Vorsicht.",
          3: "Liebe Schulklasse 5A: Eure Führung im Museum startet pünktlich um 10 Uhr. Treffpunkt am Haupteingang. "
             "Eine Kamera braucht ihr nicht mitbringen, nur ein kleines Notebook für Notizen. "
             "Mittagessen gibt es um 12 Uhr im Café. Achtet bitte auf Ruhe — andere Besucher sind auch da. Bis morgen!",
          4: "Hi Markus, hier ist Tom. Ich habe meine Museumskarte verloren. "
             "Nicht vergessen, wirklich verloren. Und krank bin ich auch nicht. "
             "Habe schon angerufen, sie machen Ersatz. Aber dauert eine Woche. "
             "Heute kann ich nicht mit ins Museum, Eintritt zu teuer ohne Karte. Geh ohne mich, sorry. Nächste Woche dann zusammen."},
      t2=[L("Anna", "f", "Markus, wir planen eine Museums-Tour mit allen. Was mag denn jeder?"),
          L("Markus", "m", "Lukas liebt Geschichte, alte Schlachten, Könige und das Mittelalter."),
          L("Anna", "f", "Geschichte, spannend! Und Lisa? Klassische Kunst oder modern?"),
          L("Markus", "m", "Lisa mag moderne Kunst, Picasso, Warhol, Banksy. Klassische Kunst findet sie langweilig."),
          L("Anna", "f", "Okay! Und Tom? Der liebt doch Tiere, oder?"),
          L("Markus", "m", "Genau, Tom interessiert sich für Naturkunde, Tiere, Pflanzen und Dinosaurier."),
          L("Anna", "f", "Dinosaurier, cool! Und Sara? Immer noch Ägypten?"),
          L("Markus", "m", "Ja, Sara liebt Ägypten, Pharaonen, Mumien, Pyramiden. Sehr fasziniert seit Jahren."),
          L("Anna", "f", "Seit Jahren, wow! Und Tim? Sport oder Technik?"),
          L("Markus", "m", "Tim mag das Technik-Museum, alte Maschinen, Autos und Flugzeuge. Sport im Museum gibt es ja nicht."),
          L("Anna", "f", "Stimmt! Und Musik und Mode interessieren keinen von euch?"),
          L("Markus", "m", "Nein, Musik hören wir lieber zu Hause, und Mode ist nichts für uns."),
          L("Anna", "f", "Gut, dann gehen wir Samstag zuerst in die Geschichte und danach zu den Mumien!"),
          L("Markus", "m", "Einverstanden! Treffpunkt um zehn am Haupteingang, jeder kauft seine Karte selbst.")],
      t3=[[L("Besucher", "m", "Guten Tag! Was kostet der Eintritt für Erwachsene?"),
           L("Kassiererin", "f", "Erwachsene zahlen 10 Euro, ermäßigt 6 Euro. Kostenlos ist es leider nie."),
           L("Besucher", "m", "Ich bin Student. Zahle ich auch 6 Euro?"),
           L("Kassiererin", "f", "Ja, mit Studentenkarte zahlen Sie 6 Euro, bitte schön."),
           L("Besucher", "m", "Gut, hier ist meine Karte. Vielen Dank!")],
          [L("Touristin", "f", "Entschuldigung, wo finde ich die Picasso-Ausstellung?"),
           L("Mitarbeiter", "m", "Im ersten Stock, Saal 5. Nehmen Sie die Rolltreppe oder den Aufzug."),
           L("Touristin", "f", "Gut, dann nehme ich den Aufzug."),
           L("Mitarbeiter", "m", "Oh, der Aufzug ist heute kaputt. Bitte nehmen Sie die Treppe."),
           L("Touristin", "f", "Na gut, dann die Treppe. Vielen Dank!")],
          [L("Tochter", "f", "Papa, kann ich hier ein Foto machen?"),
           L("Vater", "m", "Frag bitte die Mitarbeiterin, ich weiß es nicht."),
           L("Mitarbeiterin", "f", "Fotografieren ist erlaubt, aber bitte ohne Blitz. Und leise sprechen, ja?"),
           L("Tochter", "f", "Okay, ohne Blitz und ganz leise. Schau, so mache ich es."),
           L("Mitarbeiterin", "f", "Perfekt! Viel Spaß im Museum!")],
          [L("Besucher1", "m", "Wie lange dauert die Führung durch das Museum?"),
           L("Führerin", "f", "Normalerweise 60 Minuten, mit allen Sälen."),
           L("Besucher1", "m", "Das ist zu lang. Gibt es eine kurze Version?"),
           L("Führerin", "f", "Ja, 30 Minuten nur mit den Highlights. Oder gar keine Führung, nur Audio-Guide."),
           L("Besucher1", "m", "Dann nehmen wir die kurze Führung für 30 Minuten.")],
          [L("Mutter", "f", "Klein-Lukas, sei vorsichtig! Fass nichts an!"),
           L("Mitarbeiter", "m", "Bitte das Kunstwerk nicht berühren! Er hat es angefasst!"),
           L("Mutter", "f", "Oh nein, Entschuldigung! Er hat es nicht gewusst. Er hat nichts zerbrochen, oder?"),
           L("Mitarbeiter", "m", "Nein, nichts zerbrochen, alles gut. Und geschrien hat er auch nicht, braver Junge."),
           L("Mutter", "f", "Komm, Lukas, wir schauen nur noch mit den Augen.")]])

# ---------------- TEST 46 am-bahnhof ----------------
apply(46,
      t1={0: "Achtung Reisende: Der ICE 723 nach Hamburg fährt heute nicht von Gleis 5, sondern von Gleis 12. "
             "Nicht Gleis 2, wirklich Gleis 12, bitte aufpassen. "
             "Wir bitten alle Fahrgäste, zum neuen Gleis zu gehen. Die Abfahrt ist pünktlich um 14 Uhr 30. "
             "Wir entschuldigen uns für die Umstände. Vielen Dank.",
          1: "Hallo Lisa, hier ist Anna. Also, mein Zug ist verspätet — komme zwei Stunden später. "
             "Statt 16 Uhr bin ich erst um 18 Uhr da. Sorry! Um 20 Uhr wäre zu spät, aber 18 Uhr klappt sicher. "
             "Geh nicht hungrig — iss schon. Ich nehme dann später was im Restaurant. Hol mich aber bitte ab. Bis dann!",
          2: "Liebe Reisende: Die Bahnhofs-Information ist nicht mehr im ersten Stock, sondern direkt am Haupteingang. "
             "Nicht im Keller und nicht mehr oben, direkt am Eingang. "
             "Geöffnet von 6 bis 22 Uhr täglich. Tickets, Auskunft, Lost-and-Found — alles dort. "
             "Wir haben das geändert für bessere Erreichbarkeit. Vielen Dank für Ihre Aufmerksamkeit.",
          3: "Hi Markus, hier ist Tom. Ich habe mein Bahnticket verloren! "
             "Nicht vergessen, wirklich verloren. Der Zug ist zum Glück noch nicht weg. "
             "Komme nicht in den Zug. Muss neues kaufen, kostet 80 Euro. Ärgerlich! "
             "Bin später zu dir, hole Ticket erst. Ruf mich an. Vielleicht hast du Idee. Sonst halt teurer. Stress total.",
          4: "Achtung am Bahnhof: Wegen Bauarbeiten ist der Aufzug zum Gleis 8 außer Betrieb. "
             "Gleis 8 ist offen, nur der Aufzug ist kaputt. "
             "Reisende mit Koffern oder Kinderwagen können den Aufzug am Gleis 6 nehmen, dann über die Brücke gehen. "
             "Es dauert 5 Minuten länger. Wir entschuldigen uns für die Umstände."},
      t2=[L("Anna", "f", "Markus, alle fahren heute weg! Erzähl mal, wer fährt wohin?"),
          L("Markus", "m", "Lukas fährt nach Berlin, Wochenende bei Freunden, schon lange geplant."),
          L("Anna", "f", "Nach Berlin, schön! Und Lisa? Auch weg?"),
          L("Markus", "m", "Ja, Lisa fährt nach Hamburg, sie hat dort ein Bewerbungs-Gespräch."),
          L("Anna", "f", "Drück ihr die Daumen! Und Tom? Wohin fährt er?"),
          L("Markus", "m", "Tom fährt nach Köln, seine Tante besuchen. Sie ist krank, leider."),
          L("Anna", "f", "Oh, gute Besserung! Und Sara? München oder Stuttgart?"),
          L("Markus", "m", "Sara fährt nach München, zum Konzert von ihrer Lieblings-Band. Nicht Stuttgart."),
          L("Anna", "f", "Ein Konzert, cool! Und Tim? Geschäftsreise nach Frankfurt?"),
          L("Markus", "m", "Nein, nicht Frankfurt. Tim fährt nach Dresden, Geschäftsreise für drei Tage."),
          L("Anna", "f", "Drei Tage Dresden! Und Leipzig und Nürnberg bleiben leer aus, oder?"),
          L("Markus", "m", "Ja, dahin fährt heute keiner von uns. Vielleicht im Sommer einmal."),
          L("Anna", "f", "Und wir? Wir bleiben zu Hause und machen es uns gemütlich!"),
          L("Markus", "m", "Genau! Wir kaufen Kuchen und schauen einen Film, einverstanden?")],
      t3=[[L("Reisender", "m", "Guten Tag! Eine Fahrkarte nach München, bitte, hin und zurück."),
           L("Verkäuferin", "f", "Gerne! Erste oder zweite Klasse? Spezial-Klasse haben wir leider nicht."),
           L("Reisender", "m", "Was kostet die erste Klasse?"),
           L("Verkäuferin", "f", "120 Euro. Zweite Klasse kostet nur 80 Euro."),
           L("Reisender", "m", "Dann nehme ich die zweite Klasse, danke!")],
          [L("Reisende", "f", "Wie lange dauert die Fahrt nach Frankfurt mit dem ICE?"),
           L("Schaffner", "m", "Etwa 2 Stunden 30, wenn alles pünktlich ist."),
           L("Reisende", "f", "Und mit dem Regional-Zug? Auch nur eine Stunde?"),
           L("Schaffner", "m", "Nein, eine Stunde sicher nicht. Regional dauert 4 Stunden, aber günstiger."),
           L("Reisende", "f", "Gut, dann nehme ich den ICE. Danke!")],
          [L("Tochter", "f", "Mama, ich finde Papa nicht! Wo ist er?"),
           L("Mutter", "f", "Bleib ruhig. Wo sollten wir warten, am Gleis oder im Café?"),
           L("Tochter", "f", "Beim Café! Da haben wir uns verabredet."),
           L("Mutter", "f", "Oder bei der Information? Nein, wir gehen zum Café. Er sucht uns sicher auch."),
           L("Tochter", "f", "Ja, schnell zum Café! Da ist Papa schon!")],
          [L("Tourist", "m", "Entschuldigung, wo ist die Gepäck-Aufbewahrung?"),
           L("Mitarbeiterin", "f", "Im Untergeschoss, neben den Toiletten. Folgen Sie den Schildern."),
           L("Tourist", "m", "Nicht im ersten Stock und nicht am Eingang?"),
           L("Mitarbeiterin", "f", "Genau, nur im Untergeschoss. 5 Euro pro Tag und Koffer."),
           L("Tourist", "m", "Gut, danke! Dann gehe ich gleich nach unten mit den Koffern.")],
          [L("Reisender", "m", "Entschuldigung, ist hier noch frei? Oder muss ich stehen?"),
           L("Frau", "f", "Eigentlich ist der Platz reserviert. Aber mein Mann sitzt weiter hinten."),
           L("Reisender", "m", "Soll ich mir einen anderen Platz suchen?"),
           L("Frau", "f", "Nein, bleiben Sie! Sie können sich hier setzen, kein Problem."),
           L("Reisender", "m", "Vielen Dank! Das ist sehr nett von Ihnen.")]],
      t4=[L("Reporter", "m", "Frau Hubert, Sie arbeiten seit 18 Jahren als Schaffnerin. Wie sind Sie dazu gekommen?"),
          L("Hubert", "f", "Ich wollte etwas mit Reisen machen, aber nicht als Pilotin oder Stewardess — Flugzeug-Angst! Bahn war perfekt. Habe Ausbildung gemacht, dann gleich gestartet. Ich liebe Züge, schon seit Kindheit."),
          L("Reporter", "m", "Was machen Sie genau im Zug?"),
          L("Hubert", "f", "Tickets kontrollieren, Auskunft geben, manchmal Konflikte schlichten. Notfälle behandeln — wenn jemand krank wird, zum Beispiel. Auch Sicherheit beachten. Mehr als nur Tickets prüfen."),
          L("Reporter", "m", "Was sind die häufigsten Probleme?"),
          L("Hubert", "f", "Reisende ohne Ticket — sie sagen, vergessen oder verloren. Oft Lüge. Strafe 60 Euro. Auch Streit über Sitzplätze — Reservierungen verstehen viele nicht. Und betrunkene Fahrgäste am Wochenende — die schwierigsten."),
          L("Reporter", "m", "Was ist das Schwierigste?"),
          L("Hubert", "f", "Verspätungen erklären. Wir können nichts dafür, aber Fahrgäste sind sauer. Manche sehr unfreundlich. Geduld brauchen wir viel. Auch lange Schichten — manchmal 12 Stunden."),
          L("Reporter", "m", "Würden Sie den Beruf weiterempfehlen? Ist das ein Beruf fürs Leben?"),
          L("Hubert", "f", "Ja, gerne. Für mich ist es ein Beruf fürs Leben! Spannend, Menschen-Kontakt, jeden Tag anders. Aber harte Arbeit, nichts für sensible Leute. Wer Stress mag und Reisen liebt — perfekt.")])

# ---------------- TEST 47 computer-und-probleme ----------------
apply(47,
      t1={0: "Hallo Lisa, hier ist Anna. Mein Laptop ist kaputt. Geht plötzlich nicht mehr an. "
             "Nicht verloren und nicht gestohlen, er ist einfach kaputt. "
             "Hatte gestern noch gearbeitet — alles weg. Brauche ihn für die Arbeit, kann ich deinen alten ausleihen für drei Tage? "
             "Bis Reparatur fertig. Bitte ruf zurück, danke!",
          1: "Liebe Kunden des Computer-Shops Tech-Plus: Wir haben Sonderangebote diese Woche! "
             "Laptops 20% billiger, Tablets 30%, Drucker 50% billiger. Aber Vorsicht — Smartphones bleiben zum Normalpreis. "
             "Nur bis Samstag das Angebot. Kommen Sie vorbei, Beratung ist kostenlos. Wir freuen uns auf Ihren Besuch im Stadtzentrum.",
          4: "Hi Sara, hier ist Lukas. Ich habe Probleme mit meinem Drucker. Er druckt schon, aber nur halbe Seiten. "
             "Neu kaufen wäre gerade zu teuer. Habe Toner gewechselt, hat nicht geholfen. "
             "Vielleicht kommt der Service-Mann? Kostet aber 80 Euro. Oder ich kaufe einen neuen — 150 Euro im Angebot. Was meinst du?"},
      t2=[L("Anna", "f", "Markus, alle arbeiten heute am Computer. Was macht denn jeder?"),
          L("Markus", "m", "Lukas programmiert eine App, ein Hobby-Projekt. Er will sie später verkaufen."),
          L("Anna", "f", "Verkaufen, ehrgeizig! Und Lisa? Schreibt sie wieder Texte?"),
          L("Markus", "m", "Nein, keine Texte. Lisa bearbeitet Fotos, mit Photoshop, für ihre Hochzeits-Fotos."),
          L("Anna", "f", "Hochzeits-Fotos, wie schön! Und Tom? Produziert er Musik?"),
          L("Markus", "m", "Nein, keine Musik. Tom schneidet Videos für seinen YouTube-Kanal, dreimal pro Woche ein neues Video."),
          L("Anna", "f", "Dreimal pro Woche, wow! Und Sara? Auch Videos?"),
          L("Markus", "m", "Nein, Sara designt eine Webseite für ihre kleine Firma, mit Logo und allem."),
          L("Anna", "f", "Mit Logo, professionell! Und Tim? Beantwortet er E-Mails?"),
          L("Markus", "m", "E-Mails später. Tim macht Online-Spiele, gerade spielt er in einer Computer-Liga, sehr ehrgeizig."),
          L("Anna", "f", "Eine Liga, spannend! Und Animationen erstellt keiner von euch?"),
          L("Markus", "m", "Nein, Animationen kann keiner von uns. Vielleicht lernen wir es einmal zusammen."),
          L("Anna", "f", "Gute Idee! Aber jetzt machen wir erst eine Pause, meine Augen sind müde."),
          L("Markus", "m", "Einverstanden! Kaffee trinken, und dann arbeiten wir alle weiter.")],
      t3=[[L("Kundin", "f", "Guten Tag! Mein Computer ist so langsam. Kann man da was machen?"),
           L("Techniker", "m", "Ja, mehr Arbeitsspeicher oder eine SSD-Festplatte hilft immer."),
           L("Kundin", "f", "Was kostet das? Nur RAM oder nur SSD?"),
           L("Techniker", "m", "Beides zusammen kostet 200 Euro, mit Einbau."),
           L("Kundin", "f", "Gut, dann machen Sie beides, bitte!")],
          [L("Sohn", "m", "Mama, mein Tablet ist runtergefallen! Alles voller Risse!"),
           L("Mutter", "f", "Oh nein, ist das Display kaputt? Kannst du ohne Tablet leben?"),
           L("Sohn", "m", "Nein, ich brauche es für die Schule! Neues kaufen oder reparieren lassen?"),
           L("Mutter", "f", "Neues kostet 300, Reparatur nur 150. Was meinst du?"),
           L("Sohn", "m", "Dann reparieren lassen, das ist billiger!")],
          [L("Frau", "f", "Guten Tag! Mein Passwort funktioniert plötzlich nicht mehr."),
           L("IT-Mann", "m", "Haben Sie es vergessen? Oder erinnert das System sich falsch?"),
           L("Frau", "f", "Nein, vergessen habe ich nichts. Aber das System sagt immer falsch."),
           L("IT-Mann", "m", "Dann mache ich etwas: Ich setze es zurück. Neues Passwort kommt per E-Mail."),
           L("Frau", "f", "Vielen Dank! Dann warte ich auf die E-Mail.")],
          [L("Vater", "m", "Wie lange noch am Computer? Es ist schon spät!"),
           L("Tochter", "f", "Nur noch kurz, bis 20 Uhr. Ich mache Hausaufgaben fertig."),
           L("Vater", "m", "Bis 18 Uhr wäre besser gewesen. Aber gut, 20 Uhr ist okay."),
           L("Tochter", "f", "Und bis 22 Uhr sicher nicht, versprochen, Papa!"),
           L("Vater", "m", "Versprochen ist versprochen. Dann Pause, Augen werden müde!")],
          [L("Kunde", "m", "Guten Tag! Welcher Laptop ist gut fürs Studium? Ich studiere Informatik."),
           L("Verkäuferin", "f", "Für Informatik brauchen Sie mindestens 16 GB RAM. 8 GB sind zu wenig."),
           L("Kunde", "m", "Und 32 GB? Wäre das nicht besser?"),
           L("Verkäuferin", "f", "32 GB brauchen nur Profis. Dieser hier mit 16 GB ist perfekt, 1000 Euro."),
           L("Kunde", "m", "Gut, dann nehme ich ihn. Vielen Dank!")]])

print("41-47 applied")
