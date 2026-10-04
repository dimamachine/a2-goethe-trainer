#!/usr/bin/env python3
"""Rewrite T2 as direct speech, batch B (13,14,16,18,19,20,21,22,24,25)."""
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


# ---------------- TEST 13 verkehr-und-stadt ----------------
# Anna(g Zug) Markus(b Auto) Sara(h Flugzeug) Lukas(d Fernbus) Tom+Lisa(a zu Fuß)
apply(13, [
    L("Anna", "f", "Also, Hochzeit in Berlin! Wie kommt jeder hin? Ich komme mit dem Zug."),
    L("Markus", "m", "Gut! Ich fahre mit dem Auto und nehme zwei andere mit."),
    L("Sara", "f", "Ich fliege von München direkt nach Berlin, Ticket schon gefunden."),
    L("Lukas", "m", "Ich nehme den Fernbus, billig, aber dauert lang."),
    L("Tom", "m", "Lisa und ich gehen zu Fuß, nur 15 Minuten von uns."),
    L("Lisa", "f", "Genau, zusammen zu Fuß! Und Taxi nimmt keiner?"),
    L("Anna", "f", "Taxi? Nein, zu teuer. Fährt jemand Fahrrad?"),
    L("Markus", "m", "Fahrrad nach Berlin? Zu weit! Fähre fährt auch keine, oder?"),
    L("Sara", "f", "Keine Fähre, kein Motorrad bei uns. Alles geplant, oder?"),
    L("Lukas", "m", "Ja, alles geplant! Wann sehen wir uns dort?"),
    L("Tom", "m", "Am Freitagabend im Hotel, einverstanden?"),
    L("Lisa", "f", "Bis Freitag in Berlin! Gute Reise allen!"),
    L("Anna", "f", "Noch etwas: Anzüge und Kleider nicht vergessen!"),
    L("Markus", "m", "Stimmt! Und die Ringe hat der Bräutigam, hoffentlich!"),
], check_order=["Anna", "Markus", "Sara", "Lukas", "Tom", "Lisa"])

# ---------------- TEST 14 familienfeste ----------------
# Tante Eva(f Location) Mama(d Essen) Papa(c Fotos) Lukas(i Musik) Onkel Robert(e Rede)
apply(14, [
    L("Tante Eva", "f", "Also, Goldene Hochzeit von Oma und Opa! Planen wir alles? Ich organisiere die Location."),
    L("Mama", "f", "Schön! Ich koche das Hauptessen, nach altem Familienrezept, das Oma liebt."),
    L("Papa", "m", "Und ich mache die Fotos, mit guter Kamera, auch ein paar Filme."),
    L("Lukas", "m", "Ich spiele Musik, Klavier, auch Lieder für die Großeltern."),
    L("Onkel Robert", "m", "Und ich halte die Rede, als ältester Sohn kenne ich die Geschichte am besten."),
    L("Tante Eva", "f", "Perfekt! Wer schmückt den Saal?"),
    L("Mama", "f", "Schmücken? Keiner bisher. Du, Papa?"),
    L("Papa", "m", "Nein, nur Fotos bei mir. Bringt jemand einen Kuchen mit?"),
    L("Lukas", "m", "Kuchen? Nein, nur Musik. Fährt jemand die Großeltern?"),
    L("Onkel Robert", "m", "Die Großeltern kommen mit dem Taxi, alles klar. Kauft jemand ein Geschenk?"),
    L("Tante Eva", "f", "Geschenk und Einladungen machen Anna und Markus, schon erledigt."),
    L("Mama", "f", "Sehr gut! Wann fangen wir an, um drei?"),
    L("Papa", "m", "Ja, um drei im Saal! Bis dann!"),
    L("Lukas", "m", "Bis dann! Es wird ein schönes Fest!"),
], check_order=["Tante Eva", "Mama", "Papa", "Lukas", "Onkel Robert"])

# ---------------- TEST 16 kochen-und-essen ----------------
# Mama(f Hauptgericht) Tante Eva(c Suppe) Tim(b Nachtisch) Lisa(h Salat) Markus(i Getränke)
apply(16, [
    L("Mama", "f", "Also, Familienessen am Sonntag! Wer macht was? Ich koche das Hauptgericht."),
    L("Tante Eva", "f", "Schön! Ich bringe eine Suppe mit, lecker und warm."),
    L("Tim", "m", "Und ich backe den Nachtisch, einen Kuchen, ganz allein."),
    L("Lisa", "f", "Ich mache einen Salat, frisch und knackig, mit Joghurt."),
    L("Markus", "m", "Und ich bringe die Getränke mit, alles, was wir brauchen."),
    L("Mama", "f", "Perfekt! Wer macht Vorspeisen?"),
    L("Tante Eva", "f", "Vorspeisen? Keiner, Suppe reicht doch. Oder, Tim?"),
    L("Tim", "m", "Nein, nur Nachtisch bei mir. Wer dekoriert den Tisch?"),
    L("Lisa", "f", "Dekorieren? Keiner, wir essen doch. Bringt jemand Blumen mit?"),
    L("Markus", "m", "Blumen nicht, nur Getränke. Bringt jemand Brot mit?"),
    L("Mama", "f", "Brot haben wir genug zu Hause. Wann essen wir, um eins?"),
    L("Tante Eva", "f", "Ja, um eins bei uns! Bis Sonntag, tschüss!"),
    L("Tim", "m", "Bis dann! Ich freue mich schon!"),
    L("Lisa", "f", "Ich auch! Guten Appetit schon mal!"),
    L("Markus", "m", "Noch etwas: Hunger mitbringen, ganz viel!"),
    L("Mama", "f", "Immer! Und gute Laune auch, einverstanden?"),
], check_order=["Mama", "Tante Eva", "Tim", "Lisa", "Markus"])

# ---------------- TEST 18 internet-und-technik ----------------
# Vater(g Smartphone) Mutter(d Tablet) Lukas(a Kopfhörer) Sara(e Smartwatch) Lisa(h Laptop)
apply(18, [
    L("Vater", "m", "Also, Weihnachten kommt! Was wünscht sich jeder? Ich will ein neues Smartphone."),
    L("Mutter", "f", "Schön! Ich will ein Tablet, zum Lesen und für Rezepte in der Küche."),
    L("Lukas", "m", "Ich will kabellose Kopfhörer, für Musik und Gaming, jeden Tag."),
    L("Sara", "f", "Ich will eine Smartwatch, für Sport und Schritte zählen, genau."),
    L("Lisa", "f", "Und ich will einen Laptop, für die Schule, ganz dringend."),
    L("Vater", "m", "Alles notiert! Will jemand eine Kamera?"),
    L("Mutter", "f", "Kamera? Nein, nur Tablet bei mir. Wer will einen E-Reader?"),
    L("Lukas", "m", "E-Reader nicht, nur Kopfhörer für mich."),
    L("Sara", "f", "Und ein Foto-Album will keiner? Alles digital heute."),
    L("Lisa", "f", "Genau, alles digital! Will jemand einen Spielcomputer?"),
    L("Vater", "m", "Spielcomputer zu teuer, wirklich nicht, zu teuer."),
    L("Mutter", "f", "Am 24. wie immer! Bis dann!"),
    L("Lukas", "m", "Bis dann! Ich freue mich schon!"),
    L("Sara", "f", "Ich auch! Frohe Weihnachten schon mal!"),
    L("Lisa", "f", "Noch etwas: Geduld haben bis Weihnachten, einverstanden?"),
    L("Vater", "m", "Einverstanden! Keiner schaut vorher nach, versprochen?"),
], check_order=["Vater", "Mutter", "Lukas", "Sara", "Lisa"])

# ---------------- TEST 19 bank-und-geld ----------------
# Markus(h Miete) Anna(e Strom) Mutter(c Sparkonto) Vater(g Versicherungen) Lisa(a Einkauf)
apply(19, [
    L("Markus", "m", "Also, Geld-Sachen im Monat! Wer macht was? Ich zahle die Miete."),
    L("Anna", "f", "Gut! Ich zahle die Stromrechnungen, jeden Monat pünktlich, versprochen."),
    L("Mutter", "f", "Und ich verwalte das Sparkonto der Kinder, schon seit Jahren, zuverlässig."),
    L("Vater", "m", "Ich prüfe die Versicherungen, alle Verträge einmal im Jahr, gründlich."),
    L("Lisa", "f", "Und ich mache den Lebensmittel-Einkauf, jede Woche frisch und günstig."),
    L("Markus", "m", "Perfekt! Wer verwaltet das Online-Banking?"),
    L("Anna", "f", "Online-Banking? Keiner speziell, jeder seins. Du, Mutter?"),
    L("Mutter", "f", "Nein, nur Sparkonto bei mir. Wer zahlt Steuern?"),
    L("Vater", "m", "Steuern macht der Steuerberater, nicht wir. Kauft jemand Geschenke?"),
    L("Lisa", "f", "Geschenke kaufen wir zusammen, zu Weihnachten, alle zusammen."),
    L("Markus", "m", "Bank-Karten? Keiner, alles okay damit, wirklich."),
    L("Anna", "f", "Sonntag zum Essen, wie immer?"),
    L("Mutter", "f", "Einverstanden! Bis Sonntag, tschüss!"),
    L("Vater", "m", "Bis dann! Und spart fleißig weiter!"),
    L("Lisa", "f", "Noch etwas: Quittungen sammeln, ganz wichtig!"),
    L("Markus", "m", "Stimmt! Ohne Quittungen kein Überblick, einverstanden?"),
], check_order=["Markus", "Anna", "Mutter", "Vater", "Lisa"])

# ---------------- TEST 20 sprachen-lernen ----------------
# Anna(h Spanisch) Lisa(f Italienisch) Markus(i Französisch) Sara(b Chinesisch) Lukas(d Russisch)
apply(20, [
    L("Anna", "f", "Also, welche Sprachen lernt ihr? Ich lerne Spanisch, seit einem Jahr, mit viel Spaß."),
    L("Lisa", "f", "Schön! Ich lerne Italienisch, für den Urlaub nächstes Jahr in Rom."),
    L("Markus", "m", "Ich lerne Französisch, schwierige Aussprache, aber tolle Sprache."),
    L("Sara", "f", "Ich lerne Chinesisch, ganz anders als Deutsch, aber spannend."),
    L("Lukas", "m", "Und ich lerne Russisch, kyrillisch schreiben ist schwer, wirklich."),
    L("Anna", "f", "Cool, alle lernen! Lernt jemand von euch Portugiesisch?"),
    L("Lisa", "f", "Portugiesisch? Nein, nur Italienisch bei mir, wirklich."),
    L("Markus", "m", "Japanisch nicht, nur Französisch, nichts anderes."),
    L("Sara", "f", "Englisch können wir schon alle. Lernt jemand von euch Arabisch?"),
    L("Lukas", "m", "Arabisch nicht, nur Russisch. Machen wir einen Tandem-Abend zusammen?"),
    L("Anna", "f", "Gute Idee, Tandem! Wann treffen wir uns, Freitag?"),
    L("Lisa", "f", "Freitag um sechs, bei mir zu Hause?"),
    L("Markus", "m", "Perfekt, bis Freitag, ich freue mich!"),
    L("Sara", "f", "Bis dann! Viel Erfolg uns allen!"),
    L("Lukas", "m", "Noch etwas: Hefte mitbringen, ganz wichtig!"),
    L("Anna", "f", "Stimmt! Und Stifte auch, einverstanden?"),
], check_order=["Anna", "Lisa", "Markus", "Sara", "Lukas"])

# ---------------- TEST 21 auto-und-fahren ----------------
# Vater(e Bremsen) Mutter(i Reifen) Markus(d Batterie) Sara(b Öl) Tom(h gestohlen)
apply(21, [
    L("Vater", "m", "Also, Autoprobleme überall! Bei mir sind die Bremsen kaputt, gefährlich, ich fahre nicht mehr."),
    L("Mutter", "f", "Oh nein! Bei mir ist ein Reifen platt, seit gestern Abend, ärgerlich."),
    L("Markus", "m", "Und bei mir ist die Batterie kaputt, morgens geht nichts mehr, schrecklich."),
    L("Sara", "f", "Bei mir läuft Öl aus, ein Fleck unter dem Auto jeden Morgen."),
    L("Tom", "m", "Und mein Auto wurde gestohlen! Ganz weg, Polizei ist informiert."),
    L("Vater", "m", "Gestohlen, schrecklich! Macht euer Motor Geräusche?"),
    L("Mutter", "f", "Motor okay bei mir. Hat jemand kein Benzin mehr?"),
    L("Markus", "m", "Benzin habe ich, nur Batterie leer. Türschloss defekt bei jemandem?"),
    L("Sara", "f", "Türschloss okay bei mir. Scheibenwischer kaputt bei jemandem?"),
    L("Tom", "m", "Scheibenwischer egal jetzt. Fahren wir morgen alle in die Werkstatt?"),
    L("Vater", "m", "Ja, alle zusammen! Um acht bei Müller, pünktlich."),
    L("Mutter", "f", "Bis morgen! Gute Nacht, bis morgen!"),
    L("Markus", "m", "Bis dann! Hoffentlich wird alles gut!"),
    L("Sara", "f", "Drückt mir die Daumen, bitte!"),
    L("Tom", "m", "Noch etwas: Danke für eure Hilfe, wirklich!"),
    L("Vater", "m", "Gern! Familie hilft immer zusammen, einverstanden?"),
], check_order=["Vater", "Mutter", "Markus", "Sara", "Tom"])

# ---------------- TEST 22 kleidung-und-mode ----------------
# Lisa(f Tagebuch) Sara(g Fotoalbum) Tom(d Wein) Lukas(h Reisetasche) Anna+Markus(b Geld)
apply(22, [
    L("Lisa", "f", "Also, Geburtstag von Julia! Was schenken wir? Ich schenke ein elegantes Tagebuch, mit Gravur."),
    L("Sara", "f", "Schön! Ich schenke ein Foto-Album, mit unseren Bildern vom Sommer."),
    L("Tom", "m", "Ich schenke eine Flasche Wein, guten Rotwein aus Italien."),
    L("Lukas", "m", "Ich schenke eine Reisetasche, praktisch für den Urlaub im Sommer."),
    L("Anna", "f", "Wir schenken Geld in einem Umschlag, Markus und ich zusammen, einverstanden?"),
    L("Markus", "m", "Genau, zusammen! Schenkt jemand einen Spa-Gutschein?"),
    L("Lisa", "f", "Spa? Nein, nur Tagebuch bei mir. Schenkt jemand ein Kochbuch?"),
    L("Sara", "f", "Kochbuch nicht, nur Album. Schenkt jemand Blumen?"),
    L("Tom", "m", "Blumen? Vielleicht dazu, aber Wein ist mein Geschenk, wirklich."),
    L("Lukas", "m", "Geschirr nicht, nur Tasche bei mir. Wann feiern wir?"),
    L("Anna", "f", "Samstag um sieben, bei Julia zu Hause?"),
    L("Markus", "m", "Bis dann! Es wird toll!"),
    L("Lisa", "f", "Bis Samstag! Ich freue mich!"),
    L("Sara", "f", "Ich auch! Tschüss zusammen!"),
    L("Tom", "m", "Noch etwas: Karte schreiben wir alle zusammen, einverstanden?"),
    L("Lisa", "f", "Einverstanden! Mit vielen Grüßen und Unterschriften!"),
], check_order=["Lisa", "Sara", "Tom", "Lukas", "Anna", "Markus"])

# ---------------- TEST 24 kinder-und-erziehung ----------------
# Lukas(f Fußball) Lisa(a Klavier) Marie(c Ballett) Tim(g Malen) Anna(e Sprachen)
apply(24, [
    L("Lukas", "m", "Also, erzählt mal, welche Hobbys habt ihr? Ich spiele Fußball im Verein, zweimal Training pro Woche."),
    L("Lisa", "f", "Cool! Ich lerne Klavier, seit zwei Jahren schon, mit einer netten Lehrerin."),
    L("Marie", "f", "Schön! Ich tanze Ballett, zweimal pro Woche, mit viel Spaß und netten Freundinnen."),
    L("Tim", "m", "Ich male und zeichne viel, am liebsten Tiere, mit Buntstiften und Wasserfarben."),
    L("Anna", "f", "Und ich lerne Sprachen, Englisch in der Schule und Französisch im Kurs."),
    L("Lukas", "m", "Toll, alle sind aktiv! Geht jemand von euch reiten?"),
    L("Lisa", "f", "Reiten? Nein, nur Klavier bei mir. Macht jemand von euch Karate?"),
    L("Marie", "f", "Karate nicht, nur Ballett bei mir. Spielt jemand von euch Schach?"),
    L("Tim", "m", "Schach nicht, nur Malen bei mir. Singt jemand von euch im Kinderchor?"),
    L("Anna", "f", "Chor nicht, nur Sprachen bei mir. Treffen wir uns am Samstag alle?"),
    L("Lukas", "m", "Ja, Samstag im Park, einverstanden? Um drei Uhr nachmittags?"),
    L("Lisa", "f", "Einverstanden! Bis Samstag, ich freue mich schon!"),
    L("Marie", "f", "Bis dann! Bringt gute Laune mit, einverstanden?"),
    L("Tim", "m", "Immer! Bis Samstag, tschüss zusammen!"),
    L("Anna", "f", "Tschüss! Bis Samstag im Park!"),
], check_order=["Lukas", "Lisa", "Marie", "Tim", "Anna"])

# ---------------- TEST 25 bibliothek-und-lesen ----------------
# Mutter(i Krimis) Vater(f Biografien) Lisa(e Liebesromane) Tom(c SciFi) Marie(a Kinderbücher)
apply(25, [
    L("Mutter", "f", "Also, Buchclub! Was lest ihr gerade? Ich lese Krimis, spannend bis zum Schluss."),
    L("Vater", "m", "Schön! Ich lese Geschichtsbücher und Biografien, sehr interessant und lehrreich."),
    L("Lisa", "f", "Ich lese Liebesromane, romantisch und schön, zum Träumen."),
    L("Tom", "m", "Ich lese Science-Fiction, Zukunft und Roboter, wirklich cool."),
    L("Marie", "f", "Und ich lese Kinderbücher und Märchen, jeden Abend vor dem Schlafen."),
    L("Mutter", "f", "Schön, alle lesen! Liest jemand Gedichte?"),
    L("Vater", "m", "Gedichte? Nein, nur Geschichte bei mir, wirklich."),
    L("Lisa", "f", "Reiseberichte nicht, nur Romane bei mir."),
    L("Tom", "m", "Kochbücher nicht, nur SciFi bei mir."),
    L("Marie", "f", "Comics nicht, ich bleibe bei Märchen. Treffen wir uns nächste Woche?"),
    L("Mutter", "f", "Ja, Donnerstag um sieben, bei uns zu Hause?"),
    L("Vater", "m", "Einverstanden! Bis Donnerstag, tschüss!"),
    L("Lisa", "f", "Bis dann! Ich bringe Kuchen mit, versprochen!"),
    L("Tom", "m", "Lecker! Bis Donnerstag, tschüss zusammen!"),
    L("Marie", "f", "Noch etwas: Bücher tauschen wir danach, einverstanden?"),
    L("Mutter", "f", "Einverstanden! Tauschen macht Spaß, bis Donnerstag!"),
], check_order=["Mutter", "Vater", "Lisa", "Tom", "Marie"])

print("batch B applied")
