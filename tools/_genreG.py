"""Genre batch G: tests 77-88 (synced from data)."""
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
("Lukas","m","Also, unsere Polizeisachen! Alles gut, Lisa, oder?"),
("Lisa","f","Na ja! Viel Ärger, diese Woche, leider."),
("Lukas","m","Oh! Sag mal, melde ich mein Fahrrad als gestohlen, mit Anzeige, gestern Abend, spät, wirklich?"),
("Lisa","f","Ja, klar! Rot und neu, vor dem Haus, weg, schade."),
("Lukas","m","Schade, ich melde mein Fahrrad als gestohlen! Meldest du einen Autounfall, heute Morgen, früh, genau, toll?"),
("Lisa","f","Genau, ich melde einen Autounfall, an der Kreuzung, ohne Verletzte, puh, super, früh."),
("Lukas","m","Puh! Hat Tom eine Brieftasche gefunden und abgegeben, mit Geld, im Park, toll, super, schön?"),
("Lisa","f","Genau, Tom hat eine Brieftasche gefunden und abgegeben, mit Ausweis, toll, super, gut, schön."),
("Lukas","m","Toll! Hat Sara sich über laute Nachbarn beschwert, wegen Musik, nachts, um zwei, wirklich, oder?"),
("Lisa","f","Ja, Sara hat sich über laute Nachbarn beschwert, sie schlafen nie, die Armen, oder, wirklich, gut?"),
("Lukas","m","Arme! Hat Tim seinen Pass verloren, im Zug, nach Berlin, wirklich, oder, genau?"),
("Lisa","f","Genau, Tim hat seinen Pass verloren, er sucht schon, überall, Hilfe, schnell, bitte, ja?"),
("Lukas","m","Genau, Tim hat seinen Pass verloren, er sucht schon, überall, Hilfe, schnell."),
("Lisa","f","Nein, keiner, alles ruhig, wirklich, oder, genau, ja?"),
("Lukas","m","Puh! Dann viel Glück, bei der Polizei, tschüss, bis bald, viel Spaß!"),
("Lisa","f","Dir auch! Bis morgen, tschüss, mach es gut, oder?"),
]

D[78] = [
("Lukas","m","Also, unsere Tänze! Bist du bereit, Lisa, für Freitag, oder, sag mal, genau?"),
("Lisa","f","Total! Neue Schuhe, toll, wirklich, oder, genau?"),
("Lukas","m","Toll! Sag mal, tanze ich Salsa, schnell, mit Partnerin, am Freitag, gut, toll, super, schön?"),
("Lisa","f","Ja, klar! Du drehst viel, mit Freude, super, toll."),
("Lukas","m","Super, ich tanze Salsa! Tanzt du Walzer, schön, im großen Saal, mit Kleid, toll, super, schön, gut?"),
("Lisa","f","Genau, ich tanze Walzer, langsam, toll, mit Musik, toll, super."),
("Lukas","m","Super! Tanzt Tom Hip-Hop, cool, mit Freunden, auf der Bühne, stark, gut, toll, super, schön?"),
("Lisa","f","Ja, Tom tanzt Hip-Hop, mit Mütze, jeden Samstag, super, toll."),
("Lukas","m","Super! Tanzt Sara Tango, leidenschaftlich, eng und langsam, toll, wow, gut, super, schön?"),
("Lisa","f","Genau, Sara tanzt Tango, mit Rose, am Abend, schön, toll, super, schön, gut, neu?"),
("Lukas","m","Schön! Tanzt Tim Discofox, überall, auf Partys, mit Schwung, einfach, super, gut, toll, super, schön?"),
("Lisa","f","Ja, Tim tanzt Discofox, schnell gelernt, mit Spaß, wirklich, toll, super, schön."),
("Lukas","m","Wirklich! Tanzt jemand Cha-Cha-Cha, schnell, heute, oder? Oder Foxtrott, langsam, gut?"),
("Lisa","f","Nein, beides nicht. Zu schnell, wirklich, oder, genau, ja, gut?"),
("Lukas","m","Verstehe! Dann viel Spaß, beim Tanzen, tschüss, bis bald, viel Spaß, tschüss, oder?"),
("Lisa","f","Dir auch! Bis Freitag, tschüss, mach es gut, tschüss!"),
]

D[79] = [
("Lukas","m","Also, unsere Fotos! Alles bereit, Lisa, oder, sag mal?"),
("Lisa","f","Fast! Die Kamera lädt noch, im Flur, oder, wirklich?"),
("Lukas","m","Gut! Sag mal, brauche ich ein Bewerbungsfoto, nett, für die Mappe, dringend, toll, super?"),
("Lisa","f","Ja, klar! Mit Hemd, vor Weiß, beim Fotografen, schnell, gut, toll, super."),
("Lukas","m","Schnell, ich brauche ein Bewerbungsfoto! Brauchst du Hochzeitsfotos, romantisch, im Park, mit Blumen, schön, toll, super?"),
("Lisa","f","Genau, ich brauche Hochzeitsfotos, im Juni, mit Sonne, wunderbar, super, toll, schön, gut."),
("Lukas","m","Wunderbar! Braucht Tom Babyfotos, süß und klein, vom Neugeborenen, mit Mütze, toll, super?"),
("Lisa","f","Ja, Tom braucht Babyfotos, drei Wochen alt, mit Decke, super, toll, schön, gut."),
("Lukas","m","Schön! Braucht Sara ein Passfoto, für den Ausweis, schnell, heute, gut, toll, super?"),
("Lisa","f","Genau, Sara braucht ein Passfoto, beim Amt, mit Nummer, langweilig, oder, toll, super."),
("Lukas","m","Langweilig! Braucht Tim Tierfotos, vom Hund, draußen, im Garten, mit Ball, lustig, toll, super?"),
("Lisa","f","Ja, Tim braucht Tierfotos, der Hund rennt viel, super, toll, schön, gut."),
("Lukas","m","Toll! Braucht jemand Urlaubsfotos, vom Strand, mit Sonne, schön, gut, toll, super?"),
("Lisa","f","Nein, keiner, alle zu Hause, wirklich, oder, genau, ja, gut?"),
("Lukas","m","Verstehe! Dann gut Licht, allen, tschüss, bis bald, viel Spaß!"),
("Lisa","f","Dir auch! Bis bald, beim Fotografen, oder, tschüss, mach es gut, tschüss!"),
]

D[80] = [
("Lukas","m","Also, unsere Schuhe! Bist du bereit, Lisa, oder, sag mal?"),
("Lisa","f","Immer! Alte weg, neue her, hurra, toll, wirklich, oder?"),
("Lukas","m","Hurra! Sag mal, kaufe ich Laufschuhe, leicht und schnell, im Herbst, teuer, gut, weit, toll?"),
("Lisa","f","Ja, klar! Bequem und leicht, super, toll, schön, gut."),
("Lukas","m","Super, ich kaufe Laufschuhe! Kaufst du High Heels, hoch, für die Party, in Rot, wow, schön, toll?"),
("Lisa","f","Genau, ich kaufe High Heels, zum Kleid, schön, toll, super, schön, gut, neu?"),
("Lukas","m","Schön! Kauft Tom Wanderschuhe, fest und hoch, für die Berge, gut, toll, super, schön?"),
("Lisa","f","Ja, Tom kauft Wanderschuhe, für Touren, mit Socken, dick, super, toll, schön."),
("Lukas","m","Dick! Kauft Sara Sandalen, leicht, für den Sommer, am Strand, bequem, toll, super, schön?"),
("Lisa","f","Genau, Sara kauft Sandalen, mit Blumen, barfuß, frei, schön, toll, super, gut."),
("Lukas","m","Frei! Kauft Tim Arbeitsschuhe, sicher und stark, Pflicht, gut, toll, super, schön?"),
("Lisa","f","Ja, Tim kauft Arbeitsschuhe, schwer und fest, gut, toll, super, schön, gut, neu?"),
("Lukas","m","Gut! Kauft jemand Sneaker, bunt und cool, für die Schule, heute, oder, sag mal?"),
("Lisa","f","Nein, keiner, alle haben schon, wirklich, oder, genau, ja, gut, toll?"),
("Lukas","m","Verstehe! Dann guten Schritt, allen, tschüss, bis bald, viel Spaß!"),
("Lisa","f","Dir auch! Bis bald, im Laden, oder, tschüss, mach es gut!"),
]

D[81] = [
("Lukas","m","Also, unsere Kurse! Bist du dabei, Lisa, oder, sag mal, genau?"),
("Lisa","f","Klar! Neues lernen, jeden Monat, gern, toll, super."),
("Lukas","m","Super! Sag mal, mache ich einen Sprachkurs, Spanisch, abends, zweimal pro Woche, mit Spaß, gut, toll, super?"),
("Lisa","f","Ja, klar! Mit Buch und CD, fleißig, super, toll, schön, gut."),
("Lukas","m","Super, ich mache einen Sprachkurs! Machst du einen Kochkurs, italienisch, freitags, toll, super, schön, gut?"),
("Lisa","f","Genau, ich mache einen Kochkurs, mit Freunden, viel Hunger, super, toll, gut, schön."),
("Lukas","m","Super! Macht Tom einen Computerkurs, mit Internet, für Senioren, gern, toll, super, schön, gut?"),
("Lisa","f","Genau, Tom macht einen Computerkurs, für Senioren, gern, toll, super, schön, gut, neu?"),
("Lukas","m","Toll! Macht Sara einen Malkurs, mit Öl, samstags, schön, gut, toll, super, schön?"),
("Lisa","f","Genau, Sara macht einen Malkurs, bunt und schön, toll, super, schön, gut, neu?"),
("Lukas","m","Schön! Macht Tim einen Yoga-Kurs, morgens, ruhig, gut, toll, super, schön?"),
("Lisa","f","Genau, Tim macht einen Yoga-Kurs, gegen Stress, super, toll, schön, gut, neu?"),
("Lukas","m","Super! Macht jemand einen Tanzkurs, mit Musik, abends, schön, gut, toll, super, schön?"),
("Lisa","f","Nein, keiner, alle lernen, wirklich, oder, genau, ja?"),
("Lukas","m","Verstehe! Macht jemand einen Fotokurs, mit Kamera, draußen, toll, super, schön, gut?"),
("Lisa","f","Nein, keiner. Viel Erfolg, in den Kursen, tschüss, bis bald, viel Spaß!"),
]

D[82] = [
("Lukas","m","Also, unsere Mietwagen! Bist du bereit, Lisa, oder, sag mal, genau?"),
("Lisa","f","Fast! Geld, und los geht es, schnell, gut, schnell."),
("Lukas","m","Super! Sag mal, miete ich einen Kleinwagen, billig und klein, für die Stadt, drei Tage, gut, toll?"),
("Lisa","f","Ja, klar! Zum Parken, überall, praktisch, toll, super, schön, gut."),
("Lukas","m","Toll, ich miete einen Kleinwagen! Mietest du einen Transporter, groß und stark, für den Umzug, am Samstag, praktisch, schnell, gut?"),
("Lisa","f","Genau, ich miete einen Transporter, mit Hilfe, in zwei Stunden, schnell, gut, toll, super."),
("Lukas","m","Schnell! Mietet Tom ein Cabrio, offen und schnell, fürs Wochenende, toll, super, schön?"),
("Lisa","f","Genau, Tom mietet ein Cabrio, an die See, toll, super, schön, gut, toll."),
("Lukas","m","Super! Mietet Sara einen Familienwagen, mit Kindersitzen, für vier, bequem, gut, toll?"),
("Lisa","f","Genau, Sara mietet einen Familienwagen, bequem und groß, toll, schön, gut, super."),
("Lukas","m","Schön! Mietet Tim ein Wohnmobil, riesig und frei, für zwei Wochen, toll, super, schön?"),
("Lisa","f","Genau, Tim mietet ein Wohnmobil, Abenteuer pur, super, toll, schön, gut, toll."),
("Lukas","m","Toll! Mietet jemand einen Sportwagen, rot und schnell, heute, oder, sag mal?"),
("Lisa","f","Nein, keiner, zu teuer, wirklich, oder, genau, ja, gut?"),
("Lukas","m","Schade! Mietet jemand ein Motorrad, laut, allein, heute, oder?"),
("Lisa","f","Nein, keiner. Gute Fahrt, allen, tschüss, gute Fahrt!"),
]

D[83] = [
("Lukas","m","Also, unsere Haut! Alles gut, Lisa, oder, sag mal, genau?"),
("Lisa","f","Na ja! Es ist schlimm, seit gestern, leider, wirklich, oder, genau?"),
("Lukas","m","Oh! Sag mal, habe ich Pickel, viele, im Gesicht, seit Wochen, schlimm, oder, genau, ja?"),
("Lisa","f","Ja, klar! Rot und dick, mit Creme, täglich, gut, toll, super."),
("Lukas","m","Gut, ich habe Pickel! Hast du einen Ausschlag, rot, am Arm, seit gestern, oder, genau, ja, gut?"),
("Lisa","f","Genau, ich habe einen Ausschlag, vielleicht Allergie, mit Creme, gut, wirklich, toll, super."),
("Lukas","m","Wirklich! Braucht Tom eine Muttermal-Kontrolle, am Rücken, jährlich, wichtig, oder, genau, ja?"),
("Lisa","f","Genau, Tom braucht eine Muttermal-Kontrolle, jährlich, wichtig, gut, toll, super."),
("Lukas","m","Gut! Hat Sara trockene Haut, im Winter, an den Händen, wirklich, oder, genau, ja?"),
("Lisa","f","Genau, Sara hat trockene Haut, mit Creme, täglich, gut, oder, toll, super."),
("Lukas","m","Oder! Hat Tim einen Sonnenbrand, rot und heiß, vom Strand, aua, toll, super?"),
("Lisa","f","Genau, Tim hat einen Sonnenbrand, aua, seit Sonntag, wirklich, toll, super."),
("Lukas","m","Wirklich! Hat jemand Warzen, an den Händen, schlimm, oder, genau, ja, gut?"),
("Lisa","f","Nein, keiner, alle gesund, wirklich, oder, genau, ja, gut, toll."),
("Lukas","m","Schön! Hat jemand einen Insektenstich, rot und dick, heute, oder, sag mal, genau, ja?"),
("Lisa","f","Nein, keiner. Gute Besserung, allen, tschüss, bis bald, viel Spaß!"),
]

D[84] = [
("Lukas","m","Also, unsere Stadt! Bist du fertig, Lisa, oder, sag mal, genau?"),
("Lisa","f","Immer! Stadtplan, und los geht es, schnell, gut, schnell."),
("Lukas","m","Super! Sag mal, mache ich eine Stadtführung, zu Fuß, mit Gruppe, am Samstag, interessant, toll, super?"),
("Lisa","f","Ja, klar! Alt und neu, mit Geschichten, super, toll, schön, gut."),
("Lukas","m","Super, ich mache eine Stadtführung! Besuche ich das Museum, am Sonntag, mit Bildern, gut, schön, toll?"),
("Lisa","f","Genau, ich besuche das Museum, mit Geschichte, lehrreich, toll, super, schön."),
("Lukas","m","Toll! Macht Tom eine Bootsfahrt, auf dem Fluss, abends, schön, gut, toll?"),
("Lisa","f","Genau, Tom macht eine Bootsfahrt, mit Lichtern, romantisch, super, toll, schön, gut."),
("Lukas","m","Super! Steigt Sara auf den Aussichtsturm, ganz hoch, bei Sonne, toll, super, schön?"),
("Lisa","f","Genau, Sara steigt auf den Aussichtsturm, mit Blick, toll, super, schön, gut, toll."),
("Lukas","m","Toll! Geht Tim auf den Markt, bunt und laut, samstags, gern, toll, super?"),
("Lisa","f","Genau, Tim geht auf den Markt, mit Hunger, lecker, toll, super, schön, gut."),
("Lukas","m","Toll! Geht jemand in den Park, grün und groß, heute, oder, sag mal?"),
("Lisa","f","Nein, keiner, alle in der Stadt, wirklich, oder, genau, ja, gut?"),
("Lukas","m","Schade! Geht jemand ins Theater, abends, schön, gut, toll, super?"),
("Lisa","f","Nein, keiner. Viel Spaß, in der Stadt, tschüss, bis bald, viel Spaß!"),
]

D[85] = [
("Lukas","m","Also, unsere Musik! Was läuft, Lisa, bei dir, oder, sag mal, genau, ja?"),
("Lisa","f","Alles! Radio an, den ganzen Tag, gern, toll, super."),
("Lukas","m","Super! Sag mal, spiele ich Gitarre, seit zwei Jahren, mit Unterricht, Rock und Pop, laut, toll, super?"),
("Lisa","f","Ja, klar! Jeden Tag, fleißig, toll, super, schön."),
("Lukas","m","Toll, ich spiele Gitarre! Spielst du Klavier, seit der Kindheit, mit Gefühl, täglich, schön, gut, toll, super?"),
("Lisa","f","Genau, ich spiele Klavier, mit Gefühl, schön, toll, super, gut, schön."),
("Lukas","m","Super! Spielt Tom Schlagzeug, laut, im Keller, mit Freunden, toll, super, schön, gut?"),
("Lisa","f","Genau, Tom spielt Schlagzeug, pow, super, toll, schön, gut, super."),
("Lukas","m","Toll! Spielt Sara Geige, hell, im Orchester, freitags, gut, schön, toll, super?"),
("Lisa","f","Genau, Sara spielt Geige, schön und gut, freitags, toll, super, schön, gut."),
("Lukas","m","Gut! Spielt Tim Trompete, hoch und klar, im Verein, toll, super, schön, gut, neu, toll?"),
("Lisa","f","Genau, Tim spielt Trompete, immer, toll, super, schön, gut, neu?"),
("Lukas","m","Toll! Spielt jemand Saxophon, laut und tief, heute, oder, sag mal, genau, gut, toll?"),
("Lisa","f","Nein, keiner, zu laut, wirklich, oder, genau, ja, gut, toll?"),
("Lukas","m","Schade! Spielt jemand Flöte, hell und schön, auch, gut, toll, super, schön?"),
("Lisa","f","Nein, keine. Viel Spaß, mit Musik, tschüss, bis bald, oder, tschüss, gut!"),
]

D[86] = [
("Lukas","m","Also, unsere Schmerzen! Alles gut, Lisa, oder, sag mal, genau, ja?"),
("Lisa","f","Na ja! Alles weh, seit Tagen, leider, wirklich, oder, genau?"),
("Lukas","m","Oh! Sag mal, habe ich Rückenschmerzen, unten, seit Wochen, vom Sitzen, schlimm, sehr, toll, super, oder?"),
("Lisa","f","Ja, klar! Steif, mit Wärme, besser, gut, toll, super."),
("Lukas","m","Besser, ich habe Rückenschmerzen! Hast du ein verletztes Knie, vom Sport, dick, seit gestern, aua, toll, super?"),
("Lisa","f","Genau, ich habe ein verletztes Knie, kaum Gehen, morgen, früh, toll, super."),
("Lukas","m","Oder! Hat Tom Schulterschmerzen, rechts, vom Tragen, schwer, seit Tagen, gut, toll, super, oder?"),
("Lisa","f","Genau, Tom hat Schulterschmerzen, schwer, seit Tagen, wirklich, oder, toll, super."),
("Lukas","m","Wirklich! Hat Sara einen steifen Nacken, morgens, nach dem Schlafen, gut, oder, toll, super, oder?"),
("Lisa","f","Genau, Sara hat einen steifen Nacken, mit Wärme, gut, toll, super, schön."),
("Lukas","m","Gut! Hat Tim einen verstauchten Fuß, hochgelegt, mit Eis, gut, toll, super, oder?"),
("Lisa","f","Genau, Tim hat einen verstauchten Fuß, oben, mit Eis, toll, super, schön."),
("Lukas","m","Toll! Hat jemand Kopfschmerzen, stark und lang, heute, oder, sag mal, genau, gut, toll?"),
("Lisa","f","Nein, keiner, alle fit, wirklich, oder, genau, ja, gut, toll."),
("Lukas","m","Fit! Hat jemand Hüftschmerzen, beim Gehen, auch, gut, toll, super, oder?"),
("Lisa","f","Nein, keiner. Gute Besserung, allen, tschüss, bis bald, oder, tschüss, gut!"),
]

D[87] = [
("Lukas","m","Also, unsere Geschenke! Hast du Ideen, Lisa, oder, sag mal?"),
("Lisa","f","Viele! Für die Kleinen, zu Weihnachten, toll, super."),
("Lukas","m","Super! Sag mal, kaufe ich eine Eisenbahn, groß und schnell, für den Kleinen, zu Weihnachten, teuer, gut, toll?"),
("Lisa","f","Ja, klar! Im Kreis, super, toll."),
("Lukas","m","Super, ich kaufe eine Eisenbahn! Kaufst du eine Puppe, mit Kleid, für die Kleine, zum Geburtstag, toll, super?"),
("Lisa","f","Genau, ich kaufe eine Puppe, schön und lieb, super, toll, schön, gut."),
("Lukas","m","Super! Kauft Tom einen Baukasten, mit Steinen, zum Bauen, für Regentage, toll, super, schön?"),
("Lisa","f","Ja, Tom kauft einen Baukasten, groß und bunt, mit Plan, super, toll, schön, gut."),
("Lukas","m","Super! Kauft Sara ein Brettspiel, für die Familie, abends, lustig, toll, super, schön?"),
("Lisa","f","Genau, Sara kauft ein Brettspiel, ab acht, mit Glück, super, toll, schön, gut."),
("Lukas","m","Super! Kauft Tim ein Kuscheltier, weich und groß, einen Bären, zum Kuscheln, süß, toll, super?"),
("Lisa","f","Ja, Tim kauft ein Kuscheltier, zum Liebhaben, weich, toll, super, schön, gut."),
("Lukas","m","Toll! Kauft jemand ein Fahrrad, rot und schnell, heute, oder, sag mal?"),
("Lisa","f","Nein, keiner, zu teuer, wirklich, oder, genau, ja, gut?"),
("Lukas","m","Schade! Kauft jemand ein Puzzle, bunt und klein, auch, gut, toll?"),
("Lisa","f","Nein, keines. Viel Freude, beim Schenken, tschüss, bis bald, viel Spaß!"),
]

D[88] = [
("Lukas","m","Also, unser Einkauf! Bist du bereit, Lisa, oder, sag mal, genau?"),
("Lisa","f","Fast! Zettel da, und los geht es, schnell, gut, wirklich?"),
("Lukas","m","Super! Sag mal, bestelle ich Kleidung, online, oft, bequem, gut, toll, super, schön?"),
("Lisa","f","Ja, klar! Hosen, jede Woche, viel, super, toll, schön, gut."),
("Lukas","m","Super, ich bestelle Kleidung! Bestellst du Bücher, jede Woche, spannend, toll, super, schön, gut?"),
("Lisa","f","Genau, ich bestelle Bücher, Krimis und Romane, im Bett, toll, super, schön, gut, neu, schick?"),
("Lukas","m","Toll! Bestellt Tom Elektronik, neueste, schnell, zum Arbeiten, gut, toll, super, schön?"),
("Lisa","f","Ja, Tom bestellt Elektronik, mit Stecker, super, toll, schön, gut, neu, schick?"),
("Lukas","m","Super! Bestellt Sara Möbel, groß und schwer, mit Lieferung, fürs Wohnzimmer, modern, toll, super, schön?"),
("Lisa","f","Genau, Sara bestellt Möbel, mit Aufbau, am Samstag, super, toll, schön, gut, neu, schick, toll?"),
("Lukas","m","Toll! Bestellt Tim Lebensmittel, frisch und kühl, jede Woche, gut, toll, super, schön?"),
("Lisa","f","Ja, Tim bestellt Lebensmittel, praktisch, toll, super, schön, gut, neu, toll, schick?"),
("Lukas","m","Toll! Bestellt jemand Schuhe, braun und neu, heute, oder, sag mal, genau?"),
("Lisa","f","Nein, keine, zu teuer, wirklich, oder, genau, ja, gut, toll, super."),
("Lukas","m","Schade! Bestellt jemand Werkzeug, stark und neu, auch, gut, toll, super?"),
("Lisa","f","Nein, keins. Viel Spaß, bis bald, oder, gut, tschüss!"),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
