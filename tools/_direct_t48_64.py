#!/usr/bin/env python3
"""Rewrite T2 as direct speech, batch E (48-64). Verbose turns."""
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


# ---------------- TEST 48 im-supermarkt ----------------
# Lukas(f Fleisch) Lisa(b Getränke) Tom(i Brot) Sara(g Gemüse) Tim(e Nachtisch)
apply(48, [
    L("Lukas", "m", "Also, Grillparty am Samstag! Was bringt jeder mit? Ich bringe Fleisch mit, Würstchen und Steaks."),
    L("Lisa", "f", "Super! Ich bringe Getränke mit, Wasser, Saft und Limonade, zwei Kästen."),
    L("Tom", "m", "Ich bringe Brot und Brötchen mit, frisch vom Bäcker, noch warm."),
    L("Sara", "f", "Ich bringe Gemüse für Salat mit, Tomaten, Gurken und Paprika."),
    L("Tim", "m", "Und ich bringe den Nachtisch mit, Eis und Kuchen, lecker."),
    L("Lukas", "m", "Perfekt, alles dabei! Bringt jemand Fisch mit oder nicht?"),
    L("Lisa", "f", "Fisch? Nein, nur Getränke bei mir, wirklich nur die."),
    L("Tom", "m", "Chips und Snacks bringt keiner mit, oder? Ich habe nur Brot dabei."),
    L("Sara", "f", "Chips nicht, nur Gemüse. Bringt jemand Käse mit?"),
    L("Tim", "m", "Käse nicht, nur Nachtisch bei mir. Bringt jemand Wein mit?"),
    L("Lukas", "m", "Wein nicht, nur Fleisch. Treffen wir uns um fünf im Garten?"),
    L("Lisa", "f", "Ja, um fünf bei mir, einverstanden? Mit Hunger?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Teller mitbringen, einverstanden? Jeder seine!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 49 im-theater ----------------
# Lukas(e Romeo&Julia) Lisa(b Cats) Tom(d Comedy) Sara(h Oper) Tim(g Ballett)
apply(49, [
    L("Lukas", "m", "Also, Theater im Mai! Was schaut ihr? Ich sehe Romeo und Julia, mit der Klasse."),
    L("Lisa", "f", "Schön! Ich sehe das Musical Cats, mit tollen Kostümen und Musik."),
    L("Tom", "m", "Ich sehe ein Comedy-Stück, zum Lachen, mit Freunden zusammen."),
    L("Sara", "f", "Ich sehe die Oper Don Giovanni, klassisch und groß, mit meiner Mutter."),
    L("Tim", "m", "Und ich sehe Ballett Schwanensee, wunderschön getanzt, freue mich."),
    L("Lukas", "m", "Bunt gemischt! Schaut jemand Faust oder nicht?"),
    L("Lisa", "f", "Faust? Nein, nur Cats bei mir, wirklich nur das."),
    L("Tom", "m", "Kinderstück schaut keiner hier, oder? Ich bleibe bei Comedy."),
    L("Sara", "f", "Kinderstück nicht, nur Oper. Geht jemand ins Kabarett?"),
    L("Tim", "m", "Kabarett nicht, nur Ballett bei mir. Geht jemand ins Krimi-Theater?"),
    L("Lukas", "m", "Krimi nicht, nur Romeo. Erzählen wir uns danach alles?"),
    L("Lisa", "f", "Ja, nächste Woche im Café, einverstanden? Mit Kuchen?"),
    L("Tom", "m", "Einverstanden! Bis dann, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Bis nächste Woche alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Karten nicht verlieren, einverstanden? Gut aufpassen!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 50 beim-tierarzt ----------------
# Lukas(e Hund) Lisa(i Katze) Tom(a Hamster) Sara(g Fische) Tim(b Papagei)
apply(50, [
    L("Lukas", "m", "Also, Haustiere! Welche habt ihr? Ich habe einen Hund, einen Labrador, sehr lieb."),
    L("Lisa", "f", "Süß! Ich habe eine Katze, grau getigert, schläft den ganzen Tag."),
    L("Tom", "m", "Ich habe einen Hamster, klein und schnell, im Käfig mit Rad."),
    L("Sara", "f", "Ich habe Fische, ein großes Aquarium, bunt und ruhig."),
    L("Tim", "m", "Und ich habe einen Papagei, er spricht schon Hallo und Tschüss."),
    L("Lukas", "m", "Tolle Tiere alle! Hat jemand ein Pferd oder nicht?"),
    L("Lisa", "f", "Pferd? Nein, nur Katze bei mir, wirklich nur die."),
    L("Tom", "m", "Schildkröte hat keiner hier, oder? Ich bleibe beim Hamster."),
    L("Sara", "f", "Schildkröte nicht, nur Fische. Hat jemand ein Kaninchen?"),
    L("Tim", "m", "Kaninchen nicht, nur Papagei bei mir. Hat jemand eine Schlange?"),
    L("Lukas", "m", "Schlange nicht, nur Hund. Treffen wir uns im Park mit Tieren?"),
    L("Lisa", "f", "Ja, Sonntag um elf, einverstanden? Mit Leine?"),
    L("Tom", "m", "Einverstanden! Bis Sonntag, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Bis Sonntag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Leckerlis mitbringen, einverstanden? Für alle Tiere!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 51 beim-augenarzt ----------------
# Lukas(e normal) Lisa(g Linsen) Tom(c Lesebrille) Sara(i Sonne) Tim(h OP)
apply(51, [
    L("Lukas", "m", "Also, Augen! Wer braucht was? Ich brauche eine normale Brille, seit letztem Jahr."),
    L("Lisa", "f", "Ich trage Kontaktlinsen, jeden Tag, sehr praktisch beim Sport."),
    L("Tom", "m", "Ich brauche eine Lesebrille, nur zum Lesen, abends am Sofa."),
    L("Sara", "f", "Ich habe eine Sonnenbrille mit Sehstärke, für Sommer und Winter."),
    L("Tim", "m", "Und ich brauche eine Augen-Operation, nächsten Monat, Laser."),
    L("Lukas", "m", "Alles klar! Braucht jemand gar keine Sehhilfe oder nicht?"),
    L("Lisa", "f", "Ohne? Nein, nur Linsen bei mir, wirklich nur die."),
    L("Tom", "m", "Sportbrille braucht keiner hier, oder? Ich bleibe bei Lesebrille."),
    L("Sara", "f", "Sportbrille nicht, nur Sonne. Braucht jemand eine Bifokal-Brille?"),
    L("Tim", "m", "Bifokal nicht, nur OP bei mir. Braucht jemand eine Computer-Brille?"),
    L("Lukas", "m", "Computer nicht, nur normal. Gehen wir zusammen zum Optiker?"),
    L("Lisa", "f", "Ja, Freitag um vier, einverstanden? In der Stadt?"),
    L("Tom", "m", "Einverstanden! Bis Freitag, gute Sicht uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Freitag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Freitag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Brillenputztücher mitbringen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 52 im-schwimmbad-und-sauna ----------------
# Lukas(i Sauna) Lisa(e Bahnen) Tom(f Rutsche) Sara(a Turm) Tim(b Whirlpool)
apply(52, [
    L("Lukas", "m", "Also, Schwimmbad morgen! Was macht jeder? Ich gehe in die Sauna, heiß und gut."),
    L("Lisa", "f", "Schön! Ich schwimme Bahnen, zwanzig Stück, Ausdauer pur."),
    L("Tom", "m", "Ich gehe auf die Wasserrutsche, immer wieder, juhu!"),
    L("Sara", "f", "Ich springe vom Turm, vom Dreier, mutig und toll."),
    L("Tim", "m", "Und ich gehe in den Whirlpool, warm und gemütlich, herrlich."),
    L("Lukas", "m", "Super, alle im Wasser! Macht jemand Aqua-Fitness oder nicht?"),
    L("Lisa", "f", "Aqua? Nein, nur Bahnen bei mir, wirklich nur die."),
    L("Tom", "m", "Massage bucht keiner hier, oder? Ich bleibe bei Rutsche."),
    L("Sara", "f", "Massage nicht, nur Turm. Geht jemand ins Kinderbecken?"),
    L("Tim", "m", "Kinderbecken nicht, nur Whirlpool bei mir. Geht jemand ins Dampfbad?"),
    L("Lukas", "m", "Dampfbad nicht, nur Sauna. Treffen wir uns um zehn dort?"),
    L("Lisa", "f", "Ja, um zehn am Eingang, einverstanden? Mit Badesachen?"),
    L("Tom", "m", "Einverstanden! Bis morgen, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Bis morgen alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Handtücher nicht vergessen, einverstanden? Zwei Stück!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 53 familienfeier-und-hochzeit ----------------
# Lukas(b DJ) Lisa(e Blumen) Tom(h Fotos) Sara(a Torte) Tim(f Rede)
apply(53, [
    L("Lukas", "m", "Also, Hochzeit im Juni! Wer macht was? Ich mache Musik als DJ, den ganzen Abend."),
    L("Lisa", "f", "Schön! Ich bringe Blumen, weiße Rosen, für die Tische."),
    L("Tom", "m", "Ich mache die Fotos, mit guter Kamera, den ganzen Tag."),
    L("Sara", "f", "Ich backe die Torte, drei Stockwerke, mit Erdbeeren."),
    L("Tim", "m", "Und ich halte die Rede, lustig und kurz, versprochen."),
    L("Lukas", "m", "Perfekt, alles verteilt! Schreibt jemand Einladungen oder nicht?"),
    L("Lisa", "f", "Einladungen? Nein, nur Blumen bei mir, wirklich nur die."),
    L("Tom", "m", "Auto schmückt keiner hier, oder? Ich bleibe bei Fotos."),
    L("Sara", "f", "Auto nicht, nur Torte. Organisiert jemand Spiele?"),
    L("Tim", "m", "Spiele nicht, nur Rede bei mir. Zieht jemand besondere Kleidung an?"),
    L("Lukas", "m", "Kleidung? Alle schick, klar! Treffen wir uns Freitag zur Probe?"),
    L("Lisa", "f", "Ja, Freitag um sechs, in der Halle, einverstanden?"),
    L("Tom", "m", "Einverstanden! Bis Freitag, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Bis Freitag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Gute Laune mitbringen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 54 beim-optiker ----------------
# Lukas(f Hornbrille) Lisa(e randlos) Tom(a rund) Sara(b rot) Tim(g Pilot)
apply(54, [
    L("Lukas", "m", "Also, neue Brillen! Welche nehmt ihr? Ich nehme die schwarze Hornbrille, klassisch."),
    L("Lisa", "f", "Schön! Ich nehme die randlose Brille, leicht und modern."),
    L("Tom", "m", "Ich nehme die runde Brille, steht mir gut, finde ich."),
    L("Sara", "f", "Ich nehme die rote farbige Brille, mutig und lustig."),
    L("Tim", "m", "Und ich nehme die Pilotenbrille, cool und groß, super."),
    L("Lukas", "m", "Schicke Brillen alle! Nimmt jemand eine Sportbrille oder nicht?"),
    L("Lisa", "f", "Sportbrille? Nein, nur randlos bei mir, wirklich nur die."),
    L("Tom", "m", "Lesebrille braucht keiner hier, oder? Ich bleibe bei rund."),
    L("Sara", "f", "Lesebrille nicht, nur rot. Nimmt jemand eine Bifokal-Brille?"),
    L("Tim", "m", "Bifokal nicht, nur Pilot bei mir. Nimmt jemand eine goldene Brille?"),
    L("Lukas", "m", "Gold nicht, nur Horn. Zeigen wir sie uns Freitag?"),
    L("Lisa", "f", "Ja, Freitag im Café, einverstanden? Um vier Uhr?"),
    L("Tom", "m", "Einverstanden! Bis Freitag, gute Sicht uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Freitag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Freitag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Etuis nicht vergessen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 55 beim-fussball ----------------
# Lukas(i Bayern) Lisa(a Dortmund) Tom(e Schalke) Sara(g HSV) Tim(b Bremen)
apply(55, [
    L("Lukas", "m", "Also, Fußball! Für wen seid ihr? Ich bin für Bayern München, schon immer."),
    L("Lisa", "f", "Ich bin für Dortmund, mit toller Stimmung im Stadion."),
    L("Tom", "m", "Ich bin für Schalke 04, aus Tradition, seit Kindheit."),
    L("Sara", "f", "Ich bin für Hamburger SV, meine Stadt, mein Verein."),
    L("Tim", "m", "Und ich bin für Werder Bremen, grün-weiß, für immer."),
    L("Lukas", "m", "Starke Vereine alle! Ist jemand für Hertha Berlin oder nicht?"),
    L("Lisa", "f", "Hertha? Nein, nur Dortmund bei mir, wirklich nur die."),
    L("Tom", "m", "Köln mag keiner hier, oder? Ich bleibe bei Schalke."),
    L("Sara", "f", "Köln nicht, nur HSV. Ist jemand für RB Leipzig?"),
    L("Tim", "m", "Leipzig nicht, nur Bremen bei mir. Ist jemand für Frankfurt?"),
    L("Lukas", "m", "Frankfurt nicht, nur Bayern. Schauen wir Samstag zusammen?"),
    L("Lisa", "f", "Ja, Samstag um drei, bei mir, einverstanden?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Samstag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Chips mitbringen, einverstanden? Jeder eine Tüte!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 56 beim-baecker ----------------
# Lukas(g Brezeln) Lisa(f Croissants) Tom(a Vollkornbrot) Sara(b Käsekuchen) Tim(e Berliner)
apply(56, [
    L("Lukas", "m", "Also, Frühstück beim Bäcker! Was nehmt ihr? Ich nehme Brezeln, zwei Stück."),
    L("Lisa", "f", "Lecker! Ich nehme Croissants, butterweich und warm."),
    L("Tom", "m", "Ich nehme Vollkornbrot, gesund und lecker, ein ganzes."),
    L("Sara", "f", "Ich nehme Käsekuchen, ein Stück, zum Kaffee."),
    L("Tim", "m", "Und ich nehme Berliner, mit Marmelade, zwei Stück."),
    L("Lukas", "m", "Guten Appetit alle! Nimmt jemand Schwarzbrot oder nicht?"),
    L("Lisa", "f", "Schwarzbrot? Nein, nur Croissants bei mir, wirklich nur die."),
    L("Tom", "m", "Apfelstrudel will keiner hier, oder? Ich bleibe bei Brot."),
    L("Sara", "f", "Strudel nicht, nur Kuchen. Nimmt jemand Donuts?"),
    L("Tim", "m", "Donuts nicht, nur Berliner bei mir. Nimmt jemand Brötchen?"),
    L("Lukas", "m", "Brötchen nicht, nur Brezeln. Schmeckt es allen?"),
    L("Lisa", "f", "Ja, sehr lecker! Noch Kaffee dazu, einverstanden?"),
    L("Tom", "m", "Einverstanden! Guten Appetit weiterhin, ihr Lieben!"),
    L("Sara", "f", "Euch auch! Tschüss, bis morgen zusammen!"),
    L("Tim", "m", "Tschüss! Bis morgen alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Morgen wieder hier, einverstanden? Gleiche Zeit!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 57 wohnungssuche-und-makler ----------------
# Lukas(d WG) Lisa(f 1-Zimmer) Tom(b Familienwohnung) Sara(i Maisonette) Tim(c Hauskauf)
apply(57, [
    L("Lukas", "m", "Also, Wohnungssuche! Was sucht ihr? Ich suche ein WG-Zimmer, zentral und billig."),
    L("Lisa", "f", "Ich suche eine Ein-Zimmer-Wohnung, klein aber mein, ruhig."),
    L("Tom", "m", "Ich suche eine Familie-Wohnung mit Garten, für uns fünf."),
    L("Sara", "f", "Ich suche eine Maisonette mit Dachterrasse, hell und modern."),
    L("Tim", "m", "Und ich suche ein Haus zum Kaufen, mit Garten, für immer."),
    L("Lukas", "m", "Schwierig alles! Sucht jemand ein Bauernhaus oder nicht?"),
    L("Lisa", "f", "Bauernhaus? Nein, nur Wohnung bei mir, wirklich nur die."),
    L("Tom", "m", "Studio sucht keiner hier, oder? Ich bleibe bei Familie."),
    L("Sara", "f", "Studio nicht, nur Maisonette. Sucht jemand ein Penthouse?"),
    L("Tim", "m", "Penthouse nicht, nur Haus bei mir. Sucht jemand ein Loft?"),
    L("Lukas", "m", "Loft nicht, nur WG. Tauschen wir Anzeigen aus alle?"),
    L("Lisa", "f", "Ja, schickt alles in die Gruppe, einverstanden?"),
    L("Tom", "m", "Einverstanden! Viel Glück uns allen zusammen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis bald zusammen!"),
    L("Tim", "m", "Tschüss! Bis bald alle zusammen, viel Glück!"),
    L("Lukas", "m", "Noch etwas: Makler anrufen, einverstanden? Morgen früh!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 58 beim-friseur-und-beauty ----------------
# Lukas(d Rasieren) Lisa(g Maniküre) Tom(a Massage) Sara(e Gesicht) Tim(f Pediküre)
apply(58, [
    L("Lukas", "m", "Also, Beauty-Wochenende! Was macht jeder? Ich lasse mich rasieren, klassisch mit Klinge."),
    L("Lisa", "f", "Schön! Ich mache Maniküre, wöchentlich, sehr gepflegte Hände."),
    L("Tom", "m", "Ich gehe zur Massage, Rücken vom Büro, jede Woche eine Stunde."),
    L("Sara", "f", "Ich mache eine Gesichtsbehandlung, Haut-Pflege, jeden Monat."),
    L("Tim", "m", "Und ich lasse Pediküre machen, als Sportler wichtig, gepflegte Füße."),
    L("Lukas", "m", "Entspannt alle! Färbt jemand die Haare oder nicht?"),
    L("Lisa", "f", "Färben? Nein, nur Maniküre bei mir, wirklich nur die."),
    L("Tom", "m", "Wimpern lässt keiner hier, oder? Ich bleibe bei Massage."),
    L("Sara", "f", "Wimpern nicht, nur Gesicht. Zupft jemand Augenbrauen?"),
    L("Tim", "m", "Augenbrauen nicht, nur Pediküre bei mir. Geht jemand ins Solarium?"),
    L("Lukas", "m", "Solarium nicht, ungesund. Treffen wir uns danach alle?"),
    L("Lisa", "f", "Ja, um fünf im Café, einverstanden? Mit Kuchen?"),
    L("Tom", "m", "Einverstanden! Bis dann, erholt euch gut alle!"),
    L("Sara", "f", "Euch auch! Tschüss, bis später zusammen!"),
    L("Tim", "m", "Tschüss! Bis später alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Vorher-nachher-Fotos, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 59 beim-friseur-maenner (all m) ----------------
# Lukas(h Glatze) Lars(b Iro) Tom(d Mittelscheitel) Sven(c Dutt) Tim(i Undercut)
apply(59, [
    L("Lukas", "m", "Also, neue Frisuren überall! Wer hat was? Ich habe eine Glatze, selbst rasiert."),
    L("Lars", "m", "Mutig! Ich habe einen Iro, auffällig und hoch, Mohawk."),
    L("Tom", "m", "Ich habe einen Mittelscheitel, klassisch, mit langen Haaren."),
    L("Sven", "m", "Ich habe einen Dutt, Haare zusammen, sportlich und modisch."),
    L("Tim", "m", "Und ich habe einen Undercut, kurz an den Seiten, oben länger."),
    L("Lukas", "m", "Coole Schnitte alle! Hat jemand einen Pferdeschwanz oder nicht?"),
    L("Lars", "m", "Pferdeschwanz? Nein, nur Iro bei mir, wirklich nur der."),
    L("Tom", "m", "Dreadlocks hat keiner hier, oder? Ich bleibe bei Scheitel."),
    L("Sven", "m", "Dreadlocks nicht, nur Dutt. Hat jemand Locken?"),
    L("Tim", "m", "Locken nicht, nur Undercut bei mir. Hat jemand Bürstenschnitt?"),
    L("Lukas", "m", "Bürste nicht, nur Glatze. Zeigen wir sie Freitag alle?"),
    L("Lars", "m", "Ja, Freitag in der Stadt, einverstanden? Um sieben?"),
    L("Tom", "m", "Einverstanden! Bis Freitag, viel Spaß uns allen!"),
    L("Sven", "m", "Euch auch! Tschüss, bis Freitag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Freitag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Fotos machen, einverstanden? Alle zusammen!"),
], check_order=["Lukas", "Lars", "Tom", "Sven", "Tim"])

# ---------------- TEST 60 im-park-und-erholung ----------------
# Lukas(c Joggen) Lisa(b Fahrrad) Tom(h Bank lesen) Sara(d Picknick) Tim(g Fußball)
apply(60, [
    L("Lukas", "m", "Also, Park heute! Was macht jeder? Ich gehe joggen, zehn Kilometer jeden Tag."),
    L("Lisa", "f", "Sportlich! Ich fahre Fahrrad, entspannt, mit der Familie."),
    L("Tom", "m", "Ich lese auf einer Bank, Bücher, ruhig unter Bäumen."),
    L("Sara", "f", "Ich mache Picknick mit Freundinnen, Decke, Essen, Getränke."),
    L("Tim", "m", "Und ich spiele Fußball, mit anderen Jungs, jeden Sonntag."),
    L("Lukas", "m", "Schön draußen alle! Macht jemand Tai Chi oder nicht?"),
    L("Lisa", "f", "Tai Chi? Nein, nur Fahrrad bei mir, wirklich nur das."),
    L("Tom", "m", "Hund hat keiner dabei hier, oder? Ich bleibe beim Lesen."),
    L("Sara", "f", "Hund nicht, nur Picknick. Spielt jemand Frisbee?"),
    L("Tim", "m", "Frisbee nicht, nur Fußball bei mir. Geht jemand spazieren?"),
    L("Lukas", "m", "Spazieren auch schön, aber ich jogge. Treffen wir uns um vier?"),
    L("Lisa", "f", "Ja, um vier am Brunnen, einverstanden? Mit Decke?"),
    L("Tom", "m", "Einverstanden! Bis dann, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis später zusammen!"),
    L("Tim", "m", "Tschüss! Bis später alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Wetter prüfen, einverstanden? Hoffentlich Sonne!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 61 im-fitnessstudio ----------------
# Lukas(g Kraft) Lisa(f Spinning) Tom(h Yoga) Sara(d Schwimmen) Tim(i Boxen)
apply(61, [
    L("Lukas", "m", "Also, Fitnessstudio! Was macht jeder? Ich mache Krafttraining, schwere Gewichte."),
    L("Lisa", "f", "Stark! Ich gehe zum Spinning, schnelles Rad mit Musik."),
    L("Tom", "m", "Ich mache Yoga, Entspannung gegen Stress im Büro."),
    L("Sara", "f", "Ich schwimme, jeden Morgen Bahnen, im Becken."),
    L("Tim", "m", "Und ich boxe, zweimal die Woche, sehr anstrengend."),
    L("Lukas", "m", "Sportlich alle! Macht jemand Pilates oder nicht?"),
    L("Lisa", "f", "Pilates? Nein, nur Spinning bei mir, wirklich nur das."),
    L("Tom", "m", "Zumba macht keiner hier, oder? Ich bleibe bei Yoga."),
    L("Sara", "f", "Zumba nicht, nur Schwimmen. Klettert jemand hier?"),
    L("Tim", "m", "Klettern nicht, nur Boxen bei mir. Läuft jemand auf dem Laufband?"),
    L("Lukas", "m", "Laufband nicht, nur Gewichte. Trainieren wir Montag alle?"),
    L("Lisa", "f", "Ja, Montag um sechs, einverstanden? Mit Handtuch?"),
    L("Tom", "m", "Einverstanden! Bis Montag, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Montag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Montag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Wasser mitbringen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 62 auf-dem-wochenmarkt ----------------
# Lukas(g Fisch) Lisa(e Blumen) Tom(c Käse) Sara(a Obst) Tim(h Honig)
apply(62, [
    L("Lukas", "m", "Also, Wochenmarkt Samstag! Was kauft jeder? Ich kaufe Fisch, frisch vom Kutter."),
    L("Lisa", "f", "Lecker! Ich nehme Blumen mit, jeden Samstag einen Strauß."),
    L("Tom", "m", "Ich liebe Käse, probiere Sorten, immer verschiedene."),
    L("Sara", "f", "Ich kaufe Obst, Beeren und Äpfel, direkt vom Bauern."),
    L("Tim", "m", "Und ich hole Honig, vom Imker, immer ein großes Glas."),
    L("Lukas", "m", "Frisch alles! Kauft jemand Eier oder nicht?"),
    L("Lisa", "f", "Eier? Nein, nur Blumen bei mir, wirklich nur die."),
    L("Tom", "m", "Fleisch kauft keiner hier, oder? Ich bleibe bei Käse."),
    L("Sara", "f", "Fleisch nicht, nur Obst. Kauft jemand Gemüse?"),
    L("Tim", "m", "Gemüse nicht, nur Honig bei mir. Kauft jemand Brot?"),
    L("Lukas", "m", "Brot nicht, nur Fisch. Gehen wir zusammen hin alle?"),
    L("Lisa", "f", "Ja, um neun am Eingang, einverstanden? Mit Korb?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Samstag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Bargeld mitbringen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 63 in-der-autowerkstatt ----------------
# Lukas(g Batterie) Lisa(c Reifen) Tom(f Bremse) Sara(e Öl) Tim(i Klima)
apply(63, [
    L("Lukas", "m", "Also, Autoprobleme! Was ist los bei euch? Bei mir ist die Batterie leer, morgens geht nichts."),
    L("Lisa", "f", "Oh nein! Ich habe einen platten Reifen, seit gestern, Nagel drin."),
    L("Tom", "m", "Bei mir funktioniert die Bremse nicht richtig, gefährlich, Werkstatt sofort."),
    L("Sara", "f", "Mein Auto verliert Öl, Fleck unterm Wagen, jeden Morgen."),
    L("Tim", "m", "Und bei mir ist die Klimaanlage kaputt, heiß im Sommer, schrecklich."),
    L("Lukas", "m", "Viel kaputt alles! Ist der Scheibenwischer kaputt bei jemandem oder nicht?"),
    L("Lisa", "f", "Wischer? Nein, nur Reifen bei mir, wirklich nur der."),
    L("Tom", "m", "Licht geht überall hier, oder? Ich bleibe bei Bremse."),
    L("Sara", "f", "Licht okay, nur Öl. Springt euer Motor an?"),
    L("Tim", "m", "Motor ja, nur Klima bei mir. Ist der Auspuff defekt bei jemandem?"),
    L("Lukas", "m", "Auspuff nicht, nur Batterie. Fahren wir morgen alle hin?"),
    L("Lisa", "f", "Ja, um acht bei Müller, einverstanden? Mit Papieren?"),
    L("Tom", "m", "Einverstanden! Bis morgen, viel Glück uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis morgen zusammen!"),
    L("Tim", "m", "Tschüss! Bis morgen alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Warnweste anziehen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 64 im-reisebuero ----------------
# Lukas(i Strand) Lisa(a Kreuzfahrt) Tom(h Städte) Sara(g Wandern) Tim(b Safari)
apply(64, [
    L("Lukas", "m", "Also, Urlaub dieses Jahr! Wohin fahrt ihr? Ich mache Strandurlaub, Sonne und Meer."),
    L("Lisa", "f", "Schön! Ich buche eine Kreuzfahrt, Mittelmeer, sieben Tage Schiff."),
    L("Tom", "m", "Ich mache eine Städtereise, Museen und Kultur, alte Gebäude."),
    L("Sara", "f", "Ich fahre zum Wandern in die Berge, Natur und frische Luft."),
    L("Tim", "m", "Und ich mache eine Safari in Afrika, wilde Tiere, großer Traum."),
    L("Lukas", "m", "Tolle Pläne alle! Macht jemand Camping oder nicht?"),
    L("Lisa", "f", "Camping? Nein, nur Schiff bei mir, wirklich nur das."),
    L("Tom", "m", "Fahrradtour macht keiner hier, oder? Ich bleibe bei Städten."),
    L("Sara", "f", "Fahrrad nicht, nur Berge. Macht jemand Wellness-Urlaub?"),
    L("Tim", "m", "Wellness nicht, nur Safari bei mir. Macht jemand Skiurlaub?"),
    L("Lukas", "m", "Ski im Sommer nicht, nur Strand. Zeigen wir Fotos danach alle?"),
    L("Lisa", "f", "Ja, nach dem Urlaub, einverstanden? Mit allen Bildern?"),
    L("Tom", "m", "Einverstanden! Bis dann, schönen Urlaub euch allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis nachher zusammen!"),
    L("Tim", "m", "Tschüss! Bis nachher alle zusammen, gute Reise!"),
    L("Lukas", "m", "Noch etwas: Sonnencreme einpacken, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

print("batch E applied")
