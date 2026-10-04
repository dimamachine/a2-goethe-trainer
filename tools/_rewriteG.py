"""Batch G rewrite: tests 77-88 — natural direct speech, full lines."""
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

D[77] = [
("Lukas","m","Also, unsere Polizeisachen! Ich melde mein Fahrrad als gestohlen, mit Anzeige, gestern Abend."),
("Lisa","f","Oh nein! Ich melde einen Autounfall, mit Blechschaden, heute Morgen, an der Kreuzung."),
("Tom","m","Und ich habe eine Brieftasche gefunden und abgegeben, mit Geld, ehrlich, im Park."),
("Sara","f","Brav! Ich habe mich über laute Nachbarn beschwert, wegen Musik, nachts, um zwei."),
("Tim","m","Und ich habe meinen Pass verloren, im Zug, nach Berlin, Mist, wirklich."),
("Lukas","m","Viel Ärger! Lisa, ist dir nichts passiert, beim Unfall, wirklich?"),
("Lisa","f","Nein, nur Blech, mir geht es gut, zum Glück, keine Sorge."),
("Tom","m","Und Geldbeutel, war viel drin, im Portemonnaie, ehrlich?"),
("Sara","f","Zweihundert Euro! Und Nachbarn, Sara, also meine, sind sie jetzt leise?"),
("Tim","m","Sara, du fragst dich selbst! Also, deine Nachbarn, leise jetzt?"),
("Sara","f","Leise, endlich! Also, ich habe mich über laute Nachbarn beschwert, nachts!"),
("Lukas","m","Ich melde mein Fahrrad als gestohlen, gestern Abend!"),
("Lisa","f","Ich melde einen Autounfall, heute Morgen!"),
("Tom","m","Ich habe eine Brieftasche gefunden und abgegeben, im Park!"),
("Tim","m","Und ich habe meinen Pass verloren, im Zug!"),
("Lukas","m","Viel Glück allen, bei der Polizei!"),
]
# fix self-address 9/10
D[77][8] = ("Sara","f","Zweihundert Euro waren drin! Und meine Nachbarn, sind sie jetzt leise?")
D[77][9] = ("Tim","m","Hoffentlich! Mein Pass ist weg, wo suche ich zuerst, im Zug?")

D[78] = [
("Lukas","m","Also, unsere Tänze! Ich tanze Salsa, feurig und schnell, mit Partnerin, am Freitag."),
("Lisa","f","Toll! Ich tanze Walzer, klassisch und schön, im großen Saal, mit Kleid."),
("Tom","m","Und ich tanze Hip-Hop, cool und locker, mit Crew, auf der Bühne, stark."),
("Sara","f","Ich tanze Tango, leidenschaftlich, eng und langsam, mit Stolz, wow."),
("Tim","m","Und ich tanze Discofox, überall, auf Partys, mit Schwung, einfach, super."),
("Lukas","m","Schön! Lisa, ist Walzer schwer, im großen Saal, mit Drehungen?"),
("Lisa","f","Am Anfang ja, mit Übung geht es, nach Wochen, dann tanzt man."),
("Tom","m","Und Tango, Sara, ist er sehr ernst, leidenschaftlich, immer?"),
("Sara","f","Sehr ernst! Und Discofox, Tim, lernt man ihn schnell, wirklich?"),
("Tim","m","Sehr schnell! Also, ich tanze Discofox, auf Partys!"),
("Lukas","m","Ich tanze Salsa, am Freitag!"),
("Lisa","f","Ich tanze Walzer, im großen Saal!"),
("Tom","m","Ich tanze Hip-Hop, auf der Bühne!"),
("Sara","f","Ich tanze Tango, mit Stolz!"),
("Tim","m","Und ich tanze Discofox, mit Schwung!"),
("Lukas","m","Viel Spaß allen, beim Tanzen!"),
]

D[79] = [
("Lukas","m","Also, unsere Fotos! Ich brauche ein Bewerbungsfoto, seriös und nett, für die Mappe."),
("Lisa","f","Gut! Ich brauche Hochzeitsfotos, romantisch, im Park, mit Blumen, wunderschön."),
("Tom","m","Und ich brauche Babyfotos, süß und klein, vom Neugeborenen, mit Mütze, niedlich."),
("Sara","f","Ich brauche ein Passfoto, biometrisch, für den Ausweis, schnell, heute."),
("Tim","m","Und ich brauche Tierfotos, vom Hund, draußen, im Garten, mit Ball, lustig."),
("Lukas","m","Viele Fotos! Lisa, wann ist die Hochzeit, im Park, im Sommer?"),
("Lisa","f","Im Juni, bei Sonne, mit Gästen, hundert Leute, großes Fest."),
("Tom","m","Und Baby, wie alt ist es, schon einen Monat, klein?"),
("Sara","f","Drei Wochen! Und Tierfotos, Tim, bleibt der Hund still, im Garten?"),
("Tim","m","Kaum! Also, ich brauche Tierfotos, mit Ball!"),
("Lukas","m","Ich brauche ein Bewerbungsfoto, für die Mappe!"),
("Lisa","f","Ich brauche Hochzeitsfotos, im Park!"),
("Tom","m","Ich brauche Babyfotos, vom Neugeborenen!"),
("Sara","f","Ich brauche ein Passfoto, für den Ausweis!"),
("Tim","m","Und ich brauche Tierfotos, vom Hund!"),
("Lukas","m","Gut Licht allen, beim Fotografen!"),
]

D[80] = [
("Lukas","m","Also, unsere Schuhe! Ich kaufe Laufschuhe, leicht und schnell, für den Marathon, im Herbst."),
("Lisa","f","Stark! Ich kaufe High Heels, elegant und hoch, für die Party, in Rot, wow."),
("Tom","m","Und ich kaufe Wanderschuhe, fest und hoch, für die Berge, mit Profil, robust."),
("Sara","f","Ich kaufe Sandalen, luftig und leicht, für den Sommer, am Strand, bequem."),
("Tim","m","Und ich kaufe Arbeitsschuhe, sicher und stark, für die Baustelle, mit Stahl, Pflicht."),
("Lukas","m","Toll! Lisa, kannst du laufen, in Heels, den ganzen Abend?"),
("Lisa","f","Mit Übung ja, seit Jahren, auf Partys, kein Problem, wirklich."),
("Tom","m","Und Berge, Sara, äh, deine Sandalen, für den Strand, bequem?"),
("Sara","f","Sehr bequem! Und Baustelle, Tim, sind Stahlschuhe schwer, wirklich?"),
("Tim","m","Sehr schwer! Also, ich kaufe Arbeitsschuhe, Pflicht!"),
("Lukas","m","Ich kaufe Laufschuhe, für den Marathon!"),
("Lisa","f","Ich kaufe High Heels, in Rot!"),
("Tom","m","Ich kaufe Wanderschuhe, robust!"),
("Sara","f","Ich kaufe Sandalen, für den Strand!"),
("Tim","m","Und ich kaufe Arbeitsschuhe, mit Stahl!"),
("Lukas","m","Guten Schritt allen, viel Spaß!"),
]
# fix: turn 8 Tom addresses Sara but stumbles — rewrite cleanly
D[80][7] = ("Tom","m","Und Sandalen, Sara, sind sie bequem, am Strand, wirklich?")

D[81] = [
("Lukas","m","Also, unsere Kurse! Ich mache einen Sprachkurs, Spanisch, abends, zweimal pro Woche, mit Spaß."),
("Lisa","f","Toll! Ich mache einen Kochkurs, italienisch, mit Pasta, freitags, lecker, mit Freunden."),
("Tom","m","Und ich mache einen Computerkurs, mit Internet, für Senioren, ehrenamtlich, sinnvoll."),
("Sara","f","Ich mache einen Malkurs, mit Öl und Leinwand, samstags, kreativ, bunt."),
("Tim","m","Und ich mache einen Yoga-Kurs, morgens, entspannt, gegen Stress, mit Matte, ruhig."),
("Lukas","m","Schön! Lisa, kochst du gut, italienisch, nach dem Kurs?"),
("Lisa","f","Immer besser, Pasta geht schon, Pizza noch nicht, leider."),
("Tom","m","Und Malen, Sara, was malst du, Landschaften, oder Porträts?"),
("Sara","f","Landschaften! Und Yoga, Tim, hilft es wirklich, morgens?"),
("Tim","m","Sehr! Also, ich mache einen Yoga-Kurs, mit Matte!"),
("Lukas","m","Ich mache einen Sprachkurs, mit Spaß!"),
("Lisa","f","Ich mache einen Kochkurs, mit Freunden!"),
("Tom","m","Ich mache einen Computerkurs, sinnvoll!"),
("Sara","f","Ich mache einen Malkurs, kreativ!"),
("Tim","m","Und ich mache einen Yoga-Kurs, gegen Stress!"),
("Lukas","m","Viel Erfolg allen, in den Kursen!"),
]

D[82] = [
("Lukas","m","Also, unsere Mietwagen! Ich miete einen Kleinwagen, billig und klein, für die Stadt, drei Tage."),
("Lisa","f","Gut! Ich miete einen Transporter, groß und stark, für den Umzug, am Samstag, praktisch."),
("Tom","m","Und ich miete ein Cabrio, offen und schnell, fürs Wochenende, an die See, toll."),
("Sara","f","Ich miete einen Familienwagen, mit Kindersitzen, für vier, in den Urlaub, bequem."),
("Tim","m","Und ich miete ein Wohnmobil, riesig und frei, für zwei Wochen, durchs Land, Abenteuer."),
("Lukas","m","Toll! Lisa, passt alles rein, in den Transporter, wirklich?"),
("Lisa","f","Alles, mit Hilfe, in zwei Stunden, am Samstag, dann los."),
("Tom","m","Und See, fährst du offen, im Cabrio, bei Sonne?"),
("Sara","f","Klar! Und Wohnmobil, Tim, hat es Dusche, wirklich, an Bord?"),
("Tim","m","Mit Dusche! Also, ich miete ein Wohnmobil, Abenteuer!"),
("Lukas","m","Ich miete einen Kleinwagen, für die Stadt!"),
("Lisa","f","Ich miete einen Transporter, praktisch!"),
("Tom","m","Ich miete ein Cabrio, an die See!"),
("Sara","f","Ich miete einen Familienwagen, bequem!"),
("Tim","m","Und ich miete ein Wohnmobil, durchs Land!"),
("Lukas","m","Gute Fahrt allen, viel Spaß!"),
]

D[83] = [
("Lukas","m","Also, unsere Haut! Ich habe Pickel, viele, im Gesicht, seit Wochen, nervig."),
("Lisa","f","Oh! Ich habe einen Ausschlag, rot und juckend, am Arm, seit gestern, schlimm."),
("Tom","m","Und ich brauche eine Muttermal-Kontrolle, am Rücken, jährlich, zur Vorsorge, wichtig."),
("Sara","f","Ich habe trockene Haut, im Winter, an den Händen, mit Creme, täglich, besser."),
("Tim","m","Und ich habe einen Sonnenbrand, rot und heiß, vom Strand, seit Sonntag, aua."),
("Lukas","m","Arme Haut! Lisa, juckt es sehr, der Ausschlag, nachts?"),
("Lisa","f","Sehr, ich kratze mich, im Schlaf, die Creme hilft, ein bisschen."),
("Tom","m","Und Creme, Sara, hilft sie gut, bei trockener Haut, wirklich?"),
("Sara","f","Sehr gut! Und Sonne, Tim, hattest du keinen Schutz, am Strand?"),
("Tim","m","Vergessen! Also, ich habe einen Sonnenbrand, aua!"),
("Lukas","m","Ich habe Pickel, seit Wochen!"),
("Lisa","f","Ich habe einen Ausschlag, schlimm!"),
("Tom","m","Ich brauche eine Muttermal-Kontrolle, wichtig!"),
("Sara","f","Ich habe trockene Haut, mit Creme!"),
("Tim","m","Und ich habe einen Sonnenbrand, vom Strand!"),
("Lukas","m","Gute Besserung allen, der Haut!"),
]

D[84] = [
("Lukas","m","Also, unsere Stadt! Ich mache eine Stadtführung, zu Fuß, mit Guide, am Samstag, interessant."),
("Lisa","f","Schön! Ich besuche das Museum, mit Geschichte, am Sonntag, mit Audioguide, lehrreich."),
("Tom","m","Und ich mache eine Bootsfahrt, auf dem Fluss, abends, mit Lichtern, romantisch."),
("Sara","f","Ich steige auf den Aussichtsturm, ganz hoch, mit Blick, bei Sonne, atemberaubend."),
("Tim","m","Und ich gehe auf den Markt, bunt und laut, mit Kostproben, samstags, lecker."),
("Lukas","m","Toll! Lisa, ist Museum teuer, mit Audioguide, am Sonntag?"),
("Lisa","f","Zehn Euro, mit Führung, es lohnt sich, wirklich, fürs Wissen."),
("Tom","m","Und Turm, Sara, hast du keine Angst, ganz oben, bei Wind?"),
("Sara","f","Doch, ein bisschen! Und Markt, Tim, was kostet die Wurst, am Stand?"),
("Tim","m","Drei Euro! Also, ich gehe auf den Markt, samstags!"),
("Lukas","m","Ich mache eine Stadtführung, interessant!"),
("Lisa","f","Ich besuche das Museum, lehrreich!"),
("Tom","m","Ich mache eine Bootsfahrt, romantisch!"),
("Sara","f","Ich steige auf den Aussichtsturm, atemberaubend!"),
("Tim","m","Und ich gehe auf den Markt, lecker!"),
("Lukas","m","Viel Spaß allen, in der Stadt!"),
]

D[85] = [
("Lukas","m","Also, unsere Musik! Ich spiele Gitarre, seit zwei Jahren, mit Unterricht, Rock und Pop."),
("Lisa","f","Schön! Ich spiele Klavier, klassisch, seit der Kindheit, mit Gefühl, täglich."),
("Tom","m","Und ich spiele Schlagzeug, laut und wild, im Keller, mit Band, pow."),
("Sara","f","Ich spiele Geige, sanft und hell, im Orchester, freitags, wunderschön."),
("Tim","m","Und ich spiele Trompete, hoch und klar, im Verein, mit Uniform, stolz."),
("Lukas","m","Toll! Lisa, übst du täglich, Klavier, eine Stunde?"),
("Lisa","f","Eine Stunde, morgens, vor der Schule, immer, seit Jahren."),
("Tom","m","Und Geige, Sara, ist sie schwer, wirklich, mit Bogen?"),
("Sara","f","Sehr schwer! Und Trompete, Tim, sind Nachbarn genervt, vom Klang?"),
("Tim","m","Manchmal! Also, ich spiele Trompete, stolz!"),
("Lukas","m","Ich spiele Gitarre, Rock und Pop!"),
("Lisa","f","Ich spiele Klavier, täglich!"),
("Tom","m","Ich spiele Schlagzeug, pow!"),
("Sara","f","Ich spiele Geige, wunderschön!"),
("Tim","m","Und ich spiele Trompete, im Verein!"),
("Lukas","m","Viel Spaß allen, mit Musik!"),
]

D[86] = [
("Lukas","m","Also, unsere Schmerzen! Ich habe Rückenschmerzen, unten, seit Wochen, vom Sitzen, schlimm."),
("Lisa","f","Oh! Ich habe ein verletztes Knie, vom Sport, geschwollen, seit gestern, aua."),
("Tom","m","Und ich habe Schulterschmerzen, rechts, vom Tragen, schwerer Taschen, täglich."),
("Sara","f","Ich habe einen steifen Nacken, morgens, nach dem Schlafen, mit Wärme, besser."),
("Tim","m","Und ich habe einen verstauchten Fuß, umgeknickt, beim Laufen, mit Eis, hochgelegt."),
("Lukas","m","Arme alle! Lisa, kannst du gehen, mit dem Knie, wirklich?"),
("Lisa","f","Kaum, nur mit Krücken, zum Arzt, morgen, hoffentlich besser."),
("Tom","m","Und Nacken, Sara, hilft Wärme gut, morgens, wirklich?"),
("Sara","f","Sehr gut! Und Fuß, Tim, schwillt er an, stark, seit gestern?"),
("Tim","m","Stark! Also, ich habe einen verstauchten Fuß, hochgelegt!"),
("Lukas","m","Ich habe Rückenschmerzen, schlimm!"),
("Lisa","f","Ich habe ein verletztes Knie, aua!"),
("Tom","m","Ich habe Schulterschmerzen, täglich!"),
("Sara","f","Ich habe einen steifen Nacken, besser!"),
("Tim","m","Und ich habe einen verstauchten Fuß, mit Eis!"),
("Lukas","m","Gute Besserung allen, schnell gesund!"),
]

D[87] = [
("Lukas","m","Also, unsere Geschenke! Ich kaufe eine Eisenbahn, groß und schnell, für den Kleinen, zu Weihnachten."),
("Lisa","f","Toll! Ich kaufe eine Puppe, mit Kleid, für die Kleine, zum Geburtstag, hübsch."),
("Tom","m","Und ich kaufe einen Baukasten, mit Steinen, zum Bauen, für Regentage, kreativ."),
("Sara","f","Ich kaufe ein Brettspiel, für die Familie, abends, mit Würfeln, lustig."),
("Tim","m","Und ich kaufe ein Kuscheltier, weich und groß, einen Bären, zum Kuscheln, süß."),
("Lukas","m","Schön! Lisa, freut sie sich, die Kleine, auf die Puppe?"),
("Lisa","f","Sehr, sie wünscht sie sich, seit Monaten, mit Kleid, unbedingt."),
("Tom","m","Und Spiel, Sara, ist es schwer, mit Würfeln, für Kinder?"),
("Sara","f","Ab acht! Und Bär, Tim, wie groß ist er, ein Meter?"),
("Tim","m","Ein Meter! Also, ich kaufe ein Kuscheltier, süß!"),
("Lukas","m","Ich kaufe eine Eisenbahn, zu Weihnachten!"),
("Lisa","f","Ich kaufe eine Puppe, hübsch!"),
("Tom","m","Ich kaufe einen Baukasten, kreativ!"),
("Sara","f","Ich kaufe ein Brettspiel, lustig!"),
("Tim","m","Und ich kaufe ein Kuscheltier, zum Kuscheln!"),
("Lukas","m","Viel Freude allen, beim Schenken!"),
]

D[88] = [
("Lukas","m","Also, unser Einkauf! Ich bestelle Kleidung, online, mit Rücksendung, oft, bequem."),
("Lisa","f","Ich bestelle Bücher, jede Woche, mit Abo, spannend, im Briefkasten, toll."),
("Tom","m","Und ich bestelle Elektronik, mit Garantie, neueste, zum Arbeiten, schnell."),
("Sara","f","Ich bestelle Möbel, groß und schwer, mit Lieferung, fürs Wohnzimmer, modern."),
("Tim","m","Und ich bestelle Lebensmittel, frisch und kühl, jede Woche, mit Abo, praktisch."),
("Lukas","m","Bequem! Lisa, liest du viel, jede Woche, ein Buch?"),
("Lisa","f","Ein Buch, manchmal zwei, abends, im Bett, gemütlich."),
("Tom","m","Und Möbel, Sara, baut ihr selbst auf, die Lieferung, mit Anleitung?"),
("Sara","f","Mit Nachbarn! Und Essen, Tim, bleibt es frisch, gekühlt, wirklich?"),
("Tim","m","Sehr frisch! Also, ich bestelle Lebensmittel, praktisch!"),
("Lukas","m","Ich bestelle Kleidung, bequem!"),
("Lisa","f","Ich bestelle Bücher, toll!"),
("Tom","m","Ich bestelle Elektronik, schnell!"),
("Sara","f","Ich bestelle Möbel, modern!"),
("Tim","m","Und ich bestelle Lebensmittel, mit Abo!"),
("Lukas","m","Viel Spaß allen, beim Shoppen!"),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
