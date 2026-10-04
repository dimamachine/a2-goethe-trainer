#!/usr/bin/env python3
"""Rewrite T2 as direct speech, batch F3 (89-100). Verbose turns."""
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


# ---------------- TEST 89 beim-umzugsunternehmen ----------------
# Lukas(f Kartons) Lisa(h tragen) Tom(d Lkw) Sara(c aufbauen) Tim(b Essen)
apply(89, [
    L("Lukas", "m", "Also, Umzug Samstag! Wer macht was? Ich packe Kartons, schon beschriftet."),
    L("Lisa", "f", "Stark! Ich trage Möbel, mit Gurten, vorsichtig die Treppe runter."),
    L("Tom", "m", "Ich fahre den Lkw, groß mit Hebebühne, kein Problem."),
    L("Sara", "f", "Ich baue Möbel auf, Schränke und Betten, mit Werkzeug."),
    L("Tim", "m", "Und ich sorge fürs Essen, belegte Brötchen und Kaffee, für alle."),
    L("Lukas", "m", "Super Team alle! Bringt jemand Müll weg oder nicht?"),
    L("Lisa", "f", "Müll? Nein, nur Tragen bei mir, wirklich nur das."),
    L("Tom", "m", "Kinder betreut keiner hier, oder? Ich bleibe beim Fahren."),
    L("Sara", "f", "Kinder nicht, nur Aufbau. Hält jemand den Parkplatz frei?"),
    L("Tim", "m", "Parkplatz nicht, nur Essen bei mir. Putzt jemand danach?"),
    L("Lukas", "m", "Putzen später, erst Kartons. Fangen wir um sieben an alle?"),
    L("Lisa", "f", "Ja, um sieben vorm Haus, einverstanden? Mit Handschuhen?"),
    L("Tom", "m", "Einverstanden! Bis Samstag, viel Kraft uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Samstag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Samstag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Schweres zu zweit tragen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 90 im-sportgeschaeft ----------------
# Lukas(b Fahrrad) Lisa(h Schwimmbrille) Tom(i Skier) Sara(e Wanderschuhe) Tim(d Fußball)
apply(90, [
    L("Lukas", "m", "Also, Sportgeschäft! Was kauft jeder? Ich kaufe ein Fahrrad, Mountainbike, rot."),
    L("Lisa", "f", "Cool! Ich kaufe eine Schwimmbrille, dicht und bequem, blau."),
    L("Tom", "m", "Ich kaufe Skier, lang und schnell, für den Winter."),
    L("Sara", "f", "Ich kaufe Wanderschuhe, fest und wasserdicht, braun."),
    L("Tim", "m", "Und ich kaufe einen Fußball, Leder, für den Verein."),
    L("Lukas", "m", "Sportlich alle! Kauft jemand eine Yogamatte oder nicht?"),
    L("Lisa", "f", "Yoga? Nein, nur Brille bei mir, wirklich nur die."),
    L("Tom", "m", "Helm braucht keiner hier, oder? Ich bleibe bei Skiern."),
    L("Sara", "f", "Helm nicht, nur Schuhe. Kauft jemand einen Tennisschläger?"),
    L("Tim", "m", "Tennis nicht, nur Ball bei mir. Kauft jemand Hanteln?"),
    L("Lukas", "m", "Hanteln nicht, nur Rad. Testen wir alles gleich alle?"),
    L("Lisa", "f", "Ja, an der Testecke, einverstanden? Mit Beratung?"),
    L("Tom", "m", "Einverstanden! Bis dann, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis bald zusammen!"),
    L("Tim", "m", "Tschüss! Bis bald alle zusammen, sportlich!"),
    L("Lukas", "m", "Noch etwas: Kassenbon aufheben, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 91 in-der-apotheke ----------------
# Lukas(i Hustensaft) Lisa(g Tabletten) Tom(e Salbe) Sara(a Pflaster) Tim(c Vitamine)
apply(91, [
    L("Lukas", "m", "Also, Apotheke! Was braucht jeder? Ich brauche Hustensaft, starker Husten nachts."),
    L("Lisa", "f", "Gute Besserung! Ich brauche Schmerztabletten, Kopf tut weh seit gestern."),
    L("Tom", "m", "Ich brauche eine Salbe, für die Hand, nach der Arbeit."),
    L("Sara", "f", "Ich brauche Pflaster und Verband, fürs Knie, kleiner Sturz."),
    L("Tim", "m", "Und ich brauche Vitamine, für den Winter, jeden Tag eine."),
    L("Lukas", "m", "Gute Besserung alle! Braucht jemand Nasenspray oder nicht?"),
    L("Lisa", "f", "Spray? Nein, nur Tabletten bei mir, wirklich nur die."),
    L("Tom", "m", "Augentropfen braucht keiner hier, oder? Ich bleibe bei Salbe."),
    L("Sara", "f", "Tropfen nicht, nur Pflaster. Braucht jemand Fieberthermometer?"),
    L("Tim", "m", "Thermo nicht, nur Vitamine bei mir. Braucht jemand Tee gegen Husten?"),
    L("Lukas", "m", "Tee später, erst Saft. Zahlen wir zusammen alle?"),
    L("Lisa", "f", "Ja, an der Kasse, einverstanden? Mit Rezept?"),
    L("Tom", "m", "Einverstanden! Bis dann, gute Besserung uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis bald zusammen!"),
    L("Tim", "m", "Tschüss! Bis bald alle zusammen, gesund bleiben!"),
    L("Lukas", "m", "Noch etwas: Beipackzettel lesen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 92 in-der-eisdiele ----------------
# Lukas(c Schoko) Lisa(b Erdbeere) Tom(i Vanille) Sara(f Zitrone) Tim(e Pistazie)
apply(92, [
    L("Lukas", "m", "Also, Eisdiele! Welche Sorte nehmt ihr? Ich nehme Schokolade, dunkel und lecker."),
    L("Lisa", "f", "Lecker! Ich nehme Erdbeere, fruchtig und frisch, im Becher."),
    L("Tom", "m", "Ich nehme Vanille, klassisch, mit Sahne oben drauf."),
    L("Sara", "f", "Ich nehme Zitrone, sauer und frisch, im Hörnchen."),
    L("Tim", "m", "Und ich nehme Pistazie, grün und nussig, meine Lieblingssorte."),
    L("Lukas", "m", "Lecker alles! Nimmt jemand Mango oder nicht?"),
    L("Lisa", "f", "Mango? Nein, nur Erdbeere bei mir, wirklich nur die."),
    L("Tom", "m", "Joghurt will keiner hier, oder? Ich bleibe bei Vanille."),
    L("Sara", "f", "Joghurt nicht, nur Zitrone. Nimmt jemand Haselnuss?"),
    L("Tim", "m", "Haselnuss nicht, nur Pistazie bei mir. Nimmt jemand Stracciatella?"),
    L("Lukas", "m", "Stracciatella nicht, nur Schoko. Schmeckt es allen?"),
    L("Lisa", "f", "Ja, wunderbar! Noch eine Kugel, einverstanden?"),
    L("Tom", "m", "Einverstanden! Guten Appetit weiterhin, ihr Lieben!"),
    L("Sara", "f", "Euch auch! Tschüss, bis morgen zusammen!"),
    L("Tim", "m", "Tschüss! Bis morgen alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Morgen wieder hier, einverstanden? Gleiche Zeit!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 93 beim-kinderarzt ----------------
# Lukas(i Impfung) Lisa(a Fieber) Tom(g Vorsorge) Sara(c Ausschlag) Tim(e Ohren)
apply(93, [
    L("Lukas", "m", "Also, Kinderarzt! Warum seid ihr hier? Mein Sohn bekommt eine Impfung, Routine."),
    L("Lisa", "f", "Meine Tochter hat Fieber, seit gestern Abend, hoch. Tapfer bleiben!"),
    L("Tom", "m", "Meine Tochter kommt zur Vorsorgeuntersuchung, U8, alles normal."),
    L("Sara", "f", "Mein Sohn hat Hautausschlag, rote Flecken, juckt leider."),
    L("Tim", "m", "Und mein Sohn hat Ohrenschmerzen, seit nachts, weint viel."),
    L("Lukas", "m", "Gute Besserung allen Kleinen! Braucht jemand eine Augenkontrolle oder nicht?"),
    L("Lisa", "f", "Augen? Nein, nur Fieber bei uns, wirklich nur das."),
    L("Tom", "m", "Husten hat keiner hier, oder? Wir bleiben bei Vorsorge."),
    L("Sara", "f", "Husten nicht, nur Haut. Hat jemand Bauchschmerzen?"),
    L("Tim", "m", "Bauch okay, nur Ohren bei uns. Gab es eine Verletzung?"),
    L("Lukas", "m", "Sturz nicht, nur Impfung. Warten wir zusammen alle?"),
    L("Lisa", "f", "Ja, hier im Wartezimmer, einverstanden? Mit Spielzeug?"),
    L("Tom", "m", "Einverstanden! Bis gleich, gute Besserung uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis gleich zusammen!"),
    L("Tim", "m", "Tschüss! Bis gleich alle zusammen, Daumen drücken!"),
    L("Lukas", "m", "Noch etwas: Impfpässe bereithalten, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 94 an-der-tankstelle ----------------
# Lukas(f tanken) Lisa(d waschen) Tom(i Reifen) Sara(c Shop) Tim(e Luft)
apply(94, [
    L("Lukas", "m", "Also, Tankstelle! Was macht jeder? Ich tanke nur, voll, Super."),
    L("Lisa", "f", "Ich wasche das Auto, Programm mit Wachs, glänzend."),
    L("Tom", "m", "Ich prüfe den Reifendruck, alle vier, wichtig für Urlaub."),
    L("Sara", "f", "Ich kaufe im Shop ein, Kaffee und Snack, für unterwegs."),
    L("Tim", "m", "Und ich fülle Luft und Wasser nach, beides wichtig, schnell."),
    L("Lukas", "m", "Flink alle! Putzt jemand die Scheiben oder nicht?"),
    L("Lisa", "f", "Scheiben? Nein, nur Waschen bei mir, wirklich nur das."),
    L("Tom", "m", "Öl füllt keiner hier nach, oder? Ich bleibe bei Reifen."),
    L("Sara", "f", "Öl nicht, nur Shop. Kauft jemand eine Karte?"),
    L("Tim", "m", "Karte nicht, nur Luft bei mir. Saugt jemand das Auto?"),
    L("Lukas", "m", "Saugen später, erst Tanken. Fahren wir weiter alle zusammen?"),
    L("Lisa", "f", "Ja, in zehn Minuten, einverstanden? Getankt und fertig?"),
    L("Tom", "m", "Einverstanden! Bis dann, gute Fahrt uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis bald zusammen!"),
    L("Tim", "m", "Tschüss! Bis bald alle zusammen, gute Fahrt!"),
    L("Lukas", "m", "Noch etwas: Quittung mitnehmen, einverstanden? Fürs Fahrtenbuch!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 95 beim-tierfriseur ----------------
# Lukas(g Waschen) Lisa(h Haarschnitt) Tom(b Krallen) Sara(f Bürsten) Tim(a Ohren)
apply(95, [
    L("Lukas", "m", "Also, Tierfriseur! Was braucht euer Hund? Meiner wird gewaschen, nach dem Schlamm."),
    L("Lisa", "f", "Süß! Meiner bekommt einen Haarschnitt, kurz für den Sommer."),
    L("Tom", "m", "Meiner bekommt Krallen geschnitten, klackern schon auf dem Boden."),
    L("Sara", "f", "Meiner wird gebürstet, langes Fell, jeden Tag nötig."),
    L("Tim", "m", "Und bei meinem werden die Ohren gereinigt, vorsichtig und sanft."),
    L("Lukas", "m", "Schön gepflegt alle! Putzt jemand die Zähne oder nicht?"),
    L("Lisa", "f", "Zähne? Nein, nur Schnitt bei uns, wirklich nur der."),
    L("Tom", "m", "Baden tut keiner extra hier, oder? Ich bleibe bei Krallen."),
    L("Sara", "f", "Baden nicht, nur Bürsten. Färbt jemand das Fell?"),
    L("Tim", "m", "Färben nicht, nur Ohren bei uns. Pflegt jemand die Pfoten?"),
    L("Lukas", "m", "Pfoten nicht, nur Waschen. Warten wir zusammen alle?"),
    L("Lisa", "f", "Ja, hier im Wartebereich, einverstanden? Mit Hunden?"),
    L("Tom", "m", "Einverstanden! Bis gleich, viel Spaß uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis gleich zusammen!"),
    L("Tim", "m", "Tschüss! Bis gleich alle zusammen, wuff wuff!"),
    L("Lukas", "m", "Noch etwas: Leckerlis mitbringen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 96 im-blumenladen ----------------
# Lukas(a Hochzeit) Lisa(c Geburtstag) Tom(f Topfpflanzen) Sara(i Danke) Tim(b Grab)
apply(96, [
    L("Lukas", "m", "Also, Blumenladen! Für wen kauft ihr? Ich kaufe für eine Hochzeit, weiß und rosa."),
    L("Lisa", "f", "Schön! Ich kaufe für einen Geburtstag, bunt gemischt, fröhlich."),
    L("Tom", "m", "Ich kaufe Topfpflanzen für den Balkon, grün und pflegeleicht."),
    L("Sara", "f", "Ich kaufe Blumen, um mich zu bedanken, bei meiner Nachbarin."),
    L("Tim", "m", "Und ich kaufe für ein Grab, weiße Lilien, ruhig und würdevoll."),
    L("Lukas", "m", "Schöne Anlässe fast alle! Kauft jemand für die Wohnung oder nicht?"),
    L("Lisa", "f", "Wohnung? Nein, nur Geburtstag bei mir, wirklich nur das."),
    L("Tom", "m", "Entschuldigung kauft keiner hier, oder? Ich bleibe bei Töpfen."),
    L("Sara", "f", "Entschuldigung nicht, nur Danke. Kauft jemand für eine Beerdigung?"),
    L("Tim", "m", "Beerdigung ist Grab, ja, bei mir. Kauft jemand zum Muttertag?"),
    L("Lukas", "m", "Muttertag später, erst Hochzeit. Binden wir zusammen alle?"),
    L("Lisa", "f", "Ja, hier im Laden, einverstanden? Mit Schleifen?"),
    L("Tom", "m", "Einverstanden! Bis dann, viel Freude uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis bald zusammen!"),
    L("Tim", "m", "Tschüss! Bis bald alle zusammen, ruhig und schön!"),
    L("Lukas", "m", "Noch etwas: Wasser nicht vergessen, einverstanden? Frisch halten!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 97 in-der-aenderungsschneiderei ----------------
# Lukas(e Hose) Lisa(g Kleid) Tom(c Reißverschluss) Sara(h Loch) Tim(f Knöpfe)
apply(97, [
    L("Lukas", "m", "Also, Änderungsschneiderei! Was wird geändert? Bei mir Hose kürzen, zu lang."),
    L("Lisa", "f", "Bei mir Kleid enger machen, für die Feier, perfekt sitzen."),
    L("Tom", "m", "Bei mir Reißverschluss wechseln, klemmt an der Jacke."),
    L("Sara", "f", "Bei mir Loch stopfen, im Pullover, fast unsichtbar."),
    L("Tim", "m", "Und bei mir Knöpfe annähen, zwei Stück, am Mantel."),
    L("Lukas", "m", "Viel zu nähen alles! Kürzt jemand Ärmel oder nicht?"),
    L("Lisa", "f", "Ärmel? Nein, nur Kleid bei mir, wirklich nur das."),
    L("Tom", "m", "Naht näht keiner hier, oder? Ich bleibe beim Verschluss."),
    L("Sara", "f", "Naht nicht, nur Loch. Macht jemand einen Rock weiter?"),
    L("Tim", "m", "Rock nicht, nur Knöpfe bei mir. Erneuert jemand Futter?"),
    L("Lukas", "m", "Futter nicht, nur Hose. Holen wir Freitag alles ab?"),
    L("Lisa", "f", "Ja, Freitag um vier, einverstanden? Mit Zetteln?"),
    L("Tom", "m", "Einverstanden! Bis Freitag, viel Freude uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Freitag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Freitag alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Drei Tage warten, einverstanden? Geduld!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 98 im-wellnesshotel ----------------
# Lukas(g Sauna) Lisa(a Massage) Tom(i Pool) Sara(f Gesicht) Tim(e Yoga)
apply(98, [
    L("Lukas", "m", "Also, Wellnesshotel! Was macht jeder? Ich gehe in die Sauna, heiß und gut."),
    L("Lisa", "f", "Herrlich! Ich bekomme eine Massage, Rücken und Nacken, eine Stunde."),
    L("Tom", "m", "Ich schwimme im Pool, Bahnen am Morgen, fit."),
    L("Sara", "f", "Ich bekomme eine Gesichtsbehandlung, frisch und rosig."),
    L("Tim", "m", "Und ich mache Yoga, Sonnengruß am Morgen, entspannt."),
    L("Lukas", "m", "Erholt alle! Geht jemand in den Fitnessraum oder nicht?"),
    L("Lisa", "f", "Fitness? Nein, nur Massage bei mir, wirklich nur die."),
    L("Tom", "m", "Maniküre bucht keiner hier, oder? Ich bleibe beim Pool."),
    L("Sara", "f", "Maniküre nicht, nur Gesicht. Geht jemand spazieren am See?"),
    L("Tim", "m", "See später, erst Yoga bei mir. Geht jemand ins Dampfbad?"),
    L("Lukas", "m", "Dampf nicht, nur Sauna. Treffen wir uns zum Essen alle?"),
    L("Lisa", "f", "Ja, um sieben im Restaurant, einverstanden?"),
    L("Tom", "m", "Einverstanden! Bis dann, gute Erholung uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis später zusammen!"),
    L("Tim", "m", "Tschüss! Bis später alle zusammen, entspannt!"),
    L("Lukas", "m", "Noch etwas: Bademantel mitnehmen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 99 im-sprachcafe ----------------
# Lukas(c Englisch) Lisa(b Spanisch) Tom(i Französisch) Sara(h Italienisch) Tim(e Deutsch)
apply(99, [
    L("Lukas", "m", "Also, Sprachcafé! An welchen Tisch geht ihr? Ich gehe an den Englisch-Tisch, fließend üben."),
    L("Lisa", "f", "Cool! Ich gehe an den Spanisch-Tisch, für den Urlaub."),
    L("Tom", "m", "Ich gehe an den Französisch-Tisch, Aussprache üben, schwierig."),
    L("Sara", "f", "Ich gehe an den Italienisch-Tisch, mit Liedern und Spielen."),
    L("Tim", "m", "Und ich gehe an den Deutsch-Tisch, Grammatik festigen, wichtig."),
    L("Lukas", "m", "Bunt gemischt! Geht jemand an den Portugiesisch-Tisch oder nicht?"),
    L("Lisa", "f", "Portugiesisch? Nein, nur Spanisch bei mir, wirklich nur das."),
    L("Tom", "m", "Russisch spricht keiner hier, oder? Ich bleibe bei Französisch."),
    L("Sara", "f", "Russisch nicht, nur Italienisch. Geht jemand an den Arabisch-Tisch?"),
    L("Tim", "m", "Arabisch nicht, nur Deutsch bei mir. Geht jemand an den Chinesisch-Tisch?"),
    L("Lukas", "m", "Chinesisch nicht, nur Englisch. Bestellen wir Kaffee alle?"),
    L("Lisa", "f", "Ja, große Runde, einverstanden? Mit Kuchen?"),
    L("Tom", "m", "Einverstanden! Viel Spaß beim Üben euch allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis nächste Woche zusammen!"),
    L("Tim", "m", "Tschüss! Bis nächste Woche alle zusammen, pünktlich!"),
    L("Lukas", "m", "Noch etwas: Nur Deutsch... äh, nur Zielsprache sprechen, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

# ---------------- TEST 100 abschlussfeier-und-zukunftsplaene ----------------
# Lukas(i Studium) Lisa(g Ausbildung) Tom(a Ausland) Sara(f Arbeit) Tim(b Soziales Jahr)
apply(100, [
    L("Lukas", "m", "Also, nach der Schule! Was plant ihr? Ich beginne ein Studium, Medizin, in München."),
    L("Lisa", "f", "Toll! Ich beginne eine Ausbildung, zur Bankkauffrau, ab August."),
    L("Tom", "m", "Ich gehe ins Ausland, Work and Travel, ein Jahr Australien."),
    L("Sara", "f", "Ich arbeite sofort, im Café, Geld verdienen erst mal."),
    L("Tim", "m", "Und ich mache ein Soziales Jahr, im Krankenhaus, helfen."),
    L("Lukas", "m", "Spannend alles! Ist jemand noch nicht entschieden oder nicht?"),
    L("Lisa", "f", "Entschieden, ja, nur Ausbildung bei mir, wirklich nur die."),
    L("Tom", "m", "Firma gründet keiner hier, oder? Ich bleibe bei Reise."),
    L("Sara", "f", "Firma nicht, nur Job. Macht jemand ein Praktikum?"),
    L("Tim", "m", "Praktikum später, erst Soziales bei mir. Reist jemand einfach so?"),
    L("Lukas", "m", "Reisen später, erst Uni. Feiern wir den Abschluss alle?"),
    L("Lisa", "f", "Ja, Freitag in der Aula, einverstanden? Mit Eltern?"),
    L("Tom", "m", "Einverstanden! Bis Freitag, viel Glück uns allen!"),
    L("Sara", "f", "Euch auch! Tschüss, bis Freitag zusammen!"),
    L("Tim", "m", "Tschüss! Bis Freitag alle zusammen, wir schaffen das!"),
    L("Lukas", "m", "Noch etwas: In Kontakt bleiben, einverstanden? Unbedingt!"),
], check_order=["Lukas", "Lisa", "Tom", "Sara", "Tim"])

print("batch F3 applied")
