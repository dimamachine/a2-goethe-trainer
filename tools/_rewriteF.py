"""Batch F rewrite: tests 65-76 — natural direct speech, full lines."""
import json, re

def W(t): return len(re.findall(r"[A-Za-zÄÖÜäöüß]+", t))

def set_lines(n, lines):
    p = f"tools/_test{n}_data.json"
    d = json.load(open(p, encoding="utf-8"))
    te = d["teile"][1]
    assert len(lines) == len(te["lines"]), (n, len(lines), len(te["lines"]))
    for slot, (sp, g, tx) in zip(te["lines"], lines):
        slot["speaker"], slot["gender"], slot["text"] = sp, g, tx
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(p, "a").write("\n")
    print(f"#{n}: {len(lines)} turns, {sum(W(t) for _,_,t in lines)}w")

D = {}

D[65] = [
("Lukas","m","Also, unsere Technik! Ich kaufe einen Laptop, schnell und leicht, für die Uni, mit Tasche."),
("Lisa","f","Cool! Ich kaufe Kopfhörer, kabellos und bequem, für Musik, überall, täglich."),
("Tom","m","Und ich kaufe einen Fernseher, groß und flach, fürs Wohnzimmer, mit Sound, toll."),
("Sara","f","Ich kaufe eine Kamera, mit Zoom und Blitz, für den Urlaub, am Meer, super."),
("Tim","m","Und ich kaufe eine Spielekonsole, neu und schnell, mit zwei Controllern, für Abende."),
("Lukas","m","Stark! Lisa, sind Kopfhörer teuer, kabellos, gute, wirklich?"),
("Lisa","f","Hundert Euro, mit Rabatt, im Angebot, das geht gut, für den Klang."),
("Tom","m","Und die Kamera, Sara, machst du viele Fotos, im Urlaub, täglich?"),
("Sara","f","Hunderte! Und Konsole, Tim, spielst du oft, abends, nach der Arbeit?"),
("Tim","m","Jeden Abend! Also, ich kaufe eine Spielekonsole, mit zwei Controllern!"),
("Lukas","m","Ich kaufe einen Laptop, für die Uni, mit Tasche!"),
("Lisa","f","Ich kaufe Kopfhörer, für Musik, täglich!"),
("Tom","m","Ich kaufe einen Fernseher, mit Sound, toll!"),
("Sara","f","Ich kaufe eine Kamera, für den Urlaub!"),
("Tim","m","Und ich kaufe eine Spielekonsole, für Abende!"),
("Lukas","m","Viel Spaß allen, mit Technik!"),
]

D[66] = [
("Lukas","m","Also, unsere Handwerker! Ich rufe den Klempner, für das Bad, der Hahn tropft, seit Tagen."),
("Lisa","f","Gut! Ich rufe den Elektriker, für die Küche, das Licht flackert, abends, nervig."),
("Tom","m","Und ich rufe den Maler, fürs Wohnzimmer, weiß und hell, am Wochenende, frisch."),
("Sara","f","Ich rufe den Tischler, für den Schrank, die Tür klemmt, seit Wochen, ärgerlich."),
("Tim","m","Und ich rufe den Dachdecker, für das Dach, ein Ziegel fehlt, nach dem Sturm."),
("Lukas","m","Viel Arbeit! Lisa, kommt der Elektriker bald, diese Woche, schon?"),
("Lisa","f","Am Donnerstag, um zehn, mit Werkzeug, hoffentlich pünktlich, wie immer."),
("Tom","m","Und der Schrank, Sara, klemmt die Tür sehr, geht sie noch auf?"),
("Sara","f","Kaum! Und Dach, Tim, regnet es rein, durch den Ziegel, wirklich?"),
("Tim","m","Ein bisschen! Also, ich rufe den Dachdecker, nach dem Sturm!"),
("Lukas","m","Ich rufe den Klempner, der Hahn tropft!"),
("Lisa","f","Ich rufe den Elektriker, das Licht flackert!"),
("Tom","m","Ich rufe den Maler, weiß und hell!"),
("Sara","f","Ich rufe den Tischler, die Tür klemmt!"),
("Tim","m","Und ich rufe den Dachdecker, ein Ziegel fehlt!"),
("Lukas","m","Viel Glück allen, mit Handwerkern!"),
]

D[67] = [
("Lukas","m","Also, unser Zootag! Ich sehe die Löwen, stark und laut, bei der Fütterung, um elf."),
("Lisa","f","Toll! Ich sehe die Pinguine, lustig und schnell, im Wasser, mit Fischen, niedlich."),
("Tom","m","Und ich sehe die Affen, wild und frech, mit Bananen, den ganzen Tag, lustig."),
("Sara","f","Ich sehe die Giraffen, groß und ruhig, mit langem Hals, bei den Blättern, schön."),
("Tim","m","Und ich sehe die Elefanten, riesig und grau, mit Rüssel, beim Baden, toll."),
("Lukas","m","Schön! Lisa, schwimmen Pinguine schnell, wirklich, wie Fische?"),
("Lisa","f","Sehr schnell, wie Pfeile, im Wasser, mit Freude, wunderbar."),
("Tom","m","Und Giraffen, Sara, wie hoch sind sie, fünf Meter, echt?"),
("Sara","f","Fünf Meter! Und Elefanten, Tim, baden sie gern, im Sommer?"),
("Tim","m","Sehr gern! Also, ich sehe die Elefanten, beim Baden!"),
("Lukas","m","Ich sehe die Löwen, bei der Fütterung!"),
("Lisa","f","Ich sehe die Pinguine, mit Fischen!"),
("Tom","m","Ich sehe die Affen, mit Bananen!"),
("Sara","f","Ich sehe die Giraffen, bei den Blättern!"),
("Tim","m","Und ich sehe die Elefanten, mit Rüssel!"),
("Lukas","m","Viel Spaß allen, im Zoo!"),
]

D[68] = [
("Lukas","m","Also, unser Mittagessen! Ich esse Schnitzel, mit Pommes und Salat, in der Kantine, lecker."),
("Lisa","f","Gut! Ich esse einen großen Salat, mit Käse und Ei, gesund und frisch, täglich."),
("Tom","m","Und ich esse Nudeln, vegetarisch, mit Tomatensoße, mein Lieblingsessen, immer."),
("Sara","f","Ich esse Suppe, heiß und würzig, mit Brot, bei Erkältung, beste Medizin."),
("Tim","m","Und ich esse Fisch, gebraten, mit Reis, freitags, wie zu Hause, Tradition."),
("Lukas","m","Lecker! Lisa, ist Salat genug, mittags, ohne Fleisch, wirklich?"),
("Lisa","f","Ja, mit Käse und Ei, satt und fit, bis abends, locker."),
("Tom","m","Und Suppe, Sara, hilft sie wirklich, bei Erkältung, ehrlich?"),
("Sara","f","Bestimmt! Und Fisch, Tim, gibt es ihn jeden Freitag, in der Kantine?"),
("Tim","m","Jeden Freitag! Also, ich esse Fisch, wie zu Hause!"),
("Lukas","m","Ich esse Schnitzel, in der Kantine!"),
("Lisa","f","Ich esse einen großen Salat, täglich!"),
("Tom","m","Ich esse Nudeln, mein Lieblingsessen!"),
("Sara","f","Ich esse Suppe, beste Medizin!"),
("Tim","m","Und ich esse Fisch, freitags!"),
("Lukas","m","Guten Appetit allen, in der Kantine!"),
]

D[69] = [
("Lukas","m","Also, unsere Fundsachen! Ich habe einen Regenschirm verloren, rot, im Bus, gestern."),
("Lisa","f","Oh! Ich habe ein Handy verloren, neu und teuer, im Café, am Tisch, schade."),
("Tom","m","Und ich habe einen Geldbeutel verloren, mit Karten, im Park, auf der Bank, ärgerlich."),
("Sara","f","Ich habe eine Brille verloren, mit Sehstärke, im Kino, in Reihe fünf, Mist."),
("Tim","m","Und ich habe einen Schlüssel verloren, vom Fahrrad, am See, im Sand, weg."),
("Lukas","m","Viel Pech! Lisa, war das Handy an, im Café, ruft jemand an?"),
("Lisa","f","Ja, es klingelt, der Kellner antwortet, nett, ich hole es heute."),
("Tom","m","Und Geldbeutel, Tom, also meiner, sind Karten drin, alle gesperrt?"),
("Sara","f","Tom, du sprichst von dir! Also, deine Karten, alle gesperrt, schon?"),
("Tom","m","Alle gesperrt! Und Brille, Sara, siehst du ohne, gut genug?"),
("Sara","f","Kaum! Also, ich habe eine Brille verloren, in Reihe fünf!"),
("Lukas","m","Ich habe einen Regenschirm verloren, im Bus!"),
("Lisa","f","Ich habe ein Handy verloren, im Café!"),
("Tom","m","Ich habe einen Geldbeutel verloren, im Park!"),
("Tim","m","Und ich habe einen Schlüssel verloren, am See!"),
("Lukas","m","Viel Glück allen, im Fundbüro!"),
]
# fix self-address 8/9
D[69][7] = ("Tom","m","Meine Karten sind alle gesperrt, schon heute, zum Glück.")
D[69][8] = ("Sara","f","Zum Glück! Und meine Brille, wo suche ich zuerst, im Kino?")
D[69][9] = ("Tom","m","In Reihe fünf, bestimmt! Ruf dort an, heute noch, schnell.")

D[70] = [
("Lukas","m","Also, unsere Versicherungen! Ich brauche eine Autoversicherung, für den Wagen, neu, ab Januar."),
("Lisa","f","Gut! Ich brauche eine Hausratversicherung, für die Wohnung, mit Fahrrad, wichtig."),
("Tom","m","Und ich brauche eine Reiseversicherung, für den Urlaub, weltweit, mit Gepäck, sicher."),
("Sara","f","Ich brauche eine Krankenversicherung, für die Familie, mit Zahn, komplett, gut."),
("Tim","m","Und ich brauche eine Haftpflichtversicherung, für alle Fälle, billig und gut, Pflicht."),
("Lukas","m","Wichtig! Lisa, ist Hausrat teuer, mit Fahrrad, im Jahr?"),
("Lisa","f","Achtzig Euro, im Jahr, mit allem, das geht gut, wirklich."),
("Tom","m","Und Kranken, Sara, zahlt sie Zahn, alles, komplett?"),
("Sara","f","Fast alles! Und Haftpflicht, Tim, hast du schon eine, wirklich?"),
("Tim","m","Ab heute! Also, ich brauche eine Haftpflichtversicherung, Pflicht!"),
("Lukas","m","Ich brauche eine Autoversicherung, ab Januar!"),
("Lisa","f","Ich brauche eine Hausratversicherung, mit Fahrrad!"),
("Tom","m","Ich brauche eine Reiseversicherung, weltweit!"),
("Sara","f","Ich brauche eine Krankenversicherung, komplett!"),
("Tim","m","Und ich brauche eine Haftpflichtversicherung, billig und gut!"),
("Lukas","m","Gut versichert allen, viel Glück!"),
]

D[71] = [
("Lukas","m","Also, unsere Renovierung! Ich kaufe Farbe, weiß und blau, fürs Zimmer, zehn Liter."),
("Lisa","f","Schön! Ich kaufe Pflanzen, grün und groß, für den Balkon, im Frühling, frisch."),
("Tom","m","Und ich kaufe Werkzeug, mit Bohrer und Säge, für alles, im Haus, praktisch."),
("Sara","f","Ich kaufe Fliesen, hell und modern, fürs Bad, mit Muster, schick."),
("Tim","m","Und ich kaufe eine Lampe, groß und hell, fürs Wohnzimmer, modern, gemütlich."),
("Lukas","m","Toll! Lisa, gießt du oft, die Pflanzen, auf dem Balkon, täglich?"),
("Lisa","f","Jeden Morgen, mit Gießkanne, im Sommer, gern, sie wachsen gut."),
("Tom","m","Und Fliesen, Sara, legst du selbst, im Bad, wirklich?"),
("Sara","f","Mit Papa! Und Lampe, Tim, hängt sie schon, im Wohnzimmer?"),
("Tim","m","Ab Samstag! Also, ich kaufe eine Lampe, modern, gemütlich!"),
("Lukas","m","Ich kaufe Farbe, zehn Liter!"),
("Lisa","f","Ich kaufe Pflanzen, für den Balkon!"),
("Tom","m","Ich kaufe Werkzeug, praktisch!"),
("Sara","f","Ich kaufe Fliesen, schick!"),
("Tim","m","Und ich kaufe eine Lampe, groß und hell!"),
("Lukas","m","Viel Erfolg allen, beim Bauen!"),
]

D[72] = [
("Lukas","m","Also, unsere Umwelt! Ich trenne den Müll genau, mit vier Tonnen, jeden Tag, ordentlich."),
("Lisa","f","Super! Ich sammle Pfandflaschen, im Keller, mit Tasche, jede Woche, zum Laden."),
("Tom","m","Und ich kompostiere Bioabfälle, im Garten, mit Würmern, es riecht kaum, ehrlich."),
("Sara","f","Ich kaufe ohne Verpackung ein, mit Beuteln, auf dem Markt, lose, frisch."),
("Tim","m","Und ich bringe alte Geräte zum Wertstoffhof, Fernseher und Radio, am Samstag, mit Auto."),
("Lukas","m","Stark! Lisa, gibt es viel Pfand, jede Woche, im Keller?"),
("Lisa","f","Zehn Euro, manchmal mehr, fürs Eis, im Sommer, lecker."),
("Tom","m","Und lose, Sara, ist es teurer, ohne Verpackung, auf dem Markt?"),
("Sara","f","Nein, oft billiger! Und Geräte, Tim, fährt das Auto weit, zum Hof?"),
("Tim","m","Zehn Minuten! Also, ich bringe alte Geräte zum Wertstoffhof, am Samstag!"),
("Lukas","m","Ich trenne den Müll genau, ordentlich!"),
("Lisa","f","Ich sammle Pfandflaschen, jede Woche!"),
("Tom","m","Ich kompostiere Bioabfälle, mit Würmern!"),
("Sara","f","Ich kaufe ohne Verpackung ein, lose!"),
("Tim","m","Und ich bringe alte Geräte zum Wertstoffhof, mit Auto!"),
("Lukas","m","Sauber bleiben allen, weiter so!"),
]

D[73] = [
("Lukas","m","Also, unser Tierheim! Ich nehme den Hund, braun und lieb, aus dem Heim, bald."),
("Lisa","f","Toll! Ich nehme die Katze, grau und ruhig, fürs Sofa, zum Kuscheln, süß."),
("Tom","m","Und ich nehme das Kaninchen, weiß und weich, mit Käfig, für die Kinder, niedlich."),
("Sara","f","Ich nehme den Vogel, klein und laut, mit Gesang, morgens, fröhlich."),
("Tim","m","Und ich nehme den Hamster, goldig und klein, mit Rad, nachts aktiv, lustig."),
("Lukas","m","Schön! Lisa, kratzt die Katze, am Sofa, sehr?"),
("Lisa","f","Nein, sie hat einen Kratzbaum, groß, im Flur, sie liebt ihn."),
("Tom","m","Und Vogel, Sara, singt er laut, morgens, um sechs?"),
("Sara","f","Sehr laut! Und Hamster, Tim, läuft er viel, nachts, im Rad?"),
("Tim","m","Stundenlang! Also, ich nehme den Hamster, mit Rad!"),
("Lukas","m","Ich nehme den Hund, bald!"),
("Lisa","f","Ich nehme die Katze, zum Kuscheln!"),
("Tom","m","Ich nehme das Kaninchen, für die Kinder!"),
("Sara","f","Ich nehme den Vogel, fröhlich!"),
("Tim","m","Und ich nehme den Hamster, nachts aktiv!"),
("Lukas","m","Viel Glück allen, mit Tieren!"),
]

D[74] = [
("Lukas","m","Also, unser Marktbesuch! Ich trinke Glühwein, heiß und süß, am Stand, mit Freunden."),
("Lisa","f","Lecker! Ich kaufe Geschenke, kleine, für alle, an den Ständen, mit Liebe."),
("Tom","m","Und ich esse Bratwurst, mit Senf, am Grill, duftend, heiß, lecker."),
("Sara","f","Ich höre Weihnachtsmusik, vom Chor, auf der Bühne, besinnlich, schön."),
("Tim","m","Und ich fahre Karussell, schnell und hoch, mit Lichtern, abends, juhu."),
("Lukas","m","Schön! Lisa, sind Geschenke teuer, an den Ständen, wirklich?"),
("Lisa","f","Manche ja, kleine nein, mit Liebe, das zählt, immer."),
("Tom","m","Und Musik, Sara, singt der Chor gut, auf der Bühne?"),
("Sara","f","Wunderbar! Und Karussell, Tim, ist dir nicht schlecht, oben?"),
("Tim","m","Nein, nie! Also, ich fahre Karussell, abends, juhu!"),
("Lukas","m","Ich trinke Glühwein, mit Freunden!"),
("Lisa","f","Ich kaufe Geschenke, mit Liebe!"),
("Tom","m","Ich esse Bratwurst, lecker!"),
("Sara","f","Ich höre Weihnachtsmusik, besinnlich!"),
("Tim","m","Und ich fahre Karussell, mit Lichtern!"),
("Lukas","m","Frohe Weihnachten allen, viel Spaß!"),
]

D[75] = [
("Lukas","m","Also, unsere Kleidung! Ich bringe den Anzug, grau, in die Reinigung, am Montag."),
("Lisa","f","Gut! Ich bringe das Abendkleid, rot, zur Reinigung, vor der Party, wichtig."),
("Tom","m","Und ich bringe die Winterjacke, dick und warm, nach dem Winter, mit Fleck, leider."),
("Sara","f","Ich bringe die Bettdecke, groß und warm, im Frühling, jedes Jahr, frisch."),
("Tim","m","Und ich bringe Hemden zum Bügeln, fünf Stück, weiß, fürs Büro, glatt."),
("Lukas","m","Viel Stoff! Lisa, ist Rot schwer, zu reinigen, das Kleid?"),
("Lisa","f","Nein, sie können alles, professionell, seit Jahren, super."),
("Tom","m","Und Decke, Sara, passt sie rein, in die Maschine, groß?"),
("Sara","f","Klar, XXL! Und Hemden, Tim, bügeln sie gut, wirklich glatt?"),
("Tim","m","Sehr glatt! Also, ich bringe Hemden zum Bügeln, fürs Büro!"),
("Lukas","m","Ich bringe den Anzug, am Montag!"),
("Lisa","f","Ich bringe das Abendkleid, vor der Party!"),
("Tom","m","Ich bringe die Winterjacke, mit Fleck!"),
("Sara","f","Ich bringe die Bettdecke, jedes Jahr!"),
("Tim","m","Und ich bringe Hemden zum Bügeln, glatt!"),
("Lukas","m","Sauber bleiben allen, viel Glück!"),
]

D[76] = [
("Lukas","m","Also, unsere Bücher! Ich lese Krimis, spannend, am Abend, im Bett, mit Tee."),
("Lisa","f","Schön! Ich lese Liebesromane, romantisch, am Wochenende, auf dem Sofa, mit Decke."),
("Tom","m","Und ich lese Sachbücher, über Geschichte, dick und klug, fürs Wissen, gern."),
("Sara","f","Ich lese Kochbücher, mit Bildern, für Sonntag, mit Appetit, lecker."),
("Tim","m","Und ich lese Comics, bunt und lustig, im Zug, zur Arbeit, täglich."),
("Lukas","m","Toll! Lisa, weinst du manchmal, bei Romanen, wirklich?"),
("Lisa","f","Oft, besonders am Ende, mit Taschentuch, peinlich, aber schön."),
("Tom","m","Und Comics, Tim, sind sie nur für Kinder, ehrlich?"),
("Sara","f","Nein, für alle! Und Krimis, Lukas, wer ist der Mörder, oft der Gärtner?"),
("Tim","m","Haha! Also, ich lese Comics, täglich!"),
("Lukas","m","Ich lese Krimis, mit Tee!"),
("Lisa","f","Ich lese Liebesromane, mit Decke!"),
("Tom","m","Ich lese Sachbücher, gern!"),
("Sara","f","Ich lese Kochbücher, lecker!"),
("Tim","m","Und ich lese Comics, im Zug!"),
("Lukas","m","Viel Spaß allen, beim Lesen!"),
]
# fix: turn 9 Tim answers Sara's question to Lukas — Lukas answers, Tim confirms next
D[76][9] = ("Lukas","m","Manchmal der Gärtner! Also, ich lese Krimis, mit Tee!")
D[76][10] = ("Tim","m","Haha! Also, ich lese Comics, täglich!")

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
