"""Genre batch D: tests 37,38,39,41,42,43,44,45,46,47."""
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

D[37] = [
("Lukas","m","Also, unsere Jobs! Bist du zufrieden, Lisa, mit der Suche, alles gut?"),
("Lisa","f","Na ja! Viele Briefe, wenig Antworten, leider, wenig Glück."),
("Lukas","m","Kenn ich! Sag mal, suche ich Arbeit als Programmierer, in Berlin, mit Glück, bald, sicher?"),
("Lisa","f","Ja, klar! Du kannst das gut, seit der Uni, wirklich, du schaffst es."),
("Lukas","m","Danke, ich suche Arbeit als Programmierer! Suchst du Arbeit als Lehrerin, für Sport, an einer Schule, hier?"),
("Lisa","f","Genau, ich suche Arbeit als Lehrerin, für Sport und Rechnen, an einer Schule, gern, mit Kindern."),
("Lukas","m","Schön! Sucht Tom Arbeit als Buchhalter, mit Zahlen, im Büro, ruhig, sicher?"),
("Lisa","f","Ja, Tom sucht Arbeit als Buchhalter, sicher und ruhig, mit netten Leuten, ruhig."),
("Lukas","m","Toll! Sucht Sara Arbeit als Krankenschwester, im Krankenhaus, mit Menschen, gern?"),
("Lisa","f","Genau, Sara sucht Arbeit als Krankenschwester, sie hilft gern, Tag und Nacht, immer."),
("Lukas","m","Super! Sucht Tim Arbeit als Verkäufer im Einzelhandel, mit Mode, in der Stadt, neu, gut?"),
("Lisa","f","Ja, Tim sucht Arbeit als Verkäufer im Einzelhandel, er liebt Mode, sehr, wirklich."),
("Lukas","m","Passt! Sucht jemand Arbeit als Arzt oder Ingenieur, mit Studium, lang, sehr?"),
("Lisa","f","Nein, keiner, zu lang, das Studium, wirklich, lang."),
("Lukas","m","Verstehe! Dann viel Glück, bei der Suche, allen, viel Erfolg, tschüss!"),
("Lisa","f","Dir auch! Viel Glück, bitte, danke!"),
]

D[38] = [
("Lukas","m","Also, die Kinder! Was spielen sie, Lisa, zur Zeit, laut, sehr?"),
("Lisa","f","Alles! Drinnen, draußen, den ganzen Tag, laut, immer, Tag und Nacht, laut."),
("Lukas","m","Schön! Sag mal, spiele ich mit Autos, roten und blauen, überall, im Haus, überall?"),
("Lisa","f","Ja, klar! Du sammelst sie, seit Jahren, im Zimmer, viele, rot und blau, toll."),
("Lukas","m","Stimmt, ich spiele mit Autos! Spielst du mit Puppen, zwei großen, mit Kleidern, schön, neu?"),
("Lisa","f","Genau, ich spiele mit Puppen, Mia und Lena, jeden Tag, gern, immer, gern gespielt, täglich, mit Freude."),
("Lukas","m","Süß! Spielt Tom mit Dinosauriern, lauten, lustigen, im Garten, laut, brrr."),
("Lisa","f","Ja, Tom spielt mit Dinosauriern, brrr, sehr laut, aber toll, lustig, jeden Tag, laut."),
("Lukas","m","Lustig! Spielt Sara mit Plüschtieren, mit Bär und Hase, im Bett, weich, warm."),
("Lisa","f","Genau, Sara spielt mit Plüschtieren, zum Schlafen, jede Nacht, süß, klein, weich."),
("Lukas","m","Weich! Liest Tim Bücher, mit Bildern, über Tiere, am Abend, spät, abends?"),
("Lisa","f","Genau, Tim liest Bücher, mit Papa, auf dem Sofa, gern, mit Tee, warm, mit Milch."),
("Lukas","m","Gemütlich! Spielt jemand mit Bällen, draußen, im Park, bei Sonne, schön."),
("Lisa","f","Nein, nur drinnen, heute, es regnet, stark, seit Stunden, ohne Pause."),
("Lukas","m","Schade! Malt jemand Bilder, für Oma, heute, jetzt, gleich?"),
("Lisa","f","Nein, heute nicht. Räumt bitte auf, danach, sofort, bitte."),
]

D[39] = [
("Lukas","m","Also, unsere Flüge! Bist du fertig, Lisa, für den Sommer, fertig, mit Pass, ja?"),
("Lisa","f","Fast! Der Koffer steht schon, im Flur, gepackt, schwer."),
("Lukas","m","Super! Sag mal, fliege ich nach New York, für zwei Wochen, mit Freunden?"),
("Lisa","f","Ja, klar! Du freust dich schon, seit Monaten, sehr, seit langem, sehr."),
("Lukas","m","Genau, ich fliege nach New York! Fliegst du nach London, für ein Praktikum, einen Monat, lang?"),
("Lisa","f","Genau, ich fliege nach London, es zahlt gut, zum Glück, mit Geld, genug, für alles."),
("Lukas","m","Toll! Fliegt Tom nach Paris, mit der Familie, für eine Woche, mit Hotel, teuer, sehr?"),
("Lisa","f","Ja, Tom fliegt nach Paris, mit Kindern, juhu, toll, viel Spaß!"),
("Lukas","m","Juhu! Fliegt Sara nach Rom, für den Urlaub, mit Sonne, Pizza und Eis?"),
("Lisa","f","Genau, Sara fliegt nach Rom, im August, mit Freunden, toll."),
("Lukas","m","Herrlich! Fliegt Tim nach Tokio, ganz weit, mit Kamera, allein, weit weg?"),
("Lisa","f","Genau, Tim fliegt nach Tokio, drei Wochen, super, mit Rucksack, schwer."),
("Lukas","m","Toll! Also, ich fliege nach New York, mit Freunden, sicher, ganz sicher, ja, wirklich, viel?"),
("Lisa","f","Sicher! Dann gute Reise, mach Fotos, viele, schöne, viele!"),
("Lukas","m","Danke! Fliegt jemand nach Wien, oder Madrid, im Herbst, billig, toll."),
("Lisa","f","Nein, keiner. Bis dann, gute Flüge, allen, tschüss, gute Reise!"),
]

D[41] = [
("Lukas","m","Also, unser Wintertag! Bist du warm, Lisa, genug, warm, gut, heiß, warm?"),
("Lisa","f","Sehr! Mit Mütze und Tee, geht es, warm, sehr."),
("Lukas","m","Gut! Sag mal, fahre ich Snowboard, im Schnee, schnell und cool, toll, super, toll, schnell, toll."),
("Lisa","f","Ja, klar! Du fällst nie, seit Jahren, wirklich."),
("Lukas","m","Stimmt, ich fahre Snowboard! Fährst du Ski, den ganzen Tag, mit Pause, lang, sonnig."),
("Lisa","f","Genau, ich fahre Ski, in der Hütte gibt es Suppe, heiß. Läuft hier jemand Langlauf, im Wald, weit, allein?"),
("Lukas","m","Nein, keiner hier. Toll! Läuft Tom Schlittschuh, auf dem See, mit Musik, abends? Oder fährt er Ski, wie Lisa, wie der Wind, toll."),
("Lisa","f","Nein, nur Schlittschuh. Ski nur Lisa, allein, ohne mich."),
("Lukas","m","Romantisch! Fährt Sara Schlitten, mit den Kindern, den Berg hinunter, schnell, juhu, super."),
("Lisa","f","Genau, Sara fährt Schlitten, juhu, immer wieder, den ganzen Tag, toll, den Berg."),
("Lukas","m","Kalt! Spielt Tim Eishockey, im Verein, im Tor, sicher, gut."),
("Lisa","f","Genau, Tim spielt Eishockey, zweimal pro Woche, im Tor, gut, stark."),
("Lukas","m","Stark! Also, ich fahre Snowboard, cool, toll, herrlich."),
("Lisa","f","Cool! Und Skispringen, springt jemand, hoch, weit, hoch."),
("Lukas","m","Nein, zu gefährlich, heute. Und fall nicht hin, auf dem Eis, langsam, gut, gern."),
("Lisa","f","Du auch nicht, pass auf, wirklich, tschüss, bis morgen!"),
]

D[42] = [
("Lukas","m","Also, die Geschenke! Hast du Ideen, Lisa, für Papa, schnell?"),
("Lisa","f","Ein paar! Er wird sechzig, ein Fest, mit allen, zusammen, gern, sehr, wirklich."),
("Lukas","m","Schön! Sag mal, schenke ich Schmuck, eine Uhr, sehr schön, toll, teuer, neu, aus Gold, teuer?"),
("Lisa","f","Ja, klar! Papa liebt Uhren, seit Jahren, wirklich, sehr, gut."),
("Lukas","m","Genau, ich schenke Schmuck! Schenkst du ein Buch, über Fische, mit Bildern, schön, bunt, schön, groß, neu?"),
("Lisa","f","Genau, ich schenke ein Buch, er liest jeden Abend, gern, im Bett, warm, gut, weich."),
("Lukas","m","Toll! Schenkt Tom Parfüm, frisch und gut, aus der Stadt, nicht billig? Oder Wein, roten, dazu, kalt, sehr."),
("Lisa","f","Nur Parfüm! Gut verpackt, mit Karte, teuer, sehr, gut."),
("Lukas","m","Toll! Schenkt Sara Blumen, viele Blumen, bunt und frisch, vom Markt, rot, groß, schwer."),
("Lisa","f","Genau, Sara schenkt Blumen, jeden Samstag, sie liebt Märkte, sehr, immer."),
("Lukas","m","Schön! Schenkt Tim Schokolade, aus Belgien, drei Tafeln? Oder Geld, für Papa, viel?"),
("Lisa","f","Schokolade, die gute! Geld gibt es nicht, nein, leider, zu teuer, leider."),
("Lukas","m","Toll! Also, ich schenke Schmuck, zum Fest, toll, super, schön."),
("Lisa","f","Gut! Dann packen wir ein, heute Abend, schnell, sofort."),
("Lukas","m","Ja, schön, mit Liebe, sehr, toll, gut."),
("Lisa","f","Bis dann, Papa freut sich, sicher, ganz sicher, tschüss! Bis dann!"),
]

D[43] = [
("Lukas","m","Also, unsere Autos! Fährst du gern, Lisa, du auch, oder?, sag schon.?"),
("Lisa","f","Sehr! Schnell, aber sicher, immer, gern, sehr, toll, schnell, toll.."),
("Lukas","m","Genau! Sag mal, fahre ich einen BMW, schnell und bequem, schwarz, neu, teuer, gut, teuer, gut, neu.?"),
("Lisa","f","Ja, klar! Mit Radio, in der Stadt, super, toll, schnell, bequem.."),
("Lukas","m","Stimmt, ich fahre einen BMW! Fährst du einen Tesla, leise und neu, schnell, gut, wirklich.?"),
("Lisa","f","Genau, ich fahre einen Tesla, ganz modern, mit Strom, billig, gut, super, toll.."),
("Lukas","m","Modern! Fährt Tom einen VW Bus, groß und praktisch, für die Familie, groß, lang, groß?, groß, neu??"),
("Lisa","f","Ja, Tom fährt einen VW Bus, mit Hund, mit Kindern, überall, immer, täglich.."),
("Lukas","m","Praktisch! Fährt Sara einen Mini Cooper, klein und rot, in der Stadt, klein, praktisch, klein, rot, schön??"),
("Lisa","f","Genau, Sara fährt einen Mini Cooper, zum Parken, überall, schnell, toll, toll, schnell, gut.."),
("Lukas","m","Neu! Fährt Tim einen Mercedes, gebraucht, grau, alt, billig, alt, grau, gut??"),
("Lisa","f","Genau, Tim fährt einen Mercedes, gebraucht, aber gut, stark, gut, ohne Fehler.."),
("Lukas","m","Toll! Also, ich fahre einen BMW, schwarz, toll! Oder Audi, was meinst du, genau, wirklich, genau, ja?, schwarz, schön??"),
("Lisa","f","BMW bleibt! Audi nicht, zu teuer. Gute Fahrt, tschüss, gute Reise, viel Spaß!!"),
("Lukas","m","Danke! Fährt jemand Porsche, rot und schnell, hier, heute, wirklich, heute?, rot, neu??"),
("Lisa","f","Nein, keiner. Bis dann, fahr vorsichtig, bitte, danke, tschüss!!"),
]

D[44] = [
("Lukas","m","Also, unsere Musik! Was hörst du, Lisa, gerade, heute, jetzt, gleich?"),
("Lisa","f","Alles! Morgens Klassik, abends laut, je nach Tag, gern, immer."),
("Lukas","m","Cool! Sag mal, mag ich Rock, laut und toll, mit Gitarre, wirklich, gut?"),
("Lisa","f","Ja, klar! Du spielst selbst, seit Jahren, im Keller, laut, sehr, toll."),
("Lukas","m","Genau, ich mag Rock! Magst du Klassik, mit Klavier, jeden Tag, abends, gern?"),
("Lisa","f","Genau, ich mag Klassik, ruhig und schön, am Abend, mit Tee, warm, gut, toll."),
("Lukas","m","Schön! Mag Tom Jazz, abends, in der Bar? Hört er Klassik, wie du, allein, wirklich, genau, ja, sicher."),
("Lisa","f","Nein, nur Jazz. Klassik mag Lisa, allein, ohne mich, sicher."),
("Lukas","m","Also, mag Sara Hip-Hop, mit Tanz, laut, toll, super, schön."),
("Lisa","f","Genau, Sara mag Hip-Hop, zum Trainieren, jeden Morgen, früh, pünktlich, gut."),
("Lukas","m","Laut! Mag Tim Elektro, auf Partys, mit DJ? Hört er Rock, laut, stark, toll."),
("Lisa","f","Nein, nur Elektro. Rock mag Lukas, allein, ohne Pop, ohne Radio, nie, wirklich."),
("Lukas","m","Stark! Also, ich mag Rock, laut und toll! Hört jemand Volksmusik, zu Hause, heute, Abend, jetzt?"),
("Lisa","f","Nein, beides nicht. Super! Dann viel Spaß, mit Musik, bis dann!"),
("Lukas","m","Danke! Und komm mit, aufs Konzert, bald, kommst du mit?"),
("Lisa","f","Gern! Ich liebe Konzerte, sehr, toll, super."),
]

D[45] = [
("Lukas","m","Also, unser Museumstag! Bist du fertig, Lisa, alles klar, ja, gut?"),
("Lisa","f","Immer! Mit Kamera, und bequemen Schuhen, neu, bequem, toll?"),
("Lukas","m","Super! Sag mal, mag ich Geschichte, mit Burgen, sehr spannend, sehr, toll, schön."),
("Lisa","f","Ja, klar! Du liest alles, seit der Schule, dicke Bücher, viele, dicke, schwer?"),
("Lukas","m","Genau, ich mag Geschichte! Magst du Moderne Kunst, bunt und toll, toll, schön, neu?"),
("Lisa","f","Genau, ich mag Moderne Kunst, mit großen Bildern, voller Farben, bunt, schön, groß?"),
("Lukas","m","Bunt! Mag Tom Naturkunde, mit Tieren und Steinen, seit der Schule, immer, gern, gut."),
("Lisa","f","Ja, Tom mag Naturkunde, besonders Tiere, schon immer, gern, sehr, gut."),
("Lukas","m","Sag mal, mag Sara Ägypten, mit Gold, spannend, toll, schön?"),
("Lisa","f","Ägypten? Was gibt es dort, genau, was meinst du, genau, ja?"),
("Lukas","m","Na, Gold und mehr! Also, Sara mag Ägypten, mit Gold, sehr, wirklich, sehr, gut."),
("Lisa","f","Ach so, mit Gold! Mag Tim Technik, mit Computer, immer, gern, immer, oft."),
("Lukas","m","Genau, Tim mag Technik, mit Computer, immer, täglich, früh, pünktlich."),
("Lisa","f","Toll! Also, ich mag Moderne Kunst, bunt und toll! Magst du Mode, im Fernsehen, oft, gern, sehr?"),
("Lukas","m","Nein, nur Kunst. Mag jemand Sport, im Park, sehr, stark, toll, gut."),
("Lisa","f","Nein, nur Museum. Bis Samstag, mit Kamera, tschüss, viel Spaß, bis dann!"),
]

D[46] = [
("Lukas","m","Also, unsere Züge! Wohin geht es, Lisa, bei dir, wohin, sag schon?"),
("Lisa","f","In alle Richtungen, fast, dieses Jahr, viel, überall, gern."),
("Lukas","m","Überall! Sag mal, fahre ich nach Berlin, am Freitag, mit dem ICE, schnell, direkt, toll."),
("Lisa","f","Ja, klar! Schnell, in zwei Stunden, toll, super, bequem."),
("Lukas","m","Stimmt, ich fahre nach Berlin! Fährst du nach Hamburg, zu Freunden, fürs Wochenende, lang, schön, gut."),
("Lisa","f","Genau, ich fahre nach Hamburg, wir kochen zusammen, am Samstag, gern, sehr, mit Freude."),
("Lukas","m","Sag mal, fährt Tom nach Köln, zum Konzert, am Samstag, mit der Band, laut, toll."),
("Lisa","f","Ja, Tom fährt nach Köln, laut und voll, mit Freunden, super, toll, schön."),
("Lukas","m","Laut! Fährt Sara nach München, zu Oma, für eine Woche, mit Kuchen, süß, klein, neu."),
("Lisa","f","Genau, Sara fährt nach München, Oma freut sich, mit Kuchen, sehr, gut, toll."),
("Lukas","m","Süß! Fährt Tim nach Dresden, für ein Praktikum, einen Monat, lang, neu, spannend."),
("Lisa","f","Genau, Tim fährt nach Dresden, mit Tasche, viel Glück, tschüss, bis bald."),
("Lukas","m","Toll! Also, ich fahre nach Berlin, am Freitag, früh, pünktlich."),
("Lisa","f","Beide! Dann viel Erfolg, gute Reise, viel Spaß, bis dann!"),
("Lukas","m","Danke! Fährt jemand nach Leipzig, oder Stuttgart, bald, sicher, wirklich, bald?"),
("Lisa","f","Nein, keiner. Bis dann, gute Fahrt, allen, tschüss, bis morgen!"),
]

D[47] = [
("Lukas","m","Also, unsere Computer! Was läuft, Lisa, bei dir, alles klar, ja, gut?"),
("Lisa","f","Viel! Arbeit, Mails, abends, lange, täglich, lang, sehr."),
("Lukas","m","Kenn ich! Sag mal, programmiere ich eine App, fürs Handy, mit Freunden, cool, neu, toll?"),
("Lisa","f","Ja, klar! Seit Monaten, mit Freunden, cool, toll, gut, schnell."),
("Lukas","m","Stimmt, ich programmiere eine App! Bearbeitest du Fotos, für die Familie, am Abend, spät, abends?"),
("Lisa","f","Genau, ich bearbeite Fotos, stundenlang, alle scharf, toll, schön, groß, neu?"),
("Lukas","m","Schön! Schneidet Tom Videos, für YouTube, jede Woche, mit Musik, toll, laut, stark?"),
("Lisa","f","Ja, Tom schneidet Videos, tausend Zuschauer, es werden mehr, toll, toll, super, schön."),
("Lukas","m","Toll! Designt Sara eine Webseite, für den Verein, bunt und klar, bunt, schön, groß?"),
("Lisa","f","Genau, Sara designt eine Webseite, modern, mit Fotos, bald fertig, bald, sicher, bald?"),
("Lukas","m","Modern! Spielt Tim Online-Spiele, abends, mit Freunden, im Team? Oder schreibt er Mails, abends, spät, nachts, allein?"),
("Lisa","f","Spiele! Mails schreibt keiner. Tim spielt, im Team, lustig, sehr, gut, toll."),
("Lukas","m","Toll! Also, ich programmiere eine App, weiter, fleißig, weiter."),
("Lisa","f","Ach so, im Team! Dann viel Spaß, am Computer, gern, oft."),
("Lukas","m","Danke! Schreibt jemand Texte, für die Seite, heute, jetzt, gleich?"),
("Lisa","f","Nein, nur Fotos. Bis dann, viel Erfolg, allen, tschüss, bis dann!"),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
