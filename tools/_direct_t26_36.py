#!/usr/bin/env python3
"""Rewrite T2 as direct speech, batch C (26,27,28,29,30,31,32,33,34,36)."""
import json
import re
from pathlib import Path

TOOLS = Path(__file__).resolve().parent


def W(text):
    return len(re.findall(r"[A-Za-zÄÖÜäöüß]+", text))


def L(speaker, gender, text):
    return {"speaker": speaker, "gender": gender, "text": text}


def apply(n, t2, check_order=None):
    path = TOOLS / f"_test{n}_data.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    inst = data["teile"][1]["instruction"]
    idx = inst.find('Sie hören den Text einmal')
    assert idx > 0, inst
    data["teile"][1]["instruction"] = 'Sie hören ein Gespräch. ' + inst[idx:]
    data["teile"][1]["lines"] = t2
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    te = data["teile"][1]
    t2w = sum(W(x["text"]) for x in te["lines"])
    print(f"T{n} T2={t2w}w/{len(te['lines'])}t")
    if check_order:
        seen = []
        for l in te["lines"]:
            if l["speaker"] not in seen:
                seen.append(l["speaker"])
        mains = [s for s in seen if s in check_order]
        print(f"   {'ORDER OK' if mains == check_order else f'ORDER {mains} != {check_order}'}")


# ---------------- TEST 26 friseur-und-schoenheit (all f) ----------------
# Sara(a Frisur) Anna(i Maniküre) Lisa(h Gesicht) Sophie(d Wimpern) Mara(e Massage)
apply(26, [
    L("Sara", "f", "Also, Beauty-Tag mit Freundinnen! Was macht jede? Ich bekomme eine neue Frisur."),
    L("Anna", "f", "Schön! Ich mache eine Maniküre, dringend nötig, wirklich."),
    L("Lisa", "f", "Ich bekomme eine Gesichtsbehandlung, für reine Haut, hoffentlich."),
    L("Sophie", "f", "Ich lasse Wimpern verlängern, für den Urlaub am Meer."),
    L("Mara", "f", "Und ich gehe zur Massage, gegen Stress, endlich mal."),
    L("Sara", "f", "Super, alles verteilt! Färbt jemand die Haare?"),
    L("Anna", "f", "Färben? Nein, nur Maniküre bei mir. Macht jemand Pediküre?"),
    L("Lisa", "f", "Pediküre nicht, nur Gesicht. Bekommt jemand Make-up?"),
    L("Sophie", "f", "Make-up nicht, nur Wimpern bei mir. Geht jemand in die Sauna?"),
    L("Mara", "f", "Sauna nicht, nur Massage bei mir. Wann treffen wir uns?"),
    L("Sara", "f", "Um zehn im Salon, einverstanden?"),
    L("Anna", "f", "Einverstanden! Bis dann, tschüss!"),
    L("Lisa", "f", "Bis Samstag! Ich freue mich schon sehr!"),
    L("Sophie", "f", "Ich auch! Tschüss zusammen!"),
    L("Mara", "f", "Tschüss! Bis Samstag im Salon!"),
    L("Sara", "f", "Noch etwas: Gute Laune mitbringen, einverstanden?"),
], check_order=["Sara", "Anna", "Lisa", "Sophie", "Mara"])

# ---------------- TEST 27 hotel-und-uebernachten ----------------
# Eltern(g 5-Sterne) Lukas(c Herberge) Lisa(e Fewo) Tom(f Camping) Anna+Markus(h Mittelklasse)
apply(27, [
    L("Eltern", "m", "Also, Urlaub! Wo übernachtet jeder? Wir nehmen ein 5-Sterne-Hotel, mit Pool."),
    L("Lukas", "m", "Luxus! Ich nehme eine Jugendherberge, billig und lustig, mit Freunden."),
    L("Lisa", "f", "Ich nehme eine Ferienwohnung, mit Küche, am See, wunderschön."),
    L("Tom", "m", "Ich gehe auf einen Campingplatz, mit Zelt, in den Bergen, toll."),
    L("Anna", "f", "Wir nehmen ein Mittel-Klasse-Hotel, Markus und ich zusammen, gemütlich."),
    L("Markus", "m", "Genau, zusammen! Nimmt jemand von euch eine Pension?"),
    L("Eltern", "m", "Pension? Nein, nur Hotel bei uns, wirklich."),
    L("Lukas", "m", "Bauernhof nicht, nur Herberge bei mir. Schläft jemand im Bus-Hotel?"),
    L("Lisa", "f", "Bus-Hotel? Nein, nur Wohnung bei mir. Schläft jemand bei Verwandten?"),
    L("Tom", "m", "Verwandte nicht, nur Zelt bei mir. Wann fahren wir los?"),
    L("Anna", "f", "Samstag früh, einverstanden, oder?"),
    L("Markus", "m", "Einverstanden! Bis dann, tschüss!"),
    L("Eltern", "m", "Bis Samstag! Gute Reise euch allen!"),
    L("Lukas", "m", "Tschüss euch allen!"),
    L("Lisa", "f", "Noch etwas: Sonnencreme nicht vergessen, bitte!"),
    L("Tom", "m", "Stimmt! Und Mückenspray auch, ganz wichtig, wirklich."),
], check_order=["Eltern", "Lukas", "Lisa", "Tom", "Anna", "Markus"])

# ---------------- TEST 28 post-und-pakete ----------------
# Mutter(i Paket) Vater(e Rechnung) Lisa(a Postkarte) Markus(d Kreditkarte) Anna(f Buch)
apply(28, [
    L("Mutter", "f", "Also, Post ist da! Was hat jeder bekommen? Ich habe ein Paket mit einer Tasche bekommen."),
    L("Vater", "m", "Schön! Ich habe eine Steuer-Rechnung bekommen, leider wahr."),
    L("Lisa", "f", "Ich habe eine Postkarte aus dem Ausland bekommen, aus Spanien."),
    L("Markus", "m", "Ich habe eine neue Kreditkarte bekommen, endlich da."),
    L("Anna", "f", "Und ich habe ein bestelltes Buch bekommen, zum Lesen am Abend."),
    L("Mutter", "f", "Alles da! Hat jemand einen Werbeprospekt bekommen?"),
    L("Vater", "m", "Prospekt? Nein, nur Rechnung bei mir. Hat jemand ein Geburtstagsgeschenk bekommen?"),
    L("Lisa", "f", "Geschenk nicht, nur Karte. Hat jemand eine Mahnung bekommen?"),
    L("Markus", "m", "Mahnung nicht, nur Karte, zum Glück. Hat jemand eine Hochzeitseinladung bekommen?"),
    L("Anna", "f", "Einladung nicht, nur Buch. Bezahlen wir die Rechnung gleich?"),
    L("Mutter", "f", "Ja, heute noch! Sonst noch etwas Wichtiges?"),
    L("Vater", "m", "Nein, alles erledigt! Bis später, tschüss!"),
    L("Lisa", "f", "Tschüss! Bis heute Abend, ihr Lieben!"),
    L("Markus", "m", "Bis dann! Schönes Wochenende!"),
    L("Anna", "f", "Euch auch, tschüss!"),
    L("Mutter", "f", "Noch etwas: Altpapier wegbringen, einverstanden?"),
], check_order=["Mutter", "Vater", "Lisa", "Markus", "Anna"])

# ---------------- TEST 29 vereine-und-hobbys ----------------
# Vater(i Schach) Mutter(h Chor) Lukas(g Fußball) Lisa(a Theater) Sara(d Foto)
apply(29, [
    L("Vater", "m", "Also, neue Hobbys! In welchen Verein geht ihr? Ich gehe in den Schachverein."),
    L("Mutter", "f", "Schön! Ich gehe in den Chor, singen macht Spaß, wirklich."),
    L("Lukas", "m", "Ich gehe in den Fußballverein, Training zweimal pro Woche, anstrengend."),
    L("Lisa", "f", "Ich gehe in den Theaterverein, wir spielen ein Stück im Juni."),
    L("Sara", "f", "Und ich gehe in den Foto-Club, mit neuer Kamera, toll."),
    L("Vater", "m", "Toll, alle aktiv! Geht jemand in den Tanzverein?"),
    L("Mutter", "f", "Tanzen? Nein, nur Chor bei mir, wirklich."),
    L("Lukas", "m", "Musik nicht, nur Fußball bei mir. Geht jemand wandern im Wanderclub?"),
    L("Lisa", "f", "Wandern nicht, nur Theater bei mir. Geht jemand in den Buchklub?"),
    L("Sara", "f", "Bücher nicht, nur Fotos bei mir. Treffen wir uns Sonntag?"),
    L("Vater", "m", "Ja, Sonntag zum Essen, einverstanden, oder?"),
    L("Mutter", "f", "Einverstanden! Bis Sonntag, tschüss!"),
    L("Lukas", "m", "Bis dann! Ich freue mich schon!"),
    L("Lisa", "f", "Ich auch! Tschüss euch allen!"),
    L("Sara", "f", "Tschüss zusammen! Bis Sonntag alle!"),
    L("Vater", "m", "Noch etwas: Beiträge überweisen, nicht vergessen!"),
], check_order=["Vater", "Mutter", "Lukas", "Lisa", "Sara"])

# ---------------- TEST 30 behoerden-und-dokumente ----------------
# Vater(e Bürgeramt) Mutter(g Standesamt) Lukas(i Finanzamt) Lisa(c Ausländerbehörde) Markus(a TÜV)
apply(30, [
    L("Vater", "m", "Also, Ämter-Marathon heute! Wo wart ihr? Ich war beim Bürgeramt für den Personalausweis."),
    L("Mutter", "f", "Anstrengend! Ich war beim Standesamt für eine Geburtsurkunde, wichtig."),
    L("Lukas", "m", "Ich war beim Finanzamt für die Steuern, lange Schlange, schrecklich."),
    L("Lisa", "f", "Ich war bei der Ausländerbehörde, für den Aufenthaltstitel, endlich."),
    L("Markus", "m", "Und ich war beim TÜV für die Hauptuntersuchung, mit dem Auto, alles okay."),
    L("Vater", "m", "Alles geschafft! War jemand bei der Polizei für eine Verlustanzeige?"),
    L("Mutter", "f", "Polizei? Nein, nur Standesamt bei mir, wirklich."),
    L("Lukas", "m", "Arbeitsamt nicht, nur Finanzamt bei mir. War jemand beim Gericht?"),
    L("Lisa", "f", "Gericht nicht, nur Behörde bei mir. War jemand bei der Krankenkasse?"),
    L("Markus", "m", "Krankenkasse nicht, nur TÜV bei mir. Treffen wir uns zu Hause?"),
    L("Vater", "m", "Ja, um sechs zu Hause, einverstanden, oder?"),
    L("Mutter", "f", "Einverstanden! Bis dann, tschüss!"),
    L("Lukas", "m", "Bis heute Abend! Tschüss!"),
    L("Lisa", "f", "Tschüss! Erholt euch gut, ihr Lieben!"),
    L("Markus", "m", "Euch auch! Bis später!"),
    L("Vater", "m", "Noch etwas: Papiere abheften, nicht vergessen!"),
], check_order=["Vater", "Mutter", "Lukas", "Lisa", "Markus"])

# ---------------- TEST 31 beim-zahnarzt ----------------
# Vater(b Reinigung) Mutter(c Krone) Lukas(f Karies) Lisa(i Spange) Anna(d Weisheitszahn)
apply(31, [
    L("Vater", "m", "Also, Zahnarzt heute! Was wurde gemacht? Bei mir eine Zahnreinigung, ganz gründlich."),
    L("Mutter", "f", "Bei mir eine Krone, endlich fertig, nach langen Wochen."),
    L("Lukas", "m", "Bei mir Karies-Behandlung, eine Plombe, schnell und gut gemacht."),
    L("Lisa", "f", "Ich bekomme eine Zahnspange, ab nächsten Monat, aufregend."),
    L("Anna", "f", "Bei mir wird ein Weisheitszahn gezogen, nächste Woche Dienstag."),
    L("Vater", "m", "Alles klar! Hat jemand von euch Zähne bleichen lassen?"),
    L("Mutter", "f", "Bleichen? Nein, nur Krone bei mir, wirklich."),
    L("Lukas", "m", "Brücke nicht, nur Plombe bei mir. Bekommt jemand ein Implantat?"),
    L("Lisa", "f", "Implantat nicht, nur Spange bei mir. War jemand nur zur Kontrolle da?"),
    L("Anna", "f", "Kontrolle nicht, bei mir wird gezogen, leider. Tut es weh bei euch?"),
    L("Vater", "m", "Nein, alles halb so wild! Eis essen danach, einverstanden?"),
    L("Mutter", "f", "Gute Idee! Eis hilft immer, wirklich."),
    L("Lukas", "m", "Lecker! Bis morgen!"),
    L("Lisa", "f", "Bis dann! Gute Besserung uns allen!"),
    L("Anna", "f", "Euch auch! Tschüss euch allen!"),
    L("Vater", "m", "Noch etwas: Zähne putzen, nicht vergessen, niemals!"),
], check_order=["Vater", "Mutter", "Lukas", "Lisa", "Anna"])

# ---------------- TEST 32 im-schwimmbad ----------------
# Vater(g Bahnen) Mutter(e Aqua) Lisa(a Rutsche) Tim(f Kurs) Anna+Markus(c Sauna)
apply(32, [
    L("Vater", "m", "Also, Schwimmbad heute! Was macht ihr heute? Ich schwimme Bahnen, zwanzig Stück."),
    L("Mutter", "f", "Schön! Ich mache Aqua-Fitness, mit Musik im Wasser, toll."),
    L("Lisa", "f", "Ich rutsche auf der Wasserrutsche, immer wieder! Klasse!"),
    L("Tim", "m", "Ich gehe in den Schwimmkurs, lerne Kraulen, endlich."),
    L("Anna", "f", "Wir gehen in die Sauna, Markus und ich zusammen, gemütlich."),
    L("Markus", "m", "Genau, zusammen, wirklich zusammen! Trinkt jemand etwas im Café?"),
    L("Vater", "m", "Café? Nein, nur Bahnen bei mir, wirklich."),
    L("Mutter", "f", "Beckenrand nicht, nur Fitness bei mir. Springt jemand vom Sprungbrett?"),
    L("Lisa", "f", "Sprungbrett nicht, nur Rutsche bei mir. Spielt jemand Wasserball?"),
    L("Tim", "m", "Wasserball nicht, nur Kurs bei mir. Treffen wir uns danach?"),
    L("Anna", "f", "Ja, in einer Stunde am Eingang, pünktlich?"),
    L("Markus", "m", "Bis gleich! Viel Spaß euch!"),
    L("Vater", "m", "Bis dann! Schwimmt fleißig weiter!"),
    L("Mutter", "f", "Euch auch! Tschüss euch allen!"),
    L("Lisa", "f", "Tschüss! Bis gleich alle zusammen!"),
    L("Tim", "m", "Noch etwas: Duschen nicht vergessen, bitte!"),
], check_order=["Vater", "Mutter", "Lisa", "Tim", "Anna", "Markus"])

# ---------------- TEST 33 camping-und-wandern ----------------
# Vater(f Zelte) Mutter(b Essen) Lukas(c Grill) Lisa(d Spiele) Anna(h Schlafsäcke)
apply(33, [
    L("Vater", "m", "Also, Camping am Wochenende! Wer bringt was mit? Ich bringe die Zelte."),
    L("Mutter", "f", "Gut! Ich kümmere mich um das Essen, für alle Tage, reichlich."),
    L("Lukas", "m", "Ich bringe Camping-Grill und Holz mit, zum Kochen am Feuer."),
    L("Lisa", "f", "Ich bringe Spiele und Bücher mit, für den Abend am Feuer."),
    L("Anna", "f", "Und ich bringe Schlafsäcke und Isomatten mit, für alle zusammen."),
    L("Vater", "m", "Perfekt! Bringt jemand warme Decken mit?"),
    L("Mutter", "f", "Decken? Nein, nur Essen bei mir, wirklich. Bringt jemand das Geschirr mit?"),
    L("Lukas", "m", "Geschirr nicht, nur Grill bei mir. Macht jemand die Wanderpläne?"),
    L("Lisa", "f", "Wanderpläne nicht, nur Spiele bei mir. Fährt jemand das Auto?"),
    L("Anna", "f", "Auto fahren wir zusammen, abwechselnd, fair."),
    L("Vater", "m", "Einverstanden! Wann geht es los?"),
    L("Mutter", "f", "Freitag um drei, pünktlich, wirklich."),
    L("Lukas", "m", "Bis Freitag! Ich freue mich schon!"),
    L("Lisa", "f", "Ich auch! Tschüss!"),
    L("Anna", "f", "Tschüss! Bis Freitag alle zusammen!"),
    L("Vater", "m", "Noch etwas: Taschenlampen nicht vergessen, einverstanden?"),
], check_order=["Vater", "Mutter", "Lukas", "Lisa", "Anna"])

# ---------------- TEST 34 im-krankenhaus (two fathers: full labels) ----------------
# Annas Vater(e Infarkt) Annas Mutter(h Bein) Lukas(g Lunge) Lisa(a Baby) Markus' Vater(b Galle)
apply(34, [
    L("Annas Vater", "m", "Hallo zusammen, unsere Krankenhaus-Woche! Wer liegt wo? Ich hatte einen kleinen Herzinfarkt."),
    L("Annas Mutter", "f", "Oh nein! Und ich bin gestürzt, Bein gebrochen, Operation und Reha."),
    L("Annas Vater", "m", "Gute Besserung uns! Erholst du dich gut?"),
    L("Lukas", "m", "Oh nein! Ich habe eine schwere Lungenentzündung, noch eine Woche hier."),
    L("Lisa", "f", "Und ich habe ein Baby bekommen! Maxi, vor zwei Tagen geboren!"),
    L("Markus' Vater", "m", "Glückwunsch! Ich hatte Gallensteine entfernt, kein Notfall."),
    L("Annas Mutter", "f", "Alles klar! Wurde jemand am Knie operiert?"),
    L("Annas Vater", "m", "Knie nicht, nur Herz bei mir. Hat jemand Kopfschmerzen?"),
    L("Lukas", "m", "Kopf nicht, nur Lunge. Hatte jemand eine Grippe?"),
    L("Lisa", "f", "Grippe nicht, nur Baby-Glück! Ist jemand nur zur Kontrolle hier?"),
    L("Markus' Vater", "m", "Kontrolle nicht, morgen bin ich wieder zu Hause."),
    L("Annas Mutter", "f", "Schön! Besuchszeit von 14 bis 19 Uhr, einverstanden?"),
    L("Annas Vater", "m", "Einverstanden! Bringt keine Blumen mit, nur Kekse!"),
    L("Lukas", "m", "Kekse, lecker! Bis morgen!"),
    L("Lisa", "f", "Bis dann! Gute Besserung allen!"),
    L("Markus' Vater", "m", "Euch auch! Tschüss zusammen!"),
], check_order=["Annas Vater", "Annas Mutter", "Lukas", "Lisa", "Markus' Vater"])

# ---------------- TEST 36 studium-und-universitaet ----------------
# Lukas(i Medizin) Lisa(f Jura) Tom(c Informatik) Sara(b Architektur) Tim(h Wirtschaft)
apply(36, [
    L("Lukas", "m", "Also, Studium! Was studiert ihr alles? Ich studiere Medizin, im zweiten Jahr, sehr spannend."),
    L("Lisa", "f", "Toll! Ich studiere Jura, schon im dritten Semester, mit viel Arbeit, aber toll."),
    L("Tom", "m", "Ich studiere Informatik, Programmieren macht Spaß, jeden Tag."),
    L("Sara", "f", "Ich studiere Architektur, Zeichnen und Bauen, jeden Tag kreativ."),
    L("Tim", "m", "Und ich studiere Wirtschaft, mit Mathe und BWL, jeden Tag."),
    L("Lukas", "m", "Cool, alle studieren! Studiert jemand von euch Psychologie?"),
    L("Lisa", "f", "Psychologie? Nein, nur Jura bei mir, wirklich."),
    L("Tom", "m", "Biologie nicht, nur Informatik bei mir. Studiert jemand Pädagogik?"),
    L("Sara", "f", "Pädagogik nicht, nur Architektur bei mir. Studiert jemand Sprachen?"),
    L("Tim", "m", "Sprachen nicht, nur Wirtschaft bei mir. Treffen wir uns in der Mensa?"),
    L("Lukas", "m", "Ja, morgen um zwölf, einverstanden, oder?"),
    L("Lisa", "f", "Einverstanden! Bis morgen, tschüss!"),
    L("Tom", "m", "Bis dann! Viel Erfolg euch!"),
    L("Sara", "f", "Euch auch! Tschüss euch allen!"),
    L("Tim", "m", "Tschüss! Bis morgen alle zusammen!"),
    L("Lukas", "m", "Noch etwas: Skripte tauschen wir danach, okay?"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

print("batch C applied")
