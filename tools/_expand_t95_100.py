#!/usr/bin/env python3
"""Expand Goethe A2 Hören tests 95-100 to official length. Temporary mutator."""
import json
import re
from pathlib import Path

TOOLS = Path(__file__).resolve().parent


def W(text):
    return len(re.findall(r"[A-Za-zÄÖÜäöüß]+", text))


def L(speaker, gender, text):
    return {"speaker": speaker, "gender": gender, "text": text}


def apply(n, t1=None, t2=None, t3=None, t4=None):
    path = TOOLS / f"_test{n}_data.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    teile = data["teile"]
    if t1:
        for i, text in t1.items():
            teile[0]["items"][i]["transcript"] = text
    if t2:
        teile[1]["lines"] = t2
    if t3:
        for i, lines in enumerate(t3):
            teile[2]["items"][i]["lines"] = lines
    if t4 is not None:
        teile[3]["transcript"] = t4
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    t1w = [W(it["transcript"]) for it in teile[0]["items"]]
    t2w = sum(W(x["text"]) for x in teile[1]["lines"])
    t3w = [sum(W(x["text"]) for x in it["lines"]) for it in teile[2]["items"]]
    t4w = sum(W(x["text"]) for x in teile[3]["transcript"])
    print(f"T{n} T1={t1w} avg={sum(t1w)/5:.0f} T2={t2w}w/{len(teile[1]['lines'])}t T3={t3w} avg={sum(t3w)/5:.0f} { [len(it['lines']) for it in teile[2]['items']] } T4={t4w}w/{len(teile[3]['transcript'])}t")


# ── 95 Beim Tierfriseur ───────────────────────────────────────────
apply(
    95,
    t2=[
        L("Anna", "f", "Hallo Markus, alle gehen mit dem Hund zum Tierfriseur. Was braucht jeder Hund?"),
        L("Markus", "m", "Also, Lukas' Hund wird gewaschen — er hat sich im Schlamm gewälzt. Die Zähne putzen sie nicht."),
        L("Anna", "f", "Typisch. Und Lisas Hund? Das Fell ist doch so lang."),
        L("Markus", "m", "Lisas Hund bekommt einen Haarschnitt — das Fell ist viel zu lang geworden. Färben will sie nicht."),
        L("Anna", "f", "Gut. Und Toms Hund? Der klickt auf dem Boden, oder?"),
        L("Markus", "m", "Bei Toms Hund werden die Krallen geschnitten — die sind viel zu lang. Baden mit Spezial-Shampoo braucht er nicht."),
        L("Anna", "f", "Und Saras Hund? Der haart so stark."),
        L("Markus", "m", "Saras Hund wird gebürstet — er haart stark und das Fell ist verfilzt. Die Pfoten pflegt sie zu Hause."),
        L("Anna", "f", "Und Tims Hund? Der hat oft Probleme mit den Ohren."),
        L("Markus", "m", "Bei Tims Hund werden die Ohren gereinigt — er hat oft Probleme damit. Einen Haarschnitt braucht er nicht."),
        L("Anna", "f", "Dann hat jeder Hund die richtige Behandlung. Gehst du auch hin?"),
        L("Markus", "m", "Nächste Woche, ja. Mein Hund braucht nur eine Wäsche, das geht schnell."),
        L("Anna", "f", "Ruf vorher an, die Termine sind oft voll, besonders samstags."),
        L("Markus", "m", "Mache ich, danke für den Tipp. Samstagvormittag wäre mir am liebsten."),
    ],
    t3=[
        [
            L("Kundin", "f", "Was kostet das Waschen? 25 Euro, 40 Euro oder nur 15 Euro?"),
            L("Tierfriseur", "m", "Bei einem kleinen Hund 25 Euro. 15 Euro wäre zu wenig, 40 Euro ist der Preis für große Hunde."),
            L("Kundin", "f", "Und bei einem großen? 40 oder bleiben 25?"),
            L("Tierfriseur", "m", "Bei einem großen 40 Euro. Nicht 25 und nicht 15, ein großer Hund kostet 40."),
            L("Kundin", "f", "Verstehe, dann 40 Euro für meinen Großen. Danke."),
        ],
        [
            L("Mann", "m", "Mein Hund hat Angst vor dem Föhn. Geht es mit dem Handtuch oder an der Luft?"),
            L("Tierfriseurin", "f", "Kein Problem, wir trocknen mit dem Handtuch. Der Föhn muss nicht sein, an der Luft dauert es zu lang."),
            L("Mann", "m", "Dauert das nicht länger als mit dem Föhn?"),
            L("Tierfriseurin", "f", "Ein bisschen, aber der Hund bleibt ruhig. Also mit dem Handtuch, nicht mit dem Föhn, nicht an der Luft."),
            L("Mann", "m", "Perfekt, dann bitte mit dem Handtuch. Danke."),
        ],
        [
            L("Frau", "f", "Wie kurz soll das Fell werden? Der Hund ist nicht krank, und teurer soll es nicht sein."),
            L("Tierfriseur", "m", "Wie möchten Sie es? Weil er krank ist, oder weil es bald Winter wird?"),
            L("Frau", "f", "Nicht zu kurz, es ist bald Winter. Er ist nicht krank, und der Preis ist okay."),
            L("Tierfriseur", "m", "Gute Idee, dann etwas kürzen. Wegen des Winters, nicht weil er krank ist, nicht wegen des Preises."),
            L("Frau", "f", "Genau, wegen des Winters. Danke."),
        ],
        [
            L("Kunde", "m", "Wie lange dauert die Behandlung? Soll ich warten, oder später abholen, oder helfen?"),
            L("Tierfriseurin", "f", "Etwa zwei Stunden. Warten müssen Sie nicht, und helfen auch nicht, das stört den Hund."),
            L("Kunde", "m", "Soll ich warten? Oder später abholen? Helfen darf ich nicht, oder?"),
            L("Tierfriseurin", "f", "Nein, holen Sie ihn später ab. Nicht warten und nicht helfen, später abholen ist am besten."),
            L("Kunde", "m", "Gut, dann hole ich ihn in zwei Stunden ab. Danke."),
        ],
        [
            L("Kundin", "f", "Brauche ich einen Termin? Nie, nur am Wochenende, oder am besten anrufen?"),
            L("Tierfriseur", "m", "Ja, am besten anrufen. Nie ohne Termin ist riskant, und nur am Wochenende stimmt nicht."),
            L("Kundin", "f", "Geht es auch ohne? Also nie anrufen, oder nur am Wochenende?"),
            L("Tierfriseur", "m", "Nur wenn gerade jemand absagt. Am besten anrufen, nicht nie und nicht nur am Wochenende."),
            L("Kundin", "f", "Verstanden, ich rufe an. Danke."),
        ],
    ],
    t4=[
        L("Reporter", "m", "Frau Kraus, was machen Sie genau bei der Arbeit?"),
        L("Kraus", "f", "Ich pflege das Fell von Hunden und Katzen. Ich wasche, schneide und bürste sie. Das ist der Hauptteil meiner Arbeit, jeden Tag."),
        L("Reporter", "m", "Ist die Arbeit mit den Tieren schwer? Kann man mit ängstlichen Tieren hektisch sein?"),
        L("Kraus", "f", "Manchmal, viele Tiere haben Angst. Ich brauche viel Geduld und Ruhe. Mit ängstlichen Tieren darf man nicht hektisch sein, sonst wird es schlimmer."),
        L("Reporter", "m", "Sollen die Besitzer das Fell selbst pflegen, zum Beispiel bürsten?"),
        L("Kraus", "f", "Das Bürsten ja. Aber das Schneiden ist schwer. Dafür kommen Sie besser zu mir. Das Bürsten sollen die Besitzer selbst machen, am besten jede Woche."),
        L("Reporter", "m", "Wollen die Leute manchmal seltsame Sachen, zum Beispiel den Hund bunt färben?"),
        L("Kraus", "f", "Ja, manche wollen den Hund bunt färben. Das mache ich nicht. Ein Tier ist kein Spielzeug. Ich färbe Hunde nicht gern bunt, das mag ich nicht."),
        L("Reporter", "m", "Was lieben Sie an Ihrem Beruf? Arbeiten Sie gern mit Tieren?"),
        L("Kraus", "f", "Ich liebe Tiere. Aus einem traurigen Tier wird ein glückliches. Ich arbeite sehr gern mit Tieren, das ist der schönste Teil."),
    ],
)

# ── 96 Im Blumenladen ─────────────────────────────────────────────
apply(
    96,
    t1={
        0: "Guten Tag, hier ist der Blumenladen Rosengarten. Ihr bestellter Strauß für die Hochzeit ist fertig. Aber wir hatten keine weißen Rosen mehr, deshalb haben wir cremefarbene genommen, die passen sehr gut. Zu teuer waren die weißen nicht, es gab einfach keine mehr. Sie können ihn am Samstag ab 9 Uhr abholen. Bis dann, auf Wiederhören!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, alle kaufen gerade Blumen. Wofür braucht jeder welche?"),
        L("Markus", "m", "Also, Lukas kauft Blumen für eine Hochzeit — er ist eingeladen und braucht einen Strauß. Zur Entschuldigung ist das nicht."),
        L("Anna", "f", "Schön. Und Lisa? Ihre beste Freundin hat Geburtstag, oder?"),
        L("Markus", "m", "Lisa kauft Blumen für einen Geburtstag — für ihre beste Freundin. Zum Muttertag kauft sie extra."),
        L("Anna", "f", "Und Tom? Der macht den Balkon neu."),
        L("Markus", "m", "Tom kauft Topfpflanzen für den Balkon — er macht es sich draußen schön. Für die Wohnung nimmt er nichts."),
        L("Anna", "f", "Und Sara? Eine Kollegin hat ihr geholfen."),
        L("Markus", "m", "Sara kauft Blumen, um sich zu bedanken — bei einer Kollegin, die ihr geholfen hat. Eine Beerdigung ist das nicht."),
        L("Anna", "f", "Und Tim? Er besucht das Grab, habe ich gehört."),
        L("Markus", "m", "Tim kauft Blumen für ein Grab — er besucht das Grab seiner Großmutter. Kein Geburtstag, nur das Grab."),
        L("Anna", "f", "Dann hat jeder einen guten Grund. Gehst du auch in den Laden?"),
        L("Markus", "m", "Ja, ich brauche etwas für den Tisch zu Hause, nur ein kleiner Strauß."),
        L("Anna", "f", "Nimm Tulpen, die halten lange. Der Laden an der Ecke ist gut."),
        L("Markus", "m", "Gute Idee, Tulpen nehme ich. Bis später dann."),
    ],
    t3=[
        [
            L("Kundin", "f", "Guten Tag, was kostet ein bunter Strauß? 15 Euro, 25 oder schon 35?"),
            L("Floristin", "f", "Ab 15 Euro, je nach Größe. 35 Euro wäre ein sehr großer Strauß."),
            L("Kundin", "f", "Einen schönen großen, bitte. 25 oder 35?"),
            L("Floristin", "f", "Dann nehmen wir den für 25 Euro. Nicht 15 und nicht 35, 25 Euro ist ein schöner großer Strauß."),
            L("Kundin", "f", "Perfekt, dann 25 Euro. Danke."),
        ],
        [
            L("Mann", "m", "Welche Blumen halten lange? Rosen, Tulpen und Nelken, oder keine?"),
            L("Florist", "m", "Tulpen und Nelken halten gut. Rosen halten kürzer, und keine wäre falsch."),
            L("Mann", "m", "Und Rosen? Halten die so lang wie Tulpen und Nelken?"),
            L("Florist", "m", "Die halten leider nicht so lange. Also Tulpen und Nelken, nicht Rosen, und nicht keine."),
            L("Mann", "m", "Dann Tulpen und Nelken, bitte. Danke."),
        ],
        [
            L("Frau", "f", "Können Sie eine Karte dazulegen? Zum Geburtstag, zur Hochzeit oder gute Besserung?"),
            L("Floristin", "f", "Gern. Was soll draufstehen? Hochzeit und gute Besserung gehen auch."),
            L("Frau", "f", "Alles Gute zum Geburtstag. Nicht zur Hochzeit und nicht gute Besserung."),
            L("Floristin", "f", "Mache ich, kein Problem. Alles Gute zum Geburtstag, nicht zur Hochzeit, nicht gute Besserung."),
            L("Frau", "f", "Danke, das reicht. Nur der Geburtstagstext."),
        ],
        [
            L("Kunde", "m", "Liefern Sie auch heute noch? Oder erst morgen, oder übermorgen?"),
            L("Florist", "m", "Ja, bis 17 Uhr bestellt, heute geliefert. Morgen und übermorgen gehen auch, aber heute klappt es oft."),
            L("Kunde", "m", "Es ist jetzt 16 Uhr. Also noch heute, nicht morgen?"),
            L("Florist", "m", "Dann klappt es noch heute. Nicht morgen und nicht übermorgen, noch heute."),
            L("Kunde", "m", "Super, dann bitte noch heute liefern. Danke."),
        ],
        [
            L("Kundin", "f", "Wie oft muss ich diese Pflanze gießen? Jeden Tag, zweimal die Woche oder einmal im Monat?"),
            L("Floristin", "f", "Zweimal die Woche reicht. Jeden Tag wäre zu viel, einmal im Monat zu wenig."),
            L("Kundin", "f", "Und in die Sonne? Also nicht jeden Tag gießen?"),
            L("Floristin", "f", "Nein, lieber an einen hellen Platz ohne pralle Sonne. Gießen Sie zweimal die Woche, nicht jeden Tag, nicht einmal im Monat."),
            L("Kundin", "f", "Gut, zweimal die Woche. Danke für den Tipp."),
        ],
    ],
    t4=[
        L("Reporter", "m", "Frau Blum, wann haben Sie am meisten zu tun im Laden?"),
        L("Blum", "f", "Am Valentinstag, am Muttertag und an Weihnachten. Dann ist sehr viel los. Am Muttertag habe ich besonders viel zu tun, das Geschäft ist voll."),
        L("Reporter", "m", "Was soll man beim Blumenkauf beachten, zum Beispiel die Jahreszeit?"),
        L("Blum", "f", "Kaufen Sie Blumen der Jahreszeit. Sie sind frischer und halten länger. Das rate ich immer, Blumen der Jahreszeit sind die beste Wahl."),
        L("Reporter", "m", "Verschenken Männer und Frauen andere Blumen? Kaufen Männer oft rote Rosen?"),
        L("Blum", "f", "Ein bisschen. Männer kaufen oft rote Rosen, Frauen lieber bunte Sträuße. Das sehe ich fast jedes Wochenende."),
        L("Reporter", "m", "Ist Ihr Beruf anstrengend, oder gar nicht?"),
        L("Blum", "f", "Ja, schon. Ich stehe früh auf und trage schwere Eimer mit Wasser. Der Beruf ist anstrengend, nicht leicht, aber ich mache ihn gern."),
        L("Reporter", "m", "Was ist das Schönste an Ihrem Beruf? Finden Sie ihn schön?"),
        L("Blum", "f", "Ich mache die Menschen glücklich. Mit Blumen kann man Danke sagen. Ich finde meinen Beruf sehr schön, das ist der Grund, warum ich bleibe. Auch an langen Tagen im Laden macht die Arbeit Freude."),
    ],
)

# ── 97 In der Änderungsschneiderei ────────────────────────────────
apply(
    97,
    t1={
        2: "Achtung Kunden: Bitte beachten Sie unsere Preise genau. Eine Hose kürzen kostet 12 Euro, einen Reißverschluss wechseln 15 Euro. Ein Knopf annähen ist günstig, nur 3 Euro, nicht 12 und nicht 15. Für größere Änderungen machen wir vorher ein Angebot. Express gegen Aufpreis. Fragen Sie einfach, wir beraten Sie gern!",
        4: "Liebe Kunden: Werfen Sie kaputte Kleidung nicht weg. Oft können wir sie reparieren — ein Loch stopfen, eine Naht nähen, einen Reißverschluss erneuern. Das spart Geld und schont die Umwelt. Reparieren statt wegwerfen ist wieder modern, besser als neue Kleidung zu kaufen. Bringen Sie Ihre Lieblingsstücke zu uns. Wir helfen gern!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, alle bringen Kleidung zur Schneiderei. Was lässt jeder machen?"),
        L("Markus", "m", "Also, Lukas lässt seine Hose kürzen — sie ist zu lang für ihn. Die Ärmel sind in Ordnung."),
        L("Anna", "f", "Klassisch. Und Lisa? Sie hat doch abgenommen."),
        L("Markus", "m", "Lisa lässt ihr Kleid enger machen — sie hat etwas abgenommen. Weiter machen muss sie nichts."),
        L("Anna", "f", "Und Tom? Seine Jacke klemmt, oder?"),
        L("Markus", "m", "Tom lässt einen Reißverschluss wechseln — der an seiner Jacke ist kaputt. Das Futter ist noch gut."),
        L("Anna", "f", "Und Sara? Ihr Pullover hat ein Loch."),
        L("Markus", "m", "Sara lässt ein Loch stopfen — in ihrem Lieblingspullover. Eine Naht nähen muss sie nicht extra."),
        L("Anna", "f", "Und Tim? An seinem Hemd fehlen Knöpfe."),
        L("Markus", "m", "Tim lässt Knöpfe annähen — an seinem Hemd sind zwei abgefallen. Kürzen muss er nichts."),
        L("Anna", "f", "Dann hat jeder eine kleine Änderung. Wann ist das fertig, weißt du das?"),
        L("Markus", "m", "Meistens in drei Tagen. Express geht bis morgen, aber das kostet extra."),
        L("Anna", "f", "Ich warte lieber die drei Tage. Das spart Geld und Stress."),
        L("Markus", "m", "Ja, das mache ich auch. Die Schneiderin ist sehr zuverlässig und nett."),
    ],
    t3=[
        [
            L("Kundin", "f", "Wann ist die Hose fertig? Morgen, in drei Tagen oder in einer Woche?"),
            L("Schneider", "m", "Normal in drei Tagen. Eine Woche brauchen wir selten, morgen nur mit Express."),
            L("Kundin", "f", "Geht es schneller? Morgen statt in drei Tagen?"),
            L("Schneider", "m", "Mit Express bis morgen, plus 5 Euro. Normal in drei Tagen, nicht in einer Woche."),
            L("Kundin", "f", "Dann normal in drei Tagen. Danke."),
        ],
        [
            L("Mann", "m", "Können Sie die Ärmel kürzen? Einen Zentimeter, drei oder fünf?"),
            L("Schneiderin", "f", "Ja, ich messe gleich nach. Einen Zentimeter ist wenig, fünf oft zu viel."),
            L("Mann", "m", "Wie viel kürzer? Drei Zentimeter, oder fünf?"),
            L("Schneiderin", "f", "Etwa drei Zentimeter. Nicht einen und nicht fünf, drei Zentimeter passen gut."),
            L("Mann", "m", "Gut, dann drei Zentimeter. Danke."),
        ],
        [
            L("Frau", "f", "Der Reißverschluss klemmt. Reparieren Sie ihn, tauschen Sie ihn aus, oder lassen Sie ihn so?"),
            L("Schneider", "m", "Den muss ich austauschen. Reparieren hält nicht lange, und so lassen geht nicht."),
            L("Frau", "f", "Lohnt sich das noch? Also austauschen, nicht reparieren?"),
            L("Schneider", "m", "Ja, die Jacke ist sonst noch top. Ich tausche ihn aus, repariere ihn nicht und lasse ihn nicht so."),
            L("Frau", "f", "Dann bitte austauschen. Danke."),
        ],
        [
            L("Kunde", "m", "Guten Tag, was kostet das Kürzen einer Hose? 12 Euro, 20 oder 24?"),
            L("Schneiderin", "f", "Bei einer Jeans 12 Euro. 24 Euro wären zwei Hosen zum normalen Preis."),
            L("Kunde", "m", "Und bei zwei Hosen zusammen? 20 Euro oder 24 Euro?"),
            L("Schneiderin", "f", "Dann mache ich Ihnen 20 Euro. Nicht 12 für zwei und nicht 24, zwei Hosen zusammen 20 Euro."),
            L("Kunde", "m", "Super, dann zwei Hosen für 20 Euro. Danke schön."),
        ],
        [
            L("Kundin", "f", "Muss ich zur Anprobe kommen? Oder nichts tun, oder später wiederkommen?"),
            L("Schneider", "m", "Ja, einmal vor der Änderung. Nichts tun geht nicht, und später wiederkommen brauchen Sie nur zur Abholung."),
            L("Kundin", "f", "Geht das jetzt gleich? Also zur Anprobe, nicht nichts?"),
            L("Schneider", "m", "Ja, kommen Sie in die Kabine. Zur Anprobe jetzt, nicht nichts und nicht erst später."),
            L("Kundin", "f", "Gut, dann jetzt zur Anprobe. Danke."),
        ],
    ],
    t4=[
        L("Reporter", "m", "Frau Yilmaz, wie hat sich Ihre Arbeit in den letzten Jahren verändert?"),
        L("Yilmaz", "f", "Früher kauften die Leute oft neu. Jetzt lassen sie Kleidung wieder reparieren. Heute lassen die Leute Kleidung wieder mehr reparieren, das merke ich klar."),
        L("Reporter", "m", "Was sind die häufigsten Aufträge in der Werkstatt?"),
        L("Yilmaz", "f", "Hosen kürzen, das mache ich jeden Tag. Auch Reißverschlüsse wechseln. Hosen kürzen ist ein häufiger Auftrag, fast stündlich."),
        L("Reporter", "m", "Lohnt sich das Reparieren immer, auch bei billiger Kleidung?"),
        L("Yilmaz", "f", "Nicht immer. Bei billiger Kleidung ist es manchmal zu teuer. Bei guter lohnt es sich. Das Reparieren lohnt sich also nicht immer, das muss man prüfen."),
        L("Reporter", "m", "Können junge Leute noch nähen, oder immer weniger?"),
        L("Yilmaz", "f", "Leider immer weniger. Manche kommen nur, um einen Knopf annähen zu lassen. Immer weniger junge Leute können nähen, das ist schade."),
        L("Reporter", "m", "Was wünschen Sie sich? Ist Reparieren gut für die Umwelt?"),
        L("Yilmaz", "f", "Dass die Menschen Kleidung wieder mehr schätzen. Reparieren ist gut für die Umwelt, nicht schlecht. Weniger wegwerfen hilft uns allen. Ein Lieblingsstück zu retten macht oft mehr Freude als ein neues Teil im Schrank."),
    ],
)

# ── 98 Im Wellnesshotel ───────────────────────────────────────────
apply(
    98,
    t1={
        0: "Liebe Gäste: Willkommen in unserem Wellnesshotel. Der große Pool ist heute leider geschlossen, wir reinigen ihn. Aber die Sauna und das kleine Becken sind normal geöffnet. Die Sauna ist also nicht zu, nur der große Pool. Ab morgen können Sie wieder im großen Pool schwimmen. Wir entschuldigen uns und wünschen einen erholsamen Tag!",
        4: "Liebe Gäste: Unser Wellnessbereich ist von 7 bis 22 Uhr geöffnet. Die letzten Behandlungen wie Massagen beginnen aber spätestens um 20 Uhr, nicht um 22 Uhr und nicht schon um 18 Uhr. Bitte buchen Sie Massagen früh, sie sind schnell ausgebucht. Bademäntel und Handtücher finden Sie auf Ihrem Zimmer. Wir wünschen viel Entspannung!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, im Wellnesshotel genießt jeder etwas anderes. Was macht jeder am liebsten?"),
        L("Markus", "m", "Also, Lukas geht am liebsten in die Sauna — er schwitzt gern und entspannt dabei. Ins Dampfbad geht er selten."),
        L("Anna", "f", "Passt zu ihm. Und Lisa? Die hat oft Verspannungen."),
        L("Markus", "m", "Lisa bucht immer eine Massage — gegen ihre Verspannungen im Rücken. In den Fitnessraum geht sie nicht."),
        L("Anna", "f", "Und Tom? Der schwimmt doch jeden Morgen."),
        L("Markus", "m", "Tom schwimmt im Pool — er zieht jeden Morgen seine Bahnen. Eine Maniküre will er nicht."),
        L("Anna", "f", "Und Sara? Die achtet auf ihre Haut."),
        L("Markus", "m", "Sara macht eine Gesichtsbehandlung — für eine schöne, gepflegte Haut. Spazieren am See macht sie danach."),
        L("Anna", "f", "Und Tim? Der mag Yoga, oder?"),
        L("Markus", "m", "Tim macht Yoga — das Hotel bietet morgens einen Kurs am See an. Die Sauna mag er weniger."),
        L("Anna", "f", "Dann hat jeder sein Programm. Buchen wir auch etwas?"),
        L("Markus", "m", "Ich würde gern eine Massage nehmen, wenn noch ein Termin frei ist."),
        L("Anna", "f", "Ich komme mit zum See, der Yoga-Kurs klingt schön und ist am Morgen."),
        L("Markus", "m", "Gut, dann sehen wir uns später beim Frühstück. Um acht?"),
    ],
    t3=[
        [
            L("Gast", "m", "Guten Tag, was kostet eine Massage bei Ihnen? 40 Euro, 70 oder 100?"),
            L("Mitarbeiterin", "f", "Die halbe Stunde kostet 40 Euro. 100 Euro wäre eine Extra-Behandlung mit Öl."),
            L("Gast", "m", "Und eine ganze Stunde Massage? 70 Euro oder 100 Euro?"),
            L("Mitarbeiterin", "f", "Eine ganze Stunde 70 Euro. Nicht 40 und nicht 100, eine Stunde kostet 70 Euro."),
            L("Gast", "m", "Dann bitte eine ganze Stunde für 70 Euro. Danke."),
        ],
        [
            L("Gästin", "f", "Wann beginnt der Yoga-Kurs? Um 8 Uhr, um 10 Uhr oder am Nachmittag?"),
            L("Mitarbeiter", "m", "Morgens um 8 Uhr am See. Um 10 Uhr ist Frühstücksschluss, am Nachmittag gibt es keinen Kurs."),
            L("Gästin", "f", "Muss ich mich anmelden? Also wirklich um 8, nicht um 10?"),
            L("Mitarbeiter", "m", "Nein, kommen Sie einfach hin. Der Kurs beginnt um 8 Uhr, nicht um 10 und nicht am Nachmittag."),
            L("Gästin", "f", "Super, dann um 8 Uhr am See. Danke."),
        ],
        [
            L("Gast", "m", "Gibt es Bademäntel? Auf dem Zimmer, an der Rezeption oder an der Sauna?"),
            L("Mitarbeiterin", "f", "Ja, auf Ihrem Zimmer. An der Rezeption liegen keine extra Bademäntel."),
            L("Gast", "m", "Und Handtücher für die Sauna? Auch auf dem Zimmer?"),
            L("Mitarbeiterin", "f", "Die bekommen Sie am Eingang zur Sauna. Nicht auf dem Zimmer und nicht an der Rezeption, an der Sauna."),
            L("Gast", "m", "Verstanden, Bademantel auf dem Zimmer, Handtuch an der Sauna. Danke."),
        ],
        [
            L("Gästin", "f", "Ist das Frühstück im Preis dabei? Bis 9 Uhr, bis 10 Uhr 30 oder bis 12 Uhr?"),
            L("Mitarbeiter", "m", "Ja, ein großes Buffet. Bis 9 Uhr wäre früh, bis 12 Uhr gibt es schon Mittagessen."),
            L("Gästin", "f", "Bis wann gibt es das? 10 Uhr 30, oder schon 9?"),
            L("Mitarbeiter", "m", "Bis 10 Uhr 30. Nicht bis 9 Uhr und nicht bis 12 Uhr, bis halb elf."),
            L("Gästin", "f", "Prima, dann bis 10 Uhr 30. Danke."),
        ],
        [
            L("Gast", "m", "Darf man Kinder mit in die Sauna nehmen? Ab 12, ab 16 oder jedes Alter?"),
            L("Mitarbeiterin", "f", "Erst ab 16 Jahren, aus Gesundheitsgründen. Ab 12 und jedes Alter gelten hier nicht."),
            L("Gast", "m", "Und in den Pool? Auch ab 16, oder jedes Alter?"),
            L("Mitarbeiterin", "f", "In den Pool dürfen Kinder, ja. In die Sauna erst ab 16, nicht ab 12 und nicht jedes Alter."),
            L("Gast", "m", "Gut, Pool ja, Sauna ab 16. Danke."),
        ],
    ],
    t4=[
        L("Reporter", "m", "Frau Adler, warum kommen die Menschen ins Wellnesshotel?"),
        L("Adler", "f", "Vor allem, um sich zu erholen. Viele arbeiten zu viel und sind müde. Die meisten Gäste kommen, um sich zu erholen, das ist der Hauptgrund."),
        L("Reporter", "m", "Sind solche Hotels immer sehr teuer, oder gibt es Angebote?"),
        L("Adler", "f", "Nicht alle. Unter der Woche gibt es oft günstige Angebote. Wellnesshotels sind also nicht immer sehr teuer, man muss nur den Tag wählen."),
        L("Reporter", "m", "Was ist bei den Gästen am beliebtesten, Massagen oder Sauna?"),
        L("Adler", "f", "Die Massagen. Danach kommen Sauna und Pool. Auch Yoga mögen viele. Massagen sind bei den Gästen am beliebtesten, das buchen fast alle."),
        L("Reporter", "m", "Kommen auch Firmen zu Ihnen, mit ihren Mitarbeitern?"),
        L("Adler", "f", "Ja, immer mehr. Sie schicken ihre Mitarbeiter zur Erholung. Immer mehr Firmen machen das, nach stressigen Monaten."),
        L("Reporter", "m", "Was raten Sie gestressten Menschen? Geht Erholung nur im teuren Hotel?"),
        L("Adler", "f", "Nehmen Sie sich auch zu Hause Zeit für sich. Ein Bad oder ein Spaziergang hilft schon. Erholung gibt es nicht nur im teuren Hotel, das kann jeder machen. Zehn Minuten Ruhe am Abend sind schon ein Anfang."),
    ],
)

# ── 99 Im Sprachcafé ──────────────────────────────────────────────
apply(
    99,
    t1={
        4: "Liebe Sprachfreunde: Wir suchen ehrenamtliche Helfer. Wer Deutsch als Muttersprache spricht und anderen beim Üben helfen möchte, ist herzlich willkommen. Bezahlte Lehrer und Übersetzer brauchen wir nicht, nur ehrenamtliche Helfer. Sie müssen kein Lehrer sein, nur Geduld und Freude am Reden mitbringen. Einmal die Woche für zwei Stunden. Melden Sie sich bei uns!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, im Sprachcafé übt jeder eine andere Sprache. Was übt jeder?"),
        L("Markus", "m", "Also, Lukas übt Englisch — er braucht es für seinen neuen Job. Portugiesisch lernt er nicht."),
        L("Anna", "f", "Praktisch. Und Lisa? Die reist im Sommer, oder?"),
        L("Markus", "m", "Lisa übt Spanisch — sie reist im Sommer durch Südamerika. Russisch mag sie nicht so."),
        L("Anna", "f", "Und Tom? Seine Freundin kommt aus Frankreich."),
        L("Markus", "m", "Tom übt Französisch — seine Freundin kommt aus Frankreich. Arabisch lernt er nicht."),
        L("Anna", "f", "Und Sara? Die liebt Italien, das Essen vor allem."),
        L("Markus", "m", "Sara übt Italienisch — sie liebt das Land und das Essen. Chinesisch ist ihr zu schwer jetzt."),
        L("Anna", "f", "Und Tim? Der ist neu hier."),
        L("Markus", "m", "Tim übt Deutsch — er ist neu im Land und will sich schnell einleben. Englisch kann er schon."),
        L("Anna", "f", "Schön, dann treffen sie sich dort. Gehst du auch mittwochs hin?"),
        L("Markus", "m", "Ja, ich helfe manchmal am Deutsch-Tisch. Es macht Spaß und kostet nichts."),
        L("Anna", "f", "Ich komme nächste Woche mit. Ist ein Getränk genug?"),
        L("Markus", "m", "Ja, ein Tee reicht. Setz dich einfach dazu, die Leute sind nett."),
    ],
    t3=[
        [
            L("Besucherin", "f", "Wann ist das Sprachcafé offen? Jeden Montag, Mittwoch oder Freitag?"),
            L("Helfer", "m", "Jeden Mittwoch von 18 bis 21 Uhr. Montags und freitags haben wir zu."),
            L("Besucherin", "f", "Auch in den Ferien? Also nicht montags und nicht freitags?"),
            L("Helfer", "m", "Ja, das ganze Jahr. Jeden Mittwoch, nicht montags und nicht freitags."),
            L("Besucherin", "f", "Perfekt, dann jeden Mittwoch. Danke."),
        ],
        [
            L("Mann", "m", "Ich spreche noch nicht gut Deutsch. Ist das zu schlecht, soll ich erst einen Kurs machen?"),
            L("Helferin", "f", "Das macht nichts, hier übt man ja. Zu schlecht ist niemand, und ein Kurs muss nicht zuerst sein."),
            L("Mann", "m", "Werde ich verbessert? Oder ist mein Deutsch zu schlecht für hier?"),
            L("Helferin", "f", "Nur wenn du möchtest, ganz entspannt. Das macht nichts, hier übt man. Nicht zu schlecht."),
            L("Mann", "m", "Danke, dann setze ich mich dazu. Das beruhigt mich."),
        ],
        [
            L("Frau", "f", "Suchst du einen Tandem-Partner? Nicht zum Essen und nicht für einen Kurs."),
            L("Mann", "m", "Ja, ich lerne Deutsch. Zusammen essen können wir später, einen Kurs buche ich nicht."),
            L("Frau", "f", "Ich lerne deine Sprache, perfekt! Also ein Tandem, nicht nur essen?"),
            L("Mann", "m", "Super, tauschen wir die Nummern. Wir bilden ein Tandem, essen ist extra, keinen Kurs buchen."),
            L("Frau", "f", "Genau, zuerst das Tandem. Freut mich."),
        ],
        [
            L("Gast", "m", "Was kostet der Eintritt? 5 Euro, nichts oder 10 Euro?"),
            L("Helfer", "m", "Nichts, es ist kostenlos. 5 Euro und 10 Euro wären Eintritt, den gibt es nicht."),
            L("Gast", "m", "Wirklich gratis? Nicht 5 Euro und nicht 10?"),
            L("Helfer", "m", "Ja, bestellen Sie nur ein Getränk. Der Eintritt kostet nichts, nicht 5 und nicht 10 Euro."),
            L("Gast", "m", "Super, dann ein Tee bitte. Danke."),
        ],
        [
            L("Besucherin", "f", "Gibt es heute ein Thema? Essen, Reisen oder Arbeit?"),
            L("Helferin", "f", "Ja, heute geht es ums Reisen. Essen und Arbeit kommen nächste Woche."),
            L("Besucherin", "f", "Oh, da kann ich viel erzählen! Also Reisen, nicht Essen?"),
            L("Helferin", "f", "Perfekt, setzen Sie sich dazu. Heute Reisen, nicht Essen und nicht die Arbeit."),
            L("Besucherin", "f", "Gerne, dann setze ich mich zum Reisen-Tisch. Danke."),
        ],
    ],
    t4=[
        L("Reporter", "m", "Frau Stark, warum haben Sie das Sprachcafé gemacht?"),
        L("Stark", "f", "Beim Sprachenlernen muss man reden. Ich wollte einen Ort ohne Druck und ohne Prüfung. Einen Ort zum Üben ohne Druck, das war mein Ziel."),
        L("Reporter", "m", "Wer kommt zu Ihnen? Nur Studenten, oder auch andere Menschen?"),
        L("Stark", "f", "Menschen aus vielen Ländern. Manche lernen Deutsch, andere Englisch oder Spanisch. Es kommen nicht nur Studenten, auch Berufstätige und Rentner."),
        L("Reporter", "m", "Was ist der größte Vorteil für die Gäste?"),
        L("Stark", "f", "Die Leute verlieren die Angst zu reden. Und sie finden neue Freunde. Viele Gäste verlieren dort die Angst zu reden, das höre ich oft."),
        L("Reporter", "m", "Hilft das auch beim Einleben, zum Beispiel bei der Arbeit?"),
        L("Stark", "f", "Ja, sehr, wer die Sprache spricht, findet leichter Arbeit und Freunde. Die Sprache öffnet Türen, das sehe ich jede Woche."),
        L("Reporter", "m", "Was raten Sie beim Sprachenlernen? Soll man aus Angst vor Fehlern schweigen?"),
        L("Stark", "f", "Reden Sie viel und haben Sie keine Angst vor Fehlern. Bleiben Sie dran. Schweigen aus Angst ist keine gute Idee, Fehler gehören dazu. Jeden Tag ein paar Sätze helfen schon sehr beim Lernen."),
    ],
)

# ── 100 Abschlussfeier und Zukunftspläne ──────────────────────────
apply(
    100,
    t2=[
        L("Anna", "f", "Hallo Markus, nach dem Abschluss hat jeder andere Pläne. Was macht jeder?"),
        L("Markus", "m", "Also, Lukas beginnt ein Studium — er will Ingenieur werden. Eine Firma gründen will er später."),
        L("Anna", "f", "Passt zu ihm. Und Lisa? Sie will in die Pflege, oder?"),
        L("Markus", "m", "Lisa macht eine Ausbildung — als Krankenschwester im Krankenhaus. Ein Praktikum hat sie schon hinter sich."),
        L("Anna", "f", "Und Tom? Der redet immer von Australien."),
        L("Markus", "m", "Tom geht ins Ausland — ein Jahr in Australien, reisen und arbeiten. Nur reisen ohne Arbeit will er nicht."),
        L("Anna", "f", "Und Sara? Die will schnell unabhängig sein."),
        L("Markus", "m", "Sara sucht sofort eine Arbeit — sie will Geld verdienen und unabhängig sein. Noch nicht entschieden ist sie nicht."),
        L("Anna", "f", "Und Tim? Der wollte doch erst helfen, bevor er studiert."),
        L("Markus", "m", "Tim macht ein soziales Jahr — er hilft in einem Altenheim, bevor er studiert. Eine Firma gründet er nicht."),
        L("Anna", "f", "Spannend, so viele Wege. Und du, bleibst du in der Stadt?"),
        L("Markus", "m", "Erst mal ja. Die Feier am Samstag sehe ich als Start, nicht als Ende."),
        L("Anna", "f", "Schön gesagt. Treffen wir uns vor der Aula um sechs?"),
        L("Markus", "m", "Ja, um sechs vor der Tür. Zieh dich festlich an, die Eltern kommen auch."),
    ],
    t3=[
        [
            L("Schülerin", "f", "Hast du deine Note schon? Eine Eins, eine Zwei oder eine Drei?"),
            L("Schüler", "m", "Ja, eine Zwei. Eine Drei hätte mich geärgert, eine Eins war knapp."),
            L("Schülerin", "f", "Eine Eins, ich kann es kaum glauben! Nicht die Zwei und nicht die Drei."),
            L("Schüler", "m", "Wow, gratuliere! Du hast eine Eins, ich eine Zwei, eine Drei hat niemand von uns."),
            L("Schülerin", "f", "Danke, ich bin so froh über die Eins."),
        ],
        [
            L("Mutter", "f", "Was ziehst du zur Feier an? Das schwarze Kleid, das blaue oder eine Hose?"),
            L("Tochter", "f", "Das blaue Kleid. Die Hose ist zu sportlich, das schwarze zu ernst."),
            L("Mutter", "f", "Nicht das schwarze? Und keine Hose?"),
            L("Tochter", "f", "Nein, das blaue ist festlicher. Nicht das schwarze und keine Hose, das blaue Kleid."),
            L("Mutter", "f", "Gut, dann das blaue Kleid. Die Schuhe hole ich dir."),
        ],
        [
            L("Vater", "m", "Was möchtest du als Geschenk? Ein Auto, eine Reise oder Geld?"),
            L("Sohn", "m", "Eigentlich nichts Großes. Ein Auto ist zu viel, Geld allein ist langweilig."),
            L("Vater", "m", "Komm schon, du hast es verdient. Auto, Reise oder Geld?"),
            L("Sohn", "m", "Na gut, vielleicht eine Reise. Kein Auto und nicht nur Geld, eine Reise wäre schön."),
            L("Vater", "m", "Eine Reise also. Das machen wir, versprochen."),
        ],
        [
            L("Lehrerin", "f", "Was sind deine Pläne, Tom? Koch, Mechaniker oder Verkäufer?"),
            L("Tom", "m", "Ich beginne eine Ausbildung. Nicht als Mechaniker und nicht als Verkäufer."),
            L("Lehrerin", "f", "In welchem Beruf? Als Koch, oder doch Mechaniker?"),
            L("Tom", "m", "Als Koch, ich liebe das Kochen. Nicht als Mechaniker und nicht als Verkäufer, als Koch."),
            L("Lehrerin", "f", "Das passt zu dir. Viel Erfolg als Koch!"),
        ],
        [
            L("Freundin", "f", "Bleiben wir in Kontakt? Oder uns nie wiedersehen, oder zusammen studieren?"),
            L("Freund", "m", "Klar, auf jeden Fall in Kontakt bleiben. Nie wiedersehen will ich nicht, zusammen studieren wir nicht."),
            L("Freundin", "f", "Machen wir ein Klassentreffen? Also Kontakt, nicht nie wiedersehen?"),
            L("Freund", "m", "Ja, jedes Jahr, das wäre schön. In Kontakt bleiben, uns nicht nie wiedersehen, und nicht unbedingt zusammen studieren."),
            L("Freundin", "f", "Abgemacht, jedes Jahr. Ich freue mich."),
        ],
    ],
    t4=[
        L("Reporter", "m", "Frau Wagner, was bedeutet dieser Tag für die Schüler?"),
        L("Wagner", "f", "Es ist ein großer Tag. Sie haben viele Jahre gelernt. Jetzt beginnt etwas Neues. Für mich ist dieser Tag ein großer Tag, das spürt man in der Aula."),
        L("Reporter", "m", "Sind die jungen Leute unsicher wegen der Zukunft? Müssen sie heute schon alles wissen?"),
        L("Wagner", "f", "Manche schon. Ich sage ihnen: Ihr müsst nicht heute schon alles wissen. Die Schüler müssen heute noch nicht alles wissen, das betone ich oft."),
        L("Reporter", "m", "Müssen alle studieren, oder ist eine Ausbildung genauso gut?"),
        L("Wagner", "f", "Nein, eine Ausbildung ist genauso gut wie ein Studium. Wir brauchen auch Handwerker und Pfleger. Beides ist wertvoll, das Studium und die Ausbildung."),
        L("Reporter", "m", "Was geben Sie den Schülern mit? Sollen sie nach der Schule nicht mehr lernen?"),
        L("Wagner", "f", "Lernt weiter, euer ganzes Leben lang. Bleibt neugierig und helft einander. Nach der Schule nicht mehr zu lernen, das rate ich nicht, im Gegenteil."),
        L("Reporter", "m", "Was wünschen Sie sich für die Schüler, für ihr Leben?"),
        L("Wagner", "f", "Dass sie glücklich werden und einen Beruf finden, der ihnen gefällt. Ich wünsche mir, dass die Schüler glücklich werden, das ist das Wichtigste."),
    ],
)

print("95-100 applied")

