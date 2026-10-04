"""Batch D rewrite: tests 37-47 — natural direct speech."""
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
("Lukas","m","Also, unsere Jobs! Ich suche Arbeit als Programmierer, mit Java und Apps, in Berlin."),
("Lisa","f","Toll! Ich suche Arbeit als Lehrerin, für Mathe und Sport, an einer Schule."),
("Tom","m","Und ich suche Arbeit als Buchhalter, mit Zahlen, in einem Büro, ruhig und sicher."),
("Sara","f","Ich suche Arbeit als Krankenschwester, im Krankenhaus, mit Menschen, das mag ich."),
("Tim","m","Und ich suche Arbeit als Verkäufer im Einzelhandel, mit Mode, in der Stadt."),
("Lukas","m","Sehr gut! Lisa, hast du schon Bewerbungen geschrieben, als Lehrerin, viele?"),
("Lisa","f","Zehn schon, zwei Antworten, ein Gespräch nächste Woche, ich bin nervös."),
("Tom","m","Und Buchhalter, gibt es viele Stellen, zurzeit, in der Stadt?"),
("Sara","f","Bestimmt! Und Krankenschwester, überall gesucht, mit gutem Gehalt, wirklich."),
("Tim","m","Und Mode verkaufen, macht das Spaß, jeden Tag, im Laden?"),
("Lukas","m","Sicher! Also, ich suche Arbeit als Programmierer, in Berlin!"),
("Lisa","f","Ich suche Arbeit als Lehrerin, für Mathe und Sport!"),
("Tom","m","Ich suche Arbeit als Buchhalter, ruhig und sicher!"),
("Sara","f","Ich suche Arbeit als Krankenschwester, mit Menschen!"),
("Tim","m","Und ich suche Arbeit als Verkäufer im Einzelhandel, mit Mode!"),
("Lukas","m","Viel Glück allen, bei der Suche!"),
]

D[38] = [
("Lukas","m","Also, die Kinder und ihr Spielzeug! Ich spiele mit Autos, rote und blaue, überall."),
("Lisa","f","Schön! Ich spiele mit Puppen, zwei große, mit Kleidern, jeden Tag."),
("Tom","m","Und ich spiele mit Dinosauriern, laute und wilde, im Garten, brrr!"),
("Sara","f","Ich spiele mit Plüschtieren, ein Bär und ein Hase, im Bett, zum Kuscheln."),
("Tim","m","Und ich lese Bücher, mit Bildern, über Tiere, am Abend, mit Papa."),
("Lukas","m","Toll! Lisa, wie heißen deine Puppen, haben sie Namen, schöne?"),
("Lisa","f","Mia und Lena, sie haben viele Kleider, rot und blau, sehr hübsch."),
("Tom","m","Und Dinosaurier, sind sie gefährlich, nachts, im Dunkeln?"),
("Sara","f","Nur ein bisschen! Und Plüschtiere, kuschelt ihr auch, im Bett?"),
("Tim","m","Klar! Und Bücher, liest du schon allein, am Abend, wirklich?"),
("Lukas","m","Fast! Also, ich spiele mit Autos, rote und blaue!"),
("Lisa","f","Ich spiele mit Puppen, Mia und Lena!"),
("Tom","m","Ich spiele mit Dinosauriern, im Garten!"),
("Sara","f","Ich spiele mit Plüschtieren, zum Kuscheln!"),
("Tim","m","Und ich lese Bücher, über Tiere!"),
("Lukas","m","Super, viel Spaß allen, beim Spielen!"),
]

D[39] = [
("Lukas","m","Also, unsere Flüge im Sommer! Ich fliege nach New York, für zwei Wochen, mit Freunden."),
("Lisa","f","Wow! Ich fliege nach London, für ein Praktikum, einen Monat, spannend."),
("Tom","m","Und ich fliege nach Paris, mit der Familie, für eine Woche, mit Hotel."),
("Sara","f","Ich fliege nach Rom, für den Urlaub, mit Sonne und Pizza, herrlich."),
("Tim","m","Und ich fliege nach Tokio, ganz weit, für drei Wochen, mit Kamera."),
("Lukas","m","Toll! Lisa, ist London teuer, für einen Monat, mit Zimmer?"),
("Lisa","f","Sehr teuer! Aber das Praktikum zahlt gut, es geht, zum Glück."),
("Tom","m","Und Paris, was macht ihr dort, nur Stadt, oder auch Ausflüge?"),
("Sara","f","Stadt und ein Ausflug, ans Meer, für zwei Tage, mit dem Zug."),
("Tim","m","Und Tokio, sprichst du Japanisch, ein bisschen, für die Reise?"),
("Lukas","m","Ein bisschen! Also, ich fliege nach New York, mit Freunden!"),
("Lisa","f","Ich fliege nach London, für ein Praktikum!"),
("Tom","m","Ich fliege nach Paris, mit der Familie!"),
("Sara","f","Ich fliege nach Rom, mit Sonne und Pizza!"),
("Tim","m","Und ich fliege nach Tokio, mit Kamera!"),
("Lukas","m","Schönen Urlaub allen, gute Reise!"),
]

D[40] = [
("Lukas","m","Also, unser Strandtag! Ich surfe, mit dem Brett, in den Wellen, super!"),
("Lisa","f","Cool! Ich fahre Wasserski, hinter dem Boot, schnell und wild, juhu!"),
("Tom","m","Und ich bade in der Sonne und lese, mit Buch und Decke, ganz ruhig."),
("Sara","f","Ich baue Sandburgen, große mit Turm, am Wasser, den ganzen Tag."),
("Tim","m","Und ich tauche, mit Brille und Flossen, zu den Fischen, tief unten."),
("Lukas","m","Herrlich! Lisa, ist Wasserski schwer, für Anfänger, wirklich?"),
("Lisa","f","Am Anfang ja, nach einer Stunde geht es, mit Übung, glaub mir."),
("Tom","m","Und was liest du, in der Sonne, ein dickes Buch, spannend?"),
("Sara","f","Tom, er fragt dich! Also, was liest du, am Strand?"),
("Tom","m","Einen Krimi, sehr dick, fünfhundert Seiten, fast fertig."),
("Lukas","m","Und die Burg, Sara, wie hoch wird sie, mit Turm, ein Meter?"),
("Sara","f","Ein Meter! Also, ich baue Sandburgen, mit Turm!"),
("Lukas","m","Ich surfe, mit dem Brett, super!"),
("Lisa","f","Ich fahre Wasserski, schnell und wild!"),
("Tom","m","Ich bade in der Sonne und lese, ganz ruhig!"),
("Tim","m","Und ich tauche, zu den Fischen!"),
]
# fix: turn 9 self-address (Sara asks Tom, but phrased to self) — rewrite 8/9
D[40][7] = ("Sara","f","Und Tims Fische, sieht er Haie, beim Tauchen, tief unten?")
D[40][8] = ("Tom","m","Haie, hoffentlich nicht! Also, ich lese einen Krimi, fast fertig.")

D[41] = [
("Lukas","m","Also, unser Wintertag! Ich fahre Snowboard, auf der Piste, schnell und cool."),
("Lisa","f","Stark! Ich fahre Ski, den ganzen Tag, mit Pause, in der Hütte."),
("Tom","m","Und ich laufe Schlittschuh, auf dem See, mit Musik, abends, wunderschön."),
("Sara","f","Ich fahre Schlitten, mit den Kindern, den Berg hinunter, juhu!"),
("Tim","m","Und ich spiele Eishockey, im Verein, zweimal pro Woche, als Torwart."),
("Lukas","m","Toll! Lisa, ist die Piste gut, heute, mit viel Schnee?"),
("Lisa","f","Perfekt, frischer Schnee, seit gestern, die Sonne scheint sogar."),
("Tom","m","Und der See, ist das Eis dick genug, zum Laufen, sicher?"),
("Sara","f","Zehn Zentimeter, ganz sicher, die Kinder laufen schon, schau!"),
("Tim","m","Und Eishockey, gewinnst du oft, als Torwart, im Verein?"),
("Lukas","m","Oft! Also, ich fahre Snowboard, schnell und cool!"),
("Lisa","f","Ich fahre Ski, den ganzen Tag!"),
("Tom","m","Ich laufe Schlittschuh, auf dem See!"),
("Sara","f","Ich fahre Schlitten, mit den Kindern!"),
("Tim","m","Und ich spiele Eishockey, als Torwart!"),
("Lukas","m","Viel Spaß allen, im Schnee!"),
]

D[42] = [
("Lukas","m","Also, die Geschenke für Papa! Ich schenke Schmuck, eine Uhr, aus Silber, sehr edel."),
("Lisa","f","Toll! Ich schenke ein Buch, über Angeln, mit Bildern, er liebt es."),
("Tom","m","Und ich schenke Parfüm, herb und frisch, aus der Stadt, nicht billig."),
("Sara","f","Ich schenke Blumen, einen großen Strauß, bunt und frisch, vom Markt."),
("Tim","m","Und ich schenke Schokolade, die feine, aus Belgien, drei Tafeln."),
("Lukas","m","Schön! Lisa, liest Papa viel, wirklich, jeden Abend, im Sessel?"),
("Lisa","f","Ja, jeden Abend, eine Stunde, mit Tee, ganz gemütlich."),
("Tom","m","Und die Uhr, Lukas, ist sie teuer, aus Silber, wirklich?"),
("Sara","f","Nicht so teuer! Und Blumen, wie lange halten sie, frisch, eine Woche?"),
("Tim","m","Eine Woche! Und Schokolade, isst Papa viel, oder wenig, zurzeit?"),
("Lukas","m","Wenig! Also, ich schenke Schmuck, eine Uhr, aus Silber!"),
("Lisa","f","Ich schenke ein Buch, über Angeln!"),
("Tom","m","Ich schenke Parfüm, herb und frisch!"),
("Sara","f","Ich schenke Blumen, vom Markt!"),
("Tim","m","Und ich schenke Schokolade, aus Belgien!"),
("Lukas","m","Perfekt, Papa freut sich, bestimmt!"),
]

D[43] = [
("Lukas","m","Also, unsere Autos! Ich fahre einen BMW, schnell und bequem, schwarz, toll."),
("Lisa","f","Schön! Ich fahre einen Tesla, elektrisch und leise, ganz modern."),
("Tom","m","Und ich fahre einen VW Bus, groß und praktisch, für die Familie, mit Hund."),
("Sara","f","Ich fahre einen Mini Cooper, klein und rot, in der Stadt, perfekt."),
("Tim","m","Und ich fahre einen Mercedes, gebraucht und günstig, aber gut, silbern."),
("Lukas","m","Toll! Lisa, wie weit fährt der Tesla, mit einer Ladung, wirklich?"),
("Lisa","f","Vierhundert Kilometer, das reicht gut, für die Woche, locker."),
("Tom","m","Und der Bus, passt der Hund rein, bequem, mit Korb, hinten?"),
("Sara","f","Klar! Und Mini, parkt er überall, in der Stadt, schnell?"),
("Tim","m","Überall! Und Mercedes, ist er zuverlässig, gebraucht, wirklich?"),
("Lukas","m","Sehr! Also, ich fahre einen BMW, schwarz, toll!"),
("Lisa","f","Ich fahre einen Tesla, elektrisch und leise!"),
("Tom","m","Ich fahre einen VW Bus, mit Hund!"),
("Sara","f","Ich fahre einen Mini Cooper, klein und rot!"),
("Tim","m","Und ich fahre einen Mercedes, gebraucht, aber gut!"),
("Lukas","m","Gute Fahrt allen, immer sicher!"),
]

D[44] = [
("Lukas","m","Also, unsere Musik! Ich mag Rock, laut und live, mit Gitarre, super."),
("Lisa","f","Schön! Ich mag Klassik, mit Geige und Klavier, ruhig und schön."),
("Tom","m","Und ich mag Jazz, abends, mit Saxofon, in der Bar, gemütlich."),
("Sara","f","Ich mag Hip-Hop, mit Beat und Tanz, modern und cool, zum Trainieren."),
("Tim","m","Und ich mag Elektro, auf Partys, mit DJ, die ganze Nacht."),
("Lukas","m","Toll! Lisa, spielst du Geige, selbst, in einem Orchester?"),
("Lisa","f","Ja, seit fünf Jahren, im Orchester, jeden Freitag, es macht Spaß."),
("Tom","m","Und Jazz, gibt es gute Bars, hier, in der Stadt, mit live Musik?"),
("Sara","f","Zwei, sehr gemütlich, mit Kerzen, am Wochenende, voll."),
("Tim","m","Und Elektro, tanzt du viel, die ganze Nacht, auf Partys?"),
("Lukas","m","Immer! Also, ich mag Rock, laut und live!"),
("Lisa","f","Ich mag Klassik, ruhig und schön!"),
("Tom","m","Ich mag Jazz, in der Bar!"),
("Sara","f","Ich mag Hip-Hop, modern und cool!"),
("Tim","m","Und ich mag Elektro, auf Partys!"),
("Lukas","m","Viel Spaß allen, mit Musik!"),
]

D[45] = [
("Lukas","m","Also, unser Museumstag! Ich mag Geschichte, mit Rittern und Burgen, sehr spannend."),
("Lisa","f","Schön! Ich mag Moderne Kunst, bunt und wild, mit großen Bildern."),
("Tom","m","Und ich mag Naturkunde, mit Tieren und Steinen, seit der Schule, immer."),
("Sara","f","Ich mag Ägypten, mit Mumien und Gold, geheimnisvoll, wow."),
("Tim","m","Und ich mag Technik, mit Maschinen und Computern, zum Anfassen, cool."),
("Lukas","m","Toll! Lisa, verstehst du moderne Kunst, wirklich, oder nur so?"),
("Lisa","f","Manchmal, oft denke ich nur, interessant, und schaue weiter, ehrlich."),
("Tom","m","Und Ägypten, Sara, sind Mumien gruselig, im Dunkeln, wirklich?"),
("Sara","f","Ein bisschen, aber spannend, mit Gold und Geheimnis, toll."),
("Tim","m","Und Geschichte, Lukas, Ritter und Burgen, dein Hobby, seit wann?"),
("Lukas","m","Seit Jahren! Also, ich mag Geschichte, sehr spannend!"),
("Lisa","f","Ich mag Moderne Kunst, bunt und wild!"),
("Tom","m","Ich mag Naturkunde, seit der Schule!"),
("Sara","f","Ich mag Ägypten, geheimnisvoll!"),
("Tim","m","Und ich mag Technik, zum Anfassen!"),
("Lukas","m","Viel Spaß allen, im Museum!"),
]

D[46] = [
("Lukas","m","Also, unsere Züge! Ich fahre nach Berlin, am Freitag, mit dem ICE, schnell."),
("Lisa","f","Toll! Ich fahre nach Hamburg, zu Freunden, fürs Wochenende, mit Regionalzug."),
("Tom","m","Und ich fahre nach Köln, zum Konzert, am Samstag, mit der Band, im Zug."),
("Sara","f","Ich fahre nach München, zu Oma, für eine Woche, mit Kuchen, im Gepäck."),
("Tim","m","Und ich fahre nach Dresden, für ein Praktikum, einen Monat, mit Koffer."),
("Lukas","m","Schön! Lisa, bleiben deine Freunde zu Hause, am Wochenende, beide?"),
("Lisa","f","Ja, beide, wir kochen zusammen, am Samstag, gemütlich."),
("Tom","m","Und das Konzert, welche Band spielt, in Köln, kennst du sie?"),
("Sara","f","Tom, du fragst dich selbst! Also, welche Band spielt, in Köln?"),
("Tom","m","Eine Rockband, sehr laut, aus Hamburg, super!"),
("Lukas","m","Und Oma, Sara, freut sie sich, auf dich, mit Kuchen?"),
("Sara","f","Sehr! Also, ich fahre nach München, zu Oma!"),
("Lukas","m","Ich fahre nach Berlin, mit dem ICE!"),
("Lisa","f","Ich fahre nach Hamburg, zu Freunden!"),
("Tom","m","Ich fahre nach Köln, zum Konzert!"),
("Tim","m","Und ich fahre nach Dresden, für ein Praktikum!"),
]
# fix self-address turns 9/10
D[46][8] = ("Sara","f","Und das Konzert, Tom, welche Band spielt, in Köln?")
D[46][9] = ("Tom","m","Eine Rockband, sehr laut, aus Hamburg, super!")

D[47] = [
("Lukas","m","Also, unsere Computer! Ich programmiere eine App, fürs Handy, mit Freunden, cool."),
("Lisa","f","Toll! Ich bearbeite Fotos, für die Familie, mit Programm, am Abend."),
("Tom","m","Und ich schneide Videos, für YouTube, jede Woche, mit Musik, spannend."),
("Sara","f","Ich designe eine Webseite, für den Verein, bunt und klar, modern."),
("Tim","m","Und ich spiele Online-Spiele, abends, mit Freunden, im Team, lustig."),
("Lukas","m","Schön! Lisa, sind die Fotos gut, von der Familie, im Urlaub?"),
("Lisa","f","Sehr gut, über hundert Stück, vom Strand, wunderschön."),
("Tom","m","Und Videos, hast du viele Zuschauer, auf YouTube, schon?"),
("Sara","f","Tom, du fragst dich selbst! Also, deine Zuschauer, wie viele?"),
("Tom","m","Tausend schon, es werden mehr, jede Woche, toll!"),
("Lukas","m","Und die Webseite, Sara, wann ist sie fertig, bald, diese Woche?"),
("Sara","f","Bald! Also, ich designe eine Webseite, bunt und klar!"),
("Lukas","m","Ich programmiere eine App, mit Freunden!"),
("Lisa","f","Ich bearbeite Fotos, am Abend!"),
("Tom","m","Ich schneide Videos, jede Woche!"),
("Tim","m","Und ich spiele Online-Spiele, im Team!"),
]
# fix self-address turns 9/10
D[47][8] = ("Sara","f","Und deine Videos, Tom, hast du viele Zuschauer, schon?")
D[47][9] = ("Tom","m","Tausend schon, es werden mehr, jede Woche, toll!")

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
