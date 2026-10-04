"""Batch B rewrite: tests 13,14,16,18,19,20,21,22,24,25 — natural direct speech."""
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
("Anna","f","Also, unser Ausflug am Sonntag! Ich komme mit dem Zug, um neun, vom Hauptbahnhof."),
("Markus","m","Sehr gut! Ich komme mit dem Auto, es nimmt drei Leute mit, dich, Anna, und Lukas."),
("Sara","f","Und ich fliege mit dem Flugzeug, aus Hamburg, ich lande um halb zehn."),
("Lukas","m","Ich komme mit dem Fernbus, ganz billig, um zehn, direkt zum Treffpunkt."),
("Tom","m","Und wir gehen zu Fuß, Lisa und ich, wir wohnen ganz in der Nähe."),
("Lisa","f","Genau, wir gehen zu Fuß, nur zehn Minuten, durch den Park, sehr schön."),
("Anna","f","Perfekt, alle kommen anders! Markus, wen nimmst du mit, im Auto?"),
("Markus","m","Dich, Anna, vom Bahnhof, und Lukas vom Bus, das passt gut."),
("Sara","f","Und wer holt mich ab, vom Flughafen, um halb zehn, bitte?"),
("Lukas","m","Ich, Sara! Der Bus hält am Flughafen, um zehn, wir treffen uns dort."),
("Tom","m","Und das Wetter, wird es schön, am Sonntag, zum Wandern?"),
("Lisa","f","Ja, sonnig und warm, ideal für uns, zu Fuß durch den Park!"),
("Anna","f","Also, ich komme mit dem Zug, um neun, vom Hauptbahnhof!"),
("Markus","m","Ich komme mit dem Auto und nehme andere mit, drei Plätze!"),
("Sara","f","Ich fliege mit dem Flugzeug, aus Hamburg, um halb zehn!"),
("Lukas","m","Und ich komme mit dem Fernbus, um zehn, zum Treffpunkt!"),
]

D[14] = [
("Tante Eva","f","Also, die Hochzeit am Samstag! Ich organisiere die Location, den Saal am See, mit Terrasse."),
("Mama","f","Wunderbar! Ich koche das Hauptessen, für achtzig Gäste, mit zwei Helfern."),
("Papa","m","Und ich mache die Fotos, mit meiner neuen Kamera, den ganzen Tag."),
("Lukas","m","Ich spiele Musik, als DJ, am Abend, mit Tanz und allem."),
("Onkel Robert","m","Und ich halte die Rede, kurz und lustig, nach dem Essen."),
("Tante Eva","f","Sehr gut! Mama, schaffst du das Essen, für achtzig Gäste, allein mit zwei Helfern?"),
("Mama","f","Ja, wir kochen zwei Tage lang, alles frisch, keine Sorge, es reicht."),
("Papa","m","Und die Rede, Robert, wie lange dauert sie, bitte nicht zu lange?"),
("Onkel Robert","m","Nur fünf Minuten, versprochen, kurz und lustig, alle lachen."),
("Lukas","m","Und das Brautpaar, wann kommt es, um sechs, in den Saal?"),
("Tante Eva","f","Um sechs! Also, ich organisiere die Location, den Saal am See!"),
("Mama","f","Ich koche das Hauptessen, für achtzig Gäste!"),
("Papa","m","Ich mache die Fotos, mit meiner Kamera, den ganzen Tag!"),
("Lukas","m","Ich spiele Musik, als DJ, am Abend!"),
("Onkel Robert","m","Und ich halte die Rede, kurz und lustig!"),
("Tante Eva","f","Perfekt, alles klar! Bis Samstag, um sechs, im Saal!"),
]

D[16] = [
("Mama","f","Also, das Abendessen am Sonntag! Ich koche das Hauptgericht, einen Braten, mit Kartoffeln."),
("Tante Eva","f","Lecker! Ich bringe eine Suppe, als Vorspeise, mit frischem Brot."),
("Tim","m","Und ich backe den Nachtisch, einen Apfelkuchen, mit Zimt, nach Omas altem Rezept."),
("Lisa","f","Schön! Ich mache einen Salat, mit Tomaten und Gurken, ganz frisch."),
("Markus","m","Und ich bringe die Getränke, mit Saft und Wasser, kalt aus dem Keller."),
("Mama","f","Perfekt! Tim, brauchst du Hilfe, beim Kuchen, mit dem Teig?"),
("Tim","m","Nein, danke, das kann ich schon, Omas Rezept ist ganz einfach."),
("Tante Eva","f","Und der Salat, Lisa, reicht ein Salat, für sechs Personen?"),
("Lisa","f","Ja, eine große Schüssel, mit viel Gemüse, das reicht sicher für alle."),
("Markus","m","Und wann essen wir, um sechs, bei euch, wie immer?"),
("Mama","f","Um sechs! Also, ich koche das Hauptgericht, einen Braten!"),
("Tante Eva","f","Ich bringe eine Suppe, mit frischem Brot!"),
("Tim","m","Ich backe den Nachtisch, Apfelkuchen mit Zimt!"),
("Lisa","f","Ich mache einen Salat, ganz frisch!"),
("Markus","m","Und ich bringe die Getränke, kalt aus dem Keller, für alle!"),
("Mama","f","Sehr gut, bis Sonntag, um sechs, bei uns!"),
]

D[18] = [
("Vater","m","Also, die Geschenke zu Weihnachten! Ich bekomme ein neues Smartphone, mit großer Kamera und viel Speicher."),
("Mutter","f","Schön! Ich bekomme ein Tablet, zum Lesen und für Filme, im Bett, jeden Abend."),
("Lukas","m","Und ich bekomme kabellose Kopfhörer, für Musik und Sport, endlich, ich freue mich sehr!"),
("Sara","f","Ich bekomme eine Smartwatch, mit Schrittzähler, fürs Laufen, jeden Morgen."),
("Lisa","f","Und ich bekomme einen Laptop, für die Schule, mit schnellem Internet und neuer Tasche."),
("Vater","m","Tolle Geschenke! Mutter, welches Tablet, mit großem Bildschirm, oder klein?"),
("Mutter","f","Mit großem Bildschirm, zum Lesen, meine Augen sind nicht mehr jung."),
("Lukas","m","Und die Kopfhörer, Lukas, also meine, halten sie lange, der Akku?"),
("Sara","f","Lukas, fragst du dich selbst? Also, deine Kopfhörer halten zehn Stunden!"),
("Lisa","f","Sehr gut! Und mein Laptop, kommt er noch an, vor Weihnachten?"),
("Vater","m","Bestimmt! Also, ich bekomme ein neues Smartphone, mit Kamera!"),
("Mutter","f","Ich bekomme ein Tablet, mit großem Bildschirm!"),
("Lukas","m","Ich bekomme kabellose Kopfhörer, für Musik und Sport!"),
("Sara","f","Ich bekomme eine Smartwatch, fürs Laufen!"),
("Lisa","f","Und ich bekomme einen Laptop, für die Schule!"),
("Vater","m","Perfekt, alle glücklich! Frohe Weihnachten, ihr Lieben!"),
]
# fix self-address turns 8/9
D[18][7] = ("Lukas","m","Halten deine Kopfhörer lange, fragst du? Zehn Stunden, super!")
D[18][8] = ("Sara","f","Lukas, sprichst du mit dir selbst? Sehr lustig, wirklich!")

D[19] = [
("Markus","m","Also, unser Geld im Monat! Ich zahle die Miete, am Ersten, per Dauerauftrag, pünktlich."),
("Anna","f","Gut! Ich zahle die Stromrechnungen, alle zwei Monate, online, ganz schnell, in zwei Minuten."),
("Mutter","f","Und ich verwalte das Sparkonto der Kinder, mit Taschengeld, jeden Monat, sehr ordentlich."),
("Vater","m","Ich prüfe die Versicherungen, einmal im Jahr, im Januar, alles genau, mit Brille."),
("Lisa","f","Und ich mache den Lebensmittel-Einkauf, jede Woche, mit Liste, sparsam, mit guten Angeboten."),
("Markus","m","Sehr gut! Anna, ist der Strom teuer, diesen Monat, im Winter?"),
("Anna","f","Leider ja, fast hundert Euro, wegen der Heizung, im Januar."),
("Mutter","f","Und das Sparkonto, reicht das Taschengeld, für die Kinder, im Monat?"),
("Vater","m","Ja, fünfzig Euro pro Kind, das reicht gut, sie sparen sogar."),
("Lisa","f","Und mein Einkauf, zweihundert Euro pro Woche, für alle, passt das?"),
("Markus","m","Passt! Also, ich zahle die Miete, am Ersten!"),
("Anna","f","Ich zahle die Stromrechnungen, online!"),
("Mutter","f","Ich verwalte das Sparkonto der Kinder!"),
("Vater","m","Ich prüfe die Versicherungen, im Januar!"),
("Lisa","f","Und ich mache den Lebensmittel-Einkauf, jede Woche!"),
("Markus","m","Perfekt, alles geregelt! Bis nächsten Monat!"),
]

D[20] = [
("Anna","f","Also, unsere Sprachen im Kurs! Ich lerne Spanisch, für den Urlaub, im Sommer, am Strand."),
("Lisa","f","Schön! Ich lerne Italienisch, für die Reise nach Rom, im Herbst, in Rom."),
("Markus","m","Und ich lerne Französisch, für die Arbeit, mit Kunden aus Paris, jeden Tag."),
("Sara","f","Ich lerne Chinesisch, an der Uni, sehr schwer, aber spannend und nützlich."),
("Lukas","m","Und ich lerne Russisch, für die Familie, meine Oma kommt von dort, aus Moskau."),
("Anna","f","Toll! Lisa, sprichst du schon Italienisch, ein bisschen, nach Rom?"),
("Lisa","f","Ein bisschen, Essen bestellen geht schon, mehr noch nicht, leider."),
("Markus","m","Und Chinesisch, Sara, die Zeichen, sind sie sehr schwer, wirklich?"),
("Sara","f","Sehr schwer! Tausend Zeichen schon, und es werden mehr, jeden Tag."),
("Lukas","m","Und Russisch, hilft dir Oma, beim Lernen, zu Hause?"),
("Anna","f","Bestimmt! Also, ich lerne Spanisch, für den Urlaub!"),
("Lisa","f","Ich lerne Italienisch, für Rom, im Herbst!"),
("Markus","m","Ich lerne Französisch, für die Arbeit, mit Kunden!"),
("Sara","f","Ich lerne Chinesisch, an der Uni!"),
("Lukas","m","Und ich lerne Russisch, für die Familie!"),
("Anna","f","Super, viel Erfolg allen, beim Lernen, viel Spaß!"),
]

D[21] = [
("Vater","m","Also, die Autos in der Familie! Meine Bremsen sind kaputt, seit gestern, ganz schlimm."),
("Mutter","f","Oh nein! Ich habe einen platten Reifen, heute Morgen, vor der Arbeit."),
("Markus","m","Und meine Batterie ist kaputt, das Auto startet nicht, gar nichts geht."),
("Sara","f","Bei mir läuft Öl aus, unter dem Motor, jeden Tag, ein Fleck."),
("Tom","m","Und mein Auto wurde gestohlen, letzte Nacht, vor dem Haus, weg!"),
("Vater","m","Was, gestohlen? Tom, hast du die Polizei gerufen, schon heute?"),
("Tom","m","Ja, sofort, heute Morgen, sie suchen schon, hoffentlich finden sie es."),
("Mutter","f","Und dein Reifen, Mutter, also meiner, ist er ganz platt, oder nur wenig?"),
("Markus","m","Mutter, du sprichst von dir selbst! Also, dein Reifen, wie schlimm ist es?"),
("Mutter","f","Ganz platt, leider! Der Nachbar hilft mir, am Abend, mit dem Wechsel."),
("Vater","m","Also, meine Bremsen sind kaputt, seit gestern!"),
("Mutter","f","Ich habe einen platten Reifen, seit heute Morgen!"),
("Markus","m","Meine Batterie ist kaputt, nichts geht!"),
("Sara","f","Bei mir läuft Öl aus, jeden Tag!"),
("Tom","m","Und mein Auto wurde gestohlen, letzte Nacht!"),
("Vater","m","Viel Ärger! In die Werkstatt, alle, morgen früh!"),
]
# fix self-address turns 8/9
D[21][7] = ("Mutter","f","Mein Reifen ist ganz platt, leider! Der Nachbar hilft mir am Abend.")
D[21][8] = ("Markus","m","Gut, der Nachbar hilft! Und meine Batterie, was mache ich nur?")

D[22] = [
("Lisa","f","Also, die Geschenke für Oma! Ich schenke ein elegantes Tagebuch, mit Leder, sehr schön."),
("Sara","f","Toll! Ich schenke ein Foto-Album, mit alten Bildern, von der Familie."),
("Tom","m","Und ich schenke eine Flasche Wein, roten, aus Frankreich, sehr gut."),
("Lukas","m","Ich schenke eine Reisetasche, für den Urlaub, groß und praktisch."),
("Anna","f","Und wir schenken Geld in einem Umschlag, Markus und ich, für Oma."),
("Markus","m","Genau, wir schenken Geld in einem Umschlag, hundert Euro, von uns beiden."),
("Lisa","f","Sehr gut! Sara, sind die Bilder schon eingeklebt, im Album, alle?"),
("Sara","f","Fast alle, nur zwei fehlen noch, vom Sommer, dann ist es fertig."),
("Tom","m","Und der Wein, ist er nicht zu teuer, aus Frankreich, wirklich?"),
("Lukas","m","Nein, zwanzig Euro, das geht gut, Oma liebt roten Wein."),
("Anna","f","Und die Tasche, Lukas, welche Farbe, für Oma, blau oder rot?"),
("Markus","m","Blau, bitte! Also, wir schenken Geld in einem Umschlag, hundert Euro!"),
("Lisa","f","Ich schenke ein elegantes Tagebuch, mit Leder!"),
("Sara","f","Ich schenke ein Foto-Album, mit alten Bildern!"),
("Tom","m","Ich schenke eine Flasche Wein, aus Frankreich!"),
("Lukas","m","Und ich schenke eine Reisetasche, groß und praktisch!"),
]

D[24] = [
("Lukas","m","Also, unsere Hobbys! Ich spiele Fußball im Verein, zweimal pro Woche, mit Freunden, im Park."),
("Lisa","f","Stark! Ich lerne Klavier, seit zwei Jahren, mit einer Lehrerin, es macht großen Spaß."),
("Marie","f","Und ich tanze Ballett, jeden Mittwoch, in der Tanzschule, mit schönen rosa Schuhen."),
("Tim","m","Ich male und zeichne, am liebsten Tiere, mit Farben und Stiften, überall, zu Hause und in der Schule."),
("Anna","f","Und ich lerne Sprachen, Englisch und Spanisch, in Kursen, nach der Schule, zweimal pro Woche."),
("Lukas","m","Toll! Lisa, spielst du schon gut Klavier, nach zwei Jahren, wirklich?"),
("Lisa","f","Ganz gut, kleine Stücke gehen schon, große noch nicht, leider."),
("Marie","f","Und Ballett, ist es anstrengend, jeden Mittwoch, mit den Schuhen?"),
("Tim","m","Bestimmt! Und meine Bilder, hängen sie schon, in der Schule, im Flur?"),
("Anna","f","Ja, zwei hängen schon! Und Sprachen, Anna, also meine, sind sie schwer?"),
("Marie","f","Die Schuhe drücken manchmal, aber Tanzen macht glücklich, jeden Tag."),
("Lukas","m","Also, ich spiele Fußball im Verein, zweimal pro Woche!"),
("Lisa","f","Ich lerne Klavier, seit zwei Jahren!"),
("Marie","f","Ich tanze Ballett, jeden Mittwoch!"),
("Tim","m","Ich male und zeichne, am liebsten Tiere!"),
]
# fix self-address turn 10
D[24][9] = ("Anna","f","Ja, zwei hängen schon! Sprachen sind nicht schwer, nur viel Übung.")

D[25] = [
("Mutter","f","Also, unsere Bücher! Ich lese Krimis, am Abend, im Bett, sehr spannend."),
("Vater","m","Schön! Ich lese Geschichtsbücher und Biografien, über alte Zeiten, gern."),
("Lisa","f","Und ich lese Liebesromane, auf dem Sofa, am Wochenende, wunderschön."),
("Tom","m","Ich lese Science-Fiction, über das Weltall, mit Raumschiffen, cool."),
("Marie","f","Und ich lese Kinderbücher und Märchen, vor dem Schlafen, jeden Tag."),
("Mutter","f","Toll! Vater, welches Buch liest du gerade, über wen, aus der Geschichte?"),
("Vater","m","Über einen alten König, sehr dick, fünfhundert Seiten, aber gut."),
("Lisa","f","Und Science-Fiction, Tom, fliegen sie zum Mars, in deinem Buch?"),
("Tom","m","Ja, zum Mars und weiter, mit einem großen Schiff, sehr spannend."),
("Mutter","f","Und du, Tom, fliegst du auch mal, zum Mars, im Traum?"),
("Tom","m","Jede Nacht! Also, ich lese Science-Fiction, über das Weltall!"),
("Tom","m","Und Krimis, wer ist der Mörder, in deinem Buch, weißt du schon?"),
("Marie","f","Mein Lieblingsmärchen ist Rotkäppchen! Also, ich lese Kinderbücher und Märchen, jeden Tag!"),
("Mutter","f","Noch nicht! Also, ich lese Krimis, am Abend, sehr spannend!"),
("Vater","m","Ich lese Geschichtsbücher und Biografien!"),
("Lisa","f","Ich lese Liebesromane, am Wochenende!"),
]
for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
