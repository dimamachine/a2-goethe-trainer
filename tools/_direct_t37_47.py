#!/usr/bin/env python3
"""Rewrite T2 as direct speech, batch D (37-47). Verbose turns."""
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


# ---------------- TEST 37 bewerbung-und-job-suchen ----------------
# Lukas(c Programmierer) Lisa(a Lehrerin) Tom(f Buchhalter) Sara(g Schwester) Tim(d Verkäufer)
apply(37, [
    L("Lukas", "m", "Also, erzählt mal alle, in welchen Berufen arbeitet ihr eigentlich? Ich bin Programmierer in einer kleinen Firma in der Stadt."),
    L("Lisa", "f", "Schön! Ich bin Lehrerin an einer Grundschule, zweite Klasse, sehr lebendig und laut."),
    L("Tom", "m", "Ich bin Buchhalter, mit Zahlen den ganzen Tag, im Büro in der Stadt, ruhig und genau."),
    L("Sara", "f", "Ich bin Krankenschwester im Krankenhaus, auch Nachtschicht, anstrengend aber wirklich schön."),
    L("Tim", "m", "Und ich bin Verkäufer im Einzelhandel, in einem Sportgeschäft, Beratung und Kasse zusammen."),
    L("Lukas", "m", "Toll, alle haben gute Arbeit! Ist jemand von euch Ingenieur geworden oder nicht?"),
    L("Lisa", "f", "Ingenieur? Nein, nur Lehrerin bei mir, wirklich nur das, nichts anderes."),
    L("Tom", "m", "Architekt ist keiner von uns, oder? Ich bin nur Buchhalter, nichts anderes."),
    L("Sara", "f", "Polizist auch nicht, nur Schwester bei mir. Ist jemand von euch Arzt hier?"),
    L("Tim", "m", "Arzt nicht, nur Verkäufer bei mir. Treffen wir uns am Freitag alle zusammen?"),
    L("Lukas", "m", "Ja, Freitag um sieben, beim Italiener um die Ecke, einverstanden?"),
    L("Lisa", "f", "Einverstanden! Bis Freitag, ich freue mich schon sehr!"),
    L("Tom", "m", "Bis dann! Schönes Wochenende euch allen zusammen! Tschüss!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Freitag alle zusammen!"),
    L("Tim", "m", "Tschüss! Bis Freitag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Pünktlich kommen, einverstanden? Wirklich pünktlich bitte!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 38 babys-und-kleinkinder ----------------
# Lukas(i Autos) Lisa(d Puppen) Tom(e Dinos) Sara(c Plüsch) Tim(f Bücher)
apply(38, [
    L("Lukas", "m", "Also, Geschenke für das Kinderfest im Kindergarten! Was bringt jeder mit? Ich bringe kleine Autos mit, viele bunte."),
    L("Lisa", "f", "Schön! Ich bringe Puppen mit, zwei schöne, mit Kleidern zum Wechseln."),
    L("Tom", "m", "Ich bringe Dinosaurier mit, große grüne, die Kinder lieben sie."),
    L("Sara", "f", "Ich bringe Plüschtiere mit, weiche Bären und Hasen, zum Kuscheln."),
    L("Tim", "m", "Und ich bringe Bücher mit, Bilderbücher mit Tieren, zum Vorlesen."),
    L("Lukas", "m", "Super, alles zusammen! Bringt jemand Bauklötze mit oder nicht?"),
    L("Lisa", "f", "Bauklötze? Nein, nur Puppen bei mir, wirklich nur die."),
    L("Tom", "m", "Bälle bringt keiner mit, oder? Ich habe nur Dinos dabei."),
    L("Sara", "f", "Bälle nicht, nur Plüschtiere. Malt jemand mit den Kindern?"),
    L("Tim", "m", "Malen nicht, nur Bücher bei mir. Macht jemand Musik mit ihnen?"),
    L("Lukas", "m", "Musik nicht, nur Autos. Wann geht es los, Samstag um zehn?"),
    L("Lisa", "f", "Ja, Samstag um zehn, im Kindergarten, einverstanden?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Geschenke einpacken, einverstanden? Schön bunt bitte!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 39 am-flughafen ----------------
# Lukas(c New York) Lisa(h London) Tom(f Paris) Sara(a Rom) Tim(d Tokio)
apply(39, [
    L("Lukas", "m", "Also, Urlaubsflüge im Sommer! Wohin fliegt ihr? Ich fliege nach New York, eine ganze Woche."),
    L("Lisa", "f", "Cool! Ich fliege nach London, für ein Wochenende, Shopping und Musical."),
    L("Tom", "m", "Ich fliege nach Paris, mit meiner Freundin, romantisch und schön."),
    L("Sara", "f", "Ich fliege nach Rom, Pizza und Geschichte, ich freue mich schon."),
    L("Tim", "m", "Und ich fliege nach Tokio, weit weg, ganz anders und spannend."),
    L("Lukas", "m", "Toll, alle fliegen weit! Fliegt jemand nach Wien oder nicht?"),
    L("Lisa", "f", "Wien? Nein, nur London bei mir, wirklich nur das."),
    L("Tom", "m", "Istanbul fliegt keiner an, oder? Ich bleibe bei Paris."),
    L("Sara", "f", "Istanbul nicht, nur Rom. Fliegt jemand nach Amsterdam?"),
    L("Tim", "m", "Amsterdam nicht, nur Tokio bei mir. Fliegt jemand nach Madrid?"),
    L("Lukas", "m", "Madrid nicht, nur New York. Treffen wir uns vorher alle?"),
    L("Lisa", "f", "Ja, Freitag im Café, einverstanden? Um sechs Uhr abends?"),
    L("Tom", "m", "Einverstanden! Bis Freitag, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Guten Flug euch allen zusammen!"),
    L("Lukas", "m", "Euch auch! Und Pässe nicht vergessen, einverstanden? Wirklich nicht!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 40 sommer-und-strand ----------------
# Lukas(i Surfen) Lisa(b Wasserski) Tom(h Sonnenbaden) Sara(d Sandburgen) Tim(f Tauchen)
apply(40, [
    L("Lukas", "m", "Also, Strandtag am Samstag! Was macht jeder? Ich gehe surfen, mit geliehenem Brett."),
    L("Lisa", "f", "Cool! Ich fahre Wasserski, hinter dem Boot, schnell und nass."),
    L("Tom", "m", "Ich mache Sonnenbaden und lese, ganz ruhig, mit viel Sonnencreme."),
    L("Sara", "f", "Ich baue Sandburgen, große mit Türmen, wie als Kind."),
    L("Tim", "m", "Und ich gehe tauchen, mit Brille und Flossen, Fische schauen."),
    L("Lukas", "m", "Super, alle am Wasser! Fährt jemand Kajak oder nicht?"),
    L("Lisa", "f", "Kajak? Nein, nur Wasserski bei mir, wirklich nur das."),
    L("Tom", "m", "Schnorcheln tut keiner hier, oder? Ich bleibe beim Lesen."),
    L("Sara", "f", "Schnorcheln nicht, nur Burgen. Segelt jemand von euch?"),
    L("Tim", "m", "Segeln nicht, nur Tauchen bei mir. Spielt jemand Beach-Volleyball?"),
    L("Lukas", "m", "Volleyball nicht, nur Surfen. Treffen wir uns um zehn am Strand?"),
    L("Lisa", "f", "Ja, um zehn am Kiosk, einverstanden? Mit Badesachen?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Sonnencreme nicht vergessen, einverstanden? Wirklich wichtig!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 41 winter-und-skifahren ----------------
# Lukas(e Snowboard) Lisa(d Ski) Tom(b Schlittschuh) Sara(g Schlitten) Tim(f Eishockey)
apply(41, [
    L("Lukas", "m", "Also, Winter-Samstag mit Freunden! Was macht jeder? Ich gehe Snowboarden, mit neuem Board."),
    L("Lisa", "f", "Cool! Ich fahre Ski, schon seit Kindheit, blaue und rote Pisten."),
    L("Tom", "m", "Ich gehe Schlittschuhlaufen, auf der Eisbahn in der Stadt, zweimal pro Woche."),
    L("Sara", "f", "Ich fahre Schlitten, mit den Kindern, am kleinen Hügel hinterm Haus."),
    L("Tim", "m", "Und ich spiele Eishockey, im Verein, schon Turniere gewonnen."),
    L("Lukas", "m", "Toll, alle im Schnee! Macht jemand Curling oder nicht?"),
    L("Lisa", "f", "Curling? Nein, nur Ski bei mir, wirklich nur das."),
    L("Tom", "m", "Skispringen ist nichts für uns, oder? Ich bleibe bei der Eisbahn."),
    L("Sara", "f", "Skispringen nicht, nur Schlitten. Macht jemand Langlauf hier?"),
    L("Tim", "m", "Langlauf nicht, nur Eishockey bei mir. Macht jemand Eisklettern?"),
    L("Lukas", "m", "Eisklettern nicht, Wahnsinn! Treffen wir uns Samstag um zehn?"),
    L("Lisa", "f", "Ja, um zehn am Lift, einverstanden? Mit warmer Kleidung?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Handschuhe nicht vergessen, einverstanden? Wirklich wichtig!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 42 geburtstag-und-geschenke ----------------
# Lukas(b Schmuck) Lisa(h Buch) Tom(f Parfüm) Sara(e Blumen) Tim(i Schokolade)
apply(42, [
    L("Lukas", "m", "Also, Wichteln zum Geburtstag! Was schenkt jeder? Ich schenke Schmuck, eine Silberkette."),
    L("Lisa", "f", "Schön! Ich schenke ein Buch, einen dicken Krimi, selbst gelesen."),
    L("Tom", "m", "Ich schenke Parfüm, das Lieblingsparfüm, gut gemerkt."),
    L("Sara", "f", "Ich schenke Blumen, dreißig rote Rosen, ein großer Strauß."),
    L("Tim", "m", "Und ich schenke Schokolade, eine Riesen-Box aus Belgien, lecker."),
    L("Lukas", "m", "Super, alles dabei! Schenkt jemand eine CD oder nicht?"),
    L("Lisa", "f", "CD? Nein, nur Buch bei mir, wirklich nur das."),
    L("Tom", "m", "Geld schenkt keiner hier, oder? Ich bleibe beim Parfüm."),
    L("Sara", "f", "Geld nicht, nur Blumen. Schenkt jemand Wein?"),
    L("Tim", "m", "Wein nicht, nur Schokolade bei mir. Schenkt jemand eine Konzertkarte?"),
    L("Lukas", "m", "Konzertkarte nicht, nur Schmuck. Feiern wir Samstag alle?"),
    L("Lisa", "f", "Ja, Samstag um sieben, bei mir, einverstanden?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Schön einpacken, einverstanden? Mit Schleife bitte!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 43 reise-mit-dem-auto ----------------
# Lukas(d BMW) Lisa(b Tesla) Tom(i VW Bus) Sara(h Mini) Tim(f Mercedes)
apply(43, [
    L("Lukas", "m", "Also, neue Autos überall! Was fahrt ihr? Ich habe einen BMW gekauft, sportlich und schnell."),
    L("Lisa", "f", "Cool! Ich fahre einen Tesla, Elektroauto, modern und umweltfreundlich."),
    L("Tom", "m", "Ich habe einen VW Bus, praktisch für Familienreisen mit drei Kindern."),
    L("Sara", "f", "Ich habe einen Mini Cooper, klein und süß, perfekt für die Stadt."),
    L("Tim", "m", "Und ich habe einen Mercedes, fürs Geschäftsleben, repräsentativ und bequem."),
    L("Lukas", "m", "Tolle Autos alle! Fährt jemand Porsche oder nicht?"),
    L("Lisa", "f", "Porsche? Nein, nur Tesla bei mir, wirklich nur der."),
    L("Tom", "m", "Audi fährt keiner hier, oder? Ich bleibe beim Bus."),
    L("Sara", "f", "Audi nicht, nur Mini. Fährt jemand Ford?"),
    L("Tim", "m", "Ford nicht, nur Mercedes bei mir. Fährt jemand Opel?"),
    L("Lukas", "m", "Opel nicht, nur BMW. Waschen wir sie Sonntag alle?"),
    L("Lisa", "f", "Ja, Sonntag um zehn, bei mir, einverstanden?"),
    L("Tom", "m", "Einverstanden! Bis Sonntag, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Bis Sonntag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Eimer mitbringen, einverstanden? Jeder einen!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 44 musik-und-konzerte ----------------
# Lukas(f Rock) Lisa(b Klassik) Tom(a Jazz) Sara(e HipHop) Tim(i Elektro)
apply(44, [
    L("Lukas", "m", "Also, Musik! Was hört ihr? Ich liebe Rock-Musik, laut und hart, schon seit der Schule."),
    L("Lisa", "f", "Schön! Ich höre nur klassische Musik, Beethoven und Mozart, jeden Abend."),
    L("Tom", "m", "Ich mag Jazz, Improvisationen und Saxophon-Solos, sehr stilvoll."),
    L("Sara", "f", "Ich liebe Hip-Hop, Rapper und Beats, überall mit Kopfhörern."),
    L("Tim", "m", "Und ich höre nur Elektro, Techno und House, oft auf Festivals."),
    L("Lukas", "m", "Bunt gemischt! Hört jemand Country oder nicht?"),
    L("Lisa", "f", "Country? Nein, nur Klassik bei mir, wirklich nur die."),
    L("Tom", "m", "Reggae hört keiner hier, oder? Ich bleibe beim Jazz."),
    L("Sara", "f", "Reggae nicht, nur Hip-Hop. Hört jemand Pop?"),
    L("Tim", "m", "Pop nicht, nur Elektro bei mir. Hört jemand Volksmusik?"),
    L("Lukas", "m", "Volksmusik nicht, nur Rock. Machen wir Samstag eine Party?"),
    L("Lisa", "f", "Ja, Samstag bei mir, einverstanden? Jeder bringt Musik mit?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Kein Reggae die ganze Nacht, einverstanden? Bitte!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 45 im-museum ----------------
# Lukas(i Geschichte) Lisa(e Moderne Kunst) Tom(d Naturkunde) Sara(g Ägypten) Tim(c Technik)
apply(45, [
    L("Lukas", "m", "Also, Museums-Tour am Samstag! Was mag jeder? Ich liebe Geschichte, Schlachten und Mittelalter."),
    L("Lisa", "f", "Spannend! Ich mag moderne Kunst, Picasso und Banksy, sehr bunt."),
    L("Tom", "m", "Ich interessiere mich für Naturkunde, Tiere und Dinosaurier, toll."),
    L("Sara", "f", "Ich liebe Ägypten, Pharaonen und Pyramiden, sehr fasziniert, seit Jahren."),
    L("Tim", "m", "Und ich mag das Technik-Museum, Maschinen und Flugzeuge, super."),
    L("Lukas", "m", "Bunt gemischt! Mag jemand Sport im Museum oder nicht?"),
    L("Lisa", "f", "Sport? Nein, nur Kunst bei mir, wirklich nur die."),
    L("Tom", "m", "Klassische Kunst mag keiner hier, oder? Ich bleibe bei Tieren."),
    L("Sara", "f", "Klassik nicht, nur Ägypten. Interessiert sich jemand für Musik?"),
    L("Tim", "m", "Musik nicht, nur Technik bei mir. Interessiert sich jemand für Mode?"),
    L("Lukas", "m", "Mode nicht, nur Geschichte. Treffen wir uns um zehn dort?"),
    L("Lisa", "f", "Ja, um zehn am Eingang, einverstanden? Jeder kauft Karten?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, ich freue mich schon sehr!"),
    L("Sara", "f", "Ich auch! Bis dann, tschüss zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Kaffee danach im Café, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 46 am-bahnhof ----------------
# Lukas(f Berlin) Lisa(d Hamburg) Tom(h Köln) Sara(c München) Tim(g Dresden)
apply(46, [
    L("Lukas", "m", "Also, alle fahren heute weg! Wohin fahrt ihr? Ich fahre nach Berlin, Freunde besuchen."),
    L("Lisa", "f", "Schön! Ich fahre nach Hamburg, Bewerbungs-Gespräch dort, aufregend."),
    L("Tom", "m", "Ich fahre nach Köln, Tante besuchen, sie ist leider krank."),
    L("Sara", "f", "Ich fahre nach München, Konzert der Lieblings-Band, super."),
    L("Tim", "m", "Und ich fahre nach Dresden, Geschäftsreise für drei Tage."),
    L("Lukas", "m", "Überall hin! Fährt jemand nach Leipzig oder nicht?"),
    L("Lisa", "f", "Leipzig? Nein, nur Hamburg bei mir, wirklich nur das."),
    L("Tom", "m", "Stuttgart fährt keiner hier, oder? Ich bleibe bei Köln."),
    L("Sara", "f", "Stuttgart nicht, nur München. Fährt jemand nach Frankfurt?"),
    L("Tim", "m", "Frankfurt nicht, nur Dresden bei mir. Fährt jemand nach Nürnberg?"),
    L("Lukas", "m", "Nürnberg nicht, nur Berlin. Schreiben wir uns alle?"),
    L("Lisa", "f", "Ja, Fotos schicken, einverstanden? Aus jeder Stadt?"),
    L("Tom", "m", "Einverstanden! Bis bald, gute Reise euch allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis bald zusammen!"),
    L("Tim", "m", "Tschüss! Gute Reise alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Pünktlich am Gleis sein, einverstanden? Wirklich wichtig!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 47 computer-und-probleme ----------------
# Lukas(c App) Lisa(d Fotos) Tom(b Videos) Sara(i Webseite) Tim(f Spiele)
apply(47, [
    L("Lukas", "m", "Also, alle am Computer heute! Was macht jeder? Ich programmiere eine App, zum Verkaufen."),
    L("Lisa", "f", "Spannend! Ich bearbeite Fotos, Hochzeits-Fotos, mit Photoshop."),
    L("Tom", "m", "Ich schneide Videos, für YouTube, dreimal pro Woche neu."),
    L("Sara", "f", "Ich designe eine Webseite, für meine Firma, mit Logo und allem."),
    L("Tim", "m", "Und ich mache Online-Spiele, in einer Liga, sehr ehrgeizig."),
    L("Lukas", "m", "Fleißig alle! Produziert jemand Musik oder nicht?"),
    L("Lisa", "f", "Musik? Nein, nur Fotos bei mir, wirklich nur die."),
    L("Tom", "m", "Animationen erstellt keiner hier, oder? Ich bleibe bei Videos."),
    L("Sara", "f", "Animationen nicht, nur Webseite. Schreibt jemand Texte?"),
    L("Tim", "m", "Texte nicht, nur Spiele bei mir. Beantwortet jemand E-Mails?"),
    L("Lukas", "m", "E-Mails später, erst Pause! Machen wir Kaffee alle?"),
    L("Lisa", "f", "Ja, Kaffee jetzt, einverstanden? Fünf Minuten?"),
    L("Tom", "m", "Einverstanden! Bis gleich, erfrischt weiter!"),
    L("Sara", "f", "Bis gleich! Tschüss, bis gleich zusammen!"),
    L("Tim", "m", "Bis gleich alle zusammen! Weiter geht es!"),
    L("Lukas", "m", "Noch etwas: Augen schonen, einverstanden? Pause wichtig!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

print("batch D applied")
