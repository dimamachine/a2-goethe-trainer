"""Genre batch C: tests 26,27,29,30,31,32,33,34,36."""
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

D[26] = [
("Sara","f","Also, unser freier Tag! Bist du fertig, Anna, für Freitag, mit mir, zusammen, auch?"),
("Anna","f","Total! Ich freue mich schon, seit Tagen, darauf, sehr, und du?"),
("Sara","f","Ich auch! Sag mal, mache ich eine neue Frisur, kurz und modern, sehr?"),
("Anna","f","Ja, bitte! Kurz steht dir gut, mit deinen Augen, wirklich, glaub mir."),
("Sara","f","Danke, ich mache eine neue Frisur! Machst du eine Maniküre, in Rot, dunkel, schön?"),
("Anna","f","Genau, ich mache eine Maniküre, rot wie immer, zum Kleid, zum Kleid, dunkel, toll."),
("Sara","f","Schön! Bekommt Lisa eine Gesichtsbehandlung, zur Ruhe, wie schön, toll, wirklich?"),
("Anna","f","Ja, Lisa bekommt eine Gesichtsbehandlung, sie arbeitet viel, zur Zeit, leider, die Arme."),
("Sara","f","Verstehe! Lässt Sophie Wimpern verlängern, für die Hochzeit, lang und schwarz?"),
("Anna","f","Genau, Sophie lässt Wimpern verlängern, in zwei Wochen ist es so weit, bald, im Juni, toll, schön?"),
("Sara","f","Spannend! Geht Mara zur Massage, für den Rücken, eine Stunde?"),
("Anna","f","Ja, Mara geht zur Massage, sie hat Schmerzen, seit langem, leider, die Arme, wirklich, wird schon."),
("Sara","f","Arme! Färbt jemand die Haare, blond oder braun, vorher?"),
("Anna","f","Nein, keine Zeit, alle Termine voll, diese Woche, wirklich, alle voll, überall."),
("Sara","f","Schade! Dann bis Freitag, beim Friseur, um elf, tschüss, bis dann, viel Spaß, bis Freitag!"),
("Anna","f","Bis Freitag! Ich freue mich, auf dich!"),
]

D[27] = [
("Eltern","m","Also, unser Urlaub! Planst du mit, Lukas, mit uns?"),
("Lukas","m","Klar! Sommer, Sonne, weg von hier, endlich, nach dem Winter, endlich Sommer."),
("Eltern","m","Genau! Sag mal, übernachten wir in einem 5-Sterne-Hotel, mit Schwimmbad, eine Woche, lang?"),
("Lukas","m","Wow, toll! Ja, ihr übernachtet in einem 5-Sterne-Hotel, nach dem Jahr, klar, gute Reise, viel Spaß."),
("Eltern","m","Danke! Und du, übernachtest du in einer Jugendherberge, mit Freunden, billig, allein?"),
("Lukas","m","Genau, ich übernachte in einer Jugendherberge, mit Frühstück, in der Stadt, billig und gut, für mich."),
("Eltern","m","Praktisch! Übernachtet Lisa in einer Ferienwohnung, mit Küche, am See, schön?"),
("Lukas","m","Ja, Lisa übernachtet in einer Ferienwohnung, schön, mit Blick aufs Wasser, toll, mit Sonne."),
("Eltern","m","Schön! Übernachtet Tom auf einem Campingplatz, mit Zelt, in den Bergen, hoch?"),
("Lukas","m","Genau, Tom übernachtet auf einem Campingplatz, Abenteuer pur, mit Sternen, allein, mit Hund."),
("Eltern","m","Toll! Übernachten Anna und Markus in einem Mittel-Klasse-Hotel, mit Frühstück, gut?"),
("Lukas","m","Ja, sie übernachten in einem Mittel-Klasse-Hotel, drei Nächte, in der Stadt, ruhig, mit Bad."),
("Eltern","m","Toll! Schläft jemand bei Verwandten, auf dem Sofa, wirklich, bei Oma?"),
("Lukas","m","Nein, alle haben gebucht, schon im März, alles voll, im Sommer, toll."),
("Eltern","m","Verstehe! Dann schönen Urlaub, allen, bis bald, tschüss!"),
("Lukas","m","Euch auch! Schickt Fotos, vom Hotel, bitte, viele, schöne!"),
]

D[29] = [
("Vater","m","Also, unsere Vereine! Bist du aktiv, Mutter, du auch, oder?"),
("Mutter","f","Na klar! Ohne Verein geht nichts, bei uns, immer, seit Jahren."),
("Vater","m","Stimmt! Sag mal, bin ich im Schachverein, jeden Dienstag, mit Freunden, alt und jung, zusammen?"),
("Mutter","f","Ja, sicher! Du spielst gut, seit Jahren, wirklich, glaub mir."),
("Vater","m","Danke, ich bin im Schachverein! Bist du im Chor, singst donnerstags, in der Kirche, sonntags, morgens?"),
("Mutter","f","Genau, ich bin im Chor, mit dreißig Leuten, es klingt toll, im Chor, laut."),
("Vater","m","Schön! Ist Lukas im Fußballverein, immer, zweimal pro Woche, fleißig?"),
("Mutter","f","Ja, Lukas ist im Fußballverein, er trainiert hart, mit Freude, gern, sehr."),
("Vater","m","Stark! Ist Lisa im Theaterverein, spielt im Frühling, ein lustiges Stück, mit Musik?"),
("Mutter","f","Genau, Lisa ist im Theaterverein, als Nachbarin, mit viel Text, schwer, aber toll."),
("Vater","m","Lustig! Ist Sara im Foto-Club, mit Kamera, mit Ausstellungen, groß?"),
("Mutter","f","Ja, Sara ist im Foto-Club, sie zeigt Bilder, in der Stadt, bald, gern, im Mai, mit Blumen."),
("Vater","m","Toll! Ist jemand im Tanzverein, am Wochenende, oft, samstags?"),
("Mutter","f","Nein, keiner tanzt, alle spielen oder singen, bei uns, zu Hause, abends."),
("Vater","m","Verstehe! Dann viel Spaß, allen, in den Vereinen, tschüss!"),
("Mutter","f","Dir auch! Bis Dienstag, beim Schach, viel Glück, tschüss, bis bald, viel Spaß!"),
]

D[30] = [
("Vater","m","Also, unsere Ämter! Hast du den Plan, Mutter, alles klar, ja, gut?"),
("Mutter","f","Leider ja! Volle Woche, mit Nummern, überall."),
("Vater","m","Puh! Sag mal, gehe ich zum Bürgeramt für den Personalausweis, am Montag, früh?"),
("Mutter","f","Ja, genau! Mit Foto, neu, nicht vergessen, wichtig, sehr."),
("Vater","m","Gut, ich gehe zum Bürgeramt für den Personalausweis! Gehst du zum Standesamt für die Geburtsurkunde, schnell, bitte?"),
("Mutter","f","Genau, ich gehe zum Standesamt für die Geburtsurkunde, am Dienstag, für den Pass, neu, aus Papier."),
("Vater","m","Wichtig! Geht Lukas zum Finanzamt für die Steuern, am Mittwoch, mit Papieren, allen?"),
("Mutter","f","Ja, Lukas geht zum Finanzamt für die Steuern, er zahlt nach, dieses Jahr."),
("Vater","m","Teuer! Geht Lisa zur Ausländerbehörde, für das Visum, am Donnerstag, lange?"),
("Mutter","f","Genau, Lisa geht zur Ausländerbehörde, mit Pass, drei Stunden Wartezeit, lang, sehr, puh."),
("Vater","m","Lang! Hat Markus TÜV, die Hauptuntersuchung, am Freitag, mit dem Auto, alt?"),
("Mutter","f","Ja, Markus hat TÜV, die Hauptuntersuchung, hoffentlich alles gut, hoffentlich, viel Glück."),
("Vater","m","Viel Glück! Geht jemand zur Polizei, mit Anzeige, wegen Problemen? Oder vor Gericht, wirklich, genau, ja?"),
("Mutter","f","Nein, zum Glück nichts los, alles ruhig, diese Woche, puh, gut, alles ruhig."),
("Vater","m","Puh! Dann viel Geduld, bei den Ämtern, allen, tschüss!"),
("Mutter","f","Danke! Und bring Zeit mit, viel Zeit, und Kaffee, stark."),
]

D[31] = [
("Vater","m","Also, unsere Zähne! Alles gut, Mutter, alles klar?"),
("Mutter","f","Na ja! Ein Zahn tut weh, seit gestern, leider, seit Tagen, schlimm."),
("Vater","m","Oh! Sag mal, bekomme ich eine Zahnreinigung, am Montag, früh, um acht?"),
("Mutter","f","Ja, richtig! Beim Zahnarzt, eine Stunde, ganz ruhig, keine Angst, wirklich."),
("Vater","m","Gut, ich bekomme eine Zahnreinigung! Bekommst du eine Krone, am Dienstag, neu, weiß?"),
("Mutter","f","Genau, ich bekomme eine Krone, für den Backenzahn, neu, aber gut, für Jahre, super, toll."),
("Vater","m","Teuer! Braucht Lukas eine Karies-Behandlung mit Plombe, am Mittwoch, leider ein Loch, tief?"),
("Mutter","f","Ja, Lukas braucht eine Karies-Behandlung mit Plombe, er isst zu viel Süßes, viel zu viel, leider, schlimm."),
("Vater","m","Stimmt! Bekommt Lisa eine Zahnspange, am Donnerstag, für zwei Jahre, lang?"),
("Mutter","f","Genau, Lisa bekommt eine Zahnspange, kaum zu sehen, gut, man sieht fast nichts, gut."),
("Vater","m","Modern! Lässt Anna den Weisheitszahn ziehen, am Freitag, er tut sehr weh, Tag und Nacht?"),
("Mutter","f","Ja, Anna lässt den Weisheitszahn ziehen, dann geht es, keine Angst, alles gut."),
("Vater","m","Arme! Bleibt jemand ohne Behandlung, nur Kontrolle, gesund, ohne Sorgen?"),
("Mutter","f","Nein, alle haben was, dieses Jahr, leider, wirklich, alle, viel Glück."),
("Vater","m","Na dann! Gute Besserung, allen Zähnen, schnell, gute Zähne!"),
("Mutter","f","Danke! Und putzt alle, morgens und abends, immer, gern."),
]

D[32] = [
("Vater","m","Also, unser Badetag! Bist du fit, Mutter, alles klar, ja?"),
("Mutter","f","Total! Sonne, Wasser, den ganzen Tag, herrlich, heiß, super, toll."),
("Vater","m","Schön! Sag mal, schwimme ich Bahnen, morgens, zwanzig Stück, für die Fitness, täglich, früh?"),
("Mutter","f","Ja, klar! Du bist schnell, seit Jahren, wirklich, schnell, wie ein Fisch, groß."),
("Vater","m","Danke, ich schwimme Bahnen! Machst du Aqua-Fitness, um zehn, mit Musik, laut, toll."),
("Mutter","f","Genau, ich mache Aqua-Fitness, im flachen Wasser, mit Gruppe, lustig, sehr, mit Freude."),
("Vater","m","Lustig! Rutscht Lisa auf der Wasserrutsche, den ganzen Tag, immer wieder, toll, schnell?"),
("Mutter","f","Ja, Lisa rutscht auf der Wasserrutsche, schnell und sicher, juhu, weiter, toll!"),
("Vater","m","Juhu! Geht Tim in den Schwimmkurs, um elf, mit Trainer, gern, sehr?"),
("Mutter","f","Genau, Tim geht in den Schwimmkurs, er übt täglich, nach der Schule, müde, kaputt, fertig."),
("Vater","m","Fleißig! Gehen Anna und Markus in die Sauna, nach dem Schwimmen, zur Ruhe, allein, oder zusammen?"),
("Mutter","f","Ja, sie gehen in die Sauna, um zwölf, herrlich, warm, rot."),
("Vater","m","Herrlich! Springt jemand vom Turm, von oben, allein, oben, hoch?"),
("Mutter","f","Nein, keiner, zu hoch, für uns, heute, zu hoch, Hilfe, bitte."),
("Vater","m","Verstehe! Dann viel Spaß, im Bad, allen, tschüss, bis morgen!"),
("Mutter","f","Dir auch! Vergiss die Creme nicht, für die Nase, wichtig, sehr, wirklich."),
]

D[33] = [
("Vater","m","Also, unser Camping! Bist du fertig, Mutter, alles klar, ja?"),
("Mutter","f","Fast! Die Taschen stehen schon, im Flur, fertig, los geht’s."),
("Vater","m","Super! Sag mal, bringe ich die Zelte, zwei große, für alle, groß, neu?"),
("Mutter","f","Ja, bitte! Du kennst den Platz, am See, seit Jahren, gut, wie immer."),
("Vater","m","Gut, ich bringe die Zelte! Kümmerst du dich um das Essen, für drei Tage, lang, weit weg?"),
("Mutter","f","Genau, ich kümmere mich um das Essen, mit viel Gemüse, gesund, frisch, vom Markt."),
("Vater","m","Gesund! Bringt Lukas Grill und Holz, für abends, fürs Camping, für alle, viel, zum Sitzen?"),
("Mutter","f","Ja, Lukas bringt Grill und Holz, viel Holz, vom Wald, viel, genug, gut."),
("Vater","m","Toll! Bringt Lisa Spiele und Bücher, für den Regen, falls es regnet, stark?"),
("Mutter","f","Genau, Lisa bringt Spiele und Bücher, Karten und ein dickes Buch, spannend, dick."),
("Vater","m","Klug! Bringt Anna Schlafsäcke und Isomatten, für alle, warm und weich, warm, gut?"),
("Mutter","f","Ja, Anna bringt Schlafsäcke und Isomatten, neu, aus dem Laden, neu, warm."),
("Vater","m","Neu! Fährt jemand das Auto, mit allem, zum See, weit, mit Auto?"),
("Mutter","f","Nein, wir fahren zusammen, mit einem Wagen, alles passt, super, toll."),
("Vater","m","Perfekt! Dann bis Freitag, am See, mit allem, tschüss, bis dann!"),
("Mutter","f","Bis Freitag! Ich freue mich, riesig, toll, bis Freitag!"),
]

D[34] = [
("Annas Vater","m","Also, unsere Gesundheit! Geht es dir gut, heute, gut?"),
("Annas Mutter","f","Ja, viel besser, danke! Das Bein ist gut, seit Wochen, besser, jeden Tag."),
("Annas Vater","m","Schön! Sag mal, hatte ich einen Herzinfarkt, im Frühling, wirklich, im Mai?"),
("Annas Mutter","f","Ja, leider! Aber jetzt geht es dir gut, zum Glück, gesund, alles gut, keine Angst."),
("Annas Vater","m","Gut, ich hatte einen Herzinfarkt, jetzt gesund! Hast du dir das Bein gebrochen, im Sommer, beim Wandern, hoch?"),
("Annas Mutter","f","Genau, ich habe mir das Bein gebrochen, es wird gut, nur Treppen sind schwer."),
("Annas Vater","m","Schon gut! Hatte Lukas eine Lungenentzündung, im Herbst, mit Fieber, hoch?"),
("Annas Mutter","f","Ja, Lukas hatte eine Lungenentzündung, jetzt gesund, zum Glück, puh, gut."),
("Annas Vater","m","Super! Hat Lisa ein Baby bekommen, im Winter, klein und gesund, ein Junge?"),
("Annas Mutter","f","Genau, Lisa hat ein Baby bekommen, süß und gesund, wunderbar, toll."),
("Annas Vater","m","Wunderbar! Hat man bei Markus Vater Gallensteine entfernt, im Januar, alles gut, wirklich?"),
("Annas Mutter","f","Ja, bei Markus Vater hat man Gallensteine entfernt, gut gegangen, keine Sorge, gut, alles ruhig."),
("Annas Vater","m","Toll! War jemand nur zur Kontrolle, gesund, ohne Sorgen? Hatte jemand Grippe, im Winter, kalt?"),
("Annas Mutter","f","Nein, aber alle gesund, jetzt, das zählt, sehr, wichtig."),
("Annas Vater","m","Stimmt! Auf uns, auf die Gesundheit, prost, noch einmal!"),
("Annas Mutter","f","Prost, Schatz! Und bleib gesund, ja, bitte?"),
]

D[36] = [
("Lukas","m","Also, unser Studium! Was läuft, Lisa, bei dir, alles klar, ja, gut?"),
("Lisa","f","Viel! Lesen, Lernen, wenig Schlaf, leider, zu wenig, immer."),
("Lukas","m","Kenn ich! Sag mal, studiere ich Medizin, seit einem Jahr, sehr spannend, wirklich, schwer, toll, super, schön."),
("Lisa","f","Ja, klar! Du lernst Tag und Nacht, mit Büchern, überall."),
("Lukas","m","Stimmt, ich studiere Medizin! Studierst du Jura, im ersten Jahr, mit viel Lesen, dick, schwer, toll."),
("Lisa","f","Genau, ich studiere Jura, tausend Seiten, pro Woche, schwer, sehr, wirklich, fleißig."),
("Lukas","m","Stark! Studiert Tom Informatik, mit Computer, den ganzen Tag, immer, ohne Pause, nie, wirklich, gern."),
("Lisa","f","Ja, Tom studiert Informatik, mit Kaffee, Tag und Nacht, wirklich, fleißig, jeden Tag."),
("Lukas","m","Typisch! Studiert Sara Architektur, mit Zeichnen, jeden Tag, früh, um sieben, pünktlich, ja."),
("Lisa","f","Genau, Sara studiert Architektur, ihr Zimmer war voller Bilder, früher, als Kind, klein."),
("Lukas","m","Schön! Studiert Tim Wirtschaft, mit Zahlen und Englisch, für die Karriere, mit Geld, viel, gut."),
("Lisa","f","Ja, Tim studiert Wirtschaft, international, mit Job, bald, nach Berlin, weit?"),
("Lukas","m","Toll! Studiert jemand Sprachen, mit Auslandsjahr, in Paris? Mag jemand Biologie, mit Tieren, groß, neu?"),
("Lisa","f","Nein, keiner, alle bleiben hier, dieses Jahr, leider."),
("Lukas","m","Verstehe! Dann viel Erfolg, im Studium, allen, tschüss, viel Glück!"),
("Lisa","f","Dir auch! Bis morgen! Tschüss, bis bald!"),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
