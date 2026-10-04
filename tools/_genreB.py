"""Genre batch B: tests 13,14,16,18,19,20,21,22,24,25."""
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

D[13] = [
("Anna","f","Also, unser Ausflug am Sonntag! Bist du fertig, Markus, mit allem, gut?"),
("Markus","m","Fast! Das Wetter wird gut, hoffentlich, kein Regen, nur Sonne."),
("Anna","f","Hoffentlich! Sag mal, komme ich mit dem Zug, um neun, vom Bahnhof, mit Platz?"),
("Markus","m","Ja, gut! Der Zug ist schnell und billig, am Morgen, früh."),
("Anna","f","Genau, ich komme mit dem Zug! Kommst du mit dem Auto, mit freien Plätzen?"),
("Markus","m","Klar, ich komme mit dem Auto und nehme andere mit, drei Plätze frei, für euch."),
("Anna","f","Super! Fliegt Sara mit dem Flugzeug, aus Hamburg, um halb zehn, allein?"),
("Markus","m","Ja, Sara fliegt mit dem Flugzeug, sie landet spät, hoffentlich pünktlich, wie immer."),
("Anna","f","Viel Glück! Kommt Lukas mit dem Fernbus, ganz billig, um zehn, pünktlich?"),
("Markus","m","Genau, Lukas kommt mit dem Fernbus, direkt zum Treffpunkt, direkt und billig."),
("Anna","f","Praktisch! Gehen Tom und Lisa zu Fuß, durch den Park, zehn Minuten, schnell?"),
("Markus","m","Ja, sie gehen zu Fuß, sie wohnen nah, um die Ecke, gesund und froh."),
("Anna","f","Schön! Fährt jemand mit dem Fahrrad, oder nimmt ein Taxi, zum Treffpunkt?"),
("Markus","m","Nein, keiner, alle haben Pläne, schon fest, seit gestern, fest."),
("Anna","f","Schade! Dann bis Sonntag, um neun, am Bahnhof!"),
("Markus","m","Bis Sonntag! Und vergiss die Jacke nicht, es wird kalt, abends, wirklich, tschüss!"),
]

D[14] = [
("Tante Eva","f","Also, die Hochzeit! Bist du froh, Mama, sehr, findest du, auch?"),
("Mama","f","Sehr! So ein Fest, nur einmal im Jahr, mit allen, wunderbar, wie früher."),
("Tante Eva","f","Stimmt! Sag mal, organisiere ich die Location, den Saal am See?"),
("Mama","f","Ja, bitte! Du kennst den Ort, mit Terrasse, perfekt für Juni, mit Sonne."),
("Tante Eva","f","Gut, ich organisiere die Location! Kochst du das Hauptessen, für achtzig Gäste?"),
("Mama","f","Genau, ich koche das Hauptessen, mit zwei Helfern, alles frisch, aus dem Garten."),
("Tante Eva","f","Toll! Macht Papa die Fotos, mit der neuen Kamera, den ganzen Tag, überall?"),
("Mama","f","Ja, Papa macht die Fotos, er übt schon, seit Wochen, jeden Tag, gern."),
("Tante Eva","f","Schön! Spielt Lukas Musik, als DJ, am Abend, mit Tanz, bis spät?"),
("Mama","f","Genau, Lukas spielt Musik, er hat tolle Lieder, für alle, mit Tanz."),
("Tante Eva","f","Super! Hält Onkel Robert die Rede, kurz und lustig, nach dem Essen, mit Witz?"),
("Mama","f","Ja, Onkel Robert hält die Rede, fünf Minuten, alle lachen viel und laut."),
("Tante Eva","f","Herrlich! Backt jemand einen Kuchen, für das Paar, heute, frisch? Bringt jemand ein Geschenk?"),
("Mama","f","Nein, die Mutter der Braut backt. Geschenke bringen wir keine, nur Geld, viel Glück."),
("Tante Eva","f","Verstehe! Dann bis Samstag, um sechs, im Saal, pünktlich!"),
("Mama","f","Bis Samstag! Und bring gute Schuhe mit, zum Tanzen, bequeme, neue!"),
]

D[16] = [
("Mama","f","Also, das Essen am Sonntag! Hilfst du mir, Tante Eva, in der Küche, mit mir?"),
("Tante Eva","f","Klar! Ich koche gern, mit dir, wie immer, zusammen, gern, immer."),
("Mama","f","Schön! Sag mal, koche ich das Hauptgericht, einen Braten, mit Kartoffeln, frisch und heiß?"),
("Tante Eva","f","Ja, bitte! Dein Braten ist toll, in der Familie, seit Jahren, und allen schmeckt es."),
("Mama","f","Gut, ich koche das Hauptgericht! Bringst du eine Suppe, als Vorspeise, heiß?"),
("Tante Eva","f","Gern, ich bringe eine Suppe, mit frischem Brot, dazu, warm, mit viel Butter."),
("Mama","f","Toll! Backt Tim den Nachtisch, Apfelkuchen, wie Oma, mit Liebe, wie früher?"),
("Tante Eva","f","Genau, Tim backt den Nachtisch, nach Omas Rezept, mit Liebe, wie immer."),
("Mama","f","Wunderbar! Macht Lisa einen Salat, mit Tomaten, ganz frisch, aus dem Garten?"),
("Tante Eva","f","Ja, Lisa macht einen Salat, viel und frisch, für alle, mit Freude."),
("Mama","f","Super! Bringt Markus die Getränke, Saft und Wasser, kalt, für alle, viel?"),
("Tante Eva","f","Genau, Markus bringt die Getränke, aus dem Keller, kalt gestellt, von unten."),
("Mama","f","Perfekt! Dekoriert jemand den Tisch, mit Blumen, schön, rot und weiß, frisch, vom Markt?"),
("Tante Eva","f","Nein, keine Zeit, das Essen reicht, wirklich, für alle, keine Sorge, glaub mir."),
("Mama","f","Genau! Dann bis Sonntag, um sechs, bei uns, pünktlich, ja?"),
("Tante Eva","f","Bis Sonntag! Ich freue mich schon, auf euch, bis dann!"),
]

D[18] = [
("Vater","m","Also, die Geschenke! Freust du dich schon, Mutter, sehr, du auch?"),
("Mutter","f","Sehr! Weihnachten ist bald, ich liebe Feste, mit Kerzen, überall."),
("Vater","m","Ich auch! Sag mal, bekomme ich ein neues Smartphone, mit Kamera, neu? Ich wünsche es mir lange, sehr."),
("Mutter","f","Vielleicht! Du wünschst es dir, seit Monaten, jeden Tag."),
("Vater","m","Genau, ich bekomme ein neues Smartphone! Bekommst du ein Tablet, zum Lesen, abends, im Bett, warm."),
("Mutter","f","Genau, ich bekomme ein Tablet, ganz bequem, für mich."),
("Vater","m","Praktisch! Bekommt Lukas Kopfhörer, kabellos, für Musik und Sport, teuer? Er hört immer, überall, gern, täglich."),
("Mutter","f","Ja, Lukas bekommt kabellose Kopfhörer, endlich, er freut sich riesig, seit Wochen, jeden Tag."),
("Vater","m","Schön! Bekommt Sara eine Smartwatch, zum Laufen, mit Musik, neu?"),
("Mutter","f","Genau, Sara bekommt eine Smartwatch, sie läuft jeden Morgen, früh."),
("Vater","m","Sportlich! Bekommt Lisa einen Laptop, für die Schule, mit Internet, schnell? Zum Schreiben und Rechnen."),
("Mutter","f","Ja, Lisa bekommt einen Laptop, zum Lernen, mit neuer Tasche, für Bücher, viele, dicke, schwer."),
("Vater","m","Toll! Bekommt jemand eine Kamera, für Fotos, im Urlaub, am Meer, mit Sonne, am Strand?"),
("Mutter","f","Nein, Kameras hat jeder im Handy, heute, nicht wichtig, alle haben eins, heute."),
("Vater","m","Stimmt! Dann schönen Abend, mit allen zusammen."),
("Mutter","f","Frohe Weihnachten, bis bald, bis morgen, tschüss!"),
]

D[19] = [
("Markus","m","Also, unser Geld! Hast du den Plan, Anna, gut, alles klar?"),
("Anna","f","Fast! Viele Zahlen, im Monat, jeden Tag, viel Arbeit, im Büro."),
("Markus","m","Kenn ich! Sag mal, zahle ich die Miete, am Ersten, pünktlich, sicher, ganz?"),
("Anna","f","Ja, bitte! Du vergisst nie, alles pünktlich, jeden Tag, toll, danke dir."),
("Markus","m","Gut, ich zahle die Miete! Zahlst du die Stromrechnungen, online, schnell, allein, ohne mich?"),
("Anna","f","Genau, ich zahle die Stromrechnungen, alle zwei Monate, in zwei Minuten, schnell und gut, super, fix und fertig."),
("Markus","m","Fix! Verwaltet deine Mutter das Sparkonto der Kinder, mit Taschengeld, für Eis, im Sommer?"),
("Anna","f","Ja, meine Mutter verwaltet das Sparkonto der Kinder, sehr gut, jeden Monat, pünktlich, immer."),
("Markus","m","Toll! Prüft dein Vater die Versicherungen, einmal im Jahr, im Januar, wie immer?"),
("Anna","f","Genau, mein Vater prüft die Versicherungen, mit Brille, alles genau, ohne Fehler, perfekt."),
("Markus","m","Super! Macht Lisa den Lebensmittel-Einkauf, jede Woche, mit Liste, lang?"),
("Anna","f","Ja, Lisa macht den Lebensmittel-Einkauf, sparsam, mit guten Angeboten, für alle, billig."),
("Markus","m","Super! Zahlt jemand Steuern, im März, schon?"),
("Anna","f","Nein, erst im Mai, mit Hilfe, keine Sorge, alles gut, ruhig."),
("Markus","m","Puh! Dann bis nächsten Monat, mit dem Plan, bis dann, tschüss!"),
("Anna","f","Bis dann! Und kauf nichts Teures, bitte, hörst du, ja?"),
]

D[20] = [
("Anna","f","Also, unsere Sprachen! Lernst du fleißig, Lisa, jeden Tag?"),
("Lisa","f","Jeden Tag! Neue Wörter, morgens, mit Kaffee, jeden Morgen, früh."),
("Anna","f","Toll! Sag mal, lerne ich Spanisch, für den Urlaub, im Sommer, am Strand, mit Sonne?"),
("Lisa","f","Ja, klar! Du sprichst schon gut, nach dem Kurs, im Sommer, in Spanien?"),
("Anna","f","Danke, ich lerne Spanisch! Lernst du Italienisch, für Rom, im Herbst, in Rom, mit Eis?"),
("Lisa","f","Genau, ich lerne Italienisch, Essen bestellen geht schon, im Restaurant, mehr noch nicht, leider."),
("Anna","f","Lustig! Lernt Markus Französisch, für die Arbeit, mit Kunden aus Paris, wirklich, genau?"),
("Lisa","f","Ja, Markus lernt Französisch, jeden Tag, am Telefon, fleißig, ohne Pause, nie, wirklich."),
("Anna","f","Fix! Lernt Sara Chinesisch, an der Uni, sehr schwer, mit Zeichen, tausend?"),
("Lisa","f","Genau, Sara lernt Chinesisch, tausend Zeichen und mehr, jeden Tag, viel Arbeit, jeden Tag."),
("Anna","f","Wow! Lernt Lukas Russisch, für die Familie, mit Oma, aus Moskau, wirklich?"),
("Lisa","f","Ja, Lukas lernt Russisch, Oma hilft, zu Hause, gern, mit vielen dicken Büchern."),
("Anna","f","Schön! Lernt jemand Arabisch, mit neuer Schrift, oder Japanisch, ganz schwer, für alle?"),
("Lisa","f","Nein, keiner, fünf Sprachen reichen, beide nicht, für uns, wirklich."),
("Anna","f","Stimmt! Dann viel Erfolg, beim Lernen, viel Spaß, beim Üben!"),
("Lisa","f","Dir auch! Bis morgen, im Kurs, tschüss, viel Glück!"),
]

D[21] = [
("Vater","m","Also, unsere Autos! Hast du gehört, Mutter, was los ist, genau?"),
("Mutter","f","Ja, nur Ärger, überall, diese Woche, schlimm."),
("Vater","m","Also, sag mal, sind meine Bremsen kaputt, seit gestern, ganz schlimm, wirklich, jeden Tag?"),
("Mutter","f","Leider ja! Fahr vorsichtig, bitte, bis morgen, gut, ja?"),
("Vater","m","Schade, meine Bremsen sind kaputt! Hast du einen platten Reifen, heute Morgen, kalt?"),
("Mutter","f","Ja, ich habe einen platten Reifen, vor der Arbeit, ganz platt, leider, teuer, sehr, wirklich."),
("Vater","m","Oh nein! Ist die Batterie von Markus kaputt, startet nichts, gar nichts, schade."),
("Mutter","f","Genau, seine Batterie ist kaputt, das Auto bleibt stehen, bis morgen, lange."),
("Vater","m","Ärgerlich! Läuft bei Sara Öl aus, unter dem Motor, jeden Tag, immer?"),
("Mutter","f","Ja, bei Sara läuft Öl aus, ein Fleck, in der Garage, schlimm, sehr, schlimm."),
("Vater","m","Schlimm! Wurde Toms Auto gestohlen, letzte Nacht, vor dem Haus, weg?"),
("Mutter","f","Ja, Toms Auto wurde gestohlen, die Polizei sucht schon, seit heute Morgen, früh, um sieben."),
("Vater","m","Das gibt es doch nicht! Fährt jemand mit dem Bus, morgen früh, zur Arbeit, wie immer, früh?"),
("Mutter","f","Nein, der Nachbar hilft, mit seinem Wagen, zum Glück, nett, vom Nachbarn."),
("Vater","m","Puh! Dann in die Werkstatt, alle, morgen früh, pünktlich, alle!"),
("Mutter","f","Alle, ja! Und danach Kaffee, stark und schwarz, bitte, danke."),
]

D[22] = [
("Lisa","f","Also, die Geschenke für Oma! Hast du Ideen, Sara, hast du Zeit?"),
("Sara","f","Viele! Oma wird achtzig, ein Fest, mit allen, zusammen."),
("Lisa","f","Schön! Sag mal, schenke ich ein elegantes Tagebuch, mit Leder, sehr schön, dunkel?"),
("Sara","f","Ja, bitte! Oma schreibt viel, jeden Tag, ins Buch, täglich."),
("Lisa","f","Gut, ich schenke ein elegantes Tagebuch! Schenkst du ein Foto-Album, mit Bildern, aus dem Urlaub?"),
("Sara","f","Genau, ich schenke ein Foto-Album, mit alten Bildern, von der Familie, alle lachen."),
("Lisa","f","Toll! Schenkt Tom eine Flasche Wein, roten, aus Frankreich, sehr gut, teuer, aus dem Laden?"),
("Sara","f","Ja, Tom schenkt eine Flasche Wein, Oma liebt roten, zum Essen, rot."),
("Lisa","f","Toll! Schenkt Lukas eine Reisetasche, groß und praktisch, für den Urlaub, im Sommer, am Meer?"),
("Sara","f","Genau, Lukas schenkt eine Reisetasche, blau, mit viel Platz, für alles, immer."),
("Lisa","f","Praktisch! Schenken Anna und Markus Geld in einem Umschlag, hundert Euro, viel, zu viel?"),
("Sara","f","Ja, sie schenken Geld in einem Umschlag, von beiden, für Oma, lieb."),
("Lisa","f","Und Schmuck, schenkt jemand Schmuck, mit Gold, zum Geburtstag, mit Karte, selbst gemacht."),
("Sara","f","Nein, Oma mag keinen Schmuck, nur Blumen, sagt sie, immer."),
("Lisa","f","Verstehe! Dann bis Samstag, mit Geschenken, verpackt, schön, mit Band!"),
("Sara","f","Verpackt und mit Karte, bis dann, tschüss! Bis Samstag!"),
]

D[24] = [
("Lukas","m","Also, unsere Hobbys! Was läuft bei dir, heute, alles gut??"),
("Lisa","f","Viel! Schule, Kurse, wenig Zeit, leider, zu viel, wirklich.."),
("Lukas","m","Kenn ich! Sag mal, spiele ich Fußball im Verein, zweimal pro Woche, mit Freunden, im Park, bei Sonne, gern, sehr??"),
("Lisa","f","Ja, klar! Du schießt viele Tore, im Sturm, super, weiter so, stark, toll.."),
("Lukas","m","Stimmt, ich spiele Fußball im Verein! Lernst du Klavier, seit zwei Jahren, schon lange, seit Herbst, genau??"),
("Lisa","f","Genau, ich lerne Klavier, mit Lehrerin, es macht großen Spaß, jeden Tag, mit Spaß.."),
("Lukas","m","Toll! Tanzt Marie Ballett, jeden Mittwoch, wie immer, sehr??"),
("Lisa","f","Ja, Marie tanzt Ballett, in der Tanzschule, toll, jeden Tag, abends?."),
("Lukas","m","Schön! Malt Tim und zeichnet, Tiere, mit Farben, bunt, toll, schön, bunt??"),
("Lisa","f","Genau, Tim malt und zeichnet, am liebsten Tiere, zu Hause und in der Schule, überall, Tag und Nacht, immer.."),
("Lukas","m","Stark! Lernt Anna Sprachen, Englisch und Spanisch, nach der Schule, spät, abends, nach acht??"),
("Lisa","f","Ja, Anna lernt Sprachen, zweimal pro Woche, in Kursen, fleißig, sehr, mit Freude, für alle.."),
("Lukas","m","Fleißig! Spielt jemand Schach oder Karate, im Verein, samstags, morgens, um zehn, früh?"),
("Lisa","f","Nein, keiner, Spiele nur zu Hause, am Abend, gern, sehr.."),
("Lukas","m","Schade! Dann viel Spaß, mit Hobbys, weiter so, tschüss, bis bald!!"),
]

D[25] = [
("Mutter","f","Also, unsere Bücher! Liest du viel, Vater, du auch, oder, was meinst du, genau?"),
("Vater","m","Jeden Abend! Im Bett, mit Tee, warm, mit Milch."),
("Mutter","f","Schön! Sag mal, lese ich Krimis, am Abend, sehr spannend, findest du, auch, oder?"),
("Vater","m","Ja, klar! Du rätst immer mit, wer es war, genau."),
("Mutter","f","Stimmt, ich lese Krimis! Liest du Geschichtsbücher und Biografien, gern, sehr, wirklich?"),
("Vater","m","Genau, ich lese Geschichtsbücher und Biografien, über alte Zeiten, dick und gut, schwer, aber gut, sehr interessant, wirklich?"),
("Mutter","f","Interessant! Liest Lisa Liebesromane, auf dem Sofa, am Wochenende, lange, bis spät?"),
("Vater","m","Ja, Lisa liest Liebesromane, bis zum Ende, immer, gern, mit Tee."),
("Mutter","f","Süß! Liest Tom Science-Fiction, über den Mars, spannend, toll, cool?"),
("Vater","m","Genau, Tom liest Science-Fiction, mit Reisen zum Mars, toll und spannend, sehr, wirklich, genau?"),
("Mutter","f","Cool! Liest Marie Kinderbücher und Märchen, vor dem Schlafen, jeden Tag, abends, im Bett?"),
("Vater","m","Ja, Marie liest Kinderbücher und Märchen, Rotkäppchen liebt sie, sehr, seit Jahren, jeden Tag, abends?"),
("Mutter","f","Süß! Liest jemand Gedichte, laut und schön, am Morgen, um sechs?"),
("Vater","m","Nein, keiner, Gedichte mag niemand, hier, leider, nie, wirklich."),
("Mutter","f","Schade! Dann gute Nacht, mit Buch, bis morgen, ihr Lieben, tschüss!"),
("Vater","m","Gute Nacht! Schlaf gut, träum was Schönes, süß, tschüss!"),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
