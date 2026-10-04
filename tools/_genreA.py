"""Genre batch A: tests 1,4,5,6,7,8,10,11,12 — two speakers discuss five."""
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

D[1] = [
("Markus","m","Also, unsere Berlin-Reise! Bist du schon fertig, Anna, mit Packen?"),
("Anna","f","Sehr! Ich freue mich schon, seit Wochen, auf die Stadt. Letztes Mal war es so voll, im Sommer, überall."),
("Markus","m","Ich auch! Sag mal, buche ich die Zugtickets, online, heute Abend?"),
("Anna","f","Ja, bitte! Du findest immer die billigen, wie immer."),
("Markus","m","Genau, ich buche die Zugtickets, mit Sitzplatz, für alle."),
("Anna","f","Super! Und ich buche das Hotel, ein kleines, in der Mitte, mit Frühstück. Frühstück ist wichtig, für den langen Tag."),
("Markus","m","Perfekt! Was ist mit Essen, reserviert Jan das Restaurant, für Freitag?"),
("Anna","f","Ja, Jan reserviert das Restaurant, italienisch, in der Nähe vom Hotel. Pizza essen wir alle gern, wirklich."),
("Markus","m","Toll! Und Lisa, kauft sie die Museum-Tickets, für Samstag?"),
("Anna","f","Genau, Lisa kauft die Museum-Tickets, im Voraus, das ist billiger, im Internet."),
("Markus","m","Klug! Fährt uns dein Vater zum Bahnhof, mit dem Auto, morgens?"),
("Anna","f","Mein Vater fährt zum Bahnhof, um halb acht, er steht sehr früh auf, nur für uns."),
("Markus","m","Nett! Hütet jemand den Hund, oder kommt er mit, nach Berlin, im Zug?"),
("Anna","f","Die Nachbarin hütet den Hund, mit Garten, er liebt es dort, mit dem Garten und den Kindern. Koffer packen wir erst Donnerstag, in Ruhe."),
("Markus","m","Alles klar! Dann bis Freitag, mit Koffern, pünktlich!"),
]

D[4] = [
("Anna","f","Also, unsere Lerngruppe! Alles klar, Markus, zum Rechnen?"),
("Markus","m","Na ja! Rechnen ist schwer, aber zusammen geht es gut. Allein verstehe ich nichts, zu schwer, leider."),
("Anna","f","Genau! Sag mal, mache ich Algebra, die Aufgaben, wie immer?"),
("Markus","m","Ja, bitte! Du kannst das am besten, seit der Schule. Bei der letzten Arbeit hattest du eine Eins, toll!"),
("Anna","f","Gut, ich mache Algebra! Und du, nimmst du Geometrie, wie immer?"),
("Markus","m","Klar, ich mache Geometrie, das liegt mir, seit Jahren, mit Freude."),
("Anna","f","Schön! Macht Sara die Wahrscheinlichkeit, mit Karten, zum Üben?"),
("Markus","m","Ja, Sara macht Wahrscheinlichkeit, mit Karten, zum Üben, lustig. Letztes Mal hatte sie Glück."),
("Anna","f","Toll! Und Lisa, nimmt sie Statistik, mit Tabellen, aus dem Buch?"),
("Markus","m","Genau, Lisa macht Statistik, mit vielen Zahlen, sie liebt das, mit Kaffee und Ruhe, gern."),
("Anna","f","Wow! Und Tobias, was macht er, Präsentationen, oder Diagramme?"),
("Markus","m","Tobias macht Funktionen und Diagramme, mit dem Computer, ganz modern, mit bunten Bildern."),
("Anna","f","Perfekt! Bringt jemand Snacks mit, für die Pause, Äpfel oder so?"),
("Markus","m","Ich bringe Äpfel und Wasser mit, gesund und billig, für alle, aus dem Garten."),
("Anna","f","Super! Dann bis Donnerstag, um vier, mit Büchern, ohne Handy!"),
("Markus","m","Bis Donnerstag! Und vergiss deine Hefte nicht, und viel Glück, bis Donnerstag, tschüss!"),
]

D[5] = [
("Anna","f","Also, unser Umzug! Bist du fit, Markus, für Samstag?"),
("Markus","m","Total fit! Ich habe gut geschlafen, wie ein Baby, und Kaffee hilft, immer, schwarz und stark."),
("Anna","f","Sehr gut! Sag mal, hole ich den Lkw, morgens um acht, bei der Firma?"),
("Markus","m","Ja, bitte! Du fährst gut, auch große Autos, kein Problem, ich fahre gern."),
("Anna","f","Gut, ich hole den Lkw! Und du packst die Küche, mit Tellern, vorsichtig?"),
("Markus","m","Genau, ich packe die Küche, mit Zeitung, ganz vorsichtig, versprochen."),
("Anna","f","Danke! Packt Lisa die Bücher, alle Kisten, aus dem Regal?"),
("Markus","m","Ja, Lisa packt die Bücher, das dauert lange, sie hat so viele, zum Lesen, in Ruhe."),
("Anna","f","Und Tim, putzt er die alte Wohnung, am Sonntag, Bad und Küche?"),
("Markus","m","Genau, Tim putzt die alte Wohnung, alles sauber, für die Neuen. Er putzt gut, wirklich, wie neu!"),
("Anna","f","Super! Richtet Toms Vater das Internet ein, mit dem Techniker, wirklich?"),
("Markus","m","Ja, Toms Vater richtet das Internet ein, er kennt sich aus, zum Glück. Ohne Internet geht nichts, heute."),
("Anna","f","Toll! Bestellen wir Pizza, am Abend, für alle Helfer?"),
("Markus","m","Gute Idee! Ich bestelle Pizza, um sieben, für alle! Neue Möbel kaufen wir später, im Herbst, in Ruhe."),
("Anna","f","Perfekt! Dann bis Samstag, um acht, mit Kisten, bis dann!"),
]

D[6] = [
("Mama","f","Also, unser freier Tag! Freust du dich, Papa, sehr?"),
("Papa","m","Sehr! Ich brauche Pause, die Arbeit war schwer, diese Woche, so viel zu tun, jeden Tag."),
("Mama","f","Oh! Oh! Lasse ich eine Rückenmassage machen, gegen Schmerzen, im Rücken?"),
("Papa","m","Ja, bitte! Dein Rücken tut weh, seit Monaten, das hilft sicher, sagt der Arzt."),
("Mama","f","Gut, ich lasse eine Rückenmassage machen, am Samstag, endlich, hurra, toll!"),
("Papa","m","Super! Und ich gehe in die Sauna, am Abend, das liebe ich, seit Jahren, am Abend, gern."),
("Mama","f","Schön! Geht Tante Eva zum Friseur, vorher, mit neuer Farbe, beim Friseur?"),
("Papa","m","Nein, sie bucht zur Ruhe eine Gesichtsbehandlung, wie schön, zum Glück."),
("Mama","f","Aha! Macht Onkel Robert Yoga, am Morgen, eine Stunde?"),
("Papa","m","Genau, er macht Yoga, ruhig und langsam, für den Rücken, jeden Morgen, um sieben, früh."),
("Mama","f","Toll! Lässt Lisa eine Maniküre machen, in Rot, für die Party?"),
("Papa","m","Ja, Lisa lässt eine Maniküre machen, in Rot, sie freut sich schon, sehr, mit Freude."),
("Mama","f","Süß! Essen wir danach zusammen, im Café, um eins, nach allem, gut so? Schwimmen lassen wir aus."),
("Papa","m","Gern! Ich lade dich ein, als Dank, für alles. Du zahlst nie, heute ich, viel Spaß, Prost, ihr Lieben!"),
("Mama","f","Ach, wie nett! Dann bis Samstag, mit Handtuch, bis Samstag, tschüss, ihr Lieben!"),
]

D[7] = [
("Jonas","m","Also, unser Sommerfest! Bist du dabei, Lisa, bei der Planung, mit mir?"),
("Lisa","f","Klar! Ich helfe gern, das wird lustig, im Sommer, am See."),
("Jonas","m","Super! Sag mal, organisiere ich die Location, am See, mit Terrasse, am Wasser?"),
("Lisa","f","Ja, bitte! Du kennst den Chef, das wird billiger, sicher."),
("Jonas","m","Genau, ich organisiere die Location! Kümmert du dich um das Catering?"),
("Lisa","f","Gern, ich kümmere mich um das Catering, mit Buffet, für fünfzig Leute, mit Musik, Kuchen und Brot."),
("Jonas","m","Wow! Ist Robert der DJ, mit Musikanlage, alles dabei?"),
("Lisa","f","Ja, Robert ist DJ und bringt die Musikanlage, mit Licht und Musik, die Party wird laut und lustig."),
("Jonas","m","Stark! Besorgt Tanja die Getränke, Wein und Saft, kalt und genug, für alle?"),
("Lisa","f","Genau, Tanja besorgt die Getränke, sie kennt einen guten Laden, in der Stadt."),
("Jonas","m","Perfekt! Macht Anna die Dekoration, mit Blumen, in Blau und Weiß, wie der See?"),
("Lisa","f","Ja, Anna macht die Dekoration, sie hat tolle Ideen, mit Blumen und Licht, mit Herz."),
("Jonas","m","Toll! Schreibe ich die Einladungen, an alle, heute noch, schnell?"),
("Lisa","f","Nein, das macht das Büro, du hast genug zu tun. Kuchen bringt keiner, das Catering reicht, mit Torte und Saft."),
("Jonas","m","Puh, gut! Dann bis morgen, mit dem Plan, bis morgen, um zehn, früh!"),
]

D[8] = [
("Mama","f","Also, unser Urlaub! Freust du dich, Papa, auf die See, endlich?"),
("Papa","m","Ja, sehr! Ich liebe das Meer, seit der Kindheit, wie als Kind, am Strand."),
("Mama","f","Ich auch! Sag mal, buche ich das Hotel, direkt am Strand, mit Blick?"),
("Papa","m","Ja, bitte! Du findest immer die schönsten, mit Frühstück, am Meer, oben."),
("Mama","f","Gut, ich buche das Hotel! Fährst du das Auto, den ganzen Weg, mit Karte?"),
("Papa","m","Klar, ich fahre das Auto, ruhig, mit Pausen, keine Sorge."),
("Mama","f","Danke! Plant Lisa die Ausflüge, mit Fahrrad und Schiff, für alle?"),
("Papa","m","Genau, Lisa plant die Tagesausflüge, sie liebt Pläne, mit Karte und viel Zeit."),
("Mama","f","Praktisch! Kocht Tante Eva warmes Essen, abends, für alle?"),
("Papa","m","Ja, sie kocht warmes Essen, Fisch und Salat, wie immer, mit Liebe, für alle."),
("Mama","f","Toll! Kümmert sich Tim um den Hund, in der Pension, mit Garten?"),
("Papa","m","Genau, Tim kümmert sich um den Hund, er kennt die Leute dort, seit Jahren, gern."),
("Mama","f","Gut! Kaufen wir Souvenirs, für Oma, am Hafen?"),
("Papa","m","Nein, Oma will nichts, sie hat alles, sagt sie. Sie wird sauer, mit Geschenken."),
("Mama","f","Genau! Dann packen wir, am Freitag, mit Freude! Und Fotos, viele Fotos, nicht vergessen!"),
("Papa","m","Ja, und vergiss den Hut nicht, wie letztes Jahr, mit viel Sonne!"),
]

D[10] = [
("Anna","f","Also, unsere Party! Bist du fertig, Markus, für Samstag?"),
("Markus","m","Fertig! Die Wohnung ist fast sauber, nur das Bad fehlt noch, schnell, dann los."),
("Anna","f","Gut! Sag mal, kaufe ich Blumen, schöne bunte, für alle Zimmer, bunt und frisch."),
("Markus","m","Ja, bitte! Du hast Ideen, das wird toll, überall."),
("Anna","f","Danke, ich kaufe Blumen, morgen früh! Kaufst du Wein und Sekt, aus dem guten Laden, um die Ecke, schnell?"),
("Markus","m","Klar, ich kaufe Wein und Sekt, für den Abend, kalt gestellt."),
("Anna","f","Perfekt! Macht Lisa das Buffet, mit Käse und Brot, alles frisch, vom Markt?"),
("Markus","m","Genau, Lisa macht das Buffet, sie kocht so gut, mit Liebe, seit Jahren, für alle."),
("Anna","f","Toll! Organisiert Tom die Musik, mit Handy, die ganze Nacht, bis morgens?"),
("Markus","m","Ja, Tom organisiert die Musik, er hat tausend Lieder, für jede Stunde, Tag und Nacht."),
("Anna","f","Super! Bringt Sara Eis mit, viel Eis, zum Dessert?"),
("Markus","m","Genau, Sara bringt viel Eis zum Dessert, sie kommt spät, direkt aus dem Laden, eiskalt."),
("Anna","f","Klug! Backt jemand Kuchen, einen großen, zum Kaffee?"),
("Markus","m","Nein, Lisa macht Buffet, das reicht wirklich, für alle, finde ich."),
("Anna","f","Genau! Dann bis Samstag, um sieben, mit Hunger!"),
("Markus","m","Ja, mit großem Hunger, bis dann, mit viel Musik! Geschenke brauchen wir keine."),
]

D[11] = [
("Vater","m","Also, unsere Termine! Hast du den Plan, Mutter, im Kopf, gut?"),
("Mutter","f","Fast! Der Kalender ist voll, nächste Woche, so viele Termine, jeden Tag."),
("Vater","m","Bei mir auch! Sag mal, habe ich einen Arzt-Termin für die Impfung, am Montag, früh?"),
("Mutter","f","Ja, um neun, beim Hausarzt, mit Pass und Karte, pünktlich, bitte nicht vergessen."),
("Vater","m","Gut, ich habe einen Arzt-Termin für die Impfung! Gehst du zum Bürgeramt für den Reisepass?"),
("Mutter","f","Genau, ich gehe zum Bürgeramt für den Reisepass, am Dienstag, mit Foto, von heute. Versicherung kommt später."),
("Vater","m","Wichtig! Hat Tim einen TÜV-Termin fürs Auto, am Mittwoch, mit Auto?"),
("Mutter","f","Ja, Tim hat einen TÜV-Termin fürs Auto, hoffentlich alles gut, viel Glück!"),
("Vater","m","Viel Glück! Geht Lisa zum Tierarzt für die Katze, am Donnerstag, früh?"),
("Mutter","f","Genau, Lisa geht zum Tierarzt für die Katze, zur Kontrolle, mit der Katze, ganz ruhig."),
("Vater","m","Süß! Hast du einen Bank-Termin zum Geldwechseln, Anna, am Freitag?"),
("Mutter","f","Anna hat einen Bank-Termin zum Geldwechseln, für den Urlaub, mit Euro, genau, für alles."),
("Vater","m","Ach so, Anna! Geht jemand zum Zahnarzt, mit Schmerzen, wirklich, stark?"),
("Mutter","f","Nein, zum Glück gesund, alle Zähne gut, alle glücklich, zum Glück."),
("Vater","m","Puh! Dann los, Termin für Termin, los geht’s, tschüss!"),
]

D[12] = [
("Lisa","f","Also, unsere Tiere! Hilfst du mir, Mutter, am Wochenende, mit den Tieren, bitte?"),
("Mutter","f","Klar! Ich liebe Tiere, alle, besonders die Katze, jeden Tag."),
("Lisa","f","Ich weiß! Sag mal, gehe ich mit dem Hund spazieren, morgens und abends, bei Wind und Wetter?"),
("Mutter","f","Ja, bitte! Er wartet schon, an der Tür, seit einer Stunde, der Arme."),
("Lisa","f","Gut, ich gehe mit dem Hund spazieren! Fütterst du die Katze, zweimal am Tag, pünktlich, ja?"),
("Mutter","f","Genau, ich füttere die Katze, morgens und abends, sie freut sich immer, sehr."),
("Lisa","f","Sicher! Pflegt Tim den Kanarienvogel, mit frischem Wasser, klar?"),
("Mutter","f","Ja, Tim pflegt den Kanarienvogel, er singt so schön, morgens, im Bad, laut."),
("Lisa","f","Wunderbar! Kümmert sich Vater um die Fische, gut und gern, wirklich, oder?"),
("Mutter","f","Genau, dein Vater kümmert sich um die Fische, jeden Tag, mit Liebe und frischem Wasser."),
("Lisa","f","Toll! Kontrolliert Lukas die Wohnung und holt die Post, am Samstag?"),
("Mutter","f","Ja, Lukas kontrolliert die Wohnung und holt die Post, alles in Ordnung, wie immer, pünktlich."),
("Lisa","f","Super! Geht jemand zum Tierarzt, mit dem Vogel, zur Kontrolle?"),
("Mutter","f","Nein, alle gesund, zum Glück, dieses Mal, keine Sorge."),
("Lisa","f","Puh! Dann bis Samstag, viel Spaß! Wäsche waschen wir Sonntag, alles zusammen, schnell."),
("Mutter","f","Mit viel Liebe, bis dann, tschüss!"),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
