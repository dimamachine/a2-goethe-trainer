#!/usr/bin/env python3
"""Rewrite T2 as direct speech, batch F2 (77-88). Verbose turns."""
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


# ---------------- TEST 77 bei-der-polizei ----------------
# Lukas(a Fahrrad-Anzeige) Lisa(h Unfall melden) Tom(b Brieftasche) Sara(f Nachbarn) Tim(d Pass)
apply(77, [
    L("Lukas", "m", "Also, Polizei gestern! Warum wart ihr da? Mir wurde das Fahrrad gestohlen, Anzeige gemacht."),
    L("Lisa", "f", "Oh! Ich musste einen Autounfall melden, klein, aber Pflicht, mit Fotos."),
    L("Tom", "m", "Ich habe eine Brieftasche gefunden und ehrlich abgegeben, mit viel Geld drin."),
    L("Sara", "f", "Ich habe mich über laute Nachbarn beschwert, wegen Ruhestörung nachts."),
    L("Tim", "m", "Und ich habe meinen Pass verloren, neu beantragen, vor dem Urlaub."),
    L("Lukas", "m", "Viel los alles! Meldet jemand einen Einbruch oder nicht?"),
    L("Lisa", "f", "Einbruch? Nein, nur Unfall bei mir, wirklich nur der."),
    L("Tom", "m", "Strafzettel zahlt keiner hier, oder? Ich bleibe bei Fund."),
    L("Sara", "f", "Strafzettel nicht, nur Beschwerde. Meldet jemand eine vermisste Person?"),
    L("Tim", "m", "Vermisst nicht, nur Pass bei mir. War jemand Zeuge eines Unfalls?"),
    L("Lukas", "m", "Zeuge nicht, nur Anzeige. Trinken wir Kaffee alle zusammen?"),
    L("Lisa", "f", "Ja, morgen um vier, im Café, einverstanden?"),
    L("Tom", "m", "Einverstanden! Bis morgen, alles Gute uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis morgen zusammen!"),
    L("Tim", "m", "Tschüss! Bis morgen alle zusammen, ohne Polizei!"),
    L("Lukas", "m", "Noch etwas: Aufeinander aufpassen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 78 in-der-tanzschule ----------------
# Lukas(c Salsa) Lisa(g Walzer) Tom(a HipHop) Sara(i Tango) Tim(e Discofox)
apply(78, [
    L("Lukas", "m", "Also, Tanzschule! Welchen Tanz lernt ihr? Ich lerne Salsa, heiße Rhythmen."),
    L("Lisa", "f", "Schön! Ich tanze Walzer, elegant und romantisch, mit meinem Mann."),
    L("Tom", "m", "Ich mache Hip-Hop, moderne Bewegungen, mit den Jüngeren."),
    L("Sara", "f", "Ich lerne Tango, seit Argentinien-Urlaub, begeistert."),
    L("Tim", "m", "Und ich mache Discofox, einfach, überall tanzbar, reicht mir."),
    L("Lukas", "m", "Bunt gemischt! Tanzt jemand Cha-Cha-Cha oder nicht?"),
    L("Lisa", "f", "Cha-Cha? Nein, nur Walzer bei mir, wirklich nur der."),
    L("Tom", "m", "Foxtrott mag keiner hier, oder? Ich bleibe bei Hip-Hop."),
    L("Sara", "f", "Foxtrott nicht, nur Tango. Tanzt jemand Ballett?"),
    L("Tim", "m", "Ballett nicht, nur Discofox bei mir. Tanzt jemand Breakdance?"),
    L("Lukas", "m", "Breakdance nicht, nur Salsa. Schauen wir Mittwoch alle zu?"),
    L("Lisa", "f", "Ja, Mittwoch um sieben, einverstanden? Mit Musik?"),
    L("Tom", "m", "Einverstanden! Bis Mittwoch, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Mittwoch zusammen!"),
    L("Tim", "m", "Tschüss! Bis Mittwoch alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Schuhe mitbringen, einverstanden? Glatte Sohle!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 79 beim-fotografen ----------------
# Lukas(c Bewerbung) Lisa(a Hochzeit) Tom(d Baby) Sara(h Passfoto) Tim(f Tierfotos)
apply(79, [
    L("Lukas", "m", "Also, Fotograf! Welche Fotos braucht ihr? Ich brauche ein Bewerbungsfoto, neue Stelle."),
    L("Lisa", "f", "Spannend! Ich mache Hochzeitsfotos, heirate im Juni, mit allem."),
    L("Tom", "m", "Ich lasse Babyfotos machen, erstes Kind da, so süß."),
    L("Sara", "f", "Ich brauche ein Passfoto, Reisepass läuft ab, dringend."),
    L("Tim", "m", "Und ich mache Tierfotos, schöne Bilder vom Hund, sitzt still."),
    L("Lukas", "m", "Viele Fotos alle! Macht jemand Urlaubsfotos oder nicht?"),
    L("Lisa", "f", "Urlaub selbst, nur Hochzeit beim Fotografen, wirklich nur die."),
    L("Tom", "m", "Naturfotos nicht mein Thema hier, oder? Ich bleibe bei Baby."),
    L("Sara", "f", "Natur nicht, nur Pass. Macht jemand Familienfotos?"),
    L("Tim", "m", "Familie später, nur Hund bei mir. Macht jemand Porträtfotos?"),
    L("Lukas", "m", "Porträt nicht, nur Bewerbung. Gehen wir nächste Woche alle?"),
    L("Lisa", "f", "Ja, Dienstag um zehn, einverstanden? Mit Kaffee danach?"),
    L("Tom", "m", "Einverstanden! Bis Dienstag, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Dienstag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Dienstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Gut anziehen, einverstanden? Beste Seite!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 80 im-schuhgeschaeft ----------------
# Lukas(f Laufschuhe) Lisa(e HighHeels) Tom(b Wanderschuhe) Sara(a Sandalen) Tim(h Arbeitsschuhe)
apply(80, [
    L("Lukas", "m", "Also, Schuhe kaufen! Was braucht jeder? Ich kaufe Laufschuhe, für Marathon-Training."),
    L("Lisa", "f", "Sportlich! Ich möchte High Heels, für eine Hochzeit, schick."),
    L("Tom", "m", "Ich brauche Wanderschuhe, für Bergtour im Sommer, fest."),
    L("Sara", "f", "Ich kaufe Sandalen, leicht für Strandurlaub, bequem."),
    L("Tim", "m", "Und ich brauche feste Arbeitsschuhe, für die Baustelle, Pflicht."),
    L("Lukas", "m", "Viele Schuhe alle! Kauft jemand Sneaker oder nicht?"),
    L("Lisa", "f", "Sneaker? Nein, nur Heels bei mir, wirklich nur die."),
    L("Tom", "m", "Winterstiefel braucht keiner jetzt hier, oder? Ich bleibe bei Wanderschuhen."),
    L("Sara", "f", "Winter nicht, nur Sandalen. Kauft jemand Hausschuhe?"),
    L("Tim", "m", "Hausschuhe nicht, nur Arbeit bei mir. Kauft jemand Gummistiefel?"),
    L("Lukas", "m", "Gummi nicht, nur Laufschuhe. Treffen wir uns Samstag alle?"),
    L("Lisa", "f", "Ja, Samstag um zehn, vorm Geschäft, einverstanden?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Samstag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Größenliste mitbringen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 81 in-der-volkshochschule ----------------
# Lukas(g Sprachkurs) Lisa(i Kochkurs) Tom(f Computer) Sara(h Malkurs) Tim(d Yoga)
apply(81, [
    L("Lukas", "m", "Also, Volkshochschule! Welche Kurse nehmt ihr? Ich nehme einen Sprachkurs, Spanisch."),
    L("Lisa", "f", "Toll! Ich nehme einen Kochkurs, italienisch kochen, lecker."),
    L("Tom", "m", "Ich nehme einen Computerkurs, Tabellen und Internet, nützlich."),
    L("Sara", "f", "Ich nehme einen Malkurs, Aquarell und Öl, kreativ."),
    L("Tim", "m", "Und ich nehme einen Yoga-Kurs, Entspannung am Abend, super."),
    L("Lukas", "m", "Fleißig alle! Nimmt jemand einen Gitarrenkurs oder nicht?"),
    L("Lisa", "f", "Gitarre? Nein, nur Kochen bei mir, wirklich nur das."),
    L("Tom", "m", "Fotokurs macht keiner hier, oder? Ich bleibe bei Computer."),
    L("Sara", "f", "Foto nicht, nur Malen. Nimmt jemand einen Tanzkurs?"),
    L("Tim", "m", "Tanzen nicht, nur Yoga bei mir. Nimmt jemand einen Nähkurs?"),
    L("Lukas", "m", "Nähen nicht, nur Sprache. Melden wir uns Montag alle an?"),
    L("Lisa", "f", "Ja, Montag um fünf, einverstanden? Mit Anmeldeformular?"),
    L("Tom", "m", "Einverstanden! Bis Montag, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Montag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Montag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Geld mitbringen, einverstanden? Kursgebühr!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 82 bei-der-autovermietung ----------------
# Lukas(h Kleinwagen) Lisa(f Transporter) Tom(b Cabrio) Sara(e Familienwagen) Tim(c Wohnmobil)
apply(82, [
    L("Lukas", "m", "Also, Mietwagen! Was nehmt ihr? Ich nehme einen Kleinwagen, billig und wendig."),
    L("Lisa", "f", "Praktisch! Ich nehme einen Transporter, für den Umzug am Wochenende."),
    L("Tom", "m", "Ich nehme ein Cabrio, offen fahren, im Sommer toll."),
    L("Sara", "f", "Ich nehme einen Familienwagen, viel Platz für Kinder und Gepäck."),
    L("Tim", "m", "Und ich nehme ein Wohnmobil, für zwei Wochen Urlaub, Freiheit."),
    L("Lukas", "m", "Gute Wagen alle! Nimmt jemand einen Bus oder nicht?"),
    L("Lisa", "f", "Bus? Nein, nur Transporter bei mir, wirklich nur der."),
    L("Tom", "m", "Motorrad mietet keiner hier, oder? Ich bleibe bei Cabrio."),
    L("Sara", "f", "Motorrad nicht, nur Familie. Nimmt jemand einen Sportwagen?"),
    L("Tim", "m", "Sport nicht, nur Mobil bei mir. Nimmt jemand ein Elektroauto?"),
    L("Lukas", "m", "Elektro nicht, nur Kleinwagen. Holen wir Freitag alles ab?"),
    L("Lisa", "f", "Ja, Freitag um acht, einverstanden? Mit Führerschein?"),
    L("Tom", "m", "Einverstanden! Bis Freitag, gute Fahrt uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Freitag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Freitag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Volltanken nicht vergessen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 83 beim-hautarzt ----------------
# Lukas(g Pickel) Lisa(a Ausschlag) Tom(h Muttermal) Sara(f Haut) Tim(i Sonnenbrand)
apply(83, [
    L("Lukas", "m", "Also, Hautarzt! Was habt ihr? Bei mir Pickel, seit Wochen, nervig."),
    L("Lisa", "f", "Oh! Bei mir Ausschlag, Allergie wohl, juckt sehr."),
    L("Tom", "m", "Bei mir Muttermal-Kontrolle, einmal im Jahr, Routine."),
    L("Sara", "f", "Bei mir trockene Haut, besonders im Winter, creme viel."),
    L("Tim", "m", "Und bei mir Sonnenbrand, vom Strand, rot und heiß."),
    L("Lukas", "m", "Gute Besserung alle! Hat jemand einen Insektenstich oder nicht?"),
    L("Lisa", "f", "Stich? Nein, nur Ausschlag bei mir, wirklich nur der."),
    L("Tom", "m", "Warzen hat keiner hier, oder? Ich bleibe bei Kontrolle."),
    L("Sara", "f", "Warzen nicht, nur Haut. Hat jemand Haarausfall?"),
    L("Tim", "m", "Haare okay, nur Brand bei mir. Hat jemand Nagelpilz?"),
    L("Lukas", "m", "Pilz nicht, nur Pickel. Warten wir zusammen alle?"),
    L("Lisa", "f", "Ja, hier im Wartezimmer, einverstanden? Mit Zeitschriften?"),
    L("Tom", "m", "Einverstanden! Bis gleich, gute Besserung uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis gleich zusammen!"),
    L("Tim", "m", "Tschüss! Bis gleich alle zusammen, Daumen drücken!"),
    L("Lukas", "m", "Noch etwas: Nicht kratzen, einverstanden? Wirklich nicht!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 84 in-der-tourist-information ----------------
# Lukas(f Führung) Lisa(d Museum) Tom(b Boot) Sara(e Turm) Tim(g Markt)
apply(84, [
    L("Lukas", "m", "Also, Touristen-Programm! Was macht ihr? Ich mache eine Stadtführung, zu Fuß."),
    L("Lisa", "f", "Schön! Ich gehe ins Museum, Kunst und Geschichte, den ganzen Tag."),
    L("Tom", "m", "Ich mache eine Bootsfahrt, auf dem Fluss, eine Stunde."),
    L("Sara", "f", "Ich steige auf den Aussichtsturm, tolle Sicht über die Stadt."),
    L("Tim", "m", "Und ich gehe auf den Markt, essen und schauen, lecker."),
    L("Lukas", "m", "Tolles Programm alle! Geht jemand in den Park oder nicht?"),
    L("Lisa", "f", "Park? Nein, nur Museum bei mir, wirklich nur das."),
    L("Tom", "m", "Zoo besucht keiner hier, oder? Ich bleibe beim Boot."),
    L("Sara", "f", "Zoo nicht, nur Turm. Geht jemand ins Theater?"),
    L("Tim", "m", "Theater nicht, nur Markt bei mir. Geht jemand shoppen?"),
    L("Lukas", "m", "Shopping später, erst Führung. Treffen wir uns um sechs alle?"),
    L("Lisa", "f", "Ja, um sechs am Brunnen, einverstanden? Mit Fotos?"),
    L("Tom", "m", "Einverstanden! Bis dann, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis später zusammen!"),
    L("Tim", "m", "Tschüss! Bis später alle zusammen, viel Spaß!"),
    L("Lukas", "m", "Noch etwas: Stadtplan mitnehmen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 85 in-der-musikschule ----------------
# Lukas(e Gitarre) Lisa(i Klavier) Tom(b Schlagzeug) Sara(d Geige) Tim(g Trompete)
apply(85, [
    L("Lukas", "m", "Also, Musikschule! Was lernt ihr? Ich lerne Gitarre, seit einem Jahr."),
    L("Lisa", "f", "Schön! Ich lerne Klavier, klassisch, jeden Tag üben."),
    L("Tom", "m", "Ich lerne Schlagzeug, laut und cool, mit Band."),
    L("Sara", "f", "Ich lerne Geige, im Orchester, wunderschön."),
    L("Tim", "m", "Und ich lerne Trompete, Jazz und Blasmusik, toll."),
    L("Lukas", "m", "Musikalisch alle! Lernt jemand Saxophon oder nicht?"),
    L("Lisa", "f", "Saxophon? Nein, nur Klavier bei mir, wirklich nur das."),
    L("Tom", "m", "Gesang nimmt keiner hier, oder? Ich bleibe bei Trommeln."),
    L("Sara", "f", "Gesang nicht, nur Geige. Lernt jemand Flöte?"),
    L("Tim", "m", "Flöte nicht, nur Trompete bei mir. Lernt jemand Cello?"),
    L("Lukas", "m", "Cello nicht, nur Gitarre. Spielen wir zusammen alle?"),
    L("Lisa", "f", "Ja, Freitag im Saal, einverstanden? Mit Noten?"),
    L("Tom", "m", "Einverstanden! Bis Freitag, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Freitag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Freitag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Instrumente stimmen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 86 beim-physiotherapeuten ----------------
# Lukas(e Rücken) Lisa(c Knie) Tom(i Schulter) Sara(f Nacken) Tim(g Fuß)
apply(86, [
    L("Lukas", "m", "Also, Physio! Was tut weh? Bei mir Rückenschmerzen, vom Sitzen im Büro."),
    L("Lisa", "f", "Oh! Bei mir verletztes Knie, vom Sport, seit letzter Woche."),
    L("Tom", "m", "Bei mir Schulterschmerzen, rechts, nach dem Umzug."),
    L("Sara", "f", "Bei mir steifer Nacken, morgens schlimm, vom Kissen wohl."),
    L("Tim", "m", "Und bei mir verstauchter Fuß, umgeknickt beim Laufen."),
    L("Lukas", "m", "Gute Besserung alle! Hat jemand Handgelenk-Probleme oder nicht?"),
    L("Lisa", "f", "Handgelenk? Nein, nur Knie bei mir, wirklich nur das."),
    L("Tom", "m", "Hüfte tut keinem weh hier, oder? Ich bleibe bei Schulter."),
    L("Sara", "f", "Hüfte nicht, nur Nacken. Hat jemand Kopfschmerzen?"),
    L("Tim", "m", "Kopf okay, nur Fuß bei mir. Hat jemand Ellbogenschmerzen?"),
    L("Lukas", "m", "Ellbogen nicht, nur Rücken. Machen wir Übungen alle zusammen?"),
    L("Lisa", "f", "Ja, jeden Morgen, einverstanden? Zehn Minuten?"),
    L("Tom", "m", "Einverstanden! Bis morgen, gute Besserung uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis morgen zusammen!"),
    L("Tim", "m", "Tschüss! Bis morgen alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Termine einhalten, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 87 im-spielzeugladen ----------------
# Lukas(c Eisenbahn) Lisa(d Puppe) Tom(a Baukasten) Sara(i Brettspiel) Tim(f Kuscheltier)
apply(87, [
    L("Lukas", "m", "Also, Spielzeug kaufen! Was nehmt ihr? Ich nehme eine Eisenbahn, mit Schienen."),
    L("Lisa", "f", "Schön! Ich nehme eine Puppe, mit Kleidern, für meine Nichte."),
    L("Tom", "m", "Ich nehme einen Baukasten, zum Bauen, für meinen Sohn."),
    L("Sara", "f", "Ich nehme ein Brettspiel, für Familienabende, lustig."),
    L("Tim", "m", "Und ich nehme ein Kuscheltier, weich und groß, zum Liebhaben."),
    L("Lukas", "m", "Tolle Geschenke alle! Nimmt jemand ein Auto oder nicht?"),
    L("Lisa", "f", "Auto? Nein, nur Puppe bei mir, wirklich nur die."),
    L("Tom", "m", "Fahrrad schenkt keiner hier, oder? Ich bleibe bei Kasten."),
    L("Sara", "f", "Fahrrad nicht, nur Spiel. Nimmt jemand einen Ball?"),
    L("Tim", "m", "Ball nicht, nur Kuscheltier bei mir. Nimmt jemand ein Puzzle?"),
    L("Lukas", "m", "Puzzle nicht, nur Bahn. Packen wir ein alle zusammen?"),
    L("Lisa", "f", "Ja, an der Kasse, einverstanden? Mit Geschenkpapier?"),
    L("Tom", "m", "Einverstanden! Bis dann, viel Freude uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis bald zusammen!"),
    L("Tim", "m", "Tschüss! Bis bald alle zusammen, viel Spaß!"),
    L("Lukas", "m", "Noch etwas: Kassenbon aufheben, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 88 online-shopping-und-ruecksendung ----------------
# Lukas(h Kleidung) Lisa(f Bücher) Tom(c Elektronik) Sara(e Möbel) Tim(a Lebensmittel)
apply(88, [
    L("Lukas", "m", "Also, online bestellt! Was habt ihr gekauft? Ich habe Kleidung gekauft, Jacke und Hose."),
    L("Lisa", "f", "Schön! Ich habe Bücher gekauft, drei Romane, spannend."),
    L("Tom", "m", "Ich habe Elektronik gekauft, Kopfhörer, kabellos."),
    L("Sara", "f", "Ich habe Möbel gekauft, Regal und Stuhl, fürs Zimmer."),
    L("Tim", "m", "Und ich habe Lebensmittel gekauft, alles frisch, geliefert."),
    L("Lukas", "m", "Viel bestellt alle! Hat jemand Medikamente bestellt oder nicht?"),
    L("Lisa", "f", "Medikamente? Nein, nur Bücher bei mir, wirklich nur die."),
    L("Tom", "m", "Spielzeug bestellt keiner hier, oder? Ich bleibe bei Technik."),
    L("Sara", "f", "Spielzeug nicht, nur Möbel. Hat jemand Schuhe bestellt?"),
    L("Tim", "m", "Schuhe nicht, nur Essen bei mir. Hat jemand Werkzeug bestellt?"),
    L("Lukas", "m", "Werkzeug nicht, nur Kleidung. Schicken wir was zurück alle?"),
    L("Lisa", "f", "Ja, meins passt nicht, einverstanden? Morgen zur Post?"),
    L("Tom", "m", "Einverstanden! Bis morgen, viel Glück uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis morgen zusammen!"),
    L("Tim", "m", "Tschüss! Bis morgen alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Retoure anmelden, einverstanden? Online!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

print("batch F2 applied")
