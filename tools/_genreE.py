"""Genre batch E: tests 48-64 (synced from data)."""
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

D[48] = [
("Lukas","m","Also, unser Einkauf! Bist du fertig, Lisa, mit der Liste, mit der Liste, gut?"),
("Lisa","f","Fast! Viel steht da, für die Party, am Samstag, am Samstag, früh?"),
("Lukas","m","Stimmt! Sag mal, kaufe ich Fleisch, für den Grill, für alle?"),
("Lisa","f","Ja, bitte! Du grillst gut, seit Jahren, wirklich, wirklich, gut?"),
("Lukas","m","Danke, ich kaufe Fleisch! Kaufst du Getränke, Saft und Wasser, kalt, für alle, für alle, viel?"),
("Lisa","f","Genau, ich kaufe Getränke, drei Kästen, das reicht gut, keine Sorge, keine Sorge, gut?"),
("Lukas","m","Super! Kauft Tom Brot und Brötchen, frisch vom Bäcker, am Morgen, am Morgen, frisch?"),
("Lisa","f","Ja, Tom kauft Brot und Brötchen, warm und frisch, lecker, toll?"),
("Lukas","m","Lecker! Kauft Sara Gemüse für Salat, mit Tomaten, ganz frisch, vom Markt, vom Markt, frisch?"),
("Lisa","f","Genau, Sara kauft Gemüse für Salat, für alle, gesund, für alle, gern?"),
("Lukas","m","Gesund! Kauft Tim den Nachtisch, mit Kuchen und Eis, für alle, für alle, toll?"),
("Lisa","f","Ja, Tim kauft den Nachtisch, süß und kalt, alle lieben ihn, alle lieben ihn, sehr?"),
("Lukas","m","Toll! Kauft jemand Chips, mit Salz, zum Fernsehen? Oder Käse, zum Wein, zum Fernsehen, heute?"),
("Lisa","f","Nein, beides nicht. Genug Essen, wirklich, wirklich, glaub mir?"),
("Lukas","m","Verstehe! Dann bis Samstag, beim Grill, tschüss, beim Grill, tschüss!"),
("Lisa","f","Bis Samstag! Und bring Hunger mit, viel, viel, danke!"),
]

D[49] = [
("Lukas","m","Also, unser Theater! Gehst du oft, Lisa, heute?"),
("Lisa","f","Manchmal! Zuletzt im Mai, mit Freundin, schön, schön, sehr?"),
("Lukas","m","Schön! Sag mal, sehe ich Romeo und Julia, die Liebesgeschichte, am Freitag, am Freitag, gut?"),
("Lisa","f","Ja, klar! Du liebst Liebesfilme, seit immer, wirklich, wirklich, sehr?"),
("Lukas","m","Stimmt, ich sehe Romeo und Julia! Siehst du das Musical Cats, mit Kostümen, am Samstag, am Samstag, toll?"),
("Lisa","f","Genau, ich sehe das Musical Cats, mit Freundin, wir freuen uns sehr, wir freuen uns, sehr?"),
("Lukas","m","Toll! Sieht Tom ein Comedy-Stück, zum Lachen, am Sonntag, mit Bruder, am Sonntag, gut?"),
("Lisa","f","Ja, Tom sieht ein Comedy-Stück, lustig und laut, den ganzen Abend, den ganzen Abend, toll?"),
("Lukas","m","Lustig! Sieht Sara die Oper Don Giovanni, mit Mozart, im großen Haus, im großen Haus, schön?"),
("Lisa","f","Genau, Sara sieht die Oper Don Giovanni, drei Stunden, mit Pause, toll, mit Pause, gut?"),
("Lukas","m","Lang! Sieht Tim Ballett Schwanensee, mit schöner Musik, am Dienstag, am Dienstag, toll?"),
("Lisa","f","Ja, Tim sieht Ballett Schwanensee, mit Oma, sie liebt Ballett, sie liebt es, sehr?"),
("Lukas","m","Süß! Sieht jemand Faust, schwer und lang, am Montag, am Montag, gut?"),
("Lisa","f","Nein, keiner, zu schwer, für uns, wirklich, für uns, wirklich?"),
("Lukas","m","Verstehe! Dann viel Spaß, im Theater, allen, allen, tschüss!"),
("Lisa","f","Dir auch! Erzähl danach, wie es war, wie es war, genau?"),
]

D[50] = [
("Lukas","m","Also, unsere Tiere! Alles gut, Lisa, bei dir, bei dir, gut?"),
("Lisa","f","Na ja! Die Katze hustet, seit gestern, leider, leider, sehr?"),
("Lukas","m","Oh! Sag mal, bringe ich den Hund, zum Arzt, am Montag, er ist ruhig, am Montag, früh?"),
("Lisa","f","Ja, klar! Er sitzt ruhig, beim Arzt, wie immer, wie immer, gut?"),
("Lukas","m","Gut, ich bringe den Hund! Bringst du die Katze, zur Kontrolle, am Dienstag, ruhig, gut?"),
("Lisa","f","Genau, ich bringe die Katze, sie hat Angst, leider, die Arme, leider, arm?"),
("Lukas","m","Arme! Bringt Tom den Hamster, mit Husten, am Mittwoch, der Kleine, der Kleine, arm?"),
("Lisa","f","Ja, Tom bringt den Hamster, der Arzt gibt Medizin, schnell, schnell, gut?"),
("Lukas","m","Gut! Bringt Sara die Fische, mit Flecken, am Donnerstag, im Glas, im Glas, klein?"),
("Lisa","f","Genau, Sara bringt die Fische, der Arzt schaut genau, mit Licht, mit Licht, gut?"),
("Lukas","m","Genau! Bringt Tim den Papagei, er spricht nicht mehr, am Freitag, seit Wochen, seit Wochen, arm?"),
("Lisa","f","Ja, Tim bringt den Papagei, er ist ruhig, der Arme, hoffentlich gesund, hoffentlich gesund, ja?"),
("Lukas","m","Hoffentlich! Bringt jemand das Pferd, groß und stark, auch? Oder eine Schlange, lang und grün, auch, wirklich?"),
("Lisa","f","Nein, beides nicht. Zu groß, wirklich, wirklich, nein?"),
("Lukas","m","Verstehe! Dann gute Besserung, allen Tieren, schnell, tschüss!"),
("Lisa","f","Danke! Und bleib du gesund, auch, auch, danke!"),
]

D[51] = [
("Lukas","m","Also, unsere Augen! Siehst du gut, Lisa, gut?"),
("Lisa","f","Na ja! Abends schlecht, mit Licht, leider, leider, sehr?"),
("Lukas","m","Kenn ich! Sag mal, brauche ich eine normale Brille, zum Lesen und Fahren, stark, gut?"),
("Lisa","f","Ja, klar! Mit Gestell, stark und schön, modern, modern, toll?"),
("Lukas","m","Gut, ich brauche eine normale Brille! Brauchst du Kontaktlinsen, für den Sport, gut, wirklich?"),
("Lisa","f","Genau, ich brauche Kontaktlinsen, weiche, jeden Tag, neue, super, super, toll?"),
("Lukas","m","Super! Braucht Tom eine Lesebrille, nur für Bücher, am Abend, schwach, schwach, wirklich?"),
("Lisa","f","Ja, Tom braucht eine Lesebrille, plus eins, zum Lesen, gemütlich, gemütlich, gut?"),
("Lukas","m","Gemütlich! Braucht Sara eine Sonnenbrille mit Sehstärke, für den Sommer, gut, wirklich?"),
("Lisa","f","Genau, Sara braucht eine Sonnenbrille mit Sehstärke, dunkel und cool, toll, toll, schön?"),
("Lukas","m","Toll! Braucht Tim eine Augen-Operation, im Herbst, mit Laser, dann keine Brille, gut, wirklich?"),
("Lisa","f","Ja, Tim braucht eine Augen-Operation, kurz und gut, ohne Angst, ohne Angst, gut?"),
("Lukas","m","Sag mal, braucht jemand eine Brille mehr, für alle Fälle, wirklich, nein?"),
("Lisa","f","Nein, keiner, eine reicht, wirklich, glaub mir, allen, tschüss!"),
("Lukas","m","Verstehe! Dann gute Sicht, allen, allen, viel Glück!"),
("Lisa","f","Dir auch! Und putz sie oft, die Brille, die Brille, oft?"),
]

D[52] = [
("Lukas","m","Also, unser Badetag! Bist du bereit, Lisa, heute, gut?"),
("Lisa","f","Immer! Mit Handtuch, und guter Laune, wirklich, gut?"),
("Lukas","m","Super! Sag mal, gehe ich in die Sauna, abends, gern?"),
("Lisa","f","Ja, klar! Du liebst Hitze, seit immer, wirklich, wirklich, sehr?"),
("Lukas","m","Stimmt, ich gehe in die Sauna! Schwimmst du Bahnen, morgens, zehn Stück, gut, wirklich?"),
("Lisa","f","Genau, ich schwimme Bahnen, für die Fitness, mit Pause, nach fünf, gut, gern?"),
("Lukas","m","Fleißig! Fährt Tom Wasserrutsche, immer wieder, mit Freunden?"),
("Lisa","f","Ja, Tom fährt Wasserrutsche, juhu, schnell und toll."),
("Lukas","m","Toll! Springt Sara vom Turm, hoch, allein, allein, gut?"),
("Lisa","f","Genau, Sara springt vom Turm, platsch, ins Wasser, super, super, gut?"),
("Lukas","m","Platsch! Sitzt Tim im Whirlpool, mit Blasen, ganz ruhig, allein, gut?"),
("Lisa","f","Genau, Tim sitzt im Whirlpool, warm und ruhig, allein, allein, gut?"),
("Lukas","m","Allein! Braucht jemand das Kinderbecken, klein und flach? Oder Dampfbad, heiß, heute, gut?"),
("Lisa","f","Nein, beides nicht. Alle groß, heute, wirklich, gut?"),
("Lukas","m","Nein, keiner, alle groß, heute, wirklich, allen, tschüss!"),
("Lisa","f","Verstehe! Dann viel Spaß, im Bad, allen, tschüss, danke!"),
]

D[53] = [
("Lukas","m","Also, die Hochzeit! Bist du eingeladen, Lisa, heute, gut?"),
("Lisa","f","Ja! Im Mai, mit Fest, und Tanz, schön, gut?"),
("Lukas","m","Super! Sag mal, mache ich die Musik als DJ, mit Tanz, bis Mitternacht, gut, wirklich?"),
("Lisa","f","Ja, klar! Du hast Licht und Musik, toll, wirklich, gut?"),
("Lukas","m","Stimmt, ich mache die Musik als DJ! Bringst du Blumen, für die Tische, weiß und rosa, gut, wirklich?"),
("Lisa","f","Genau, ich bringe Blumen, für zehn Tische, schön und frisch, frisch, gut?"),
("Lukas","m","Schön! Macht Tom die Fotos, mit Kamera, den ganzen Tag, überall, überall, gut?"),
("Lisa","f","Ja, Tom macht die Fotos, er rennt viel, mit zwei Kameras, schnell, gut?"),
("Lukas","m","Fleißig! Backt Sara die Torte, drei Stockwerke, hoch, gut, wirklich?"),
("Lisa","f","Genau, Sara backt die Torte, süß und hoch, mit Liebe, gut, wirklich?"),
("Lukas","m","Lecker! Hält Tim die Rede, kurz und lustig, nach dem Essen?"),
("Lisa","f","Genau, Tim hält die Rede, fünf Minuten, alle lachen."),
("Lukas","m","Toll! Schickt jemand Einladungen, per Post, heute noch, heute noch, gut?"),
("Lisa","f","Nein, alle da. Organisiert jemand Spiele, für Kinder, wirklich, gut?"),
("Lukas","m","Nein, keine Zeit. Dann bis Mai, auf der Hochzeit, tschüss!"),
("Lisa","f","Verstehe! Dann bis Mai, auf der Hochzeit, tschüss, danke!"),
]

D[54] = [
("Lukas","m","Also, unsere Brillen! Siehst du gut, Lisa, gut?"),
("Lisa","f","Na ja! Morgens schlecht, ohne Kaffee, gut, wirklich?"),
("Lukas","m","Kenn ich! Sag mal, nehme ich die schwarze Hornbrille, schwarz und stark, gut, wirklich?"),
("Lisa","f","Ja, klar! Sie steht dir gut, sehr cool, wirklich, wirklich, gut?"),
("Lukas","m","Stimmt, ich nehme die schwarze Hornbrille! Nimmst du die randlose Brille, leicht und hell, gut, wirklich?"),
("Lisa","f","Genau, ich nehme die randlose Brille, fast unsichtbar, man spürt nichts, gut, wirklich?"),
("Lukas","m","Praktisch! Nimmt Tom die runde Brille, modern und jung, mit Metall, gut, wirklich?"),
("Lisa","f","Ja, Tom nimmt die runde Brille, sie gefällt ihm sehr, seit gestern, wirklich, gut?"),
("Lukas","m","Schön! Nimmt Sara die rote farbige Brille, rot und lustig, zum Kleid, gut, wirklich?"),
("Lisa","f","Genau, Sara nimmt die rote farbige Brille, Rot steht ihr gut, wirklich, wirklich, gut?"),
("Lukas","m","Toll! Nimmt Tim die Pilotenbrille, groß und cool, wie im Film, gut, wirklich?"),
("Lisa","f","Genau, Tim nimmt die Pilotenbrille, sie passt gut, wirklich, wirklich, gut?"),
("Lukas","m","Sag mal, nimmt jemand die Lesebrille, zum Lesen? Oder Bifokal, zum Arbeiten, gut, wirklich?"),
("Lisa","f","Nein, keine. Alle sehen gut, heute, gut, wirklich?"),
("Lukas","m","Verstehe! Dann gute Sicht, allen, mit Stil, tschüss!"),
("Lisa","f","Dir auch! Bis morgen, tschüss, tschüss, danke!"),
]

D[55] = [
("Lukas","m","Also, unsere Vereine! Bist du Fan, Lisa, gut?"),
("Lisa","f","Total! Mit Schal, immer, gut, wirklich?"),
("Lukas","m","Super! Sag mal, bin ich Bayern-Fan, seit der Kindheit, in Rot-Weiß, gut, wirklich?"),
("Lisa","f","Ja, klar! Rot-weiß, jedes Spiel, mit Freude, wirklich, gut?"),
("Lukas","m","Stimmt, ich bin Bayern-Fan, aus München, seit klein, gut, wirklich?"),
("Lisa","f","Genau, ich bin Dortmund-Fan, im Stadion, laut, jedes Spiel, gut, wirklich?"),
("Lukas","m","Und Tom, ist er Schalke-Fan"),
("Lisa","f","Ja, Tom ist Schalke-Fan, er bleibt dabei, immer, wirklich, gut?"),
("Lukas","m","Toll! Ist Sara HSV-Fan, aus Hamburg, mit Freunden, im Norden, gut, wirklich?"),
("Lisa","f","Genau, Sara ist HSV-Fan, mit Freunden, im Stadion, toll, wirklich, gut?"),
("Lukas","m","Toll! Ist Tim Bremen-Fan, Werder, grün-weiß, mit Papa, gut, wirklich?"),
("Lisa","f","Genau, Tim ist Bremen-Fan, jedes Spiel, zusammen, toll, wirklich, gut?"),
("Lukas","m","Toll! Spielt jemand für Köln, am Samstag? Oder in Frankfurt, am Sonntag, gut, wirklich?"),
("Lisa","f","Nein, beides nicht. Hoffentlich steigen alle auf, wirklich, gut, wirklich?"),
("Lukas","m","Hoffentlich alle! Bis dann, viel Glück, allen, tschüss!"),
("Lisa","f","Euch auch! Und schöne Spiele, am Wochenende, tschüss, danke!"),
]

D[56] = [
("Lukas","m","Also, unser Frühstück! Hast du Hunger, Lisa?"),
("Lisa","f","Riesig! Nur Kaffee, bis jetzt, nichts."),
("Lukas","m","Kenn ich! Sag mal, hole ich Brezeln, frisch und warm, vom Bäcker, zehn Stück?"),
("Lisa","f","Ja, bitte! Frisch und warm, toll."),
("Lukas","m","Stimmt, ich hole Brezeln! Holst du Croissants, mit Butter, für alle?"),
("Lisa","f","Genau, ich hole Croissants, aus Frankreich, frisch."),
("Lukas","m","Fein! Hole ich Vollkornbrot, gesund und frisch, ein großes, für die Woche?"),
("Lisa","f","Viel, mit Hunger. Holt Tom Vollkornbrot, auch?"),
("Lukas","m","Fein! Holt Tom Vollkornbrot, gesund und frisch, für die Woche?"),
("Lisa","f","Genau, Tom holt Vollkornbrot, dunkel und gut, jeden Tag."),
("Lukas","m","Gut! Holt Sara Käsekuchen, süß, zum Kaffee?"),
("Lisa","f","Genau, Sara holt Käsekuchen, mit Zucker, am Sonntag, toll."),
("Lukas","m","Toll! Holt Tim Berliner, mit Marmelade, für die Kinder?"),
("Lisa","f","Genau, Tim holt Berliner, süß, für alle, gern."),
("Lukas","m","Toll! Holt jemand Donuts, rund und süß? Oder Schwarzbrot, dunkel?"),
("Lisa","f","Nein, beides nicht. Genug Brot, wirklich."),
]

D[57] = [
("Lukas","m","Also, unsere Wohnungen! Suchst du, Lisa?"),
("Lisa","f","Seit Monaten! Teuer, alles, in der Stadt."),
("Lukas","m","Kenn ich! Sag mal, suche ich ein WG-Zimmer, zentral und billig, mit netten Leuten?"),
("Lisa","f","Ja, klar! Du magst WGs, seit Jahren, wirklich."),
("Lukas","m","Stimmt, ich suche ein WG-Zimmer! Suchst du eine Ein-Zimmer-Wohnung, klein, mit Balkon?"),
("Lisa","f","Genau, ich suche eine Ein-Zimmer-Wohnung, ruhig, mit Balkon."),
("Lukas","m","Grün! Sucht Tom eine Familie-Wohnung mit Garten, für vier, mit Kindern?"),
("Lisa","f","Ja, Tom sucht eine Familie-Wohnung mit Garten, mit Garten, für Kinder."),
("Lukas","m","Süß! Sucht Sara eine Maisonette mit Dachterrasse, hell und modern, mit Blick?"),
("Lisa","f","Genau, Sara sucht eine Maisonette mit Dachterrasse, wow, mit Sonne, teuer."),
("Lukas","m","Teuer! Sucht Tim ein Haus zum Kaufen, mit Garten, für immer?"),
("Lisa","f","Genau, Tim sucht ein Haus zum Kaufen, ein Traum, mit Hund."),
("Lukas","m","Beides! Also, ich suche ein Haus zum Kaufen, ein Traum!"),
("Lisa","f","Ach so, ein Traum! Sucht jemand ein Loft, offen und groß, in der Stadt?"),
("Lukas","m","Verstehe! Sucht jemand ein Studio, klein und hell, allein?"),
("Lisa","f","Nein, keiner. Dann viel Glück, bei der Suche!"),
]

D[58] = [
("Lukas","m","Also, unser freier Tag! Bist du fertig, Lisa?"),
("Lisa","f","Total! Pause, nur für uns, heute."),
("Lukas","m","Super! Sag mal, lasse ich mich rasieren, beim Friseur, kurz und gut?"),
("Lisa","f","Ja, klar! Kurz und gut, wie früher, toll."),
("Lukas","m","in Blau?"),
("Lisa","f","Genau, ich mache eine Maniküre, zum Kleid, rot und schön."),
("Lukas","m","Toll! Geht Tom zur Massage"),
("Lisa","f","Ja, Tom geht zur Massage, sie hilft gut, nach einer Stunde, sicher."),
("Lukas","m","Sicher! Und danach, was machen wir, essen gehen?"),
("Lisa","f","Gern, Pizza, nach allem, super."),
("Lukas","m","Sicher! Bekommt Sara eine Gesichtsbehandlung, mit Creme, gut?"),
("Lisa","f","Genau, Sara bekommt eine Gesichtsbehandlung, sie freut sich, sehr."),
("Lukas","m","Schön! Macht Tim eine Pediküre, im Sommer, gern?"),
("Lisa","f","Genau, Tim macht eine Pediküre, ist lustig, sehr, toll."),
("Lukas","m","Lustig! Färbt jemand die Haare, blond oder braun? Oder Wimpern, lang?"),
("Lisa","f","Nein, beides nicht. Alle Natur, wirklich."),
]

D[59] = [
("Lukas","m","Also, unsere Haare! Alles gut, Lars, bei dir?"),
("Lars","m","Klar! Voll und lang, wie immer."),
("Lukas","m","Toll! Sag mal, habe ich eine Glatze, ganz glatt, seit Jahren?"),
("Lars","m","Ja, klar! Praktisch und cool, im Sommer, top."),
("Lukas","m","Stimmt, ich habe eine Glatze! Hast du einen Iro, bunt, jeden Tag?"),
("Lars","m","Genau, ich habe einen Iro, mit Gel und Farbe, jeden Morgen, früh."),
("Lukas","m","Stark! Hat Tom einen Mittelscheitel mit langen Haaren, wie ein Star?"),
("Lars","m","Ja, Tom hat einen Mittelscheitel mit langen Haaren, aus dem Film, toll."),
("Lukas","m","Toll! Hat Sven einen Dutt, oben und praktisch, beim Sport?"),
("Lars","m","Genau, Sven hat einen Dutt, sehr praktisch, beim Training, immer."),
("Lukas","m","Praktisch! Hat Tim einen Undercut, kurz an den Seiten, oben lang?"),
("Lars","m","Genau, Tim hat einen Undercut, modern, jeden Tag."),
("Lukas","m","Modern! Hat jemand Dreadlocks, lang, bis zum Rücken?"),
("Lars","m","Nein, keiner. Hat jemand Locken, kurz und rund?"),
("Lukas","m","Nein, keine. Euch auch! Bis bald, beim Friseur!"),
("Lars","m","Nein, keine. Dann schöne Haare, allen!"),
]

D[60] = [
("Lukas","m","Also, unser Parktag! Bist du fit, Lisa?"),
("Lisa","f","Na ja! Lang geschlafen, bis zehn."),
("Lukas","m","Kenn ich! Sag mal, jogge ich, morgens, weit, mit Musik?"),
("Lisa","f","Ja, klar! Du läufst schnell, seit Jahren, wirklich."),
("Lukas","m","Stimmt, ich jogge! Fährst du Fahrrad, um den See, mit Freundin?"),
("Lisa","f","Genau, ich fahre Fahrrad, weit, mit Pause, am See."),
("Lukas","m","Weit! Und du, fährst du oft, am Wochenende?"),
("Lisa","f","Oft, bei Sonne. Liest Tom viel, auch?"),
("Lukas","m","Weit! Liest Tom auf einer Bank, mit Buch und Decke, ruhig?"),
("Lisa","f","Genau, Tom liest auf einer Bank, stundenlang, jeden Tag."),
("Lukas","m","Ruhig! Macht Sara Picknick mit Freundinnen, mit Decke und Kuchen?"),
("Lisa","f","Genau, Sara macht Picknick mit Freundinnen, am Wasser, schön."),
("Lukas","m","Schön! Spielt Tim Fußball, mit Freunden, auf der Wiese?"),
("Lisa","f","Genau, Tim spielt Fußball, bis abends, mit Spaß."),
("Lukas","m","Toll! Braucht jemand Frisbee, bunt und neu? Oder geht jemand spazieren?"),
("Lisa","f","Nein, beides nicht. Alles da, wirklich."),
]

D[61] = [
("Lukas","m","Also, unser Training! Na, Lisa, Training heute?"),
("Lisa","f","Total! Neue Schuhe, und los geht es."),
("Lukas","m","Super! Sag mal, mache ich Krafttraining, schwer, dreimal pro Woche?"),
("Lisa","f","Ja, klar! Du wirst stark, seit Monaten, wirklich."),
("Lukas","m","Stimmt, ich mache Krafttraining! Machst du Spinning, mit Musik, heiß?"),
("Lisa","f","Genau, ich mache Spinning, montags, super, heiß."),
("Lukas","m","Heiß! Ist Spinning schwer, montags, nach dem Wochenende?"),
("Lisa","f","Sehr schwer, aber toll, mit Musik, super."),
("Lukas","m","Toll! Macht Tom Yoga, abends, ruhig?"),
("Lisa","f","Genau, Tom macht Yoga, ruhig und tief, mit Musik."),
("Lukas","m","Tief! Geht Sara schwimmen, morgens, zwanzig Bahnen?"),
("Lisa","f","Genau, Sara geht schwimmen, vor der Arbeit, fit, gern."),
("Lukas","m","Fit! Macht Tim Boxen, mit Trainer, dienstags, stark?"),
("Lisa","f","Genau, Tim macht Boxen, stark und schnell, pow."),
("Lukas","m","Pow! Braucht jemand Pilates, ruhig? Oder Zumba, mit Musik?"),
("Lisa","f","Nein, beides nicht. Alle fit, wirklich."),
]

D[62] = [
("Lukas","m","Also, unser Marktbesuch! Bist du bereit, Lisa?"),
("Lisa","f","Immer! Mit Tasche, gern."),
("Lukas","m","Super! Sag mal, kaufe ich Fisch, frisch vom Meer, Forelle, für Freitag?"),
("Lisa","f","Ja, klar! Frisch und gut, vom Markt."),
("Lukas","m","Toll! Kaufst du Blumen, für die Wohnung, zum Sonntag?"),
("Lisa","f","Genau, ich kaufe Blumen, bunt und schön, jeden Samstag."),
("Lukas","m","Lecker! Kauft Tom Käse, zum Wein, für Gäste?"),
("Lisa","f","Genau, Tom kauft Käse, gut und frisch, für alle."),
("Lukas","m","Frisch! Kauft Sara Obst, Äpfel und Birnen, von hier?"),
("Lisa","f","Genau, Sara kauft Obst, süß und frisch, für die Kinder."),
("Lukas","m","Süß! Kauft Tim Honig, vom Markt, süß?"),
("Lisa","f","Genau, Tim kauft Honig, zum Frühstück, jeden Tag."),
("Lukas","m","Lecker! Verkauft jemand Gemüse, frisch und grün?"),
("Lisa","f","Nein, keiner, nur Obst, heute, wirklich."),
("Lukas","m","Nein, keiner, nur Obst, heute, wirklich."),
("Lisa","f","Verstehe! Dann guten Appetit, allen, vom Markt!"),
]

D[63] = [
("Lukas","m","Also, unsere Autos! Alles gut, Lisa?"),
("Lisa","f","Na ja! Es ist laut, seit gestern."),
("Lukas","m","Oh! Sag mal, ist meine Batterie leer, seit gestern, nichts geht?"),
("Lisa","f","Ja, klar! Kein Licht, kein Radio, nichts geht, leider."),
("Lukas","m","Tot! Also, meine Batterie ist leer! Hast du einen platten Reifen, heute Morgen?"),
("Lisa","f","Genau, ich habe einen platten Reifen, ganz platt, vor der Schule, schade."),
("Lukas","m","Oh! Ist Toms Bremse defekt, laut, seit Tagen?"),
("Lisa","f","Moment, deine Batterie ist doch leer, oder beides, wirklich?"),
("Lukas","m","Oh! Ist Toms Bremse defekt, laut, seit Tagen?"),
("Lisa","f","Genau, seine Bremse ist defekt, gefährlich, seit Montag."),
("Lukas","m","Gefährlich! Verliert Saras Auto Öl, jeden Tag, schlimm?"),
("Lisa","f","Genau, Saras Auto verliert Öl, in der Garage, schlimm."),
("Lukas","m","Schlimm! Ist Tims Klimaanlage kaputt, nur heiß, im Sommer?"),
("Lisa","f","Genau, seine Klimaanlage ist kaputt, schrecklich, der Arme."),
("Lukas","m","Beides! Also, meine Klimaanlage ist kaputt, schrecklich!"),
("Lisa","f","Ach so, schrecklich! Braucht jemand Licht, nachts, im Dunkeln?"),
]

D[64] = [
("Lukas","m","Also, unser Urlaub! Bist du bereit, Lisa?"),
("Lisa","f","Total! Koffer gepackt, und los geht es."),
("Lukas","m","Super! Sag mal, mache ich Strandurlaub, mit Sonne und Meer, zwei Wochen?"),
("Lisa","f","Ja, klar! Du wirst braun, jeden Tag, sehr."),
("Lukas","m","Genau, ich mache Strandurlaub! Mache ich eine Kreuzfahrt, mit Schiff, über das Meer?"),
("Lisa","f","Moment, du machst doch Strand, oder beides, wirklich?"),
("Lukas","m","Toll! Macht Tom eine Städtereise, nach Rom, mit Museen?"),
("Lisa","f","Genau, Tom macht eine Städtereise, kurz und gut, mit Fotos."),
("Lukas","m","Kurz! Geht Sara wandern in den Bergen, mit Rucksack?"),
("Lisa","f","Genau, Sara geht wandern in den Bergen, frische Luft, toll."),
("Lukas","m","Toll! Macht Tim Safari in Afrika, mit Tieren, weit?"),
("Lisa","f","Genau, Tim macht Safari in Afrika, ein Traum, mit Zelt."),
("Lukas","m","Beides! Also, ich mache Safari in Afrika, ein Traum!"),
("Lisa","f","Ach so, ein Traum! Braucht jemand Camping, mit Zelt, in der Natur?"),
("Lukas","m","Nein, keiner, alle anders, wirklich, glaub mir!"),
("Lisa","f","Verstehe! Dann schönen Urlaub, allen!"),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
