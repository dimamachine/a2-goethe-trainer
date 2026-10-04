#!/usr/bin/env python3
"""Expand Goethe A2 Hören tests 83-88 to official length. Temporary mutator."""
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


# ── 83 Beim Hautarzt ──────────────────────────────────────────────
apply(
    83,
    t1={
        0: "Guten Tag, hier ist die Hautarztpraxis Dr. Sommer. Ihr Termin für die Hautkrebs-Vorsorge ist nächste Woche. Am Montag geht es leider nicht, und auch am Mittwoch haben wir keinen Platz. Wir haben Sie auf Dienstag um 9 Uhr gesetzt. Bitte kommen Sie ungeschminkt und ohne Creme auf der Haut. Bringen Sie Ihre Versichertenkarte mit. Auf Wiederhören!",
        4: "Liebe Patienten: Unsere Praxis bietet ab Mai eine Akne-Sprechstunde speziell für Jugendliche an, jeden Mittwochnachmittag. Die Sprechstunde ist nicht für ältere Menschen und auch nicht für Babys. Auch eine Beratung zum richtigen Sonnenschutz gibt es. Bitte vereinbaren Sie vorher einen Termin. Die Wartezeit beträgt zurzeit etwa drei Wochen. Wir bitten um Geduld!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, sag mal, alle unsere Freunde gehen gerade zum Hautarzt. Ich verstehe das nicht so ganz. Was hat denn jeder?"),
        L("Markus", "m", "Ja, da ist wirklich viel los. Also, Lukas hat Pickel — Akne, schon seit der Jugend. Er will keine Creme aus der Drogerie mehr."),
        L("Anna", "f", "Armer Lukas. Und Lisa? Hat sie das gleiche Problem?"),
        L("Markus", "m", "Nein, Lisa hat einen Ausschlag — wahrscheinlich eine Allergie, sie weiß nicht wovon. Einen Insektenstich hat sie nicht."),
        L("Anna", "f", "Das juckt bestimmt. Und Tom? Der sieht doch immer so gesund aus."),
        L("Markus", "m", "Tom geht nur zur Muttermal-Kontrolle — Vorsorge, einmal im Jahr. Er hat keine Warzen, er ist einfach vorsichtig."),
        L("Anna", "f", "Das ist klug von ihm. Und Sara? Die klagt doch oft über die Haut."),
        L("Markus", "m", "Sara hat trockene Haut — sie braucht eine besondere Creme. Haarausfall oder Nagelpilz hat sie nicht."),
        L("Anna", "f", "Gut zu wissen. Und Tim? Der war doch letzte Woche am Strand."),
        L("Markus", "m", "Genau, Tim hat einen Sonnenbrand — er war zu lange am Strand ohne Schutz. Er ärgert sich jetzt sehr."),
        L("Anna", "f", "Typisch Tim. Nächstes Mal nimmt er hoffentlich eine Creme mit."),
        L("Markus", "m", "Ja, das hoffe ich auch. Dann wissen wir jetzt, wer welches Problem hat."),
    ],
    t3=[
        [
            L("Patientin", "f", "Guten Tag, ich brauche einen Termin beim Hautarzt, möglichst bald."),
            L("Sprechstundenhilfe", "f", "Gerne. Ist es wegen Pickeln oder wegen trockener Haut? Das können wir nächste Woche machen."),
            L("Patientin", "f", "Nein, nicht wegen Pickeln und auch nicht wegen trockener Haut. Ein Muttermal hat sich verändert."),
            L("Sprechstundenhilfe", "f", "Dann kommen Sie bitte morgen, das prüfen wir gleich. Das ist wichtiger als Pickel oder trockene Haut."),
            L("Patientin", "f", "Ja, morgen ist gut. Vielen Dank für den schnellen Termin."),
        ],
        [
            L("Arzt", "m", "Guten Tag, wie lange haben Sie den Ausschlag schon?"),
            L("Patient", "m", "Seit zwei Wochen schon, und es wird nicht besser."),
            L("Arzt", "m", "Haben Sie etwas Neues gegessen? Zum Beispiel Nüsse oder Fisch?"),
            L("Patient", "m", "Nüsse esse ich nie, und Fisch mag ich nicht. Aber ja, viele Erdbeeren. Ich habe fast jeden Tag welche gegessen."),
            L("Arzt", "m", "Dann kommen die Beschwerden wahrscheinlich von den Erdbeeren, nicht von Nüssen oder Fisch."),
        ],
        [
            L("Patientin", "f", "Guten Tag, welchen Sonnenschutz empfehlen Sie? Brauche ich überhaupt welchen?"),
            L("Ärztin", "f", "Ja, Sie brauchen Schutz. Faktor 10 ist zu wenig, und ohne Creme geht es nicht."),
            L("Patientin", "f", "Auch im Frühling? Manche sagen, dann reicht Faktor 10 oder sogar keinen."),
            L("Ärztin", "f", "Ja, die Sonne ist auch dann stark. Nehmen Sie mindestens Faktor 30, nicht Faktor 10 und nicht ohne Creme."),
            L("Patientin", "f", "Gut, dann kaufe ich Faktor 30. Danke für den Tipp."),
        ],
        [
            L("Arzt", "m", "Bitte tragen Sie die Creme zweimal am Tag auf, nicht nur einmal und nicht jede Stunde."),
            L("Patient", "m", "Morgens und abends? Oder wirklich jede Stunde? Einmal am Tag wäre einfacher."),
            L("Arzt", "m", "Genau, morgens und abends, also zweimal am Tag. Nicht jede Stunde, das ist zu oft, und einmal reicht nicht. Und nicht in die Sonne damit."),
            L("Patient", "m", "Verstanden, danke. Zweimal am Tag, morgens und abends."),
        ],
        [
            L("Patientin", "f", "Guten Tag, muss ich für die Vorsorge zahlen? Kostet das 50 Euro?"),
            L("Sprechstundenhilfe", "f", "Die Kontrolle zahlt die Kasse, also nichts für die normale Vorsorge. 50 Euro wäre zu viel."),
            L("Patientin", "f", "Und die spezielle Untersuchung? Ist die auch umsonst, oder kostet sie 50 Euro?"),
            L("Sprechstundenhilfe", "f", "Nein, die kostet 30 Euro extra, nicht 50 Euro und nicht nichts. Die Kasse zahlt nur die einfache Kontrolle."),
            L("Patientin", "f", "Gut, dann mache ich die spezielle Untersuchung für 30 Euro. Danke."),
        ],
    ],
    t4=[
        L("Reporter", "m", "Frau Dr. Klein, warum kommen die Patienten zu Ihnen?"),
        L("Klein", "f", "Viele junge Leute kommen wegen Pickeln. Andere haben Probleme mit der Sonne, zum Beispiel nach dem Urlaub. Manche wollen auch nur eine Kontrolle, das ist gut."),
        L("Reporter", "m", "Ist Bräune gesund? Viele denken das ja."),
        L("Klein", "f", "Nein, das ist ein Irrtum. Bräune ist nicht gesund. Jeder Sonnenbrand schadet der Haut, auch ein kleiner. Das sehe ich jeden Tag in der Praxis."),
        L("Reporter", "m", "Wie wichtig ist der Schutz vor der Sonne?"),
        L("Klein", "f", "Sehr wichtig, bitte benutzen Sie eine Creme, auch im Frühling. Viele Leute denken, nur im Sommer braucht man Schutz, aber das stimmt nicht. Die Sonne ist auch im April schon stark."),
        L("Reporter", "m", "Helfen teure Cremes besser als einfache?"),
        L("Klein", "f", "Nicht immer. Eine einfache Creme ist oft genauso gut. Teure Cremes sind nicht immer besser. Wichtig ist der Schutzfaktor, nicht der Preis im Laden."),
        L("Reporter", "m", "Was raten Sie für eine gesunde Haut?"),
        L("Klein", "f", "Trinken Sie viel Wasser, essen Sie gesund und schlafen Sie genug. Das hilft der Haut sehr. Und gehen Sie einmal im Jahr zur Kontrolle. So bleiben Sie lange gesund."),
    ],
)

# ── 84 In der Tourist-Information ─────────────────────────────────
apply(
    84,
    t1={
        0: "Liebe Gäste: Willkommen in unserer Stadt. Die große Stadtführung beginnt heute nicht um 14 Uhr und auch nicht um 16 Uhr, sondern wegen des Regens schon um 11 Uhr am Vormittag. Treffpunkt ist vor dem Rathaus. Die Führung dauert zwei Stunden. Bitte ziehen Sie sich warm an. Wir freuen uns auf Sie!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, wir sind in einer neuen Stadt und jeder will etwas anderes sehen. Was möchte jeder machen?"),
        L("Markus", "m", "Gute Frage. Also, Lukas will eine Stadtführung machen — er liebt die Geschichte von alten Städten. Ins Theater will er nicht."),
        L("Anna", "f", "Das passt zu Lukas. Und Lisa? Die mag doch Kunst."),
        L("Markus", "m", "Genau, Lisa möchte ins Museum — sie interessiert sich sehr für Kunst. In den Park will sie heute nicht."),
        L("Anna", "f", "Schön. Und Tom? Der sitzt nicht gern lange drinnen."),
        L("Markus", "m", "Tom will eine Bootsfahrt machen — die Stadt von Wasser aus sehen. Zum Zoo geht er nicht, das Wasser ist ihm lieber."),
        L("Anna", "f", "Klingt toll. Und Sara? Die fotografiert doch immer alles."),
        L("Markus", "m", "Sara möchte auf den Aussichtsturm — sie will die Stadt von oben fotografieren. Shopping ist heute nicht ihr Plan."),
        L("Anna", "f", "Klar, mit dem Blick. Und Tim? Der denkt immer zuerst ans Essen."),
        L("Markus", "m", "Tim will auf den Markt — er probiert in jeder Stadt das lokale Essen. Das Theater interessiert ihn weniger."),
        L("Anna", "f", "Dann haben alle einen Plan. Treffen wir uns später zum Kaffee?"),
        L("Markus", "m", "Ja, um fünf am Markt, dann erzählen wir, was jeder gesehen hat."),
    ],
    t3=[
        [
            L("Touristin", "f", "Guten Tag, wie komme ich zum Schloss? Mit dem Bus oder zu Fuß?"),
            L("Mitarbeiter", "m", "Mit der Linie 5, vier Stationen, das dauert etwa 10 Minuten. Zu Fuß ist es länger."),
            L("Touristin", "f", "Und zu Fuß? Eine Stunde, oder schneller?"),
            L("Mitarbeiter", "m", "Zu Fuß etwa 30 Minuten, nicht 10 Minuten und nicht eine Stunde. Der Weg ist schön durch den Park."),
            L("Touristin", "f", "Dann gehe ich zu Fuß, 30 Minuten sind okay. Danke."),
        ],
        [
            L("Mann", "m", "Guten Tag, was kostet die Stadtführung? 12 Euro für alle?"),
            L("Mitarbeiterin", "f", "Erwachsene 12 Euro, Kinder 6 Euro. 30 Euro wäre für eine ganze Familie."),
            L("Mann", "m", "Wir sind zwei Erwachsene und ein Kind. Was kostet das Kind?"),
            L("Mitarbeiterin", "f", "Das Kind kostet 6 Euro, nicht 12 und nicht 30. Zusammen macht das 30 Euro für Sie alle."),
            L("Mann", "m", "Gut, dann drei Karten, zwei Erwachsene und ein Kind für 6 Euro. Danke."),
        ],
        [
            L("Frau", "f", "Welches Museum lohnt sich heute? Ist am Sonntag oder Samstag etwas zu?"),
            L("Mitarbeiter", "m", "Das Kunstmuseum ist großartig. Samstags und sonntags ist es offen, montags ist zu."),
            L("Frau", "f", "Ist es heute geöffnet? Heute ist nicht Montag, oder?"),
            L("Mitarbeiter", "m", "Ja, bis 18 Uhr. Montags ist zu, nicht sonntags und nicht samstags. Heute können Sie hingehen."),
            L("Frau", "f", "Prima, dann gehe ich heute ins Museum. Danke."),
        ],
        [
            L("Tourist", "m", "Guten Tag, haben Sie einen Stadtplan? Ich brauche keine Eintrittskarte und kein Buch."),
            L("Mitarbeiterin", "f", "Ja, hier, der Stadtplan ist kostenlos. Eintrittskarten und Bücher verkaufen wir auch, aber der Plan ist umsonst."),
            L("Tourist", "m", "Auch auf Englisch? Super, dann nehme ich den Plan."),
            L("Mitarbeiterin", "f", "Natürlich, in mehreren Sprachen. Hier ist der kostenlose Stadtplan, nicht die Karte und nicht das Buch."),
            L("Tourist", "m", "Vielen Dank, der Plan reicht mir."),
        ],
        [
            L("Reisende", "f", "Wo kann ich gut und günstig essen? Am Bahnhof oder im Hotel?"),
            L("Mitarbeiter", "m", "Am Bahnhof ist es teuer, und im Hotel oft auch. Besser in der Altstadt."),
            L("Reisende", "f", "In der Altstadt? Mit lokalen Gerichten, nicht nur am Bahnhof?"),
            L("Mitarbeiter", "m", "Ja, in der Altstadt gibt es viele kleine Lokale. Nicht am Bahnhof und nicht im Hotel, dort ist es teurer."),
            L("Reisende", "f", "Dann esse ich in der Altstadt. Markieren Sie mir bitte zwei Lokale."),
        ],
    ],
    t4=None,
)

# ── 85 In der Musikschule ─────────────────────────────────────────
apply(
    85,
    t1={
        4: "Liebe Interessenten: Bei uns kann man Instrumente erst ausprobieren, bevor man sich entscheidet. An einem Tag im Monat dürfen Kinder alle Instrumente testen — Klavier, Geige, Trompete und mehr. Ein Konzert hören Sie an dem Tag nicht, und Noten kaufen wir auch nicht. So findet jedes Kind das passende. Der Schnuppertag ist kostenlos. Melden Sie sich im Büro an!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, alle unsere Freunde lernen jetzt ein Instrument in der Musikschule. Was spielt jeder?"),
        L("Markus", "m", "Ja, das ist schön. Also, Lukas lernt Gitarre — er will in einer Band spielen. Saxophon ist nichts für ihn."),
        L("Anna", "f", "Passt zu Lukas. Und Lisa? Die sitzt gern am Klavier, oder?"),
        L("Markus", "m", "Genau, Lisa spielt Klavier — sie übt seit einem Jahr und macht große Fortschritte. Gesang macht sie nicht."),
        L("Anna", "f", "Toll. Und Tom? Der ist doch immer so laut."),
        L("Markus", "m", "Tom lernt Schlagzeug — laut, aber er liebt den Rhythmus. Flöte ist ihm zu leise."),
        L("Anna", "f", "Das glaube ich. Und Sara? Die hört oft klassische Musik."),
        L("Markus", "m", "Sara spielt Geige — klassische Musik ist ihre Leidenschaft. Cello wollte sie nicht, die Geige gefällt ihr besser."),
        L("Anna", "f", "Schön. Und Tim? Der war doch im Urlaub auf einem Konzert."),
        L("Markus", "m", "Tim lernt Trompete — er war im Urlaub bei einem Jazz-Konzert und ist begeistert. Klavier spielt er nicht."),
        L("Anna", "f", "Dann können sie bald zusammen spielen. Kommen wir am Samstag zum Schülerkonzert?"),
        L("Markus", "m", "Ja, am Samstag um fünf. Ich bin gespannt, wie sie klingen."),
    ],
    t3=[
        [
            L("Mutter", "f", "Guten Tag, was kostet der Unterricht im Monat? 80 Euro für alles?"),
            L("Leiter", "m", "Einzelunterricht 80 Euro, Gruppe 40 Euro. 120 Euro wäre nur bei zwei Fächern."),
            L("Mutter", "f", "Was empfehlen Sie für Anfänger? Die Gruppe für 40 Euro oder einzeln für 80?"),
            L("Leiter", "m", "Am Anfang reicht die Gruppe für 40 Euro. Nicht 80 und nicht 120, das ist erst später."),
            L("Mutter", "f", "Gut, dann nehmen wir die Gruppe für 40 Euro. Danke."),
        ],
        [
            L("Vater", "m", "Guten Tag, wie oft ist der Unterricht? Eine Stunde, oder nur 15 Minuten?"),
            L("Lehrerin", "f", "Einmal pro Woche, 30 Minuten. 60 Minuten wäre für Fortgeschrittene, 15 Minuten ist zu kurz."),
            L("Vater", "m", "Reicht das? 30 Minuten klingt wenig, 60 wäre besser, oder?"),
            L("Lehrerin", "f", "Ja, 30 Minuten reichen, wenn das Kind zu Hause täglich übt. Nicht 60 und nicht nur 15."),
            L("Vater", "m", "Verstehe, dann 30 Minuten plus Üben zu Hause. Danke."),
        ],
        [
            L("Schülerin", "f", "Muss ich ein Instrument kaufen? Oder kann ich eins leihen, vielleicht kostenlos?"),
            L("Lehrer", "m", "Am Anfang können Sie eins leihen. Kostenlos geht nicht, und kaufen müssen Sie noch nicht."),
            L("Schülerin", "f", "Was kostet das Leihen? 15 Euro, oder 30?"),
            L("Lehrer", "m", "15 Euro im Monat, nicht 30 und nicht kostenlos. Nach einem Jahr können Sie kaufen."),
            L("Schülerin", "f", "Gut, dann leihe ich erst mal für 15 Euro. Danke."),
        ],
        [
            L("Mutter", "f", "Mein Sohn möchte aufhören. Es ist nicht zu teuer und er ist nicht krank, aber er mag es nicht."),
            L("Lehrerin", "f", "Schade, warum denn? Ist es das Geld, oder ist er krank?"),
            L("Mutter", "f", "Nein, es ist nicht zu teuer und er ist nicht krank. Er findet das Üben langweilig."),
            L("Lehrerin", "f", "Verstehe. Vielleicht ein anderes Instrument? Schlagzeug macht oft mehr Spaß als nur Üben am Tisch."),
            L("Mutter", "f", "Gute Idee, das frage ich ihn. Danke."),
        ],
        [
            L("Schüler", "m", "Wann ist das nächste Konzert? Müssen alle spielen, oder spielt niemand?"),
            L("Leiter", "m", "In zwei Wochen, am Samstag. Nicht alle müssen, und es spielt auch nicht niemand."),
            L("Schüler", "m", "Muss ich auch spielen? Ich habe noch Angst."),
            L("Leiter", "m", "Nur wenn du möchtest, kein Zwang. Du musst nicht, und niemand zwingt dich. Wer will, spielt."),
            L("Schüler", "m", "Dann schaue ich erst zu. Danke, das beruhigt mich."),
        ],
    ],
    t4=[
        L("Reporter", "m", "Frau Hofmann, ab welchem Alter sollen Kinder ein Instrument lernen?"),
        L("Hofmann", "f", "Mit sechs oder sieben Jahren ist ein guter Start. Aber das Kind muss Lust haben. Zwingen bringt nichts, dann macht es keinen Spaß."),
        L("Reporter", "m", "Wie wichtig ist das Üben zu Hause?"),
        L("Hofmann", "f", "Sehr wichtig. Besser jeden Tag fünfzehn Minuten als einmal in der Woche lang. Einmal die Woche lange üben ist nicht am besten, das vergessen die Kinder schnell."),
        L("Reporter", "m", "Lernen auch Erwachsene bei Ihnen, oder nur Kinder?"),
        L("Hofmann", "f", "Ja, immer mehr Erwachsene. Man ist nie zu alt für Musik. Manche kommen nach der Arbeit und sind sehr fleißig."),
        L("Reporter", "m", "Ist Musik gut für Kinder in der Schule?"),
        L("Hofmann", "f", "Ja, sehr, sie hilft beim Lernen und macht glücklich. Kinder, die musizieren, können sich oft besser konzentrieren."),
        L("Reporter", "m", "Was raten Sie Eltern, wenn ein Kind aufhören will?"),
        L("Hofmann", "f", "Nicht gleich aufgeben. Vielleicht passt ein anderes Instrument besser. Reden Sie in Ruhe mit dem Kind, und geben Sie ihm noch ein paar Wochen Zeit. Oft kommt die Lust dann wieder, wenn das Stück endlich klappt. Geduld ist hier sehr wichtig."),
    ],
)

# ── 86 Beim Physiotherapeuten ─────────────────────────────────────
apply(
    86,
    t1={
        2: "Achtung Patienten: Unsere Praxis bietet ab Mai einen neuen Kurs an — Rückengymnastik in der Gruppe, jeden Dienstagabend. Es ist nicht Schwimmen und auch nicht Yoga, sondern Gymnastik für den Rücken. Acht Termine, die Krankenkasse zahlt einen Teil. Bitte melden Sie sich früh an, die Gruppe ist klein. Auch Massagen sind weiter buchbar. Wir freuen uns auf Sie!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, alle unsere Freunde gehen gerade zur Physiotherapie. Das ist wirklich auffällig. Was hat jeder für ein Problem?"),
        L("Markus", "m", "Ja, das ist viel in letzter Zeit. Also, Lukas hat Rückenschmerzen — vom langen Sitzen im Büro. Kopfschmerzen hat er nicht."),
        L("Anna", "f", "Typisch Büro. Und Lisa? Die joggt doch so gern."),
        L("Markus", "m", "Lisa hat ein verletztes Knie — sie ist beim Joggen gestürzt. Die Hüfte ist okay, nur das Knie."),
        L("Anna", "f", "Oh, das dauert. Und Tom? Der sitzt auch viel am Computer."),
        L("Markus", "m", "Tom hat Schulterschmerzen — vom vielen Arbeiten am Computer. Das Handgelenk ist in Ordnung."),
        L("Anna", "f", "Verstehe. Und Sara? Die klagt oft morgens."),
        L("Markus", "m", "Sara hat einen steifen Nacken — sie schläft wohl falsch. Ellbogenschmerzen hat sie nicht."),
        L("Anna", "f", "Und Tim? Der spielt jedes Wochenende Fußball."),
        L("Markus", "m", "Tim hat einen verstauchten Fuß — beim Fußball umgeknickt. Das Knie ist frei, nur der Fuß."),
        L("Anna", "f", "Armer Tim. Hoffentlich helfen die Übungen bald, sonst fehlt er beim Fußball."),
        L("Markus", "m", "Ja, die Therapeuten sind gut. In ein paar Wochen geht es ihnen besser, sagt der Arzt."),
        L("Anna", "f", "Gut, dann wünsche ich ihnen allen eine schnelle Besserung."),
        L("Markus", "m", "Mache ich, ich schreibe später in die Gruppe."),
    ],
    t3=[
        [
            L("Patient", "m", "Guten Tag, wie viele Behandlungen brauche ich? Reichen drei, oder gleich zehn?"),
            L("Therapeutin", "f", "Erst mal sechs, dann sehen wir weiter. Drei ist oft zu wenig, zehn brauchen wir nicht sofort."),
            L("Patient", "m", "Und wenn es nicht besser wird? Dann zehn, oder bleiben wir bei sechs?"),
            L("Therapeutin", "f", "Dann verschreibt der Arzt mehr. Zuerst sechs, nicht drei und nicht gleich zehn."),
            L("Patient", "m", "Gut, dann starten wir mit sechs Terminen. Danke."),
        ],
        [
            L("Therapeut", "m", "Machen Sie die Übungen auch zu Hause? Oder schlafen Sie nur mehr, oder nehmen Sie Tabletten?"),
            L("Patientin", "f", "Ehrlich gesagt, selten. Ich schlafe viel und nehme manchmal Tabletten, aber üben tue ich wenig."),
            L("Therapeut", "m", "Das Üben zu Hause ist wichtig, sonst hilft es wenig. Mehr schlafen und Tabletten ersetzen die Übungen nicht."),
            L("Patientin", "f", "Okay, ich übe ab jetzt täglich zu Hause, nicht nur schlafen und keine extra Tabletten."),
        ],
        [
            L("Patientin", "f", "Darf ich weiter Sport machen? Schwimmen, joggen, radfahren?"),
            L("Therapeutin", "f", "Schwimmen ja, Joggen lieber nicht. Joggen ist jetzt zu hart für Ihr Knie."),
            L("Patientin", "f", "Und Radfahren? Ist das wie Joggen, oder eher wie Schwimmen?"),
            L("Therapeutin", "f", "Radfahren ist gut für Ihr Knie, wie Schwimmen. Nur Joggen sollen Sie nicht machen."),
            L("Patientin", "f", "Verstanden, schwimmen und radfahren ja, joggen nein. Danke."),
        ],
        [
            L("Patient", "m", "Die Massage hat sehr gutgetan. Soll ich mich jetzt hinlegen oder sofort Sport machen?"),
            L("Therapeut", "m", "Schön, ist der Nacken lockerer? Legen Sie sich nicht den ganzen Tag hin, und machen Sie heute keinen Sport."),
            L("Patient", "m", "Ja, viel besser. Was soll ich dann tun?"),
            L("Therapeut", "m", "Trinken Sie heute viel Wasser. Nicht hinlegen den ganzen Tag und nicht sofort Sport, sondern viel trinken."),
            L("Patient", "m", "Gut, dann trinke ich viel Wasser. Danke."),
        ],
        [
            L("Patientin", "f", "Ich muss meinen Termin verschieben. Dienstag geht nicht, Freitag auch nicht so gut."),
            L("Empfang", "f", "Kein Problem, auf wann? Dienstag ist voll, Freitag haben wir noch einen Platz am Nachmittag."),
            L("Patientin", "f", "Geht Donnerstag statt Dienstag? Freitag ist bei mir zu spät."),
            L("Empfang", "f", "Ja, Donnerstag um 11 Uhr. Nicht Dienstag und nicht Freitag, Donnerstag passt."),
            L("Patientin", "f", "Perfekt, dann Donnerstag um 11. Danke."),
        ],
    ],
    t4=[
        L("Reporterin", "f", "Herr Krämer, mit welchem Problem kommen die Leute am häufigsten?"),
        L("Krämer", "m", "Mit dem Rücken. Die meisten Patienten kommen mit Rückenproblemen. Wir sitzen einfach zu viel, im Büro und im Auto."),
        L("Reporterin", "f", "Wie wichtig ist die Mithilfe der Patienten zu Hause?"),
        L("Krämer", "m", "Sehr wichtig, sie müssen die Übungen auch zu Hause machen. Ohne Üben zu Hause hilft die Stunde hier wenig. Die Übungen sind also wichtig, nicht unwichtig."),
        L("Reporterin", "f", "Kann man Rückenschmerzen vermeiden, oder kommt das immer?"),
        L("Krämer", "m", "Ja, man kann sie vermeiden. Stehen Sie öfter auf, bewegen Sie sich und machen Sie Sport. Schwimmen ist gut, auch Spazierengehen hilft."),
        L("Reporterin", "f", "Sind die Geräte besser als Ihre Hände?"),
        L("Krämer", "m", "Nein, meine Hände bleiben das wichtigste Werkzeug. Die Geräte sind nicht besser als die Hände. Ich spüre mit den Händen, wo das Problem ist."),
        L("Reporterin", "f", "Was raten Sie den Menschen im Alltag?"),
        L("Krämer", "m", "Bleiben Sie aktiv. Haben Sie keine Angst vor Bewegung. Ein kurzer Spaziergang am Abend ist schon ein guter Start, jeden Tag. Auch zehn Minuten reichen am Anfang, Hauptsache regelmäßig. So bleibt der Rücken lange fit und stark genug."),
    ],
)

# ── 87 Im Spielzeugladen ──────────────────────────────────────────
apply(
    87,
    t1={
        0: "Liebe Kunden: Vor Weihnachten ist viel los in unserem Spielzeugladen. Die beliebten Puppen sind fast ausverkauft, aber wir bekommen am Freitag neue. Die großen Holzeisenbahnen sind noch da, und Bücher haben wir auch genug. Bestellen Sie früh, damit das Geschenk rechtzeitig kommt. Wir wünschen schöne Feiertage!",
        2: "Achtung Eltern: Bitte achten Sie beim Kauf auf die Altersangabe, nicht nur auf den Preis oder die Farbe. Kleine Teile sind für Kinder unter drei Jahren gefährlich, sie können sie verschlucken. Auf jeder Verpackung steht das passende Alter. Unsere Mitarbeiter beraten Sie gern. Sicherheit geht vor Spaß. Vielen Dank für Ihr Verständnis!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, alle suchen ein Geschenk für ihre Kinder. Weihnachten kommt bald. Was kauft jeder im Spielzeugladen?"),
        L("Markus", "m", "Also, Lukas kauft eine Eisenbahn — aus Holz, für seinen kleinen Sohn. Ein Auto will der Junge nicht."),
        L("Anna", "f", "Schön, Holz hält lange. Und Lisa? Ihre Tochter wünscht sich bestimmt etwas."),
        L("Markus", "m", "Lisa nimmt eine Puppe — ihre Tochter wünscht sich das schon lange. Ein Fahrrad kommt später."),
        L("Anna", "f", "Klar. Und Tom? Sein Sohn baut doch immer alles."),
        L("Markus", "m", "Tom kauft einen Baukasten — sein Sohn baut den ganzen Tag. Ein Puzzle ist ihm zu einfach."),
        L("Anna", "f", "Passt. Und Sara? Die spielt gern mit der ganzen Familie."),
        L("Markus", "m", "Sara nimmt ein Brettspiel — für gemeinsame Abende mit der Familie. Einen Ball kauft sie nicht."),
        L("Anna", "f", "Und Tim? Seine Tochter ist noch klein."),
        L("Markus", "m", "Tim kauft ein Kuscheltier — einen großen Teddybär für seine kleine Tochter. Kein Auto und kein Puzzle."),
        L("Anna", "f", "Süß. Dann haben alle ein Geschenk. Wickeln sie das im Laden ein?"),
        L("Markus", "m", "Ja, das Einpacken ist dort kostenlos. Das ist praktisch vor dem Geburtstag."),
        L("Anna", "f", "Super, dann spare ich Zeit und Papier zu Hause."),
        L("Markus", "m", "Genau, und die Schleifen sehen immer schön aus."),
    ],
    t3=[
        [
            L("Kundin", "f", "Guten Tag, für welches Alter ist dieses Spiel? Ab vier, ab sechs oder ab acht?"),
            L("Verkäufer", "m", "Ab sechs Jahren. Ab vier ist es zu schwer, ab acht oft zu leicht."),
            L("Kundin", "f", "Mein Sohn ist erst vier. Dann ist sechs zu alt?"),
            L("Verkäufer", "m", "Ja, nehmen Sie lieber dieses hier, das ist ab vier. Nicht das ab sechs und nicht das ab acht."),
            L("Kundin", "f", "Danke, dann das für vier Jahre. Das andere ist ab sechs."),
        ],
        [
            L("Mann", "m", "Was kostet diese Puppe? 25 Euro, oder schon 45?"),
            L("Verkäuferin", "f", "Die Puppe allein 25 Euro. 45 Euro wäre mit Haus und Auto, das brauchen Sie nicht."),
            L("Mann", "m", "Und mit Kleidung? Ist das Set 35 oder 45?"),
            L("Verkäuferin", "f", "Das Set mit Kleidung kostet 35 Euro, nicht 25 und nicht 45. Die Kleidung ist dabei."),
            L("Mann", "m", "Gut, dann das Set für 35 Euro. Danke."),
        ],
        [
            L("Großmutter", "f", "Ich suche etwas für ein Baby. Kein Brettspiel und kein Fahrrad, das ist zu früh."),
            L("Verkäufer", "m", "Wie alt ist das Baby? Ein Brettspiel und ein Fahrrad sind wirklich nichts für Babys."),
            L("Großmutter", "f", "Acht Monate. Also wirklich kein Brettspiel und kein Fahrrad."),
            L("Verkäufer", "m", "Dann etwas Weiches ohne kleine Teile. Kein Brettspiel, kein Fahrrad, nur weich und sicher."),
            L("Großmutter", "f", "Perfekt, dann nehme ich das Weiche. Danke."),
        ],
        [
            L("Kunde", "m", "Können Sie das Geschenk einpacken? Kostet das 2 Euro oder 5 Euro?"),
            L("Verkäuferin", "f", "Gern, das ist kostenlos. Nicht 2 Euro und nicht 5 Euro, das Einpacken ist umsonst."),
            L("Kunde", "m", "Mit einer Schleife? Wirklich kostenlos, nicht 2 Euro?"),
            L("Verkäuferin", "f", "Natürlich, welche Farbe? Es bleibt kostenlos, kein Aufpreis von 2 oder 5 Euro."),
            L("Kunde", "m", "Dann rot, bitte. Danke, dass es kostenlos ist."),
        ],
        [
            L("Frau", "f", "Das Spielzeug ist schon kaputt. Reparieren Sie es, oder geben Sie kein Geld zurück?"),
            L("Verkäufer", "m", "Seit wann haben Sie es? Reparieren können wir hier nicht, und ohne Prüfung geben wir kein Geld zurück."),
            L("Frau", "f", "Erst seit gestern. Also tauschen Sie um, oder was dann?"),
            L("Verkäufer", "m", "Dann tausche ich es sofort um. Ich repariere es nicht, und Sie bekommen kein Geld, sondern ein neues Spielzeug."),
            L("Frau", "f", "Gut, dann den Umtausch. Danke."),
        ],
    ],
    t4=[
        L("Reporter", "m", "Frau Berg, hat sich das Spielzeug in den letzten Jahren verändert?"),
        L("Berg", "f", "Ja, sehr, früher gab es einfaches Holzspielzeug. Heute hat alles oft Elektronik. Manche Kinder mögen beides, Holz und Technik."),
        L("Reporter", "m", "Was kaufen die Leute am häufigsten, und wann ist am meisten los?"),
        L("Berg", "f", "Vor Weihnachten ist am meisten los, das Geschäft ist dann voll. Beliebt sind Baukästen und Brettspiele, die kaufen viele Familien."),
        L("Reporter", "m", "Worauf achten Sie bei Ihrem Spielzeug? Auf den Preis allein?"),
        L("Berg", "f", "Auf gute Qualität und Sicherheit. Billiges Spielzeug geht schnell kaputt. Ich achte also sehr auf Qualität und Sicherheit, nicht nur auf den Preis."),
        L("Reporter", "m", "Geben die Eltern zu viel Geld aus für Spielzeug?"),
        L("Berg", "f", "Manchmal ja. Kinder brauchen nicht so viel. Wenige gute Sachen sind besser als viele billige. Das sage ich den Eltern oft."),
        L("Reporter", "m", "Was ist das Schönste an Ihrem Beruf?"),
        L("Berg", "f", "Die glücklichen Kinder. Wenn ein Kind staunt, freue ich mich. Die glücklichen Kinder sind mir sehr wichtig, ohne sie wäre der Laden leer. Deshalb arbeite ich gern hier, auch vor Weihnachten, wenn es stressig ist. Das Lachen der Kinder ist der schönste Lohn."),
    ],
)

# ── 88 Online-Shopping und Rücksendung ────────────────────────────
apply(
    88,
    t1={
        2: "Achtung Kunden: Bitte beachten Sie unsere Rückgabe-Regeln. Sie können bestellte Ware innerhalb von 14 Tagen zurückschicken, ohne Grund, nicht nur 7 Tage und nicht erst nach 30 Tagen. Die Ware muss aber unbenutzt sein. Bei uns ist die Rücksendung kostenlos. Legen Sie einfach den Rückschein ins Paket. Das Geld kommt in einer Woche zurück.",
        4: "Liebe Kunden: Ab nächstem Monat ändern sich die Versandkosten. Ab einem Einkauf von 30 Euro ist der Versand weiterhin kostenlos, nicht schon ab 20 Euro und nicht erst ab 50 Euro. Bei kleineren Bestellungen zahlen Sie aber jetzt 5 Euro statt 4. Express-Lieferung am nächsten Tag kostet 10 Euro extra. Danke, dass Sie bei uns einkaufen!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, alle bestellen ständig online, fast jede Woche. Was hat jeder zuletzt gekauft?"),
        L("Markus", "m", "Also, Lukas hat Kleidung bestellt — gleich drei Hosen zum Anprobieren zu Hause. Schuhe wollte er diesmal nicht."),
        L("Anna", "f", "Typisch Lukas. Und Lisa? Die liest doch immer."),
        L("Markus", "m", "Lisa hat Bücher bestellt — sie liest ständig und kauft im Internet. Spielzeug bestellt sie nicht."),
        L("Anna", "f", "Klar. Und Tom? Der braucht oft Technik."),
        L("Markus", "m", "Tom hat Elektronik bestellt — neue Kopfhörer für unterwegs. Werkzeug hat er schon genug."),
        L("Anna", "f", "Und Sara? Die richtet gerade die Wohnung ein."),
        L("Markus", "m", "Sara hat Möbel bestellt — ein Regal, das sie selbst aufbauen muss. Medikamente kommen nicht ins Paket."),
        L("Anna", "f", "Und Tim? Der mag doch nicht so gern im Supermarkt stehen."),
        L("Markus", "m", "Tim hat Lebensmittel bestellt — er lässt sich den Einkauf nach Hause liefern. Keine Kleidung diesmal."),
        L("Anna", "f", "Praktisch. Schicken viele von denen Sachen wieder zurück, oder behalten sie alles?"),
        L("Markus", "m", "Lukas vielleicht, wegen der Hosen. Die anderen behalten meistens, was sie bestellt haben. Zurückschicken ist ja kostenlos."),
        L("Anna", "f", "Trotzdem ist das viel Verpackung. Ich kaufe lieber weniger, aber richtig."),
        L("Markus", "m", "Ja, das ist smarter. Dann muss man nicht so oft zur Post."),
    ],
    t3=[
        [
            L("Kundin", "f", "Guten Tag, ich möchte ein Paket zurückschicken. Brauche ich Bargeld oder einen Ausweis?"),
            L("Mitarbeiter", "m", "Haben Sie den Rückschein? Bargeld und Ausweis brauchen Sie nicht, nur den Schein."),
            L("Kundin", "f", "Ja, hier ist der Rückschein. Also kein Bargeld und kein Ausweis?"),
            L("Mitarbeiter", "m", "Gut, dann kleben Sie den Rückschein aufs Paket. Nicht Bargeld, nicht den Ausweis, nur den Rückschein."),
            L("Kundin", "f", "Verstanden, der Rückschein kommt aufs Paket. Danke."),
        ],
        [
            L("Mann", "m", "Wann bekomme ich mein Geld zurück? Sofort an der Kasse, oder erst nach einem Monat?"),
            L("Mitarbeiterin", "f", "Sobald die Ware bei uns ankommt, nicht sofort und nicht erst nach einem Monat."),
            L("Mann", "m", "Und das dauert wie lange? Eine Woche, oder wirklich ein Monat?"),
            L("Mitarbeiterin", "f", "Etwa eine Woche. Nicht sofort und nicht nach einem Monat, nach etwa einer Woche ist das Geld da."),
            L("Mann", "m", "Gut, dann warte ich eine Woche. Danke."),
        ],
        [
            L("Frau", "f", "Mein Paket ist nicht angekommen. Es ist nicht kaputt und nicht zu teuer, es fehlt einfach."),
            L("Mitarbeiter", "m", "Haben Sie eine Sendungsnummer? Wenn es kaputt wäre oder zu teuer, wäre das ein anderer Fall."),
            L("Frau", "f", "Ja, hier ist sie. Also das Problem ist: das Paket ist nicht angekommen."),
            L("Mitarbeiter", "m", "Ich schaue nach, wo es gerade ist. Nicht kaputt, nicht zu teuer, sondern nicht angekommen."),
            L("Frau", "f", "Danke, bitte sagen Sie mir, wo das Paket ist."),
        ],
        [
            L("Kunde", "m", "Kann ich das Paket beim Nachbarn abholen? Es liegt nicht auf der Post und nicht im Geschäft?"),
            L("Bote", "m", "Ja, bei Familie Klein, Nummer 12. Nicht auf der Post und nicht im Geschäft, beim Nachbarn."),
            L("Kunde", "m", "Brauche ich etwas? Einen Ausweis für die Post oder fürs Geschäft?"),
            L("Bote", "m", "Nur den Zettel im Briefkasten. Das Paket ist beim Nachbarn, nicht auf der Post, nicht im Geschäft."),
            L("Kunde", "m", "Alles klar, dann gehe ich zu Familie Klein. Danke."),
        ],
        [
            L("Kundin", "f", "Die Bluse hat einen Fleck. Muss ich die Rücksendung zahlen, oder zahlt niemand?"),
            L("Mitarbeiter", "m", "Das tut mir leid. Schicken Sie sie zurück. Nicht Sie und nicht niemand, wir klären das."),
            L("Kundin", "f", "Muss ich den Versand zahlen, oder zahlt der Shop?"),
            L("Mitarbeiter", "m", "Nein, bei einem Fehler zahlen wir, der Shop. Nicht die Kundin und nicht niemand."),
            L("Kundin", "f", "Gut, dann zahlt der Shop die Rücksendung. Danke."),
        ],
    ],
    t4=[
        L("Reporterin", "f", "Herr Lang, warum kaufen die Leute gern im Internet?"),
        L("Lang", "m", "Weil es bequem ist. Man kann zu jeder Zeit bestellen, auch nachts. Online-Shopping ist bequem, weil man immer bestellen kann, nicht nur am Tag."),
        L("Reporterin", "f", "Schicken die Leute viel zurück? Ist das ein Problem?"),
        L("Lang", "m", "Ja, sehr viel, vor allem Kleidung. Das ist schlecht für die Umwelt. Viele Rücksendungen sind ein Problem, nicht kein Problem."),
        L("Reporterin", "f", "Schadet das Online-Shopping den Geschäften in der Stadt?"),
        L("Lang", "m", "Leider ja, viele kleine Läden haben Probleme. Das ist schade. Durch das Internet haben kleine Läden oft weniger Kunden."),
        L("Reporterin", "f", "Worauf soll man beim Bestellen achten, zum Beispiel bei der Größe?"),
        L("Lang", "m", "Lesen Sie die Beschreibung genau und schauen Sie auf die Größe. Prüfen Sie die Größe vor dem Bestellen, sonst passt die Hose nicht."),
        L("Reporterin", "f", "Was raten Sie noch? Soll man möglichst viel auf einmal bestellen?"),
        L("Lang", "m", "Nein, bestellen Sie nicht zu viel auf einmal. Dann müssen Sie weniger zurückschicken. Möglichst viel auf einmal ist keine gute Idee. Lieber genau bestellen, das spart Zeit und ist besser für die Umwelt. So bleibt weniger Müll übrig."),
    ],
)

print("83-88 applied")

