"""Genre batch F: tests 65-76 (synced from data)."""
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
("Lukas","m","Also, unsere Technik! Bist du fertig, Lisa, mit der Liste, lang, schwer?"),
("Lisa","f","Fast! Viel steht da, für Weihnachten, teuer, sehr, wirklich."),
("Lukas","m","Kenn ich! Sag mal, kaufe ich einen Laptop, schnell und leicht, für die Uni, mit Tasche, gut, neu, gut?"),
("Lisa","f","Ja, klar! Zum Arbeiten, jeden Tag, wirklich, oder, genau?"),
("Lukas","m","Stimmt, ich kaufe einen Laptop! Kaufst du Kopfhörer, neu und bequem, für Musik, überall, gern, viel, oft?"),
("Lisa","f","Genau, ich kaufe Kopfhörer, jeden Tag, mit Freude, super, toll, schön."),
("Lukas","m","Super! Kauft Tom einen Fernseher, groß und flach, fürs Wohnzimmer, toll, riesig, groß?"),
("Lisa","f","Ja, Tom kauft einen Fernseher, riesig, mit Familie, am Abend, super, toll."),
("Lukas","m","Riesig! Kauft Sara eine Kamera, für den Urlaub, am Meer, schön, neu, schick?"),
("Lisa","f","Genau, Sara kauft eine Kamera, viele Fotos, im Sommer, toll, super, schön, gut."),
("Lukas","m","Toll! Kauft Tim eine Spielekonsole, neu und schnell, zu zweit, für Abende, lang, super?"),
("Lisa","f","Ja, Tim kauft eine Spielekonsole, jeden Abend, mit Freunden, lustig, sehr, lustig."),
("Lukas","m","Lustig! Kauft jemand einen Drucker, groß und laut, fürs Büro, heute? Oder Lautsprecher, neu, gut, wirklich?"),
("Lisa","f","Nein, beides nicht. Alles neu, wirklich, oder, genau, wirklich, oder?"),
("Lukas","m","Verstehe! Dann viel Spaß, mit Technik, tschüss, bis bald!"),
("Lisa","f","Dir auch! Bis bald, im Laden, oder, tschüss!"),
]

D[66] = [
("Lukas","m","Also, unsere Handwerker! Alles gut, Lisa, bei dir?"),
("Lisa","f","Na ja! Viel kaputt, im Haus, seit Wochen, lange?"),
("Lukas","m","Oh! Sag mal, rufe ich den Klempner, für das Bad, das Wasser läuft, seit Tagen, schlimm, wirklich, oder, genau?"),
("Lisa","f","Ja, bitte! Wasser überall, im Bad, wirklich, oder?"),
("Lukas","m","Stimmt, ich rufe den Klempner! Rufst du den Elektriker, für die Küche, das Licht geht aus, oft?"),
("Lisa","f","Genau, ich rufe den Elektriker, abends dunkel, nervös, mit Kerzen, dunkel?"),
("Lukas","m","Oh! Ruft Tom den Maler, fürs Wohnzimmer, weiß und hell, am Wochenende, frisch, neu?"),
("Lisa","f","Ja, Tom ruft den Maler, zwei Zimmer, mit Farbe, teuer, aber schön, gut?"),
("Lukas","m","Schön! Ruft Sara den Tischler, für den Schrank, die Tür klemmt, seit Wochen, sehr, wirklich, oder?"),
("Lisa","f","Genau, Sara ruft den Tischler, er kommt Freitag, mit Werkzeug, gut, sicher?"),
("Lukas","m","Gut! Ruft Tim den Dachdecker, für das Dach, das Dach ist kaputt, nach dem Sturm, schlimm, sehr?"),
("Lisa","f","Ja, Tim ruft den Dachdecker, es regnet rein, schnell, bitte, ja?"),
("Lukas","m","Schnell! Ruft jemand den Gärtner, für den Garten, mit Blumen, heute? Oder Fensterputzer, gut, schnell, wirklich?"),
("Lisa","f","Nein, keiner, beides nicht. Erst im Frühling, wirklich, oder, genau?"),
("Lukas","m","Verstehe! Dann viel Glück, mit Handwerkern, tschüss, bis bald, viel Spaß!"),
("Lisa","f","Dir auch! Bis bald, alles wird gut, tschüss, oder?"),
]

D[67] = [
("Lukas","m","Also, unser Zootag! Bist du bereit, Lisa, mit Kamera, gut, alles klar?"),
("Lisa","f","Immer! Mit Hut, und bequemen Schuhen, toll, oder, super?"),
("Lukas","m","Super! Sag mal, sehe ich die Löwen, stark und laut, um elf, morgens, spannend, toll, super?"),
("Lisa","f","Ja, klar! Groß und stark, mit Zähnen, wirklich, super, toll."),
("Lukas","m","Toll! Ich sehe die Löwen! Siehst du die Pinguine, lustig und schnell, im Wasser?"),
("Lisa","f","Genau, ich sehe die Pinguine, sie schwimmen schnell, toll, super, schön, gut."),
("Lukas","m","Genau, ich sehe die Pinguine, sie schwimmen schnell, toll, super, schön."),
("Lisa","f","Ja, Tom sieht die Affen, sie springen hoch, mit Lärm, super, toll, schön, gut."),
("Lukas","m","Ja, Tom sieht die Affen, sie springen hoch, mit Lärm, super, toll, schön."),
("Lisa","f","Genau, Sara sieht die Giraffen, groß, mit Kindern, wow, toll, super, schön, gut."),
("Lukas","m","Genau, Sara sieht die Giraffen, groß, mit Kindern, wow, toll, super, schön."),
("Lisa","f","Ja, Tim sieht die Elefanten, sie duschen gern, im Sommer, lustig, toll, super, schön."),
("Lukas","m","Ja, Tim sieht die Elefanten, sie duschen gern, im Sommer, lustig, toll, super."),
("Lisa","f","Nein, keine. Sieht jemand Tiger, orange und groß? Oder Schlangen, lang, grün, neu?"),
("Lukas","m","Nein, beides nicht. Schade! Dann viel Spaß, im Zoo, tschüss, bis bald, viel Spaß!"),
("Lisa","f","Dir auch! Bis bald, mit Fotos, viele, tschüss, mach es gut!"),
]

D[68] = [
("Lukas","m","Also, unser Mittagessen! Hast du Hunger, Lisa, oder nicht, sag mal, genau?"),
("Lisa","f","Riesig! Nichts gegessen, seit morgens, leider, zu wenig, wirklich."),
("Lukas","m","Kenn ich! Sag mal, esse ich Schnitzel, mit Pommes und Salat, in der Kantine, toll, super, schön?"),
("Lisa","f","Ja, klar! Groß und heiß, mit Soße, wirklich, oder?"),
("Lukas","m","Toll, ich esse Schnitzel! Isst du einen großen Salat, mit Käse und Ei, gesund und frisch, täglich, gern, immer?"),
("Lisa","f","Genau, ich esse einen großen Salat, voll und fit, bis abends, super, toll, schön."),
("Lukas","m","Super! Isst Tom Nudeln, vegetarisch, mit Soße, immer, gern, viel, oft?"),
("Lisa","f","Ja, Tom isst Nudeln, jeden Tag, mit viel Hunger, lustig, sehr."),
("Lukas","m","Lustig! Isst Sara Suppe, heiß und gut, mit Brot, bei Erkältung, gut, wirklich, oder?"),
("Lisa","f","Genau, Sara isst Suppe, sie hustet viel, seit Tagen, arm, oder?"),
("Lukas","m","Arme! Isst Tim Fisch, gebraten, mit Reis, freitags, wie zu Hause, Tradition, toll, super?"),
("Lisa","f","Ja, Tim isst Fisch, jeden Freitag, mit Zitrone, toll, super."),
("Lukas","m","Sag mal, isst jemand nur Nachtisch, süß und kalt, ohne Essen, heute, wirklich?"),
("Lisa","f","Nein, keiner, alle essen warm, wirklich, oder, genau, ja?"),
("Lukas","m","Verstehe! Dann guten Appetit, allen, tschüss, bis bald, viel Spaß!"),
("Lisa","f","Dir auch! Bis morgen, in der Kantine, oder, tschüss, mach es gut!"),
]

D[69] = [
("Lukas","m","Also, unsere Fundsachen! Alles weg, Lisa, bei dir, wirklich?"),
("Lisa","f","Leider! Gestern viel verloren, überall, leider, schade."),
("Lukas","m","Oh! Sag mal, habe ich einen Regenschirm verloren, rot, im Bus, gestern, wirklich, genau?"),
("Lisa","f","Ja, klar! Im Bus, hinten, frag den Fahrer, schnell, los."),
("Lukas","m","Gut, ich habe einen Regenschirm verloren! Hast du ein Handy verloren, neu und teuer, im Café, teuer?"),
("Lisa","f","Genau, ich habe ein Handy verloren, am Tisch, der Kellner antwortet, nett, sehr, freundlich."),
("Lukas","m","Nett! Hat Tom einen Geldbeutel verloren, mit Karten, im Park, auf der Bank, ärgerlich, sehr?"),
("Lisa","f","Ja, Tom hat einen Geldbeutel verloren, alle Karten aus, zum Glück, schnell, gut, toll."),
("Lukas","m","Schnell! Hat Sara eine Brille verloren, mit Sehstärke, im Kino, in Reihe fünf, genau, fünfte?"),
("Lisa","f","Genau, Sara hat eine Brille verloren, sie sieht wenig, ohne Brille, arm, leider, wirklich."),
("Lukas","m","Gut! Hat Tim einen Schlüssel verloren, vom Fahrrad, am See, im Sand, weg, verloren?"),
("Lisa","f","Ja, Tim hat einen Schlüssel verloren, wir suchen morgen, zusammen, früh, morgen."),
("Lukas","m","Früh! Hat jemand eine Uhr verloren, aus Gold, teuer? Oder eine Tasche, neu, schön?"),
("Lisa","f","Nein, keiner, beides nicht. Alle Uhren da, wirklich, oder?"),
("Lukas","m","Verstehe! Dann viel Glück, im Fundbüro, tschüss, viel Glück!"),
("Lisa","f","Dir auch! Bis morgen, mit Glück, oder, tschüss!"),
]

D[70] = [
("Lukas","m","Also, unsere Versicherungen! Alles klar, Lisa, oder, sag mal?"),
("Lisa","f","Fast! Viele Papiere, überall, Hilfe, wirklich, oder?"),
("Lukas","m","Kenn ich! Sag mal, brauche ich eine Autoversicherung, für den Wagen, neu, ab Januar, teuer, sehr, wirklich?"),
("Lisa","f","Ja, klar! Pflicht für alle, mit Schutz, wirklich, oder, genau, ja, gut?"),
("Lukas","m","Stimmt, ich brauche eine Autoversicherung! Brauchst du eine Hausratversicherung, für die Wohnung, mit Fahrrad, wichtig, oder, genau?"),
("Lisa","f","Genau, ich brauche eine Hausratversicherung, achtzig Euro, im Jahr, billig, super, toll, super."),
("Lukas","m","Billig! Braucht Tom eine Reiseversicherung, für den Urlaub, weltweit, mit Gepäck, sicher, gut, wirklich?"),
("Lisa","f","Ja, Tom braucht eine Reiseversicherung, mit Flug, für zwei Wochen, toll, super, schön, toll."),
("Lukas","m","Toll! Braucht Sara eine Krankenversicherung, für die Familie, mit Zahn, gut, wirklich, oder?"),
("Lisa","f","Genau, Sara braucht eine Krankenversicherung, fast alles drin, super, toll, schön, gut."),
("Lukas","m","Super! Braucht Tim eine Haftpflichtversicherung, für alle Fälle, billig und gut, Pflicht, wirklich, oder?"),
("Lisa","f","Ja, Tim braucht eine Haftpflichtversicherung, ab heute, mit Vertrag, sicher, gut, toll, super."),
("Lukas","m","Sicher! Braucht jemand eine Tierversicherung, für Hund und Katze, heute, oder?"),
("Lisa","f","Nein, keiner, keine Tiere, wirklich, oder, genau, ja, gut?"),
("Lukas","m","Verstehe! Dann gut versichert, allen, tschüss, bis bald, viel Spaß!"),
("Lisa","f","Dir auch! Bis bald, ohne Sorgen, oder, tschüss, mach es gut!"),
]

D[71] = [
("Lukas","m","Also, unser Haus! Bist du fertig, Lisa, oder nicht, sag mal?"),
("Lisa","f","Fast! Viel Arbeit, am Wochenende, puh, Hilfe, bitte, danke."),
("Lukas","m","Kenn ich! Sag mal, kaufe ich Farbe, weiß und blau, fürs Zimmer, viel, billig, gut, meinst du?"),
("Lisa","f","Ja, klar! Hell und frisch, schnell, toll, super, schön, neu."),
("Lukas","m","Schnell, ich kaufe Farbe! Kaufst du Pflanzen, grün und groß, für den Balkon, im Frühling, frisch, schön, gut, toll."),
("Lisa","f","Genau, ich kaufe Pflanzen, mit Wasser, jeden Morgen, gern, viel, immer, toll, neu."),
("Lukas","m","Viel! Kauft Tom Werkzeug, für alles, im Haus, neu, gut, wirklich, toll."),
("Lisa","f","Genau, Tom kauft Werkzeug, praktisch und gut, immer, toll, super, schön."),
("Lukas","m","Gut! Kauft Sara Fliesen, hell und modern, fürs Bad, schön, neu, findest du?"),
("Lisa","f","Genau, Sara kauft Fliesen, schick und neu, fürs Bad, toll, super, schön, gut."),
("Lukas","m","Toll! Kauft Tim eine Lampe, groß und hell, fürs Wohnzimmer, schön, gut, toll, super?"),
("Lisa","f","Genau, Tim kauft eine Lampe, modern, hell, super, toll, schön, gut, neu."),
("Lukas","m","Super! Braucht jemand Tapeten, bunt und neu, fürs Zimmer, heute, glaubst du?"),
("Lisa","f","Nein, keine, weiß reicht, wirklich, genau, ja?"),
("Lukas","m","Verstehe! Braucht jemand Gartenmöbel, aus Holz, für draußen, schön, gut, toll, super?"),
("Lisa","f","Nein, keine. Viel Erfolg, beim Bauen, tschüss, bis bald, viel Spaß!"),
]

D[72] = [
("Lukas","m","Also, unsere Umwelt! Bist du dabei, Lisa, oder nicht?"),
("Lisa","f","Klar! Jeden Tag, ein bisschen, gern, immer, toll, super."),
("Lukas","m","Super! Sag mal, trenne ich den Müll genau, jeden Tag, fleißig, gut, toll, meinst du?"),
("Lisa","f","Ja, klar! Gelb, blau und schwarz, seit Jahren, wirklich, super, toll."),
("Lukas","m","Stimmt, ich trenne den Müll genau! Sammelst du Pfandflaschen, im Keller, mit Tasche, jede Woche, zum Laden, oft, gut, findest du?"),
("Lisa","f","Genau, ich sammle Pfandflaschen, zehn Euro, manchmal mehr, fürs Eis, toll, super, schön, gut."),
("Lukas","m","Toll! Kompostiert Tom Bioabfälle, im Garten, fleißig, gut, glaubst du?"),
("Lisa","f","Genau, Tom kompostiert Bioabfälle, jeden Tag, super, toll, schön, gut."),
("Lukas","m","Super! Kauft Sara ohne Verpackung ein, mit Taschen, auf dem Markt, lose und frisch, gut, meinst du?"),
("Lisa","f","Genau, Sara kauft ohne Verpackung ein, lose und frisch, oft, billig, toll, super, schön."),
("Lukas","m","Oft! Bringt Tim alte Geräte zum Wertstoffhof, am Samstag, mit Auto, weit, gut, meinst du?"),
("Lisa","f","Genau, Tim bringt alte Geräte zum Wertstoffhof, Fernseher und Radio, toll, super, schön, gut."),
("Lukas","m","Toll! Spart jemand Strom, mit Lampen, am Abend, viel, meinst du?"),
("Lisa","f","Nein, keiner. Spart jemand Wasser, beim Duschen, oft, gern, oder?"),
("Lukas","m","Nein, keiner. Sauber bleiben, allen, tschüss, bis bald, viel Spaß!"),
("Lisa","f","Dir auch! Bis morgen, tschüss, mach es gut, tschüss!"),
]

D[73] = [
("Lukas","m","Also, unsere Tiere! Bist du fertig, Lisa, oder nicht, sag mal, genau?"),
("Lisa","f","Total! Tiere suchen Häuser, bald, wirklich, oder, genau?"),
("Lukas","m","Super! Sag mal, nehme ich den Hund, braun und lieb, aus dem Heim, bald, sicher, gut, toll, oder?"),
("Lisa","f","Ja, klar! Groß und gut, super, toll, oder, wirklich, gut?"),
("Lukas","m","Super, ich nehme den Hund! Nimmst du die Katze, grau und ruhig, fürs Sofa, lieb, toll, oder, super?"),
("Lisa","f","Genau, ich nehme die Katze, ruhig, zum Schlafen, gern, toll, super, schön."),
("Lukas","m","Gut! Nimmt Tom das Kaninchen, weiß und weich, für Kinder, süß, toll, super?"),
("Lisa","f","Genau, Tom nimmt das Kaninchen, für die Kinder, toll, super, schön, groß."),
("Lukas","m","Toll! Nimmt Sara den Vogel, klein und laut, lustig, schön, gut, toll?"),
("Lisa","f","Genau, Sara nimmt den Vogel, jeden Morgen, toll, super, schön, neu."),
("Lukas","m","Schön! Nimmt Tim den Hamster, klein, für Kinder, süß, toll, super?"),
("Lisa","f","Genau, Tim nimmt den Hamster, lustig und toll, super, schön, gut, neu?"),
("Lukas","m","Toll! Nimmt jemand die Maus, grau und klein, heute, oder, sag mal, genau, gut, toll, super, schön."),
("Lisa","f","Nein, keiner, alle weg, wirklich, genau, ja, gut, toll."),
("Lukas","m","Verstehe! Nimmt jemand die Schildkröte, alt und ruhig, langsam, toll, super, schön?"),
("Lisa","f","Nein, keine. Viel Glück, mit Tieren, tschüss, bis bald, viel Spaß, tschüss!"),
]

D[74] = [
("Lukas","m","Also, unser Marktbesuch! Bist du fertig, Lisa, für den Winter, oder, sag mal, genau?"),
("Lisa","f","Total! Warm, und los geht es, schnell, gut, wirklich, oder?"),
("Lukas","m","Super! Sag mal, trinke ich Glühwein, heiß und süß, am Stand, mit Freunden, lecker, toll, super?"),
("Lisa","f","Ja, klar! Rot und warm, toll, super, oder, wirklich?"),
("Lukas","m","Toll, ich trinke Glühwein! Kaufe ich Geschenke, kleine, für alle, an den Ständen, mit Liebe, schön, gut, toll?"),
("Lisa","f","Genau, ich kaufe Geschenke, kleine, für alle, mit Liebe, immer, toll, super."),
("Lukas","m","Immer! Isst Tom Bratwurst, am Grill, heiß und gut, lecker, toll, super?"),
("Lisa","f","Genau, Tom isst Bratwurst, heiß und gut, mit Hunger, toll, super, schön, groß."),
("Lukas","m","Gut! Hört Sara Weihnachtsmusik, zu Hause, laut und schön, toll, super, gut, schön."),
("Lisa","f","Genau, Sara hört Weihnachtsmusik, schön und ruhig, toll, super, schön, gut, toll."),
("Lukas","m","Toll! Fährt Tim Karussell, schnell und hoch, mit Lichtern, super, toll, schön, gut."),
("Lisa","f","Genau, Tim fährt Karussell, abends, juhu, super, toll, schön, gut, super."),
("Lukas","m","Super! Isst jemand gebrannte Mandeln, süß und warm, heute, oder, sag mal, genau, gut?"),
("Lisa","f","Nein, keiner, zu teuer, wirklich, genau, ja, gut, toll."),
("Lukas","m","Schade! Läuft jemand Schlittschuh, auf dem Eis, heute, oder, genau, ja?"),
("Lisa","f","Nein, keiner. Frohe Weihnachten, allen, tschüss, bis bald, viel Spaß, super."),
]

D[75] = [
("Lukas","m","Also, unsere Kleidung! Alles voll, Lisa, bei dir, oder, sag mal, genau?"),
("Lisa","f","Leider! Nach dem Urlaub, alles voll, wirklich, oder, genau, ja?"),
("Lukas","m","Kenn ich! Sag mal, bringe ich den Anzug, grau, in die Reinigung, am Montag, schnell, gut, wirklich, oder?"),
("Lisa","f","Ja, klar! Nicht sauber, vom Essen, wirklich, oder?"),
("Lukas","m","Genau, ich bringe den Anzug! Bringst du das Abendkleid, rot, zur Reinigung, vor der Party, wichtig, toll, super, schön?"),
("Lisa","f","Genau, ich bringe das Abendkleid, gut und schnell, super, schön, toll, super."),
("Lukas","m","Super! Bringt Tom die Winterjacke, dick und warm, leider, alt, gut, wirklich?"),
("Lisa","f","Genau, Tom bringt die Winterjacke, nach dem Winter, alt, gut, wirklich, oder?"),
("Lukas","m","Alt! Bringt Sara die Bettdecke, groß und warm, im Frühling, schön, gut, toll?"),
("Lisa","f","Genau, Sara bringt die Bettdecke, jedes Jahr, frisch, toll, super, schön."),
("Lukas","m","Toll! Bringt Tim Hemden zum Bügeln, fünf Stück, weiß, toll, super, schön?"),
("Lisa","f","Genau, Tim bringt Hemden zum Bügeln, gut, fürs Büro, super, toll, schön, gut."),
("Lukas","m","Super! Bringt jemand den Teppich, groß und schwer, heute, oder, sag mal, genau?"),
("Lisa","f","Nein, keiner, zu schwer, wirklich, oder, genau?"),
("Lukas","m","Schade! Bringt jemand Krawatten, bunt und neu, dazu, schön, gut, toll?"),
("Lisa","f","Nein, keine. Viel Spaß, in der Reinigung, tschüss, bis bald, oder, tschüss!"),
]

D[76] = [
("Lukas","m","Also, unsere Bücher! Liest du viel, Lisa, oder, sag mal, genau?"),
("Lisa","f","Total! Jeden Tag, ein Buch, fast, immer, toll, super."),
("Lukas","m","Toll! Sag mal, lese ich Krimis, spannend, am Abend, im Bett, mit Tee, gut, super, schön?"),
("Lisa","f","Ja, klar! Dick und gut, sehr spannend, toll, super, schön, gut."),
("Lukas","m","Super, ich lese Krimis! Liest du Liebesromane, romantisch, am Wochenende, auf dem Sofa, mit Decke, schön, gut, toll?"),
("Lisa","f","Genau, ich lese Liebesromane, romantisch, bis zum Ende, toll, super, schön, gut."),
("Lukas","m","Toll! Liest Tom Sachbücher, über Geschichte, dick, zum Lernen, gut, super, schön, toll?"),
("Lisa","f","Genau, Tom liest Sachbücher, gern, immer, toll, super, schön, gut."),
("Lukas","m","Immer! Liest Sara Kochbücher, mit Bildern, für Sonntag, toll, super, schön, gut?"),
("Lisa","f","Genau, Sara liest Kochbücher, toll, mit Appetit, super, schön, gut, toll."),
("Lukas","m","Super! Liest Tim Comics, bunt und lustig, im Zug, toll, super, schön, gut?"),
("Lisa","f","Genau, Tim liest Comics, täglich, zur Arbeit, super, toll, schön, gut, super."),
("Lukas","m","Toll! Liest jemand Gedichte, laut und schön, am Morgen, gut, super, schön, toll?"),
("Lisa","f","Nein, keiner, zu schwer, wirklich, oder, genau, ja, gut?"),
("Lukas","m","Schade! Liest jemand Biografien, dick und alt, heute, oder, sag mal, genau, gut, toll?"),
("Lisa","f","Nein, keine. Viel Spaß, beim Lesen, tschüss, bis bald, oder, tschüss!"),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
