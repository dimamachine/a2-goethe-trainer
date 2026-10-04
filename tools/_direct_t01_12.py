#!/usr/bin/env python3
"""Rewrite T2 as direct speech (tests 1,3-8,10-12). Persons speak themselves."""
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
    # instruction: drop old narrator lead-in, keep the rest
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
        # first-appearance order of the 5 persons must follow items order
        mains = [s for s in seen if s in check_order]
        status = "ORDER OK" if mains == check_order else f"ORDER {mains} != {check_order}"
        print(f"   {status}")


# ---------------- TEST 1 reisen-mit-der-bahn ----------------
# Markus(i Tickets) Anna(d Hotel) Jan(g Restaurant) Lisa(b Museum) Vater(f Bahnhof)
apply(1, [
    L("Markus", "m", "Also, unser Berlin-Wochenende steht! Verteilen wir die Aufgaben, einverstanden?"),
    L("Anna", "f", "Gute Idee! Ich buche das Hotel, eine schöne Pension im Zentrum, direkt am Bahnhof, mit Frühstück."),
    L("Markus", "m", "Perfekt! Ich buche die Zugtickets, mit der Bahn-App kenne ich die besten Verbindungen, ganz einfach."),
    L("Jan", "m", "Und ich reserviere das Restaurant für Samstagabend, einen Italiener, sehr lecker."),
    L("Lisa", "f", "Schön! Ich kaufe die Museum-Tickets für Sonntag, für das Pergamon-Museum, schon gekauft."),
    L("Vater", "m", "Und ich fahre euch morgens zum Bahnhof, ich muss sowieso früh raus zur Arbeit."),
    L("Anna", "f", "Danke! Wer kauft die Snacks für den Zug?"),
    L("Markus", "m", "Snacks kaufen wir zusammen am Bahnhof, einverstanden?"),
    L("Jan", "m", "Einverstanden! Und die Koffer packt jeder selbst, oder?"),
    L("Lisa", "f", "Ja, jeder packt selbst! Das Wetter wird gut, hoffe ich."),
    L("Vater", "m", "Genau, jeder packt selbst! Ich fahre pünktlich um acht los."),
    L("Anna", "f", "Und der Hund? Bleibt er allein?"),
    L("Lisa", "f", "Der Nachbar hütet den Hund, alles ist organisiert."),
    L("Markus", "m", "Super! Dann sind wir startklar für Berlin, ich freue mich!"),
    L("Anna", "f", "Ich auch! Berlin, wir kommen! Bis Freitag am Bahnhof!"),
], check_order=["Markus", "Anna", "Jan", "Lisa", "Vater"])

# ---------------- TEST 3 im-restaurant-und-cafe ----------------
# Anna(b Kuchen) Markus(g Wein) Tim(h alkoholfrei) Mutter(d? no: Mutter(a Hauptgericht)) Sara(d Salat)
apply(3, [
    L("Anna", "f", "Also, unser großes Familienfest am Samstag! Verteilen wir das Essen, einverstanden? Ich backe einen Schokoladenkuchen."),
    L("Markus", "m", "Sehr gut! Ich bringe Wein mit, roten und weißen, vom guten Laden an der Ecke."),
    L("Tim", "m", "Und ich bringe alkoholfreie Getränke mit, für die Kinder und für Oma, zwei Kästen."),
    L("Mutter", "f", "Wunderbar! Ich koche das Hauptgericht, wie immer, mit viel Liebe und guten Zutaten."),
    L("Sara", "f", "Und ich mache einen großen Salat, frisch aus dem Garten, mit Tomaten und Gurken."),
    L("Anna", "f", "Klingt alles lecker! Wer bringt Eis mit für den Nachtisch?"),
    L("Markus", "m", "Eis? Hmm, keiner, glaube ich. Tim, du hast doch ein Auto mit Kühlung?"),
    L("Tim", "m", "Nein, Eis transportiere ich nicht. Ich habe schon die Getränke, das reicht."),
    L("Mutter", "f", "Brot bringt auch keiner mit? Egal, wir haben genug Brot zu Hause, frisches."),
    L("Sara", "f", "Stimmt! Und ein Geschenk braucht zum Glück keiner, wir feiern einfach zusammen."),
    L("Anna", "f", "Genau, keine Geschenke! Brauchen wir noch eine Käseplatte dazu?"),
    L("Markus", "m", "Käseplatte lassen wir weg, wir haben schon genug Auswahl, finde ich."),
    L("Tim", "m", "Einverstanden! Wann fangen wir an, um drei Uhr bei euch?"),
    L("Mutter", "f", "Ja, um drei bei uns! Ich freue mich schon sehr auf Samstag!"),
], check_order=["Anna", "Markus", "Tim", "Mutter", "Sara"])

# ---------------- TEST 4 schule-und-sprachkurs ----------------
# Anna(i Algebra) Markus(e Geometrie) Sara(b Wahrscheinlichkeit) Lisa(f Statistik) Tobias(a Funktionen)
apply(4, [
    L("Anna", "f", "Also, Matheprüfung nächste Woche! Teilen wir die Themen? Ich mache Algebra."),
    L("Markus", "m", "Gute Idee! Ich mache Geometrie, Dreiecke und Kreise, das kann ich gut."),
    L("Sara", "f", "Und ich mache Wahrscheinlichkeit, mit Würfeln und Karten, spannend!"),
    L("Lisa", "f", "Ich nehme Statistik, Diagramme lesen und Mittelwerte, kein Problem."),
    L("Tobias", "m", "Dann mache ich Funktionen und Diagramme zeichnen, das ist mein Thema, wirklich."),
    L("Anna", "f", "Super, alle Themen verteilt! Wer bringt Snacks und Getränke mit?"),
    L("Markus", "m", "Snacks? Keiner, wir lernen doch, kein Picknick. Oder, Tobias?"),
    L("Tobias", "m", "Nein, ich bringe keine Snacks. Nur meine Hefte und Stifte."),
    L("Sara", "f", "Und den Raum organisiert niemand? Wo lernen wir überhaupt?"),
    L("Lisa", "f", "In der Bibliothek, leise und ruhig. Bücher bringen wir selbst mit, oder?"),
    L("Anna", "f", "Ja, jeder bringt seine Bücher mit! Macht jemand eine Präsentation?"),
    L("Markus", "m", "Nein, keine Präsentation, nur zusammen üben. Wann fangen wir an?"),
    L("Tobias", "m", "Morgen um vier bei mir? Platz haben wir genug, keine Sorge."),
    L("Sara", "f", "Perfekt, morgen um vier! Bis dann, viel Erfolg uns!"),
], check_order=["Anna", "Markus", "Sara", "Lisa", "Tobias"])

# ---------------- TEST 5 wohnen-und-umzug ----------------
# Anna(g Lkw) Markus(d Küche) Lisa(e Bücher) Tim(h putzen) Vater(b Internet)
apply(5, [
    L("Anna", "f", "Also, Toms Umzug nächste Woche! Helfen wir alle? Ich hole den Lkw, ich habe den großen Führerschein."),
    L("Markus", "m", "Super! Ich packe die Küche, Geschirr und Pfannen, schnell und gut organisiert."),
    L("Lisa", "f", "Und ich packe die Bücher, ich habe schon Kartons besorgt, komme Donnerstag."),
    L("Tim", "m", "Ich putze die alte Wohnung, mit Putzzeug, am Tag danach, für die Kaution."),
    L("Vater", "m", "Und ich richte das Internet ein, Router und WLAN, gleich am ersten Tag."),
    L("Anna", "f", "Perfekt verteilt! Wer meldet den Strom an?"),
    L("Markus", "m", "Strom? Nicht ich, ich habe die Küche. Vielleicht Tom selbst?"),
    L("Lisa", "f", "Ja, Tom macht den Strom selbst. Und wer dekoriert die neue Wohnung?"),
    L("Tim", "m", "Dekorieren? Keiner jetzt, erst alles auspacken. Oder, Vater?"),
    L("Vater", "m", "Nein, keine Deko von mir, nur Technik. Kauft Tom neue Möbel?"),
    L("Anna", "f", "Keine neuen Möbel, alles kommt mit. Und Pizza für alle?"),
    L("Markus", "m", "Pizza bringt Tom selbst, als Belohnung für uns alle."),
    L("Lisa", "f", "Sehr gut! Wann geht es los, Samstag um acht?"),
    L("Tim", "m", "Ja, Samstag um acht! Bis dann, wir schaffen das!"),
], check_order=["Anna", "Markus", "Lisa", "Tim", "Vater"])

# ---------------- TEST 6 beim-arzt-und-in-der-apotheke ----------------
# Mama(e Massage) Papa(c Sauna) Tante Eva(f Gesicht) Onkel Robert(g Yoga) Lisa(i Maniküre)
apply(6, [
    L("Lisa", "f", "Also, unser Wellness-Tag am Samstag! Was macht jeder? Ich lasse eine Maniküre machen."),
    L("Mama", "f", "Schön! Ich lasse eine Rückenmassage machen, gegen meine Schmerzen, endlich mal."),
    L("Papa", "m", "Ich gehe nicht zur Massage, komisch. Ich nehme die Sauna, lang und heiß."),
    L("Tante Eva", "f", "Und ich buche eine Gesichtsbehandlung, für meine Haut, regelmäßig."),
    L("Onkel Robert", "m", "Dann probiere ich Yoga, eine Stunde für Anfänger, zum ersten Mal, ich bin gespannt."),
    L("Lisa", "f", "Yoga, mutig! Wer macht Akupunktur mit?"),
    L("Mama", "f", "Akupunktur? Nein, nur Massage für mich. Du, Papa?"),
    L("Papa", "m", "Nein, nur Sauna. Geht jemand zum Friseur danach?"),
    L("Tante Eva", "f", "Friseur nicht, keine Zeit. Geht jemand schwimmen?"),
    L("Onkel Robert", "m", "Schwimmen nicht, nur Yoga. Und Fußmassage will keiner?"),
    L("Lisa", "f", "Fußmassage nicht, nur Maniküre bei mir. Wann treffen wir uns?"),
    L("Mama", "f", "Um zehn am Eingang, einverstanden?"),
    L("Papa", "m", "Einverstanden! Und danach essen wir zusammen."),
    L("Tante Eva", "f", "Perfekt! Bis Samstag, ich freue mich!"),
], check_order=["Lisa", "Mama", "Papa", "Tante Eva", "Onkel Robert"])

# ---------------- TEST 7 im-buero-und-arbeitsleben ----------------
# Jonas(h Location) Lisa(c Catering) Robert(d DJ) Tanja(i Getränke) Anna(g Deko)
apply(7, [
    L("Anna", "f", "Also, unsere Sommer-Feier! Wer macht was? Ich mache die Dekoration."),
    L("Jonas", "m", "Gut! Ich organisiere die Location, eine schöne Halle, noch frei."),
    L("Lisa", "f", "Und ich kümmere mich um das Catering, warmes Essen für 50 Personen."),
    L("Robert", "m", "Ich bin DJ und bringe die Anlage mit, den ganzen Abend Musik."),
    L("Tanja", "f", "Und ich besorge die Getränke, Bier, Wein und Limonade vom Großmarkt."),
    L("Anna", "f", "Super, alles verteilt! Wer hält eine Rede?"),
    L("Jonas", "m", "Rede? Nicht ich, ich organisiere nur. Du, Robert?"),
    L("Robert", "m", "Nein, keine Rede, nur Musik von mir. Wer fotografiert den Abend?"),
    L("Lisa", "f", "Fotografieren? Keiner, wir feiern doch. Oder du, Tanja?"),
    L("Tanja", "f", "Nein, nur Getränke bei mir. Wer schickt die Einladungen?"),
    L("Anna", "f", "Die Einladungen schickt keiner bisher. Machen wir das zusammen?"),
    L("Jonas", "m", "Ja, zusammen online, ganz schnell. Bringt jemand einen Kuchen mit?"),
    L("Lisa", "f", "Kuchen? Nein, Catering reicht doch. Wann fangen wir an?"),
    L("Tanja", "f", "Um sechs am Freitag! Bis dann, es wird super!"),
], check_order=["Anna", "Jonas", "Lisa", "Robert", "Tanja"])

# ---------------- TEST 8 urlaub-und-reisen-planen ----------------
# Mama(e Hotel) Papa(h Auto) Lisa(a Ausflüge) Tante Eva(i kochen) Tim(b Hund)
apply(8, [
    L("Mama", "f", "Also, unser Urlaub im August! Planen wir alles? Ich buche das Hotel am Bodensee."),
    L("Papa", "m", "Sehr gut! Ich fahre das Auto, das große, mit viel Platz."),
    L("Lisa", "f", "Und ich plane die Tagesausflüge, Schwimmen, Wandern und ein Museum, alles organisiert."),
    L("Tante Eva", "f", "Schön! Ich koche einmal am Tag warm, günstiger als Restaurants."),
    L("Tim", "m", "Und ich kümmere mich um den Hund, Futter und Spaziergänge, alles, versprochen."),
    L("Mama", "f", "Perfekt! Wer kauft Souvenirs?"),
    L("Papa", "m", "Souvenirs? Später vielleicht, jetzt nicht. Wer organisiert Konzertkarten?"),
    L("Lisa", "f", "Konzertkarten? Keine Zeit dafür. Wer wäscht die Kleidung?"),
    L("Tante Eva", "f", "Wäsche waschen wir zu Hause, nicht im Urlaub, wirklich nicht."),
    L("Tim", "m", "Fotos machen wir alle zusammen, einverstanden?"),
    L("Mama", "f", "Einverstanden! Wann fahren wir los, Samstag früh?"),
    L("Papa", "m", "Ja, Samstag früh um sieben! Bis dann!"),
    L("Lisa", "f", "Um sieben, ich stelle den Wecker! Ich freue mich schon!"),
    L("Tante Eva", "f", "Ich auch! Das wird ein schöner Urlaub zusammen!"),
], check_order=["Mama", "Papa", "Lisa", "Tante Eva", "Tim"])

# ---------------- TEST 10 einkaufen-und-geschaefte ----------------
# Anna(a Blumen) Markus(h Wein) Lisa(b Buffet) Tom(f Musik) Sara(i Eis)
apply(10, [
    L("Anna", "f", "Also, unsere Einweihungsparty! Wer bringt was mit? Ich kaufe Blumen."),
    L("Markus", "m", "Schön! Ich kümmere mich um Wein und Sekt, aus dem guten Laden."),
    L("Lisa", "f", "Und ich mache das Buffet, Käse, Brot, Oliven und kleine Salate, alles frisch."),
    L("Tom", "m", "Ich organisiere die Musik, mit meiner Sammlung auf dem Handy."),
    L("Sara", "f", "Und ich bringe Eis mit, drei Sorten, am Tag der Party, versprochen."),
    L("Anna", "f", "Super! Bringt jemand selbstgebackene Kuchen mit?"),
    L("Markus", "m", "Kuchen? Nein, Lisa macht doch Buffet. Oder, Tom?"),
    L("Tom", "m", "Nein, nur Musik bei mir. Wer putzt die Wohnung?"),
    L("Lisa", "f", "Putzen wir alle zusammen am Samstag vorher?"),
    L("Sara", "f", "Gute Idee, zusammen! Wer macht Fotos auf der Party?"),
    L("Anna", "f", "Fotos machen wir alle, mit den Handys, einverstanden?"),
    L("Markus", "m", "Einverstanden! Bringt jemand ein Geschenk mit?"),
    L("Tom", "m", "Geschenk nicht nötig, nur gute Laune! Wann geht es los?"),
    L("Sara", "f", "Um sieben am Samstag! Bis dann, es wird toll!"),
], check_order=["Anna", "Markus", "Lisa", "Tom", "Sara"])

# ---------------- TEST 11 termine-und-telefon ----------------
# Vater(h Arzt) Mutter(a Bürgeramt) Tim(f TÜV) Lisa(g Tierarzt) Anna(b Bank)
apply(11, [
    L("Anna", "f", "Also, vor der Reise viele Termine! Verteilen wir sie? Ich gehe zur Bank."),
    L("Vater", "m", "Gute Idee! Ich buche den Arzt-Termin für die Impfung, beim Hausarzt, schnell gemacht."),
    L("Mutter", "f", "Und ich gehe zum Bürgeramt für den Reisepass, freitags habe ich Zeit, kann früh dort sein."),
    L("Tim", "m", "Ich mache den TÜV-Termin fürs Auto, kein Problem für mich."),
    L("Lisa", "f", "Und ich bringe die Katze zum Tierarzt, ich wohne ja in der Nähe, gern."),
    L("Anna", "f", "Super! Wer macht den Versicherungs-Termin?"),
    L("Vater", "m", "Versicherung? Nicht ich, ich habe den Arzt. Du, Tim?"),
    L("Tim", "m", "Nein, nur TÜV bei mir, versprochen. Wer geht zum Friseur?"),
    L("Lisa", "f", "Friseur nicht, keine Zeit. Wer braucht den Zahnarzt?"),
    L("Mutter", "f", "Zahnarzt keiner, alle gesund. Und der Optiker-Termin?"),
    L("Anna", "f", "Optiker auch keiner, meine Brille ist okay, wirklich. Wann starten wir?"),
    L("Vater", "m", "Morgen früh! Alle Termine diese Woche, keine Ausreden."),
    L("Mutter", "f", "Einverstanden! Dann ist alles abgedeckt, super."),
    L("Tim", "m", "Perfekt! Bis morgen, viel Erfolg uns allen!"),
], check_order=["Anna", "Vater", "Mutter", "Tim", "Lisa"])

# ---------------- TEST 12 tiere-und-haustiere ----------------
# Lisa(e Hund) Mutter(c Katze) Tim(i Vogel) Vater(h Fische) Lukas(f Post)
apply(12, [
    L("Lisa", "f", "Also, nächste Woche brauche ich Hilfe mit den Tieren! Wer macht was? Ich gehe mit Bruno spazieren, zweimal am Tag."),
    L("Mutter", "f", "Gut! Ich füttere die Katze, ich wohne in der Nähe, kurzer Weg."),
    L("Tim", "m", "Und ich kümmere mich um den Vogel, Wasser, Futter, Käfig sauber."),
    L("Vater", "m", "Ich übernehme die Fische, ich kenne mich aus seit der Kindheit."),
    L("Lukas", "m", "Und ich hole die Post und schaue nach der Wohnung, jeden zweiten Tag."),
    L("Lisa", "f", "Perfekt! Wer wäscht die Wäsche?"),
    L("Mutter", "f", "Wäsche? Nicht ich, nur die Katze. Du, Tim?"),
    L("Tim", "m", "Nein, nur der Vogel bei mir. Muss jemand zum Tierarzt?"),
    L("Vater", "m", "Tierarzt nicht nötig, alle gesund. Wer putzt die Wohnung?"),
    L("Lukas", "m", "Putzen? Nur schauen und Post holen bei mir. Wer kauft Tierfutter?"),
    L("Lisa", "f", "Tierfutter ist noch genug da, kein Einkaufen nötig!"),
    L("Mutter", "f", "Super! Wann fährst du los, Lisa?"),
    L("Lisa", "f", "Montag früh! Danke euch allen, ihr seid toll!"),
    L("Tim", "m", "Gern! Erhol dich gut im Urlaub!"),
], check_order=["Lisa", "Mutter", "Tim", "Vater", "Lukas"])

print("batch A applied")
