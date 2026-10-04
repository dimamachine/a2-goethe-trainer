"""Batch C rewrite: tests 26,27,28,29,30,31,32,33,34,36 — natural direct speech."""
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
("Sara","f","Also, unser Schönheitstag am Freitag! Ich mache eine neue Frisur, kurz und modern, beim Friseur."),
("Anna","f","Toll! Ich mache eine Maniküre, mit rotem Lack, passend zum Kleid."),
("Lisa","f","Und ich bekomme eine Gesichtsbehandlung, mit Maske und Massage, pure Entspannung."),
("Sophie","f","Schön! Ich lasse Wimpern verlängern, für die Hochzeit, lange und schwarz."),
("Mara","f","Und ich gehe zur Massage, für den Rücken, eine ganze Stunde, herrlich."),
("Sara","f","Perfekt! Anna, wann hast du den Termin, am Freitag, morgens oder mittags?"),
("Anna","f","Um elf, beim Friseur in der Stadt, danach komme ich zu euch."),
("Lisa","f","Und die Wimpern, Sophie, halten sie lange, bis zur Hochzeit?"),
("Sophie","f","Drei Wochen, ganz sicher, die Hochzeit ist in zwei Wochen, perfekt."),
("Mara","f","Und danach essen wir zusammen, im Café, um drei, einverstanden?"),
("Sara","f","Gern! Also, ich mache eine neue Frisur, kurz und modern!"),
("Anna","f","Ich mache eine Maniküre, mit rotem Lack!"),
("Lisa","f","Ich bekomme eine Gesichtsbehandlung, mit Maske!"),
("Sophie","f","Ich lasse Wimpern verlängern, für die Hochzeit!"),
("Mara","f","Und ich gehe zur Massage, eine ganze Stunde!"),
("Sara","f","Super, bis Freitag, beim Friseur, um elf!"),
]

D[27] = [
("Eltern","m","Also, unser Urlaub im Sommer! Wir übernachten in einem 5-Sterne-Hotel, mit Pool, eine Woche."),
("Lukas","m","Cool! Ich übernachte in einer Jugendherberge, mit Freunden, ganz billig."),
("Lisa","f","Und ich übernachte in einer Ferienwohnung, mit Küche, am See, sehr gemütlich."),
("Tom","m","Ich übernachte auf einem Campingplatz, mit Zelt, in den Bergen, Abenteuer pur."),
("Anna","f","Und wir übernachten in einem Mittel-Klasse-Hotel, Markus und ich, in der Stadt."),
("Markus","m","Genau, wir übernachten in einem Mittel-Klasse-Hotel, mit Frühstück, drei Nächte."),
("Eltern","m","Schön, alle anders! Lukas, ist die Jugendherberge sauber, wirklich?"),
("Lukas","m","Ja, sehr sauber, mit Frühstück, und meine Freunde sind auch dort."),
("Lisa","f","Und der Campingplatz, Tom, gibt es dort Duschen, warmes Wasser?"),
("Tom","m","Ja, warme Duschen und Strom, alles da, kein Problem."),
("Anna","f","Und unsere Hotels, sind sie weit weg, voneinander, oder in der Nähe?"),
("Markus","m","Nur zehn Minuten, mit dem Bus, wir treffen uns jeden Tag."),
("Eltern","m","Also, wir übernachten in einem 5-Sterne-Hotel, mit Pool!"),
("Lukas","m","Ich übernachte in einer Jugendherberge, mit Freunden!"),
("Lisa","f","Ich übernachte in einer Ferienwohnung, am See!"),
("Tom","m","Und ich übernachte auf einem Campingplatz, mit Zelt!"),
]

D[28] = [
("Mutter","f","Also, die Post von heute! Ich habe ein Paket mit einer Tasche bekommen, aus Berlin, von Tante."),
("Vater","m","Schön! Ich habe eine Steuer-Rechnung bekommen, leider wahr, sehr ärgerlich."),
("Lisa","f","Und ich habe eine Postkarte aus dem Ausland bekommen, aus Spanien, von meiner Freundin."),
("Markus","m","Ich habe eine neue Kreditkarte bekommen, endlich da, nach langen Wochen."),
("Anna","f","Und ich habe ein bestelltes Buch bekommen, zum Lesen am Abend, sehr spannend."),
("Mutter","f","Alles da! Vater, wie hoch ist die Rechnung, vom Finanzamt, sehr hoch?"),
("Vater","m","Zweihundert Euro, leider, ich zahle morgen, per Überweisung."),
("Lisa","f","Und die Postkarte, was schreibt deine Freundin, aus Spanien, Schönes?"),
("Markus","m","Lisa, sie fragt dich! Also, was schreibt sie, aus Spanien?"),
("Lisa","f","Sonne und Strand, jeden Tag, sie bleibt noch zwei Wochen dort."),
("Mutter","f","Schön! Also, ich habe ein Paket mit einer Tasche bekommen, aus Berlin!"),
("Vater","m","Ich habe eine Steuer-Rechnung bekommen, zweihundert Euro!"),
("Lisa","f","Ich habe eine Postkarte aus dem Ausland bekommen, aus Spanien!"),
("Markus","m","Ich habe eine neue Kreditkarte bekommen, endlich!"),
("Anna","f","Und ich habe ein bestelltes Buch bekommen, zum Lesen!"),
("Mutter","f","Perfekt, alles da! Ich räume die Post weg, in den Schrank!"),
]
# fix: turn 9 Markus addresses Lisa oddly — rewrite
D[28][8] = ("Markus","m","Klingt toll! Sonne und Strand, ich will auch Urlaub, im Sommer.")

D[29] = [
("Vater","m","Also, unsere Vereine! Ich bin im Schachverein, jeden Dienstag, mit Turnieren, in der Stadt."),
("Mutter","f","Schön! Ich bin im Chor, wir singen donnerstags, in der Kirche, mit Freude."),
("Lukas","m","Und ich bin im Fußballverein, als Stürmer, zweimal pro Woche, mit hartem Training."),
("Lisa","f","Ich bin im Theaterverein, wir spielen im Frühling, ein lustiges Stück, mit Musik."),
("Sara","f","Und ich bin im Foto-Club, mit Kamera und Ausstellungen, in der Stadt, jeden Monat."),
("Vater","m","Toll! Mutter, singt ihr gut, im Chor, mit vielen Leuten?"),
("Mutter","f","Ja, dreißig Leute, es klingt wunderbar, besonders zu Weihnachten."),
("Lukas","m","Und Theater, Lisa, welche Rolle spielst du, im Frühling?"),
("Lisa","f","Eine lustige Nachbarin, mit viel Text, ich übe jeden Tag."),
("Sara","f","Und Schach, Vater, gewinnst du oft, die Turniere, am Dienstag?"),
("Vater","m","Manchmal! Also, ich bin im Schachverein, jeden Dienstag!"),
("Mutter","f","Ich bin im Chor, wir singen donnerstags!"),
("Lukas","m","Ich bin im Fußballverein, als Stürmer!"),
("Lisa","f","Ich bin im Theaterverein, wir spielen im Frühling!"),
("Sara","f","Und ich bin im Foto-Club, mit Kamera!"),
("Vater","m","Super, alle aktiv! Bis Dienstag, beim Schach!"),
]

D[30] = [
("Vater","m","Also, unsere Ämter diese Woche! Ich gehe zum Bürgeramt für den Personalausweis, am Montag."),
("Mutter","f","Gut! Ich gehe zum Standesamt für die Geburtsurkunde, am Dienstag, für den Pass."),
("Lukas","m","Und ich gehe zum Finanzamt für die Steuern, am Mittwoch, mit allen Papieren."),
("Lisa","f","Ich gehe zur Ausländerbehörde, am Donnerstag, für mein Visum, mit Pass."),
("Markus","m","Und ich habe TÜV, die Hauptuntersuchung, am Freitag, mit dem Auto."),
("Vater","m","Viele Ämter! Mutter, hast du alle Papiere, für die Urkunde, dabei?"),
("Mutter","f","Ja, alles kopiert, zweimal sogar, sicher ist sicher, bei Ämtern."),
("Lukas","m","Und das Visum, Lisa, dauert es lange, bei der Behörde, Stunden?"),
("Lisa","f","Leider ja, drei Stunden Wartezeit, mit Nummer, wie immer."),
("Markus","m","Und mein Auto, schafft es den TÜV, was denkt ihr, ehrlich?"),
("Vater","m","Bestimmt! Also, ich gehe zum Bürgeramt für den Personalausweis, am Montag!"),
("Mutter","f","Ich gehe zum Standesamt für die Geburtsurkunde, am Dienstag!"),
("Lukas","m","Ich gehe zum Finanzamt für die Steuern, am Mittwoch!"),
("Lisa","f","Ich gehe zur Ausländerbehörde, für mein Visum!"),
("Markus","m","Und ich habe TÜV, die Hauptuntersuchung, am Freitag!"),
("Vater","m","Viel Glück allen, bei den Ämtern!"),
]

D[31] = [
("Vater","m","Also, unsere Zähne! Ich bekomme eine Zahnreinigung, am Montag, zur Vorsorge."),
("Mutter","f","Gut! Ich bekomme eine Krone, am Dienstag, für den Backenzahn, aus Keramik."),
("Lukas","m","Und ich brauche eine Karies-Behandlung mit Plombe, am Mittwoch, leider ein Loch."),
("Lisa","f","Ich bekomme eine Zahnspange, am Donnerstag, für zwei Jahre, oben und unten."),
("Anna","f","Und ich lasse den Weisheitszahn ziehen, am Freitag, er tut sehr weh."),
("Vater","m","Arme Anna! Tut er sehr weh, der Zahn, auch nachts, beim Schlafen?"),
("Anna","f","Ja, sehr! Der Arzt gibt eine Spritze, dann geht es, hoffentlich."),
("Mutter","f","Und die Spange, Lisa, sieht man sie sehr, in der Schule?"),
("Lisa","f","Nur wenig, sie ist fast unsichtbar, aus hellem Material, gut."),
("Lukas","m","Und meine Plombe, dauert es lange, am Mittwoch, beim Arzt?"),
("Vater","m","Nur eine Stunde! Also, ich bekomme eine Zahnreinigung, am Montag!"),
("Mutter","f","Ich bekomme eine Krone, am Dienstag, aus Keramik!"),
("Lukas","m","Ich brauche eine Karies-Behandlung mit Plombe, am Mittwoch!"),
("Lisa","f","Ich bekomme eine Zahnspange, am Donnerstag!"),
("Anna","f","Und ich lasse den Weisheitszahn ziehen, am Freitag!"),
("Vater","m","Gute Besserung allen, viel Glück beim Arzt!"),
]

D[32] = [
("Vater","m","Also, unser Tag im Schwimmbad! Ich schwimme Bahnen, morgens, zwanzig Bahnen, für die Fitness."),
("Mutter","f","Stark! Ich mache Aqua-Fitness, um zehn, mit Musik, im flachen Wasser."),
("Lisa","f","Und ich rutsche auf der Wasserrutsche, den ganzen Tag, immer wieder, juhu!"),
("Tim","m","Ich gehe in den Schwimmkurs, um elf, für das Silber-Abzeichen, mit Trainer."),
("Anna","f","Und wir gehen in die Sauna, Markus und ich, nach dem Schwimmen, zur Entspannung."),
("Markus","m","Genau, wir gehen in die Sauna, mit Aufguss, um zwölf, herrlich."),
("Vater","m","Sehr gut! Lisa, ist die Rutsche nicht zu wild, für dich, ganz oben?"),
("Lisa","f","Nein, sie ist super, schnell und sicher, ich liebe sie!"),
("Mutter","f","Und der Kurs, Tim, schaffst du Silber, dieses Mal, bestimmt?"),
("Tim","m","Bestimmt! Ich übe jeden Tag, nach der Schule, im Bad."),
("Anna","f","Und Papa, zwanzig Bahnen, wirklich, jeden Morgen?"),
("Vater","m","Jeden Morgen! Also, ich schwimme Bahnen, zwanzig Stück!"),
("Mutter","f","Ich mache Aqua-Fitness, um zehn, mit Musik!"),
("Lisa","f","Ich rutsche auf der Wasserrutsche, den ganzen Tag!"),
("Tim","m","Ich gehe in den Schwimmkurs, für Silber!"),
("Anna","f","Und wir gehen in die Sauna, um zwölf!"),
]

D[33] = [
("Vater","m","Also, unser Camping am Wochenende! Ich bringe die Zelte, zwei große, für alle."),
("Mutter","f","Sehr gut! Ich kümmere mich um das Essen, für drei Tage, mit viel Gemüse."),
("Lukas","m","Und ich bringe Camping-Grill und Holz, für abends, mit Würstchen."),
("Lisa","f","Ich bringe Spiele und Bücher, für den Regen, falls es regnet."),
("Anna","f","Und ich bringe Schlafsäcke und Isomatten, für alle, warm und weich."),
("Vater","m","Perfekt! Mutter, reicht das Essen, für drei Tage, für fünf Leute?"),
("Mutter","f","Ja, plus Grillwürstchen von Lukas, das reicht gut, keine Sorge."),
("Lukas","m","Und bei Regen, Lisa, welche Spiele, hast du dabei, Karten?"),
("Lisa","f","Karten und ein Buch, dick und spannend, für alle, zum Vorlesen."),
("Anna","f","Und wer fährt, zum See, mit dem ganzen Gepäck, im Auto?"),
("Vater","m","Ich! Also, ich bringe die Zelte, zwei große!"),
("Mutter","f","Ich kümmere mich um das Essen, für drei Tage!"),
("Lukas","m","Ich bringe Camping-Grill und Holz, mit Würstchen!"),
("Lisa","f","Ich bringe Spiele und Bücher, für den Regen!"),
("Anna","f","Und ich bringe Schlafsäcke und Isomatten, für alle!"),
("Vater","m","Super, bis Freitag, am See, mit allem!"),
]

D[34] = [
("Annas Vater","m","Also, unsere Gesundheit! Ich hatte einen Herzinfarkt, im Frühling, jetzt geht es gut."),
("Annas Mutter","f","Gott sei Dank! Ich habe mir das Bein gebrochen, im Sommer, beim Wandern, jetzt fast heil."),
("Lukas","m","Und ich hatte eine Lungenentzündung, im Herbst, mit Fieber, jetzt gesund."),
("Lisa","f","Ich habe ein Baby bekommen, im Winter, klein und gesund, wunderbar."),
("Markus' Vater","m","Und bei mir hat man Gallensteine entfernt, im Januar, alles gut gegangen."),
("Annas Vater","m","Alle wieder gesund! Mutter, läuft das Bein gut, ohne Schmerzen, wirklich?"),
("Annas Mutter","f","Ja, fast wie früher, nur Treppen sind schwer, noch ein bisschen."),
("Lukas","m","Und das Baby, Lisa, schläft es schon durch, die ganze Nacht?"),
("Lisa","f","Fast, nur einmal wacht es auf, um drei, dann trinkt es."),
("Markus' Vater","m","Und dein Herz, geht es dir gut, nach dem Infarkt, im Frühling?"),
("Annas Vater","m","Sehr gut! Also, ich hatte einen Herzinfarkt, jetzt gesund!"),
("Annas Mutter","f","Ich habe mir das Bein gebrochen, fast heil!"),
("Lukas","m","Ich hatte eine Lungenentzündung, jetzt gesund!"),
("Lisa","f","Ich habe ein Baby bekommen, klein und gesund!"),
("Markus' Vater","m","Und bei mir hat man Gallensteine entfernt, alles gut!"),
("Annas Vater","m","Wunderbar, alle gesund! Auf uns, prost!"),
]

D[36] = [
("Lukas","m","Also, unser Studium! Ich studiere Medizin, im zweiten Jahr, sehr spannend, aber schwer, mit viel Praxis."),
("Lisa","f","Stark! Ich studiere Jura, im ersten Jahr, mit viel Lesen, jeden Tag, bis spät."),
("Tom","m","Und ich studiere Informatik, mit Programmieren, am Computer, den ganzen Tag, mit Kaffee."),
("Sara","f","Ich studiere Architektur, mit Zeichnen und Modellen, sehr kreativ und modern."),
("Tim","m","Und ich studiere Wirtschaft, mit Mathe und Englisch, für die Karriere, international."),
("Lukas","m","Toll! Lisa, ist Jura sehr schwer, im ersten Jahr, mit den Gesetzen?"),
("Lisa","f","Sehr schwer! Tausend Seiten pro Woche, aber interessant, wirklich."),
("Tom","m","Und Architektur, Sara, zeichnest du gut, schon als Kind, immer?"),
("Sara","f","Ja, schon immer, mein Zimmer war voll Bilder, früher, überall."),
("Tim","m","Und Medizin, Lukas, wie viele Jahre, noch bis zum Arzt, sechs?"),
("Lukas","m","Sechs Jahre! Also, ich studiere Medizin, im zweiten Jahr, weiter geht es!"),
("Lisa","f","Ich studiere Jura, im ersten Jahr!"),
("Tom","m","Ich studiere Informatik, mit Programmieren!"),
("Sara","f","Ich studiere Architektur, sehr kreativ!"),
("Tim","m","Und ich studiere Wirtschaft, für die Karriere!"),
("Lukas","m","Super, viel Erfolg allen, im Studium, weiter so!"),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
