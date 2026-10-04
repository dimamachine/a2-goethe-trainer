"""Batch A rewrite: tests 1,3,4,5,6,7,8,10,11,12 — natural direct speech."""
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
("Markus","m","Also, unsere Berlin-Reise am Freitag! Ich buche die Zugtickets, online, heute Abend nach der Arbeit."),
("Anna","f","Sehr gut! Ich buche das Hotel, ein kleines Hotel in der Stadtmitte, mit Frühstück für alle."),
("Jan","m","Und ich reserviere das Restaurant, für Freitagabend, für uns fünf, in der Nähe vom Hotel."),
("Lisa","f","Schön! Ich kaufe die Museum-Tickets, für Samstagvormittag, bequem im Voraus."),
("Vater","m","Und ich fahre zum Bahnhof, mit meinem Auto, ich bringe euch alle pünktlich hin."),
("Markus","m","Perfekt! Wann fahren wir los, um acht Uhr morgens, oder lieber früher?"),
("Anna","f","Um acht reicht! Jan, welches Restaurant nimmst du, italienisch oder deutsch?"),
("Jan","m","Italienisch, es hat sehr gute Pizza, und es ist wirklich nicht teuer."),
("Lisa","f","Und welches Museum nehmen wir, nur das große, oder noch ein kleines dazu?"),
("Anna","f","Nur das große, wir haben am Samstag leider wenig Zeit, am Abend kommt das Restaurant."),
("Markus","m","Ja, ich buche die Zugtickets, heute Abend, versprochen!"),
("Anna","f","Und ich buche das Hotel, mit Frühstück, auch heute!"),
("Jan","m","Ich reserviere das Restaurant, für fünf Personen, für Freitag!"),
("Lisa","f","Ich kaufe die Museum-Tickets, für Samstag, alles klar!"),
("Vater","m","Und ich fahre zum Bahnhof, um halb acht, mit dem Auto!"),
]

D[3] = [
("Anna","f","Also, unser großes Familienfest am Samstag! Ich backe einen Schokoladenkuchen, mit viel Kakao."),
("Markus","m","Lecker! Ich bringe Wein mit, roten und weißen, vom guten Laden an der Ecke."),
("Tim","m","Und ich bringe alkoholfreie Getränke, für die Kinder und für Oma, zwei volle Kästen."),
("Mutter","f","Wunderbar! Ich koche das Hauptgericht, wie jedes Jahr, mit viel Liebe und guten Zutaten."),
("Sara","f","Und ich mache einen großen Salat, frisch aus dem Garten, mit Tomaten und Gurken."),
("Anna","f","Klingt alles sehr lecker! Wer bringt Eis mit, für den Nachtisch, weiß das jemand?"),
("Markus","m","Eis? Hmm, schwierig, Eis schmilzt so schnell, im Sommer, auf dem Weg."),
("Tim","m","Stimmt, Eis lassen wir lieber weg, wir haben Kuchen und Salat, das reicht völlig."),
("Sara","f","Richtig! Und ein Geschenk braucht auch niemand, wir feiern einfach zusammen."),
("Anna","f","Einverstanden! Also, ich backe einen Schokoladenkuchen, am Freitagabend!"),
("Markus","m","Und ich bringe Wein mit, rot und weiß, am Samstag!"),
("Tim","m","Ich bringe alkoholfreie Getränke, zwei Kästen, für alle!"),
("Mutter","f","Ich koche das Hauptgericht, wie immer, mit Liebe!"),
("Sara","f","Und ich mache einen großen Salat, frisch aus dem Garten!"),
]

D[4] = [
("Anna","f","Also, unsere Lerngruppe für Mathe! Ich mache Algebra, die Gleichungen kann ich gut."),
("Markus","m","Sehr gut! Ich mache Geometrie, mit Dreiecken und Kreisen, das mag ich."),
("Sara","f","Und ich mache Wahrscheinlichkeit, mit Würfeln und Karten, das wird lustig."),
("Lisa","f","Schön! Ich mache Statistik, mit Tabellen und Zahlen aus dem Buch."),
("Tobias","m","Und ich mache Funktionen und Diagramme, mit dem Computer, ganz modern."),
("Anna","f","Perfekt, jedes Thema hat eine Person! Wann treffen wir uns, am Donnerstag?"),
("Markus","m","Donnerstag passt! Wo, bei mir zu Hause, im Wohnzimmer, um vier?"),
("Sara","f","Gern! Bringt jemand noch etwas zu essen mit, für die Pause?"),
("Lisa","f","Gute Idee! Ich bringe Äpfel und Wasser mit, gesund und billig."),
("Tobias","m","Und ich drucke die Diagramme aus, in der Schule, kostenlos."),
("Anna","f","Noch eine Frage: Bringt jeder sein Buch mit, am Donnerstag, bitte?"),
("Anna","f","Super! Also, ich mache Algebra, die Gleichungen, am Donnerstag!"),
("Markus","m","Ich mache Geometrie, mit Dreiecken, bei mir zu Hause!"),
("Sara","f","Ich mache Wahrscheinlichkeit, mit Würfeln, das wird gut!"),
("Lisa","f","Ich mache Statistik, mit Tabellen, plus Äpfel!"),
("Tobias","m","Und ich mache Funktionen und Diagramme, mit dem Computer!"),
]

D[5] = [
("Anna","f","Also, unser Umzug am Samstag! Ich hole den Lkw, morgens um acht, beim Vermieter."),
("Markus","m","Stark! Ich packe die Küche, mit Töpfen und Tellern, ganz vorsichtig."),
("Lisa","f","Und ich packe die Bücher, alle Kartons aus dem Regal, das dauert lange."),
("Tim","m","Ich putze die alte Wohnung, am Sonntag, Bad und Küche, alles sauber."),
("Vater","m","Und ich richte das Internet ein, in der neuen Wohnung, mit dem Techniker."),
("Anna","f","Sehr gut! Markus, brauchst du Hilfe in der Küche, mit den schweren Töpfen?"),
("Markus","m","Nein, danke, das schaffe ich allein, am Freitagabend, in Ruhe."),
("Lisa","f","Und wer trägt die Bücherkartons, die sind so schwer, allein geht das nicht!"),
("Tim","m","Ich helfe dir, Lisa, am Samstag, nach dem Putzen, kein Problem."),
("Tim","m","Und am Abend bestellen wir Pizza, für alle, nach der Arbeit."),
("Vater","f","Moment, Moment! Ich bin der Vater, also, ich richte das Internet ein, der Techniker kommt um zehn.") ,
("Anna","f","Alles klar! Ich hole den Lkw, um acht, beim Vermieter!"),
("Markus","m","Ich packe die Küche, vorsichtig, am Freitag!"),
("Lisa","f","Ich packe die Bücher, mit Tims Hilfe, am Samstag!"),
("Tim","m","Ich putze die alte Wohnung, am Sonntag, alles sauber!"),
]
# fix: Vater gender + line (typo above) — will correct after
D[5][9] = ("Vater","m","Alles klar! Ich richte das Internet ein, der Techniker kommt um zehn.")

D[6] = [
("Mama","f","Also, unser Wellness-Tag am Samstag! Ich lasse eine Rückenmassage machen, gegen meine Schmerzen."),
("Papa","m","Sehr gut! Ich gehe in die Sauna, mit Aufguss, das liebe ich."),
("Tante Eva","f","Und ich buche eine Gesichtsbehandlung, mit Maske und Creme, pure Entspannung."),
("Onkel Robert","m","Ich mache Yoga, am Morgen, eine ganze Stunde, für den Rücken."),
("Lisa","f","Schön! Ich lasse eine Maniküre machen, mit rotem Lack, für die Party."),
("Mama","f","Klingt herrlich! Papa, wie lange bleibst du in der Sauna, nicht zu lange?"),
("Papa","m","Nur eine Stunde, keine Sorge, danach trinke ich viel Wasser, versprochen."),
("Tante Eva","f","Und Yoga, Robert, ist das nicht zu anstrengend, für dich, am Morgen?"),
("Onkel Robert","m","Nein, es ist sanftes Yoga, für Anfänger, ganz ruhig und langsam."),
("Lisa","f","Und danach essen wir zusammen, im Café, um eins, einverstanden?"),
("Mama","f","Gern! Also, ich lasse eine Rückenmassage machen, am Samstag!"),
("Papa","m","Ich gehe in die Sauna, mit Aufguss, eine ganze Stunde!"),
("Tante Eva","f","Ich buche eine Gesichtsbehandlung, mit Maske, Entspannung pur!"),
("Onkel Robert","m","Ich mache Yoga, am Morgen, eine Stunde!"),
("Lisa","f","Und ich lasse eine Maniküre machen, mit rotem Lack!"),
]

D[7] = [
("Jonas","m","Also, unsere Firmenfeier im Sommer! Ich organisiere die Location, am See, mit Terrasse."),
("Lisa","f","Super! Ich kümmere mich um das Catering, mit Buffet und Kuchen, für fünfzig Leute."),
("Robert","m","Und ich bin DJ und bringe die Musikanlage, mit Licht und Boxen, die Party wird laut."),
("Tanja","f","Schön! Ich besorge die Getränke, mit Wein und Saft, kalt und genug für alle."),
("Anna","f","Und ich mache die Dekoration, mit Blumen und Kerzen, alles in Blau und Weiß."),
("Jonas","m","Perfekt! Lisa, ist das Catering nicht zu teuer, für fünfzig Leute, was kostet es?"),
("Lisa","f","Nein, es bleibt im Budget, ungefähr tausend Euro, mit allem, wirklich."),
("Robert","m","Und die Musikanlage, Robert, funktioniert sie auch draußen, am See, im Freien?"),
("Tanja","f","Robert, die Frage war an dich! Also, geht die Anlage auch draußen?"),
("Robert","m","Ja, klar, sie geht auch draußen, mit Strom vom Haus, kein Problem."),
("Jonas","m","Sehr gut! Ich organisiere die Location, am See, mit Terrasse!"),
("Lisa","f","Ich kümmere mich um das Catering, für fünfzig Leute!"),
("Robert","m","Ich bin DJ und bringe die Musikanlage, mit Licht!"),
("Tanja","f","Ich besorge die Getränke, kalt und genug!"),
("Anna","f","Und ich mache die Dekoration, in Blau und Weiß!"),
]
# fix self-address in turn 8/9 — rewrite those two lines below
D[7][7] = ("Robert","m","Die Anlage funktioniert auch draußen, am See, mit Strom vom Haus.")
D[7][8] = ("Tanja","f","Wunderbar! Und das Essen, Lisa, warm oder kalt, was gibt es?")

D[8] = [
("Mama","f","Also, unser Urlaub an der See! Ich buche das Hotel, direkt am Strand, mit Meerblick."),
("Papa","m","Herrlich! Ich fahre das Auto, die ganze Strecke, über achthundert Kilometer."),
("Lisa","f","Und ich plane die Tagesausflüge, mit dem Fahrrad und dem Schiff, für alle."),
("Tante Eva","f","Schön! Ich koche warmes Essen, abends, in der Ferienwohnung, für uns alle."),
("Tim","m","Und ich kümmere mich um den Hund, in der Pension, mit großem Garten."),
("Mama","f","Sehr gut! Papa, fährst du wirklich allein, achthundert Kilometer, ohne Pause?"),
("Papa","m","Nein, wir machen Pausen, alle zwei Stunden, ganz gemütlich, keine Sorge."),
("Lisa","f","Und der Hund, Tim, bleibt er gern in der Pension, ohne uns, eine Woche?"),
("Tim","m","Ja, er kennt die Pension gut, mit Garten und anderen Hunden, er liebt es."),
("Tante Eva","f","Und was koche ich am ersten Abend, vielleicht Pasta, für alle, schnell und lecker?"),
("Tim","m","Pasta klingt gut! Und wer kauft ein, für die Woche, am ersten Tag?"),
("Mama","f","Gern, Pasta! Einkaufen gehen wir zusammen, am ersten Tag. Also, ich buche das Hotel, am Strand, mit Meerblick!"),
("Papa","m","Ich fahre das Auto, gemütlich, mit Pausen!"),
("Lisa","f","Ich plane die Tagesausflüge, mit Fahrrad und Schiff!"),
("Tante Eva","f","Ich koche warmes Essen, Pasta am ersten Abend!"),
("Tim","m","Und ich kümmere mich um den Hund, in der Pension!"),
]

D[10] = [
("Anna","f","Also, unsere Einweihungsparty am Samstag! Ich kaufe Blumen, schöne bunte, für alle Zimmer."),
("Markus","m","Sehr gut! Ich kaufe Wein und Sekt, aus dem guten Laden, für den Abend."),
("Lisa","f","Und ich mache das Buffet, mit Käse und Brot, Oliven und kleinen Salaten, alles frisch."),
("Tom","m","Ich organisiere die Musik, mit meiner Sammlung auf dem Handy, plus Boxen."),
("Sara","f","Schön! Ich bringe Eis zum Dessert, drei Sorten, am Tag der Party, versprochen."),
("Anna","f","Perfekt! Tom, reicht dein Handy für die Musik, für den ganzen Abend, wirklich?"),
("Tom","m","Ja, plus Boxen, der Akku hält lange, keine Sorge, ich habe alles getestet."),
("Lisa","f","Und das Eis, Sara, schmilzt es nicht, bis zum Dessert, im Sommer?"),
("Sara","f","Nein, ich bringe es spät, kurz vor dem Dessert, direkt aus dem Laden."),
("Tom","m","Und wer macht Fotos, auf der Party, ich habe keine Kamera?"),
("Markus","m","Und Geschenke, braucht jemand ein Geschenk, oder feiern wir einfach zusammen?"),
("Anna","f","Einfach zusammen! Also, ich kaufe Blumen, bunte, für alle Zimmer!"),
("Markus","m","Ich kaufe Wein und Sekt, aus dem guten Laden!"),
("Lisa","f","Ich mache das Buffet, mit Käse und Brot, alles frisch!"),
("Tom","m","Ich organisiere die Musik, mit Handy und Boxen!"),
("Sara","f","Und ich bringe Eis zum Dessert, drei Sorten!"),
]

D[11] = [
("Vater","m","Also, unsere Termine nächste Woche! Ich habe einen Arzt-Termin für die Impfung, am Montag."),
("Mutter","f","Gut! Ich gehe zum Bürgeramt für den Reisepass, am Dienstag, mit Foto."),
("Tim","m","Und ich habe einen TÜV-Termin fürs Auto, am Mittwoch, hoffentlich alles gut."),
("Lisa","f","Ich gehe zum Tierarzt für die Katze, am Donnerstag, zur Kontrolle."),
("Anna","f","Und ich habe einen Bank-Termin zum Geldwechseln, am Freitag, für den Urlaub."),
("Vater","m","Viele Termine! Mutter, hast du schon ein Foto, für den Reisepass, biometrisch?"),
("Mutter","f","Ja, vom Fotografen, gestern gemacht, es war nicht billig, leider."),
("Tim","m","Und das Auto, Tim, also mein Auto, schafft es den TÜV, was denkt ihr?"),
("Lisa","f","Viel Glück! Ruf mich an, nach dem Termin, gleich am Mittwoch."),
("Anna","f","Und die Katze, Lisa, mag sie den Tierarzt, oder hat sie Angst?"),
("Vater","m","Also, ich habe einen Arzt-Termin für die Impfung, am Montag!"),
("Mutter","f","Ich gehe zum Bürgeramt für den Reisepass, am Dienstag!"),
("Tim","m","Ich habe einen TÜV-Termin fürs Auto, am Mittwoch!"),
("Lisa","f","Ich gehe zum Tierarzt für die Katze, am Donnerstag!"),
("Anna","f","Und ich habe einen Bank-Termin zum Geldwechseln, am Freitag!"),
]
# fix self-address turn 8
D[11][7] = ("Tim","m","Mein Auto schafft den TÜV bestimmt, es ist fast neu, erst zwei Jahre alt.")

D[12] = [
("Lisa","f","Also, unsere Haustiere am Wochenende! Ich gehe mit dem Hund spazieren, morgens und abends."),
("Mutter","f","Sehr gut! Ich füttere die Katze, zweimal am Tag, morgens und abends."),
("Tim","m","Und ich pflege den Kanarienvogel, mit frischem Wasser und Futter, jeden Tag."),
("Vater","m","Ich kümmere mich um die Fische, mit Futter und sauberem Wasser, im Aquarium."),
("Lukas","m","Und ich kontrolliere die Wohnung und hole die Post, am Samstag, alles in Ordnung."),
("Lisa","f","Schön! Mutter, frisst die Katze gut, auch das neue Futter, ohne Problem?"),
("Mutter","f","Ja, sie liebt es, besonders am Morgen, sie wartet schon an der Tür."),
("Tim","m","Und der Vogel, singt er noch so schön, wie früher, am Morgen?"),
("Vater","m","Ja, sehr schön! Und die Fische, bekommen sie genug Licht, im Aquarium?"),
("Lukas","m","Das Licht geht automatisch an, kein Problem, ich kontrolliere alles am Samstag."),
("Mutter","f","Und das Futter, reicht es bis Montag, für alle Tiere?"),
("Lisa","f","Also, ich gehe mit dem Hund spazieren, morgens und abends!"),
("Mutter","f","Ich füttere die Katze, zweimal am Tag!"),
("Tim","m","Ich pflege den Kanarienvogel, mit Wasser und Futter!"),
("Vater","m","Ich kümmere mich um die Fische, im Aquarium!"),
("Lukas","m","Und ich kontrolliere die Wohnung und hole die Post!"),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
