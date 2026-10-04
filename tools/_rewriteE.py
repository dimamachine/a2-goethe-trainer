"""Batch E rewrite: tests 48-64 — natural direct speech."""
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
("Lukas","m","Also, unser Einkauf für die Party! Ich kaufe Fleisch, für den Grill, Würstchen und Steaks."),
("Lisa","f","Super! Ich kaufe Getränke, mit Saft und Wasser, kalt, für alle."),
("Tom","m","Und ich kaufe Brot und Brötchen, frisch vom Bäcker, am Samstagmorgen."),
("Sara","f","Ich kaufe Gemüse für Salat, mit Tomaten und Gurken, ganz frisch, vom Markt."),
("Tim","m","Und ich kaufe den Nachtisch, mit Kuchen und Eis, für alle, lecker."),
("Lukas","m","Perfekt! Lisa, reichen die Getränke, für zwanzig Leute, wirklich?"),
("Lisa","f","Ja, drei Kästen plus Saft, das reicht gut, keine Sorge."),
("Tom","m","Und das Brot, bleibt es frisch, bis abends, vom Morgen?"),
("Sara","f","Ja, im Korb mit Tuch, ganz frisch, bis abends, versprochen."),
("Tim","m","Und das Eis, schmilzt es nicht, bis zum Nachtisch, im Sommer?"),
("Lukas","m","Nein! Also, ich kaufe Fleisch, für den Grill!"),
("Lisa","f","Ich kaufe Getränke, kalt, für alle!"),
("Tom","m","Ich kaufe Brot und Brötchen, frisch vom Bäcker!"),
("Sara","f","Ich kaufe Gemüse für Salat, vom Markt!"),
("Tim","m","Und ich kaufe den Nachtisch, mit Kuchen und Eis!"),
("Lukas","m","Super, bis Samstag, beim Grill!"),
]

D[49] = [
("Lukas","m","Also, unser Theaterabend! Ich sehe Romeo und Julia, die Liebesgeschichte, am Freitag."),
("Lisa","f","Schön! Ich sehe das Musical Cats, mit tollen Kostümen, am Samstag, mit Freundin."),
("Tom","m","Und ich sehe ein Comedy-Stück, zum Lachen, am Sonntag, mit Bruder, lustig."),
("Sara","f","Ich sehe die Oper Don Giovanni, mit Mozart, im großen Haus, am Montag."),
("Tim","m","Und ich sehe Ballett Schwanensee, mit schöner Musik, am Dienstag, mit Oma."),
("Lukas","m","Toll! Lisa, ist Cats ausverkauft, am Samstag, schon lange?"),
("Lisa","f","Fast, nur wenige Plätze, oben, aber wir haben zwei, zum Glück."),
("Tom","m","Und Comedy, lacht man viel, wirklich, den ganzen Abend?"),
("Sara","f","Bestimmt! Und Oper, Sara, also meine, dauert sie lange, drei Stunden?"),
("Tim","m","Sara, du fragst dich selbst! Also, deine Oper, wie lange dauert sie?"),
("Sara","f","Drei Stunden, mit Pause! Also, ich sehe die Oper Don Giovanni, am Montag!"),
("Lukas","m","Ich sehe Romeo und Julia, am Freitag!"),
("Lisa","f","Ich sehe das Musical Cats, am Samstag!"),
("Tom","m","Ich sehe ein Comedy-Stück, am Sonntag!"),
("Tim","m","Und ich sehe Ballett Schwanensee, am Dienstag!"),
("Lukas","m","Viel Spaß allen, im Theater!"),
]
# fix self-address 9/10
D[49][8] = ("Sara","f","Und die Oper dauert drei Stunden, mit Pause, großartig!")
D[49][9] = ("Tim","m","Drei Stunden! Und Ballett, ist Oma fit, am Dienstag?")

D[50] = [
("Lukas","m","Also, unsere Tiere beim Arzt! Ich bringe den Hund, zur Impfung, am Montag, er ist brav."),
("Lisa","f","Gut! Ich bringe die Katze, zur Kontrolle, am Dienstag, sie hat Angst, leider."),
("Tom","m","Und ich bringe den Hamster, mit Husten, am Mittwoch, der Arme, ganz klein."),
("Sara","f","Ich bringe die Fische, mit komischen Flecken, am Donnerstag, im Glas, zum Arzt."),
("Tim","m","Und ich bringe den Papagei, er spricht nicht mehr, am Freitag, seit Wochen."),
("Lukas","m","Arme Tiere! Lisa, kratzt die Katze, beim Arzt, sehr?"),
("Lisa","f","Leider ja, der Arzt trägt Handschuhe, dicke, zum Schutz."),
("Tom","m","Und der Hamster, frisst er noch, mit Husten, gut?"),
("Sara","f","Wenig! Und Fische, kann der Arzt helfen, mit Flecken, wirklich?"),
("Tim","m","Bestimmt, mit Medizin, ins Wasser, dann geht es, schnell."),
("Lukas","m","Also, ich bringe den Hund, zur Impfung!"),
("Lisa","f","Ich bringe die Katze, zur Kontrolle!"),
("Tom","m","Ich bringe den Hamster, mit Husten!"),
("Sara","f","Ich bringe die Fische, im Glas!"),
("Tim","m","Und ich bringe den Papagei, er spricht nicht!"),
("Lukas","m","Gute Besserung allen Tieren!"),
]

D[51] = [
("Lukas","m","Also, unsere Augen! Ich brauche eine normale Brille, zum Lesen und Fahren, mit Gestell."),
("Lisa","f","Ich brauche Kontaktlinsen, für den Sport, weiche, jeden Tag, neue."),
("Tom","m","Und ich brauche eine Lesebrille, nur für Bücher, am Abend, schwach, plus eins."),
("Sara","f","Ich brauche eine Sonnenbrille mit Sehstärke, für den Sommer, dunkel und cool."),
("Tim","m","Und ich brauche eine Augen-Operation, im Herbst, mit Laser, dann keine Brille."),
("Lukas","m","Spannend! Lisa, sind Linsen teuer, jeden Tag neue, im Monat?"),
("Lisa","f","Dreißig Euro, das geht gut, für den Sport, super."),
("Tom","m","Und die Operation, Tim, tut sie weh, mit Laser, wirklich?"),
("Sara","f","Nein, nur kurz! Und Sonnenbrille, steht sie mir, dunkel und cool?"),
("Tim","m","Bestimmt! Also, ich brauche eine Augen-Operation, im Herbst!"),
("Lukas","m","Ich brauche eine normale Brille, mit Gestell!"),
("Lisa","f","Ich brauche Kontaktlinsen, für den Sport!"),
("Tom","m","Ich brauche eine Lesebrille, für Bücher!"),
("Sara","f","Ich brauche eine Sonnenbrille mit Sehstärke, für den Sommer!"),
("Tim","m","Und ich brauche eine Augen-Operation, mit Laser!"),
("Lukas","m","Gute Sicht allen, viel Glück!"),
]
# fix: turn 9 Sara asks about herself — rewrite 8/9 flow
D[51][8] = ("Sara","f","Nein, nur ganz kurz, mit Tropfen, keine Sorge!")
D[51][7] = ("Tom","m","Und die Operation, Tim, tut sie weh, mit Laser, wirklich?")

D[52] = [
("Lukas","m","Also, unser Badetag! Ich gehe in die Sauna, mit Aufguss, abends, herrlich."),
("Lisa","f","Schön! Ich schwimme Bahnen, morgens, zehn Stück, für die Fitness."),
("Tom","m","Und ich rutsche auf der Wasserrutsche, immer wieder, mit Freunden, juhu!"),
("Sara","f","Ich springe vom Turm, vom Dreier, mutig, mit Anlauf, platsch!"),
("Tim","m","Und ich sitze im Whirlpool, mit Blasen, ganz entspannt, warm."),
("Lukas","m","Toll! Lisa, schwimmst du schnell, die zehn Bahnen, wirklich?"),
("Lisa","f","Ganz gut, zwanzig Minuten, mit Pause, nach fünf, dann weiter."),
("Tom","m","Und der Turm, Sara, hast du keine Angst, ganz oben, ehrlich?"),
("Sara","f","Doch, ein bisschen, aber es macht Spaß, mit Anlauf, platsch!"),
("Tim","m","Und Whirlpool, ist er nicht zu heiß, mit Blasen, lange?"),
("Lukas","m","Nein! Also, ich gehe in die Sauna, abends!"),
("Lisa","f","Ich schwimme Bahnen, morgens!"),
("Tom","m","Ich rutsche auf der Wasserrutsche, juhu!"),
("Sara","f","Ich springe vom Turm, platsch!"),
("Tim","m","Und ich sitze im Whirlpool, entspannt!"),
("Lukas","m","Viel Spaß allen, im Bad!"),
]
# fix: turn 10 asks self — rewrite
D[52][9] = ("Tim","m","Warm, aber gut! Also, ich sitze im Whirlpool, entspannt!")

D[53] = [
("Lukas","m","Also, die Hochzeit im Mai! Ich mache die Musik als DJ, mit Tanz, bis Mitternacht."),
("Lisa","f","Super! Ich bringe Blumen, für die Tische, weiß und rosa, wunderschön."),
("Tom","m","Und ich mache die Fotos, mit Kamera, den ganzen Tag, überall."),
("Sara","f","Ich backe die Torte, drei Stockwerke, mit Erdbeeren, lecker."),
("Tim","m","Und ich halte die Rede, kurz und lustig, nach dem Essen, mit Witz."),
("Lukas","m","Perfekt! Lisa, sind die Blumen teuer, weiß und rosa, viele?"),
("Lisa","f","Fünfzig Euro, für zehn Tische, das geht, wirklich."),
("Tom","m","Und die Torte, Sara, schmeckt sie gut, mit Erdbeeren, sicher?"),
("Sara","f","Sehr gut! Und Rede, Tim, bist du nervös, vor allen Leuten?"),
("Tim","m","Ein bisschen, aber kurz, fünf Minuten, dann Applaus, hoffentlich."),
("Lukas","m","Also, ich mache die Musik als DJ, bis Mitternacht!"),
("Lisa","f","Ich bringe Blumen, weiß und rosa!"),
("Tom","m","Ich mache die Fotos, den ganzen Tag!"),
("Sara","f","Ich backe die Torte, mit Erdbeeren!"),
("Tim","m","Und ich halte die Rede, kurz und lustig!"),
("Lukas","m","Bis Mai, auf der Hochzeit!"),
]

D[54] = [
("Lukas","m","Also, unsere Brillen! Ich nehme die schwarze Hornbrille, klassisch und stark, sehr cool."),
("Lisa","f","Schön! Ich nehme die randlose Brille, leicht und hell, fast unsichtbar."),
("Tom","m","Und ich nehme die runde Brille, modern und jung, mit Metall, gefällt mir."),
("Sara","f","Ich nehme die rote farbige Brille, mutig und lustig, passend zum Schal."),
("Tim","m","Und ich nehme die Pilotenbrille, groß und cool, wie im Film, top."),
("Lukas","m","Toll! Lisa, ist randlos bequem, den ganzen Tag, wirklich?"),
("Lisa","f","Sehr bequem, man spürt nichts, auf der Nase, super."),
("Tom","m","Und rot, Sara, steht dir Rot, im Gesicht, ehrlich?"),
("Sara","f","Ja, sehr! Und Pilotenbrille, Tim, nicht zu groß, für dich?"),
("Tim","m","Genau richtig! Also, ich nehme die Pilotenbrille, wie im Film!"),
("Lukas","m","Ich nehme die schwarze Hornbrille, sehr cool!"),
("Lisa","f","Ich nehme die randlose Brille, fast unsichtbar!"),
("Tom","m","Ich nehme die runde Brille, modern und jung!"),
("Sara","f","Ich nehme die rote farbige Brille, passend zum Schal!"),
("Tim","m","Und ich nehme die Pilotenbrille, groß und cool!"),
("Lukas","m","Gute Sicht allen, mit Stil!"),
]

D[55] = [
("Lukas","m","Also, unsere Vereine! Ich bin Bayern-Fan, seit der Kindheit, mit Trikot, rot."),
("Lisa","f","Cool! Ich bin Dortmund-Fan, mit Schal und Fahne, jedes Spiel, im Stadion."),
("Tom","m","Und ich bin Schalke-Fan, seit Jahren, treu, auch in der Krise, immer."),
("Sara","f","Ich bin HSV-Fan, aus Hamburg, mit Freunden, im Norden, toll."),
("Tim","m","Und ich bin Bremen-Fan, Werder, grün-weiß, mit Papa, zusammen."),
("Lukas","m","Stark! Lisa, bist du oft im Stadion, in Dortmund, wirklich?"),
("Lisa","f","Jedes Heimspiel, mit Freundin, in der Kurve, laut und wild."),
("Tom","m","Und Schalke, Tom, also ich, bleibe ich treu, in der Krise, klar?"),
("Sara","f","Tom, du fragst dich selbst! Also, bleibst du treu, Schalke, immer?"),
("Tom","m","Immer! Und HSV, Sara, steigt ihr auf, dieses Jahr, endlich?"),
("Sara","f","Hoffentlich! Also, ich bin HSV-Fan, mit Freunden!"),
("Lukas","m","Ich bin Bayern-Fan, mit Trikot!"),
("Lisa","f","Ich bin Dortmund-Fan, im Stadion!"),
("Tom","m","Ich bin Schalke-Fan, treu, immer!"),
("Tim","m","Und ich bin Bremen-Fan, mit Papa!"),
("Lukas","m","Viel Glück allen Vereinen!"),
]
# fix self-address 8/9
D[55][7] = ("Tom","m","Und Schalke bleibt mein Verein, treu, in der Krise, immer.")
D[55][8] = ("Sara","f","Stark, Tom! Und HSV, steigt ihr auf, dieses Jahr, endlich?")

D[56] = [
("Lukas","m","Also, unser Frühstück! Ich hole Brezeln, frisch und warm, vom Bäcker, zehn Stück."),
("Lisa","f","Lecker! Ich hole Croissants, mit Butter, für alle, aus Frankreich, quasi."),
("Tom","m","Und ich hole Vollkornbrot, gesund und frisch, ein großes, für die Woche."),
("Sara","f","Ich hole Käsekuchen, süß und cremig, zum Kaffee, am Sonntag, mmm."),
("Tim","m","Und ich hole Berliner, mit Marmelade, für die Kinder, fünf Stück."),
("Lukas","m","Perfekt! Lisa, sind Croissants schwer, selbst zu machen, wirklich?"),
("Lisa","f","Sehr schwer! Darum vom Bäcker, frisch, jeden Sonntag, lecker."),
("Tom","m","Und Käsekuchen, Sara, mit viel Käse, cremig, wirklich?"),
("Sara","f","Sehr cremig! Und Berliner, Tim, mit welcher Marmelade, Erdbeer?"),
("Tim","m","Erdbeer! Also, ich hole Berliner, mit Marmelade!"),
("Lukas","m","Ich hole Brezeln, frisch und warm!"),
("Lisa","f","Ich hole Croissants, mit Butter!"),
("Tom","m","Ich hole Vollkornbrot, für die Woche!"),
("Sara","f","Ich hole Käsekuchen, zum Kaffee!"),
("Tim","m","Und ich hole Berliner, für die Kinder!"),
("Lukas","m","Guten Appetit allen, am Sonntag!"),
]

D[57] = [
("Lukas","m","Also, unsere Wohnungen! Ich suche ein WG-Zimmer, zentral und billig, mit netten Leuten."),
("Lisa","f","Toll! Ich suche eine Ein-Zimmer-Wohnung, klein, aber mein, mit Balkon."),
("Tom","m","Und ich suche eine Familie-Wohnung mit Garten, für vier, mit Kindern, grün."),
("Sara","f","Ich suche eine Maisonette mit Dachterrasse, hell und modern, mit Blick, wow."),
("Tim","m","Und ich suche ein Haus zum Kaufen, mit Garten, für immer, ein Traum."),
("Lukas","m","Schön! Lisa, ist die Wohnung teuer, mit Balkon, in der Stadt?"),
("Lisa","f","Sechshundert Euro, warm, das geht gut, für mich, allein."),
("Tom","m","Und Garten, Tom, also meiner, wie groß, hundert Meter, genug?"),
("Sara","f","Tom, du fragst dich selbst! Also, dein Garten, wie groß wird er?"),
("Tom","m","Hundert Meter, genug! Also, ich suche eine Familie-Wohnung mit Garten!"),
("Lukas","m","Ich suche ein WG-Zimmer, mit netten Leuten!"),
("Lisa","f","Ich suche eine Ein-Zimmer-Wohnung, mit Balkon!"),
("Sara","f","Ich suche eine Maisonette mit Dachterrasse, mit Blick!"),
("Tim","m","Und ich suche ein Haus zum Kaufen, ein Traum!"),
("Lukas","m","Viel Glück allen, bei der Suche!"),
]
# fix self-address 8/9 + need 16 turns: answer + extra turn
D[57][7] = ("Tom","m","Der Garten wird hundert Meter, genug für alle, mit Schaukel.")
D[57][8] = ("Sara","f","Mit Schaukel, toll! Und mein Blick, von der Terrasse, aufs Meer?")
D[57].insert(9, ("Lukas","m","Aufs Meer, toll! Wer hilft beim Umzug, im Sommer, alle zusammen?"))
D[57][10] = ("Tom","m","Wir alle! Also, ich suche eine Familie-Wohnung mit Garten!")

D[58] = [
("Lukas","m","Also, unser Schönheitstag! Ich lasse mich rasieren, beim Barbier, glatt und cool, klassisch."),
("Lisa","f","Schön! Ich mache eine Maniküre, mit blauem Lack, passend zum Kleid, hübsch."),
("Tom","m","Und ich gehe zur Massage, für den Nacken, eine Stunde, dringend nötig."),
("Sara","f","Ich bekomme eine Gesichtsbehandlung, mit Maske und Dampf, reine Haut, toll."),
("Tim","m","Und ich mache eine Pediküre, für den Sommer, mit Sandalen, endlich."),
("Lukas","m","Toll! Lisa, hält der Lack lange, blau, zwei Wochen?"),
("Lisa","f","Zwei Wochen, ganz sicher, mit Schutz, kein Problem."),
("Tom","m","Und Massage, hilft sie wirklich, beim Nacken, nach einer Stunde?"),
("Sara","f","Bestimmt! Und Pediküre, Tim, kitzelt es sehr, an den Füßen?"),
("Tim","m","Ein bisschen! Also, ich mache eine Pediküre, für den Sommer!"),
("Lukas","m","Ich lasse mich rasieren, beim Barbier!"),
("Lisa","f","Ich mache eine Maniküre, mit blauem Lack!"),
("Tom","m","Ich gehe zur Massage, für den Nacken!"),
("Sara","f","Ich bekomme eine Gesichtsbehandlung, reine Haut!"),
("Tim","m","Und ich mache eine Pediküre, mit Sandalen!"),
("Lukas","m","Viel Spaß allen, beim Schönheitstag!"),
]

D[59] = [
("Lukas","m","Also, unsere Haare! Ich habe eine Glatze, ganz glatt, seit Jahren, praktisch."),
("Lars","m","Cool! Ich habe einen Iro, bunt und wild, als Mohawk, mit Farbe, krass."),
("Tom","m","Und ich habe einen Mittelscheitel mit langen Haaren, wie ein Star, aus dem Film."),
("Sven","m","Ich habe einen Dutt, oben und praktisch, beim Sport, super."),
("Tim","m","Und ich habe einen Undercut, kurz an den Seiten, oben lang, modern."),
("Lukas","m","Stark! Lars, wie lange dauert der Iro, morgens, mit Farbe?"),
("Lars","m","Eine Stunde, mit Gel und Farbe, jeden Morgen, krass, aber toll."),
("Tom","m","Und Dutt, Sven, ist er praktisch, beim Sport, wirklich?"),
("Sven","m","Sehr praktisch! Und Undercut, Tim, musst du oft schneiden, alle zwei Wochen?"),
("Tim","m","Alle zwei Wochen! Also, ich habe einen Undercut, modern!"),
("Lukas","m","Ich habe eine Glatze, praktisch!"),
("Lars","m","Ich habe einen Iro, bunt und wild!"),
("Tom","m","Ich habe einen Mittelscheitel mit langen Haaren, wie ein Star!"),
("Sven","m","Ich habe einen Dutt, praktisch, beim Sport!"),
("Tim","m","Und ich habe einen Undercut, modern!"),
("Lukas","m","Coole Haare allen, weiter so!"),
]

D[60] = [
("Lukas","m","Also, unser Parktag! Ich jogge, morgens, fünf Kilometer, mit Musik, fit."),
("Lisa","f","Toll! Ich fahre Fahrrad, um den See, mit Freundin, gemütlich, sonntags."),
("Tom","m","Und ich lese auf einer Bank, mit Buch und Decke, ruhig, stundenlang."),
("Sara","f","Ich mache Picknick mit Freundinnen, mit Decke und Kuchen, am Teich, schön."),
("Tim","m","Und ich spiele Fußball, mit Freunden, auf der Wiese, bis abends."),
("Lukas","m","Schön! Lisa, ist der See weit, mit dem Rad, zehn Kilometer?"),
("Lisa","f","Zehn Kilometer, genau, mit Pause, am Kiosk, mit Eis."),
("Tom","m","Und Picknick, was gibt es Leckeres, auf der Decke, Kuchen?"),
("Sara","f","Kuchen und Obst, selbst gemacht, für alle, genug."),
("Tim","m","Und Fußball, wie viele seid ihr, auf der Wiese, zehn?"),
("Lukas","m","Zehn! Also, ich jogge, fünf Kilometer!"),
("Lisa","f","Ich fahre Fahrrad, um den See!"),
("Tom","m","Ich lese auf einer Bank, stundenlang!"),
("Sara","f","Ich mache Picknick mit Freundinnen, am Teich!"),
("Tim","m","Und ich spiele Fußball, auf der Wiese!"),
("Lukas","m","Viel Spaß allen, im Park!"),
]

D[61] = [
("Lukas","m","Also, unser Training! Ich mache Krafttraining, mit Gewichten, dreimal pro Woche, stark."),
("Lisa","f","Stark! Ich mache Spinning, mit Musik, schweißtreibend, super, montags."),
("Tom","m","Und ich mache Yoga, abends, entspannt, mit Atmung, gegen Stress, ruhig."),
("Sara","f","Ich gehe schwimmen, morgens, zwanzig Bahnen, vor der Arbeit, fit."),
("Tim","m","Und ich mache Boxen, mit Trainer, dienstags, mit Handschuhen, pow!"),
("Lukas","m","Toll! Lisa, ist Spinning schwer, montags, nach dem Wochenende?"),
("Lisa","f","Sehr schwer, aber toll, mit Musik, man schwitzt viel, super."),
("Tom","m","Und Yoga, hilft es wirklich, gegen Stress, abends?"),
("Sara","f","Sehr! Und Boxen, Tim, tut es weh, mit Handschuhen, ehrlich?"),
("Tim","m","Nur ein bisschen! Also, ich mache Boxen, dienstags!"),
("Lukas","m","Ich mache Krafttraining, dreimal pro Woche!"),
("Lisa","f","Ich mache Spinning, montags!"),
("Tom","m","Ich mache Yoga, gegen Stress!"),
("Sara","f","Ich gehe schwimmen, vor der Arbeit!"),
("Tim","m","Und ich mache Boxen, mit Trainer!"),
("Lukas","m","Viel Erfolg allen, beim Training!"),
]

D[62] = [
("Lukas","m","Also, unser Marktbesuch! Ich kaufe Fisch, frisch vom Meer, Forelle, für Freitag."),
("Lisa","f","Lecker! Ich kaufe Blumen, bunte, für die Wohnung, jeden Samstag, schön."),
("Tom","m","Und ich kaufe Käse, Bergkäse und Brie, würzig, zum Wein, am Abend."),
("Sara","f","Ich kaufe Obst, Äpfel und Birnen, aus der Region, süß, für die Kinder."),
("Tim","m","Und ich kaufe Honig, vom Imker, direkt, cremig, zum Frühstück."),
("Lukas","m","Schön! Lisa, sind Blumen teuer, jeden Samstag, auf dem Markt?"),
("Lisa","f","Fünf Euro, der Strauß, frisch, vom Feld, das geht."),
("Tom","m","Und Obst, Sara, ist es süß, aus der Region, wirklich?"),
("Sara","f","Sehr süß! Und Honig, Tim, cremig oder flüssig, welcher?"),
("Tim","m","Cremig! Also, ich kaufe Honig, vom Imker!"),
("Lukas","m","Ich kaufe Fisch, Forelle, für Freitag!"),
("Lisa","f","Ich kaufe Blumen, jeden Samstag!"),
("Tom","m","Ich kaufe Käse, zum Wein!"),
("Sara","f","Ich kaufe Obst, für die Kinder!"),
("Tim","m","Und ich kaufe Honig, zum Frühstück!"),
("Lukas","m","Guten Appetit allen, vom Markt!"),
]

D[63] = [
("Lukas","m","Also, unsere Autos in der Werkstatt! Meine Batterie ist leer, seit gestern, nichts geht."),
("Lisa","f","Oh nein! Ich habe einen platten Reifen, heute Morgen, vor der Schule."),
("Tom","m","Und meine Bremse ist defekt, quietscht laut, seit Tagen, gefährlich."),
("Sara","f","Mein Auto verliert Öl, jeden Tag, ein Fleck, in der Garage, schlimm."),
("Tim","m","Und meine Klimaanlage ist kaputt, nur heiß, im Sommer, schrecklich."),
("Lukas","m","Viel Ärger! Lisa, ist der Reifen ganz platt, oder nur wenig, Luft?"),
("Lisa","f","Ganz platt, leider, der Nachbar hilft, am Abend, mit Wechsel."),
("Tom","m","Und Öl, Sara, wie viel verlierst du, einen Liter, pro Woche?"),
("Sara","f","Einen Liter! Und Klima, Tim, schwitzt du sehr, im Auto, zurzeit?"),
("Tim","m","Sehr! Also, meine Klimaanlage ist kaputt, nur heiß!"),
("Lukas","m","Meine Batterie ist leer, nichts geht!"),
("Lisa","f","Ich habe einen platten Reifen, seit heute Morgen!"),
("Tom","m","Meine Bremse ist defekt, gefährlich!"),
("Sara","f","Mein Auto verliert Öl, jeden Tag!"),
("Tim","m","Und meine Klimaanlage ist kaputt, schrecklich!"),
("Lukas","m","In die Werkstatt, alle, morgen!"),
]

D[64] = [
("Lukas","m","Also, unser Urlaub! Ich mache Strandurlaub, mit Sonne und Meer, zwei Wochen, herrlich."),
("Lisa","f","Toll! Ich mache eine Kreuzfahrt, mit Schiff, über das Meer, mit Shows, luxuriös."),
("Tom","m","Und ich mache eine Städtereise, nach Rom, mit Museen, für ein Wochenende, kurz."),
("Sara","f","Ich gehe wandern in den Bergen, mit Rucksack, eine Woche, frische Luft, toll."),
("Tim","m","Und ich mache Safari in Afrika, mit Löwen, wild und weit, ein Traum."),
("Lukas","m","Wow! Lisa, ist Kreuzfahrt teuer, mit Schiff, eine Woche?"),
("Lisa","f","Tausend Euro, mit allem, Essen und Shows, es lohnt sich."),
("Tom","m","Und wandern, Sara, schläfst du im Zelt, in den Bergen, nachts?"),
("Sara","f","Ja, im Zelt, unter Sternen, wunderschön, mit Schlafsack."),
("Tim","m","Und Safari, siehst du Löwen, wirklich, ganz nah, gefährlich?"),
("Lukas","m","Ganz nah! Also, ich mache Strandurlaub, zwei Wochen!"),
("Lisa","f","Ich mache eine Kreuzfahrt, luxuriös!"),
("Tom","m","Ich mache eine Städtereise, nach Rom!"),
("Sara","f","Ich gehe wandern in den Bergen, mit Rucksack!"),
("Tim","m","Und ich mache Safari in Afrika, ein Traum!"),
("Lukas","m","Schönen Urlaub allen, viel Spaß!"),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
