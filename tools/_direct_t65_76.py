#!/usr/bin/env python3
"""Rewrite T2 as direct speech, batch F1 (65-76). Verbose turns."""
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


# ---------------- TEST 65 im-elektronikgeschaeft ----------------
# Lukas(g Laptop) Lisa(i Kopfhörer) Tom(e Fernseher) Sara(d Kamera) Tim(a Konsole)
apply(65, [
    L("Lukas", "m", "Also, Elektronik kaufen! Was braucht jeder? Ich kaufe einen Laptop, schnell und leicht."),
    L("Lisa", "f", "Cool! Ich kaufe Kopfhörer, kabellos, für Musik überall."),
    L("Tom", "m", "Ich kaufe einen Fernseher, groß und flach, fürs Wohnzimmer."),
    L("Sara", "f", "Ich kaufe eine Kamera, für Urlaubsfotos, mit viel Zoom."),
    L("Tim", "m", "Und ich kaufe eine Spielekonsole, neueste Version, super Grafik."),
    L("Lukas", "m", "Tolle Technik alle! Kauft jemand ein Handy oder nicht?"),
    L("Lisa", "f", "Handy? Nein, nur Kopfhörer bei mir, wirklich nur die."),
    L("Tom", "m", "Lautsprecher kauft keiner hier, oder? Ich bleibe beim Fernseher."),
    L("Sara", "f", "Lautsprecher nicht, nur Kamera. Kauft jemand einen Drucker?"),
    L("Tim", "m", "Drucker nicht, nur Konsole bei mir. Kauft jemand ein Tablet?"),
    L("Lukas", "m", "Tablet nicht, nur Laptop. Gehen wir zusammen hin alle?"),
    L("Lisa", "f", "Ja, Samstag um zehn, einverstanden? In die Stadt?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Samstag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Prospekte mitnehmen, einverstanden? Unbedingt vergleichen!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 66 handwerker-im-haus ----------------
# Lukas(g Klempner) Lisa(d Elektriker) Tom(b Maler) Sara(i Tischler) Tim(c Dachdecker)
apply(66, [
    L("Lukas", "m", "Also, Handwerker im Haus! Wen ruft ihr? Ich rufe den Klempner, Wasser tropft im Bad."),
    L("Lisa", "f", "Oh! Ich rufe den Elektriker, Licht geht nicht in der Küche."),
    L("Tom", "m", "Ich rufe den Maler, Wände streichen, alles neu und hell."),
    L("Sara", "f", "Ich rufe den Tischler, Schrank reparieren, Tür klemmt."),
    L("Tim", "m", "Und ich rufe den Dachdecker, Ziegel locker nach dem Sturm."),
    L("Lukas", "m", "Viel zu tun alle! Ruft jemand den Schlosser oder nicht?"),
    L("Lisa", "f", "Schlosser? Nein, nur Elektriker bei mir, wirklich nur der."),
    L("Tom", "m", "Fensterputzer ruft keiner hier, oder? Ich bleibe beim Maler."),
    L("Sara", "f", "Fensterputzer nicht, nur Tischler. Ruft jemand den Gärtner?"),
    L("Tim", "m", "Gärtner nicht, nur Dach bei mir. Ruft jemand den Fliesenleger?"),
    L("Lukas", "m", "Fliesen nicht, nur Rohre. Tauschen wir Nummern aus alle?"),
    L("Lisa", "f", "Ja, gute Handwerker teilen, einverstanden? Unbedingt?"),
    L("Tom", "m", "Einverstanden! Bis bald, viel Glück uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis bald zusammen!"),
    L("Tim", "m", "Tschüss! Bis bald alle zusammen, trockene Dächer!"),
    L("Lukas", "m", "Noch etwas: Rechnungen prüfen, einverstanden? Genau schauen!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 67 im-zoo ----------------
# Lukas(e Löwen) Lisa(d Pinguine) Tom(i Affen) Sara(h Giraffen) Tim(c Elefanten)
apply(67, [
    L("Lukas", "m", "Also, Zoo gestern! Was war am besten? Bei mir die Löwen, groß und laut."),
    L("Lisa", "f", "Schön! Bei mir die Pinguine, lustig watschelnd, ganz viele."),
    L("Tom", "m", "Bei mir die Affen, klettern und springen, sehr lustig."),
    L("Sara", "f", "Bei mir die Giraffen, lange Hälse, elegant und ruhig."),
    L("Tim", "m", "Und bei mir die Elefanten, riesig und grau, beeindruckend."),
    L("Lukas", "m", "Tolle Tiere alle! Mag jemand Papageien oder nicht?"),
    L("Lisa", "f", "Papageien? Nein, nur Pinguine bei mir, wirklich nur die."),
    L("Tom", "m", "Tiger sieht keiner mehr hier, oder? Ich bleibe bei Affen."),
    L("Sara", "f", "Tiger nicht, nur Giraffen. Mag jemand Schlangen?"),
    L("Tim", "m", "Schlangen nicht, nur Elefanten bei mir. Mag jemand Eisbären?"),
    L("Lukas", "m", "Eisbären nicht, nur Löwen. Gehen wir bald wieder alle?"),
    L("Lisa", "f", "Ja, nächsten Monat, einverstanden? Mit Jahreskarten?"),
    L("Tom", "m", "Einverstanden! Bis dann, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis bald zusammen!"),
    L("Tim", "m", "Tschüss! Bis bald alle zusammen, tschüss!"),
    L("Lukas", "m", "Noch etwas: Fotos zeigen, einverstanden? Alle mitbringen!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 68 in-der-kantine ----------------
# Lukas(c Schnitzel) Lisa(e Salat) Tom(h Nudeln) Sara(a Suppe) Tim(f Fisch)
apply(68, [
    L("Lukas", "m", "Also, Mittag in der Kantine! Was nehmt ihr? Ich nehme Schnitzel, mit Pommes."),
    L("Lisa", "f", "Lecker! Ich nehme einen großen Salat, frisch und gesund."),
    L("Tom", "m", "Ich nehme Nudeln, vegetarisch, mit Tomatensoße."),
    L("Sara", "f", "Ich nehme Suppe, heiß und lecker, als Vorspeise."),
    L("Tim", "m", "Und ich nehme Fisch, gebraten, mit Kartoffeln."),
    L("Lukas", "m", "Guten Appetit alle! Nimmt jemand Reis mit Gemüse oder nicht?"),
    L("Lisa", "f", "Reis? Nein, nur Salat bei mir, wirklich nur der."),
    L("Tom", "m", "Pizza gibt es heute nicht hier, oder? Ich bleibe bei Nudeln."),
    L("Sara", "f", "Pizza nicht, nur Suppe. Nimmt jemand nur Nachtisch?"),
    L("Tim", "m", "Nachtisch später, erst Fisch bei mir. Nimmt jemand Currywurst?"),
    L("Lukas", "m", "Currywurst nicht, nur Schnitzel. Schmeckt es allen?"),
    L("Lisa", "f", "Ja, sehr lecker! Noch Nachtisch danach, einverstanden?"),
    L("Tom", "m", "Einverstanden! Guten Appetit weiterhin, ihr Lieben!"),
    L("Sara", "f", "Euch auch! Tschüss, bis morgen zusammen!"),
    L("Tim", "m", "Tschüss! Bis morgen alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Morgen wieder hier, einverstanden? Gleiche Zeit!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 69 im-fundbuero ----------------
# Lukas(a Schirm) Lisa(e Handy) Tom(i Geldbeutel) Sara(g Brille) Tim(d Schlüssel)
apply(69, [
    L("Lukas", "m", "Also, Fundbüro! Was habt ihr verloren? Ich habe meinen Regenschirm verloren, rot."),
    L("Lisa", "f", "Oh! Ich habe mein Handy verloren, gestern im Bus."),
    L("Tom", "m", "Ich habe meinen Geldbeutel verloren, mit Karten und Geld."),
    L("Sara", "f", "Ich habe meine Brille verloren, ohne sie sehe ich nichts."),
    L("Tim", "m", "Und ich habe meine Schlüssel verloren, Haus und Fahrrad."),
    L("Lukas", "m", "Viel weg alles! Hat jemand eine Tasche verloren oder nicht?"),
    L("Lisa", "f", "Tasche? Nein, nur Handy bei mir, wirklich nur das."),
    L("Tom", "m", "Jacke vermisst keiner hier, oder? Ich bleibe beim Beutel."),
    L("Sara", "f", "Jacke nicht, nur Brille. Hat jemand einen Laptop verloren?"),
    L("Tim", "m", "Laptop nicht, nur Schlüssel bei mir. Hat jemand eine Uhr verloren?"),
    L("Lukas", "m", "Uhr nicht, nur Schirm. Fragen wir morgen wieder alle?"),
    L("Lisa", "f", "Ja, morgen um neun, einverstanden? Mit Ausweis?"),
    L("Tom", "m", "Einverstanden! Viel Glück uns allen zusammen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis morgen zusammen!"),
    L("Tim", "m", "Tschüss! Bis morgen alle zusammen, viel Glück!"),
    L("Lukas", "m", "Noch etwas: Alles beschriften, einverstanden? Namen drauf!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 70 bei-der-versicherung ----------------
# Lukas(b Auto) Lisa(c Hausrat) Tom(f Reise) Sara(a Kranken) Tim(i Haftpflicht)
apply(70, [
    L("Lukas", "m", "Also, Versicherungen! Welche habt ihr? Ich habe eine Autoversicherung, Vollkasko."),
    L("Lisa", "f", "Wichtig! Ich habe eine Hausratversicherung, für Wohnung und Möbel."),
    L("Tom", "m", "Ich habe eine Reiseversicherung, für Urlaub und Krankheit unterwegs."),
    L("Sara", "f", "Ich habe eine Krankenversicherung, gesetzlich, ganz normal."),
    L("Tim", "m", "Und ich habe eine Haftpflichtversicherung, unbedingt nötig, finde ich."),
    L("Lukas", "m", "Gut versichert alle! Hat jemand eine Rentenversicherung oder nicht?"),
    L("Lisa", "f", "Rente? Nein, nur Hausrat bei mir, wirklich nur die."),
    L("Tom", "m", "Lebensversicherung hat keiner hier, oder? Ich bleibe bei Reise."),
    L("Sara", "f", "Leben nicht, nur Kranken. Hat jemand eine Tierversicherung?"),
    L("Tim", "m", "Tier nicht, nur Haftpflicht bei mir. Hat jemand Rechtsschutz?"),
    L("Lukas", "m", "Recht nicht, nur Auto. Lesen wir das Kleingedruckte alle?"),
    L("Lisa", "f", "Ja, immer lesen, einverstanden? Ganz genau?"),
    L("Tom", "m", "Einverstanden! Sicher ist sicher, ihr Lieben!"),
    L("Sara", "f", "Euch auch! Tschüss, bis bald zusammen!"),
    L("Tim", "m", "Tschüss! Bis bald alle zusammen, gut versichert!"),
    L("Lukas", "m", "Noch etwas: Police abheften, einverstanden? Ordentlich!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 71 im-baumarkt ----------------
# Lukas(f Farbe) Lisa(d Pflanzen) Tom(e Werkzeug) Sara(c Fliesen) Tim(i Lampe)
apply(71, [
    L("Lukas", "m", "Also, Baumarkt Samstag! Was kauft jeder? Ich kaufe Farbe, weiß fürs Wohnzimmer."),
    L("Lisa", "f", "Schön! Ich kaufe Pflanzen, grün für Balkon und Zimmer."),
    L("Tom", "m", "Ich kaufe Werkzeug, Bohrer und Hammer, fürs Regal."),
    L("Sara", "f", "Ich kaufe Fliesen, blau fürs Bad, modern."),
    L("Tim", "m", "Und ich kaufe eine Lampe, hell für den Schreibtisch."),
    L("Lukas", "m", "Viel vor alle! Kauft jemand Holz oder nicht?"),
    L("Lisa", "f", "Holz? Nein, nur Pflanzen bei mir, wirklich nur die."),
    L("Tom", "m", "Schloss kauft keiner hier, oder? Ich bleibe bei Werkzeug."),
    L("Sara", "f", "Schloss nicht, nur Fliesen. Kauft jemand Tapeten?"),
    L("Tim", "m", "Tapeten nicht, nur Lampe bei mir. Kauft jemand Gartenmöbel?"),
    L("Lukas", "m", "Möbel nicht, nur Farbe. Fahren wir zusammen hin alle?"),
    L("Lisa", "f", "Ja, Samstag um neun, einverstanden? Mit Auto?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, viel Erfolg uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Samstag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Kassenbon aufheben, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 72 muelltrennung-und-recycling ----------------
# Lukas(b Müll trennen) Lisa(e Pfand) Tom(h Kompost) Sara(g unverpackt) Tim(c Wertstoffhof)
apply(72, [
    L("Lukas", "m", "Also, Umwelt! Was macht jeder? Ich trenne den Müll genau, alles sortiert."),
    L("Lisa", "f", "Super! Ich sammle Pfandflaschen, jede Woche, fürs Taschengeld."),
    L("Tom", "m", "Ich kompostiere Bioabfälle, im Garten, gute Erde."),
    L("Sara", "f", "Ich kaufe ohne Verpackung ein, mit Beuteln und Gläsern."),
    L("Tim", "m", "Und ich bringe alte Geräte zum Wertstoffhof, regelmäßig."),
    L("Lukas", "m", "Grün alle! Spart jemand Strom oder nicht?"),
    L("Lisa", "f", "Strom? Nein, nur Pfand bei mir, wirklich nur das."),
    L("Tom", "m", "Fahrrad fährt jeder hier, oder? Ich bleibe bei Kompost."),
    L("Sara", "f", "Fahrrad ja, aber Aufgabe ist Einkaufen. Spart jemand Wasser?"),
    L("Tim", "m", "Wasser nicht speziell, nur Hof bei mir. Kauft jemand Second-Hand?"),
    L("Lukas", "m", "Second-Hand manchmal, aber Aufgabe ist Trennen. Machen wir weiter alle?"),
    L("Lisa", "f", "Ja, jeden Tag, einverstanden? Unbedingt?"),
    L("Tom", "m", "Einverstanden! Grün bleiben, ihr Lieben!"),
    L("Sara", "f", "Euch auch! Tschüss, bis bald zusammen!"),
    L("Tim", "m", "Tschüss! Bis bald alle zusammen, umweltfreundlich!"),
    L("Lukas", "m", "Noch etwas: Nachbarn motivieren, einverstanden? Alle mitmachen!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 73 im-tierheim ----------------
# Lukas(h Hund) Lisa(i Katze) Tom(d Kaninchen) Sara(e Vogel) Tim(c Hamster)
apply(73, [
    L("Lukas", "m", "Also, Tierheim! Welches Tier nehmt ihr? Ich nehme einen Hund, groß und treu."),
    L("Lisa", "f", "Süß! Ich nehme eine Katze, klein und ruhig, zum Kuscheln."),
    L("Tom", "m", "Ich nehme ein Kaninchen, mit langen Ohren, für die Kinder."),
    L("Sara", "f", "Ich nehme einen Vogel, bunt singend, fürs Wohnzimmer."),
    L("Tim", "m", "Und ich nehme einen Hamster, winzig und schnell, im Käfig."),
    L("Lukas", "m", "Tolle Tiere alle! Nimmt jemand eine Schildkröte oder nicht?"),
    L("Lisa", "f", "Schildkröte? Nein, nur Katze bei mir, wirklich nur die."),
    L("Tom", "m", "Meerschweinchen nimmt keiner hier, oder? Ich bleibe beim Kaninchen."),
    L("Sara", "f", "Meerli nicht, nur Vogel. Nimmt jemand eine Maus?"),
    L("Tim", "m", "Maus nicht, nur Hamster bei mir. Nimmt jemand Fische?"),
    L("Lukas", "m", "Fische nicht, nur Hund. Holen wir sie Samstag alle?"),
    L("Lisa", "f", "Ja, Samstag um elf, einverstanden? Mit Boxen?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, viel Freude uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Samstag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Futter kaufen, einverstanden? Gleich morgen!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 74 auf-dem-weihnachtsmarkt ----------------
# Lukas(h Glühwein) Lisa(i Geschenke) Tom(f Bratwurst) Sara(d Musik) Tim(c Karussell)
apply(74, [
    L("Lukas", "m", "Also, Weihnachtsmarkt! Was macht jeder? Ich trinke Glühwein, heiß und süß."),
    L("Lisa", "f", "Lecker! Ich kaufe Geschenke, für alle Lieben, viele Tüten."),
    L("Tom", "m", "Ich esse Bratwurst, mit Senf, zwei Stück."),
    L("Sara", "f", "Ich höre Weihnachtsmusik, Chor und Trompeten, wunderschön."),
    L("Tim", "m", "Und ich fahre Karussell, schnell und lustig, juhu!"),
    L("Lukas", "m", "Schön voll alles! Macht jemand Fotos oder nicht?"),
    L("Lisa", "f", "Fotos? Nein, nur Geschenke bei mir, wirklich nur die."),
    L("Tom", "m", "Baum schaut jeder an hier, oder? Ich bleibe bei Wurst."),
    L("Sara", "f", "Baum ja, aber Aufgabe ist Musik. Esst ihr gebrannte Mandeln?"),
    L("Tim", "m", "Mandeln später, erst Karussell bei mir. Lauft ihr Schlittschuh?"),
    L("Lukas", "m", "Schlittschuh nicht, nur Glühwein. Treffen wir uns um sechs alle?"),
    L("Lisa", "f", "Ja, um sechs am Baum, einverstanden? Mit Mützen?"),
    L("Tom", "m", "Einverstanden! Bis dann, frohe Zeit uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis später zusammen!"),
    L("Tim", "m", "Tschüss! Bis später alle zusammen, viel Spaß!"),
    L("Lukas", "m", "Noch etwas: Warm anziehen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 75 in-der-reinigung ----------------
# Lukas(i Anzug) Lisa(d Abendkleid) Tom(c Winterjacke) Sara(f Bettdecke) Tim(h Hemden)
apply(75, [
    L("Lukas", "m", "Also, Reinigung! Was bringt jeder? Ich bringe einen Anzug, dunkelblau."),
    L("Lisa", "f", "Schick! Ich bringe ein Abendkleid, rot, für die Feier."),
    L("Tom", "m", "Ich bringe eine Winterjacke, dick und warm, Fleck drauf."),
    L("Sara", "f", "Ich bringe eine Bettdecke, groß und warm, zum Waschen."),
    L("Tim", "m", "Und ich bringe Hemden zum Bügeln, fünf Stück, weiß."),
    L("Lukas", "m", "Viel Wäsche alle! Bringt jemand einen Mantel oder nicht?"),
    L("Lisa", "f", "Mantel? Nein, nur Kleid bei mir, wirklich nur das."),
    L("Tom", "m", "Teppich bringt keiner hier, oder? Ich bleibe bei Jacke."),
    L("Sara", "f", "Teppich nicht, nur Decke. Bringt jemand Vorhänge?"),
    L("Tim", "m", "Vorhänge nicht, nur Hemden bei mir. Bringt jemand Krawatten?"),
    L("Lukas", "m", "Krawatten nicht, nur Anzug. Holen wir Freitag alles?"),
    L("Lisa", "f", "Ja, Freitag um fünf, einverstanden? Mit Zetteln?"),
    L("Tom", "m", "Einverstanden! Bis Freitag, sauber bleiben alle!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Freitag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Freitag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Zettel aufheben, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 76 in-der-buchhandlung ----------------
# Lukas(c Krimis) Lisa(a Romane) Tom(i Sachbücher) Sara(g Kochbücher) Tim(e Comics)
apply(76, [
    L("Lukas", "m", "Also, Buchhandlung! Was kauft jeder? Ich kaufe Krimis, spannend bis zum Schluss."),
    L("Lisa", "f", "Schön! Ich kaufe Liebesromane, romantisch, zum Träumen."),
    L("Tom", "m", "Ich kaufe Sachbücher, über Geschichte, interessant."),
    L("Sara", "f", "Ich kaufe Kochbücher, mit Bildern, zum Nachkochen."),
    L("Tim", "m", "Und ich kaufe Comics, lustig und bunt, viele Helden."),
    L("Lukas", "m", "Viel Lesestoff alle! Kauft jemand Biografien oder nicht?"),
    L("Lisa", "f", "Biografien? Nein, nur Romane bei mir, wirklich nur die."),
    L("Tom", "m", "Gedichte kauft keiner hier, oder? Ich bleibe bei Sachbüchern."),
    L("Sara", "f", "Gedichte nicht, nur Kochen. Kauft jemand Reiseführer?"),
    L("Tim", "m", "Reiseführer nicht, nur Comics bei mir. Kauft jemand Kinderbücher?"),
    L("Lukas", "m", "Kinder nicht, nur Krimis. Treffen wir uns im Café alle?"),
    L("Lisa", "f", "Ja, gleich nebenan, einverstanden? Mit Kuchen?"),
    L("Tom", "m", "Einverstanden! Viel Spaß beim Lesen euch allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis bald zusammen!"),
    L("Tim", "m", "Tschüss! Bis bald alle zusammen, viel Spaß!"),
    L("Lukas", "m", "Noch etwas: Lesezeichen mitnehmen, einverstanden? Gratis!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

print("batch F1 applied")
