#!/usr/bin/env python3
"""Expand Goethe A2 Hören tests 89-94 to official length. Temporary mutator."""
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


# ── 89 Beim Umzugsunternehmen ─────────────────────────────────────
apply(
    89,
    t1={
        2: "Achtung Kunden: Bitte beschriften Sie alle Kartons. Schreiben Sie drauf, in welches Zimmer sie kommen und was drin ist, nicht nur den Namen und nicht das Datum. Schwere Sachen wie Bücher in kleine Kartons, leichte in große. So geht der Umzug schneller und nichts geht kaputt. Zerbrechliche Sachen bitte extra kennzeichnen. Danke!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, beim Umzug hilft jeder mit. Das ist super, aber wer macht was genau?"),
        L("Markus", "m", "Also, Lukas packt die Kartons — er ist sehr ordentlich und beschriftet alles. Putzen macht er später."),
        L("Anna", "f", "Passt zu Lukas. Und Lisa? Die ist doch ziemlich stark."),
        L("Markus", "m", "Lisa trägt die Möbel — sie ist stark und packt richtig mit an. Die Kinder betreut sie nicht."),
        L("Anna", "f", "Gut. Und Tom? Der hat doch den großen Führerschein."),
        L("Markus", "m", "Tom fährt den Lkw — er hat den Führerschein dafür. Den Parkplatz hält ein Nachbar frei."),
        L("Anna", "f", "Praktisch. Und Sara? Die kennt sich mit Werkzeug aus."),
        L("Markus", "m", "Sara baut die Möbel auf — sie kennt sich mit Werkzeug gut aus. Den Müll bringt sie nicht weg."),
        L("Anna", "f", "Und Tim? Der kocht so gern, oder?"),
        L("Markus", "m", "Tim sorgt fürs Essen — er kocht für alle, damit niemand schlapp macht. Kartons packt er nicht."),
        L("Anna", "f", "Perfekt, dann hat jeder eine klare Aufgabe. Wann treffen wir uns?"),
        L("Markus", "m", "Samstag früh um sieben. Bitte nicht zu spät, der Lkw kommt pünktlich."),
        L("Anna", "f", "Klar, ich stelle den Wecker. Trinken haben wir auch genug?"),
        L("Markus", "m", "Ja, Wasser und Saft stehen in der Küche bereit."),
    ],
    t3=[
        [
            L("Kundin", "f", "Guten Tag, was kostet der Umzug? 600 Euro, oder schon 300?"),
            L("Mitarbeiter", "m", "Das Basis-Paket 600 Euro. 300 Euro reicht bei uns nicht, das wäre zu wenig."),
            L("Kundin", "f", "Und mit Aufbau? Ist das dann 900 oder bleiben 600?"),
            L("Mitarbeiter", "m", "Dann 900 Euro. Nicht 600 und nicht 300, mit Aufbau sind es 900."),
            L("Kundin", "f", "Verstehe, dann 900 Euro mit Aufbau. Danke."),
        ],
        [
            L("Mann", "m", "Wie viele Leute kommen? Zwei, drei oder vier?"),
            L("Mitarbeiterin", "f", "Drei Männer und ein Lkw. Nicht zwei und nicht vier, drei Leute reichen."),
            L("Mann", "m", "Reicht das für eine große Wohnung? Zwei wären zu wenig, oder?"),
            L("Mitarbeiterin", "f", "Ja, drei schaffen wir in einem Tag. Nicht zwei und nicht vier, drei sind geplant."),
            L("Mann", "m", "Gut, dann drei Leute. Das beruhigt mich."),
        ],
        [
            L("Frau", "f", "Sind die Möbel versichert? Ich frage nicht nach dem Preis und nicht nach der Uhrzeit."),
            L("Mitarbeiter", "m", "Ja, falls etwas kaputtgeht. Zum Preis und zum Termin sagen wir später mehr."),
            L("Frau", "f", "Auch das teure Klavier? Also wirklich versichert, nicht nur der Preis?"),
            L("Mitarbeiter", "m", "Ja, das ist mitversichert. Sie wollten wissen, ob die Möbel versichert sind, und ja, das sind sie."),
            L("Frau", "f", "Danke, das ist mir wichtig. Den Preis klären wir danach."),
        ],
        [
            L("Kunde", "m", "Brauchen Sie einen Parkplatz vor dem Haus? Oder einen Aufzug, oder eine Garage?"),
            L("Mitarbeiterin", "f", "Ja, einen Parkplatz direkt vor dem Haus. Einen Aufzug und eine Garage brauchen wir nicht."),
            L("Kunde", "m", "Wie groß? Reicht eine Garage, oder wirklich der Parkplatz?"),
            L("Mitarbeiterin", "f", "Für den Lkw etwa zwei Autolängen, also den Parkplatz. Nicht den Aufzug, nicht die Garage."),
            L("Kunde", "m", "Alles klar, ich halte den Parkplatz frei. Danke."),
        ],
        [
            L("Kundin", "f", "Können Sie auch am Sonntag kommen? Oder nur am Freitag?"),
            L("Mitarbeiter", "m", "Sonntags arbeiten wir nicht. Freitag geht, aber Samstag auch."),
            L("Kundin", "f", "Und am Samstag? Sonntag wirklich nicht, Freitag wäre früh."),
            L("Mitarbeiter", "m", "Samstag geht, aber etwas teurer. Nicht am Sonntag, Freitag nur wenn Sie wollen."),
            L("Kundin", "f", "Dann nehmen wir Samstag. Danke."),
        ],
    ],
    t4=None,
)

# ── 90 Im Sportgeschäft ───────────────────────────────────────────
apply(
    90,
    t1={
        0: "Liebe Kunden: Großer Saisonverkauf im Sportgeschäft. Alle Skier und Snowboards sind jetzt 40 Prozent günstiger, der Winter ist ja fast vorbei. Die neue Sommerware wie Fahrräder und Schwimmsachen ist aber nicht reduziert, nur Skier und Snowboards. Greifen Sie schnell zu, das Angebot gilt bis Sonntag. Viel Spaß beim Sport!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, alle brauchen neue Sportsachen. Was kauft jeder im Sportgeschäft?"),
        L("Markus", "m", "Also, Lukas kauft ein Fahrrad — er will jeden Tag zur Arbeit radeln. Einen Helm hat er schon."),
        L("Anna", "f", "Gut für ihn. Und Lisa? Die schwimmt doch jetzt oft."),
        L("Markus", "m", "Lisa braucht eine Schwimmbrille — sie geht jetzt zweimal die Woche schwimmen. Eine Yogamatte hat sie schon."),
        L("Anna", "f", "Und Tom? Der fährt im Winter immer in die Berge."),
        L("Markus", "m", "Tom kauft Skier — er fährt im Winter in die Alpen. Einen Tennisschläger will er nicht."),
        L("Anna", "f", "Klar. Und Sara? Die plant die große Tour."),
        L("Markus", "m", "Sara braucht Wanderschuhe — sie macht eine große Bergtour. Hanteln kauft sie nicht."),
        L("Anna", "f", "Und Tim? Der spielt jedes Wochenende, oder?"),
        L("Markus", "m", "Tim kauft einen Fußball — er spielt jedes Wochenende mit Freunden. Skier sind nichts für ihn."),
        L("Anna", "f", "Dann sind alle ausgerüstet. Gehst du auch noch in den Laden?"),
        L("Markus", "m", "Vielleicht später. Ich brauche nur Socken, das ist schnell erledigt."),
        L("Anna", "f", "Gut, dann sehen wir uns vielleicht dort. Um wie viel?"),
        L("Markus", "m", "Gegen vier, nach der Arbeit. Dann können wir zusammen schauen."),
    ],
    t3=[
        [
            L("Kunde", "m", "Was kostet dieses Fahrrad? Ist Licht und Schloss dabei, oder ein Helm, oder eine Tasche?"),
            L("Verkäufer", "m", "499 Euro, mit Licht und Schloss. Helm und Tasche sind nicht dabei."),
            L("Kunde", "m", "Ist ein Helm dabei? Oder nur Licht und Schloss, ohne Tasche?"),
            L("Verkäufer", "m", "Nein, der Helm kostet extra, und eine Tasche auch. Dabei sind Licht und Schloss."),
            L("Kunde", "m", "Verstehe, Licht und Schloss ja, Helm und Tasche extra. Danke."),
        ],
        [
            L("Kundin", "f", "Ich suche Laufschuhe. Ich laufe nicht auf der Straße und nicht im Fitnessstudio."),
            L("Verkäuferin", "f", "Laufen Sie auf der Straße oder im Wald? Im Fitnessstudio brauchen Sie andere Schuhe."),
            L("Kundin", "f", "Meistens im Wald. Also nicht Straße, nicht Studio."),
            L("Verkäuferin", "f", "Dann brauchen Sie ein festeres Modell für den Wald, nicht für die Straße und nicht fürs Studio."),
            L("Kundin", "f", "Gut, dann das Modell für den Wald. Danke."),
        ],
        [
            L("Mann", "m", "Können Sie mein Fahrrad reparieren? Der Reifen ist gut, das Licht auch."),
            L("Mechaniker", "m", "Was ist denn kaputt? Reifen und Licht kann ich auch machen, aber was genau?"),
            L("Mann", "m", "Die Bremse funktioniert nicht. Nicht der Reifen und nicht das Licht."),
            L("Mechaniker", "m", "Das mache ich gleich, in 20 Minuten. Die Bremse, nicht Reifen oder Licht."),
            L("Mann", "m", "Super, dann warte ich hier. Danke."),
        ],
        [
            L("Kundin", "f", "Kann ich die Skier auch mieten? Pro Tag 15 Euro, oder 80, oder 10?"),
            L("Verkäufer", "m", "Ja, 15 Euro pro Tag. 10 Euro wäre zu wenig, 80 Euro ist der Wochenpreis."),
            L("Kundin", "f", "Und für eine Woche? Nicht 15 pro Tag und nicht 10?"),
            L("Verkäufer", "m", "Eine Woche 80 Euro. Pro Tag bleiben 15 Euro, nicht 10 und nicht 80 am Tag."),
            L("Kundin", "f", "Dann miete ich eine Woche für 80 Euro. Danke."),
        ],
        [
            L("Vater", "m", "Mein Sohn braucht Fußballschuhe, nicht Laufschuhe und nicht Wanderschuhe."),
            L("Verkäuferin", "f", "Welche Größe? Laufschuhe und Wanderschuhe haben wir auch, aber Sie wollen Fußballschuhe."),
            L("Vater", "m", "Größe 36. Also wirklich Fußballschuhe, keine Laufschuhe."),
            L("Verkäuferin", "f", "Die haben wir, kommen Sie mit. Fußballschuhe Größe 36, nicht Laufschuhe, nicht Wanderschuhe."),
            L("Vater", "m", "Perfekt, dann nehmen wir die Fußballschuhe. Danke."),
        ],
    ],
    t4=None,
)

# ── 91 In der Apotheke ────────────────────────────────────────────
apply(
    91,
    t1={
        2: "Achtung Kunden: Bitte beachten Sie unseren Notdienst. Nachts und am Wochenende hat immer eine Apotheke in der Stadt geöffnet. Welche das ist, steht an unserer Tür und im Internet, nicht nur im Krankenhaus und nicht beim Arzt. Für dringende Medikamente fahren Sie bitte dorthin. Wir wünschen gute Besserung und ein schnelles Gesundwerden!",
        4: "Liebe Kunden: Vergessen Sie nicht Ihre Reiseapotheke für den Urlaub. Schmerzmittel, etwas gegen Durchfall und Pflaster gehören in jedes Gepäck, nicht nur Vitamine und nicht nur Sonnencreme. Wir beraten Sie gern, was Sie für Ihr Reiseland brauchen. Manche Medikamente gibt es im Ausland nicht. Kommen Sie rechtzeitig vorbei, bevor Sie fahren!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, alle müssen in die Apotheke. Was braucht jeder?"),
        L("Markus", "m", "Also, Lukas braucht Hustensaft — er ist erkältet und hustet die ganze Nacht. Nasenspray hat er schon."),
        L("Anna", "f", "Armer Lukas. Und Lisa? Die hat oft Kopfweh."),
        L("Markus", "m", "Lisa braucht Schmerztabletten — gegen ihre Kopfschmerzen. Augentropfen braucht sie nicht."),
        L("Anna", "f", "Und Tom? Der war gestern lange im Fitnessstudio."),
        L("Markus", "m", "Tom braucht eine Salbe — gegen seinen Muskelschmerz nach dem Sport. Tee gegen Husten trinkt er nicht."),
        L("Anna", "f", "Und Sara? Ihr Kind ist doch gestürzt."),
        L("Markus", "m", "Sara braucht Pflaster und Verband — ihr Kind hat sich am Knie verletzt. Ein Fieberthermometer hat sie schon."),
        L("Anna", "f", "Und Tim? Der ist im Winter immer so müde."),
        L("Markus", "m", "Tim braucht Vitamine — er fühlt sich im Winter oft müde und schlapp. Hustensaft braucht er nicht."),
        L("Anna", "f", "Dann gehen viele heute noch zur Apotheke. Soll ich etwas mitbringen?"),
        L("Markus", "m", "Nein, danke, ich brauche nichts. Ich wünsche allen gute Besserung."),
        L("Anna", "f", "Ja, ich schreibe später in die Gruppe. Bis später."),
        L("Markus", "m", "Bis später, und nimm dir Zeit in der Apotheke, dort ist oft viel los."),
    ],
    t3=[
        [
            L("Kundin", "f", "Ich brauche etwas gegen Halsschmerzen. Lutschtabletten, Spray oder Tee?"),
            L("Apotheker", "m", "Lutschtabletten oder Spray wirken schnell. Tee ist angenehm, aber langsamer."),
            L("Kundin", "f", "Was wirkt schneller? Die Lutschtabletten, das Spray oder der Tee?"),
            L("Apotheker", "m", "Das Spray. Lutschtabletten helfen auch, Tee braucht länger. Das Spray wirkt am schnellsten."),
            L("Kundin", "f", "Dann nehme ich das Spray. Danke."),
        ],
        [
            L("Mann", "m", "Brauche ich für dieses Medikament ein Rezept? Oder reicht Bargeld, oder gar nichts?"),
            L("Apothekerin", "f", "Ja, das erste gibt es nur mit Rezept. Bargeld allein reicht nicht, und nichts auch nicht."),
            L("Mann", "m", "Und etwas Ähnliches ohne Rezept? Also nichts Extra, nur ohne Schein?"),
            L("Apothekerin", "f", "Dieses hier ist rezeptfrei. Für das erste brauchen Sie ein Rezept, nicht nichts und nicht nur Bargeld."),
            L("Mann", "m", "Verstehe, dann hole ich das Rezept beim Arzt. Danke."),
        ],
        [
            L("Mutter", "f", "Mein Kind hat Fieber. Was kann ich geben? Einmal täglich, oder jede Stunde?"),
            L("Apotheker", "m", "Wie alt ist das Kind? Einmal täglich kann zu wenig sein, jede Stunde zu viel."),
            L("Mutter", "f", "Drei Jahre. Also wie oft den Saft?"),
            L("Apotheker", "m", "Dann diesen Saft, dreimal täglich. Nicht einmal und nicht jede Stunde, dreimal reicht."),
            L("Mutter", "f", "Gut, dreimal täglich. Danke."),
        ],
        [
            L("Kunde", "m", "Wie soll ich die Tabletten nehmen? Vor dem Essen, ohne Wasser, oder nach dem Essen?"),
            L("Apothekerin", "f", "Eine morgens, eine abends. Nicht ohne Wasser, das ist wichtig."),
            L("Kunde", "m", "Vor oder nach dem Essen? Ohne Wasser geht nicht, oder?"),
            L("Apothekerin", "f", "Nach dem Essen, mit Wasser. Nicht vor dem Essen und nicht ohne Wasser."),
            L("Kunde", "m", "Alles klar, nach dem Essen mit Wasser. Danke."),
        ],
        [
            L("Kundin", "f", "Ist heute Nacht eine Apotheke offen? Die Stadt-Apotheke, oder keine?"),
            L("Apotheker", "m", "Ja, die Bahnhof-Apotheke. Die Stadt-Apotheke hat zu, und keine wäre falsch."),
            L("Kundin", "f", "Die ganze Nacht? Also nicht die Stadt-Apotheke?"),
            L("Apotheker", "m", "Ja, sie hat Notdienst. Die Bahnhof-Apotheke, nicht die Stadt-Apotheke, und nicht keine."),
            L("Kundin", "f", "Danke, dann fahre ich zur Bahnhof-Apotheke."),
        ],
    ],
    t4=[
        L("Reporter", "m", "Frau Roth, warum ist die Apotheke vor Ort wichtig?"),
        L("Roth", "f", "Weil wir die Kunden beraten. Im Internet bekommt man keinen Rat. Die Beratung in der Apotheke ist wichtig, das sehe ich jeden Tag."),
        L("Reporter", "m", "Kommen die Leute auch ohne Arzt zu Ihnen, bei einer Erkältung zum Beispiel?"),
        L("Roth", "f", "Ja, oft. Bei einer leichten Erkältung kann ich gut helfen. Viele kommen zuerst zu uns, das ist in Ordnung."),
        L("Reporter", "m", "Und bei starken Schmerzen? Geben Sie dann einfach Tabletten?"),
        L("Roth", "f", "Dann schicke ich die Leute zum Arzt. Das ist sicherer. Bei starken Schmerzen ist der Arzt besser als nur eine Tablette hier."),
        L("Reporter", "m", "Nehmen die Menschen zu viele Tabletten? Soll man bei jeder Kleinigkeit eine nehmen?"),
        L("Roth", "f", "Manche schon. Oft helfen auch Ruhe, Schlaf und viel Wasser. Man soll nicht bei jeder Kleinigkeit eine Tablette nehmen."),
        L("Reporter", "m", "Was ist bei Tabletten wichtig? Muss man den Zettel lesen?"),
        L("Roth", "f", "Lesen Sie immer den Zettel. Und nehmen Sie nicht mehr als erlaubt. Den Zettel muss man lesen, das ist keine Extra-Arbeit, sondern der beste Schutz für Ihre Gesundheit. Fragen Sie uns, wenn etwas unklar ist."),
    ],
)

# ── 92 In der Eisdiele ────────────────────────────────────────────
apply(
    92,
    t1={
        0: "Liebe Gäste: Willkommen in der Eisdiele Bella. Wir haben eine neue Sorte — Lavendel-Honig, ganz besonders! Probieren Sie sie heute kostenlos. Unsere beliebte Schokolade ist leider gerade aus, kommt aber morgen wieder. Vanille haben wir wie immer. Wir machen alle Sorten frisch und selbst. Lassen Sie es sich schmecken!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, jeder hat seine Lieblingssorte in der Eisdiele. Was mag jeder am liebsten?"),
        L("Markus", "m", "Also, Lukas liebt Schokolade — er nimmt nie etwas anderes. Mango mag er nicht."),
        L("Anna", "f", "Typisch Lukas. Und Lisa? Die mag Früchte, oder?"),
        L("Markus", "m", "Lisa mag Erdbeere — am liebsten mit frischen Früchten obendrauf. Joghurt nimmt sie selten."),
        L("Anna", "f", "Und Tom? Der ist doch eher klassisch."),
        L("Markus", "m", "Tom nimmt immer Vanille — der Klassiker, sagt er. Haselnuss ist ihm zu besonders."),
        L("Anna", "f", "Und Sara? Die will im Sommer immer etwas Frisches."),
        L("Markus", "m", "Sara liebt Zitrone — schön frisch und sauer, perfekt im Sommer. Stracciatella mag sie weniger."),
        L("Anna", "f", "Und Tim? Der will immer etwas Besonderes."),
        L("Markus", "m", "Tim mag Pistazie — eine besondere Sorte, sagt er, für Kenner. Vanille ist ihm zu einfach."),
        L("Anna", "f", "Dann wissen wir, was wir bestellen. Gehen wir gleich hin?"),
        L("Markus", "m", "Ja, um vier am Markt. Die Schlange ist dann noch nicht so lang."),
        L("Anna", "f", "Gut, ich bringe Kleingeld mit. Drei Kugeln werden es bei mir, sonst ist es zu viel."),
        L("Markus", "m", "Bei mir zwei, sonst esse ich zu viel am Nachmittag. Bis später!"),
    ],
    t3=[
        [
            L("Kundin", "f", "Was kostet eine Kugel? 1 Euro 50, oder schon 3 Euro, oder 4 Euro 50?"),
            L("Verkäufer", "m", "Eine Kugel 1 Euro 50. 3 Euro wären zwei Kugeln, 4 Euro 50 drei."),
            L("Kundin", "f", "Dann drei Kugeln, bitte. Was kosten die drei?"),
            L("Verkäufer", "m", "Das macht 4 Euro 50. Nicht 1 Euro 50 für drei und nicht 3 Euro, drei Kugeln sind 4 Euro 50."),
            L("Kundin", "f", "Gut, dann 4 Euro 50. Danke."),
        ],
        [
            L("Junge", "m", "Im Becher oder in der Waffel? Zum Mitnehmen wäre auch möglich."),
            L("Mutter", "f", "Was möchtest du? Becher, Waffel oder zum Mitnehmen nach Hause?"),
            L("Junge", "m", "In der Waffel! Nicht im Becher und nicht zum Mitnehmen."),
            L("Mutter", "f", "Gut, eine Waffel. Nicht der Becher und nicht zum Mitnehmen, eine Waffel."),
            L("Junge", "m", "Danke Mama, die Waffel ist das Beste."),
        ],
        [
            L("Kunde", "m", "Haben Sie auch veganes Eis? Schokolade, Mango oder Vanille?"),
            L("Verkäuferin", "f", "Ja, mehrere Sorten. Schokolade und Vanille gibt es, aber nicht alle sind vegan."),
            L("Kunde", "m", "Welche empfehlen Sie? Schokolade, Mango oder Vanille?"),
            L("Verkäuferin", "f", "Die Mango-Sorte ist sehr beliebt und vegan. Schokolade und Vanille sind bei uns nicht vegan."),
            L("Kunde", "m", "Dann Mango, bitte. Danke für den Tipp."),
        ],
        [
            L("Frau", "f", "Ich möchte eine Eistorte bestellen. Für Freitag, Samstag oder Sonntag?"),
            L("Verkäufer", "m", "Für wann? Freitag ist schon voll, Sonntag geht auch, Samstag noch frei."),
            L("Frau", "f", "Für Samstag. Nicht Freitag und nicht Sonntag."),
            L("Verkäufer", "m", "Geht klar, holen Sie sie am Samstag ab. Nicht Freitag, nicht Sonntag, Samstag."),
            L("Frau", "f", "Perfekt, dann Samstag. Danke."),
        ],
        [
            L("Tochter", "f", "Papa, darf ich noch eine Kugel? Oder einen Becher extra?"),
            L("Vater", "m", "Du hattest schon zwei. Eine dritte Kugel ist viel, ein Becher brauchen wir nicht."),
            L("Tochter", "f", "Bitte, nur eine kleine! Nicht nein und keinen extra Becher."),
            L("Vater", "m", "Na gut, aber dann ist Schluss. Ja, noch eine Kugel, nicht nein, und keinen Becher."),
            L("Tochter", "f", "Danke Papa, nur die eine Kugel."),
        ],
    ],
    t4=[
        L("Reporterin", "f", "Herr Conti, was ist Ihr Geheimnis beim Eis?"),
        L("Conti", "m", "Gute, frische Zutaten. Echte Früchte und echte Milch. Das schmeckt man. Ohne frische Zutaten wird das Eis nicht gut."),
        L("Reporterin", "f", "Welche Sorte verkaufen Sie am meisten, Schokolade oder Vanille?"),
        L("Conti", "m", "Schokolade und Vanille. Aber die Leute probieren auch neue Sorten. Die Klassiker verkaufe ich am meisten, jeden Tag."),
        L("Reporterin", "f", "Ist es ein hartes Geschäft? Hängt es vom Wetter ab?"),
        L("Conti", "m", "Ja, sehr, wir hängen vom Wetter ab. Ein nasser Sommer ist schlecht für uns. Das Eisgeschäft ist also vom Wetter abhängig, das ist klar."),
        L("Reporterin", "f", "Essen die Leute viel Eis, vor allem im Sommer?"),
        L("Conti", "m", "Oh ja, vor allem im Sommer. Eis macht einfach glücklich. Im Sommer essen die Leute viel Eis, im Winter weniger."),
        L("Reporterin", "f", "Was lieben Sie an Ihrem Beruf? Finden Sie ihn schön?"),
        L("Conti", "m", "Die glücklichen Gesichter. Ein Kind mit einem Eis lacht über das ganze Gesicht. Ich finde meinen Beruf sehr schön, jeden einzelnen Tag. Ohne diese Freude würde ich die lange Arbeit im Sommer nicht schaffen. Deshalb stehe ich gern früh auf und mache das Eis frisch."),
    ],
)

# ── 93 Beim Kinderarzt ────────────────────────────────────────────
apply(
    93,
    t2=[
        L("Anna", "f", "Hallo Markus, alle gehen gerade mit den Kindern zum Arzt. Warum geht jeder?"),
        L("Markus", "m", "Also, Lukas geht zur Impfung — sein Sohn ist mit den Impfungen dran. Husten hat das Kind nicht."),
        L("Anna", "f", "Gut, Impfen ist wichtig. Und Lisa? Ihre Tochter ist doch krank."),
        L("Markus", "m", "Lisa geht wegen Fieber — ihre Tochter ist seit Tagen krank. Eine Augenkontrolle ist das nicht."),
        L("Anna", "f", "Arme Kleine. Und Tom? Bei ihm ist doch alles ruhig."),
        L("Markus", "m", "Tom geht zur Vorsorge — die normale Kontrolle, ob alles in Ordnung ist. Keine Verletzung, nur Vorsorge."),
        L("Anna", "f", "Und Sara? Ihr Sohn hat doch rote Flecken."),
        L("Markus", "m", "Sara geht wegen Hautausschlag — ihr Sohn hat rote Flecken am Bauch. Bauchschmerzen hat er nicht."),
        L("Anna", "f", "Und Tim? Seine Tochter weint nachts, oder?"),
        L("Markus", "m", "Tim geht wegen Ohrenschmerzen — seine Tochter weint die ganze Nacht. Es ist kein Sturz, nur das Ohr."),
        L("Anna", "f", "Dann haben alle einen Grund. Hoffentlich geht es den Kindern bald besser."),
        L("Markus", "m", "Ja, der Kinderarzt ist gut. Ich bringe später noch Saft für Lisas Tochter vorbei."),
        L("Anna", "f", "Liebe Idee. Soll ich auch etwas kaufen, vielleicht Zwieback?"),
        L("Markus", "m", "Wenn du magst, ja. Aber nur wenn du Zeit hast nach der Arbeit."),
    ],
    t3=[
        [
            L("Mutter", "f", "Wie hoch ist das Fieber jetzt? 37 Grad, 40 Grad oder 39?"),
            L("Ärztin", "f", "39 Grad. Geben Sie ihm den Saft. 37 wäre normal, 40 wäre sehr hoch."),
            L("Mutter", "f", "Wie oft den Saft? Also bei 39 Grad, nicht bei 37?"),
            L("Ärztin", "f", "Bei Bedarf, höchstens dreimal am Tag. Das Fieber ist 39, nicht 37 und nicht 40."),
            L("Mutter", "f", "Verstanden, 39 Grad, Saft bei Bedarf. Danke Ihnen."),
        ],
        [
            L("Vater", "m", "Darf mein Sohn morgen in die Schule? Nur einen Tag zu Hause, oder eine Woche?"),
            L("Arzt", "m", "Noch nicht, er ist ansteckend. Ein Tag ist zu wenig, eine Woche oft zu lang."),
            L("Vater", "m", "Wie lange muss er zu Hause bleiben? Einen Tag, eine Woche oder zwei Tage?"),
            L("Arzt", "m", "Noch zwei Tage. Nicht einen Tag und nicht eine Woche, zwei Tage reichen."),
            L("Vater", "m", "Gut, dann zwei Tage zu Hause. Danke."),
        ],
        [
            L("Mutter", "f", "Tut die Impfung weh? Sehr schmerzhaft, nur ein kleiner Pieks, oder gar nicht spürbar?"),
            L("Ärztin", "f", "Nur ein kleiner Pieks. Sehr schmerzhaft ist sie nicht, und ganz ohne Gefühl auch nicht."),
            L("Mutter", "f", "Und danach? Bleibt es nur ein Pieks, nicht sehr schmerzhaft?"),
            L("Ärztin", "f", "Der Arm kann etwas wehtun, das ist normal. Es ist ein kleiner Pieks, nicht sehr schmerzhaft und nicht unsichtbar."),
            L("Mutter", "f", "Okay, dann ein kleiner Pieks. Das schafft er."),
        ],
        [
            L("Vater", "m", "Mein Sohn isst kaum noch. Soll er viel essen, oder vor allem schlafen, oder trinken?"),
            L("Arzt", "m", "Trinkt er wenigstens? Viel essen muss er jetzt nicht, und Schlaf kommt von allein."),
            L("Vater", "m", "Ja, viel Wasser. Also ist Trinken wichtiger als Essen und Schlafen?"),
            L("Arzt", "m", "Gut, das ist das Wichtigste: dass das Kind genug trinkt. Nicht dass es viel isst, und Schlafen hilft extra."),
            L("Vater", "m", "Verstehe, vor allem trinken. Danke."),
        ],
        [
            L("Mutter", "f", "Wann ist die nächste Untersuchung? In drei Monaten, in einem Monat oder in einem Jahr?"),
            L("Sprechstundenhilfe", "f", "In drei Monaten. Ein Monat ist zu früh, ein Jahr zu spät."),
            L("Mutter", "f", "Bekomme ich eine Erinnerung? Also in drei Monaten, nicht in einem Monat?"),
            L("Sprechstundenhilfe", "f", "Ja, wir schicken Ihnen eine Karte. Der Termin ist in drei Monaten, nicht in einem Monat und nicht in einem Jahr."),
            L("Mutter", "f", "Perfekt, dann warte ich auf die Karte. Danke."),
        ],
    ],
    t4=None,
)

# ── 94 An der Tankstelle ──────────────────────────────────────────
apply(
    94,
    t1={
        0: "Liebe Kunden: An unserer Tankstelle ist der Diesel diese Woche im Angebot, fünf Cent günstiger pro Liter. Benzin bleibt leider beim normalen Preis, es ist also nicht beides günstiger. Außerdem gibt es beim Tanken ab vierzig Litern einen kostenlosen Kaffee. Nutzen Sie das Angebot, es gilt nur bis Sonntag. Gute Fahrt!",
    },
    t2=[
        L("Anna", "f", "Hallo Markus, an der Tankstelle macht jeder etwas anderes. Was macht jeder?"),
        L("Markus", "m", "Also, Lukas tankt nur — schnell volltanken und weiterfahren. Die Scheiben putzt er nicht."),
        L("Anna", "f", "Typisch eilig. Und Lisa? Ihr Auto ist oft so sauber."),
        L("Markus", "m", "Lisa wäscht ihr Auto — sie nutzt immer die Waschanlage dort. Öl füllt sie nicht nach."),
        L("Anna", "f", "Und Tom? Der fährt oft weit."),
        L("Markus", "m", "Tom prüft den Reifendruck — er kontrolliert das vor jeder langen Fahrt. Eine Karte kauft er nicht."),
        L("Anna", "f", "Klug. Und Sara? Die holt sich oft etwas zu essen."),
        L("Markus", "m", "Sara kauft im Shop ein — sie holt sich Kaffee und ein belegtes Brötchen. Staubsaugen macht sie nicht."),
        L("Anna", "f", "Und Tim? Der pflegt sein Auto so genau."),
        L("Markus", "m", "Tim füllt Luft in die Reifen und Wasser nach — er pflegt sein Auto genau. Er tankt danach extra."),
        L("Anna", "f", "Dann erledigt jeder etwas anderes. Soll ich auch den Reifendruck prüfen?"),
        L("Markus", "m", "Kannst du machen, ja. Vor der Fahrt in den Urlaub ist das wichtig."),
        L("Anna", "f", "Gut, dann fahre ich morgen früh zur Tankstelle, wenn wenig los ist."),
        L("Markus", "m", "Gute Idee, morgens um sieben ist es ruhig und oft günstiger."),
    ],
    t3=[
        [
            L("Kunde", "m", "Entschuldigung, welche Säule war das gerade? Nummer 2, Nummer 4 oder Nummer 6?"),
            L("Kassierer", "m", "Welche Nummer steht da an der Säule? 2, 4 oder 6, das muss auf dem Display stehen."),
            L("Kunde", "m", "Ah, Nummer 4. Nicht 2 und nicht 6, ich habe nachgeschaut."),
            L("Kassierer", "m", "Gut, das macht 65 Euro. Säule Nummer 4, nicht 2 und nicht 6."),
            L("Kunde", "m", "Alles klar, Nummer 4, 65 Euro. Hier ist die Karte, danke."),
        ],
        [
            L("Kundin", "f", "Guten Tag, was kostet die Autowäsche heute? 6 Euro, 9 Euro oder 12 Euro?"),
            L("Mitarbeiter", "m", "Das einfache Programm kostet 6 Euro. 12 Euro wäre das größte Programm mit Extra-Glanz."),
            L("Kundin", "f", "Und mit Wachs? Ist das 9 Euro oder 12 Euro?"),
            L("Mitarbeiter", "m", "Mit Wachs 9 Euro. Nicht 6 und nicht 12, mit Wachs sind es 9 Euro."),
            L("Kundin", "f", "Dann nehme ich mit Wachs für 9 Euro. Danke."),
        ],
        [
            L("Mann", "m", "Wo kann ich Luft in die Reifen füllen? Kostet das 2 Euro oder 5 Euro?"),
            L("Mitarbeiterin", "f", "Hinten links, neben der Waschanlage. 2 Euro oder 5 Euro wäre viel für Luft."),
            L("Mann", "m", "Kostet das was? 2 Euro, 5 Euro oder nichts?"),
            L("Mitarbeiterin", "f", "Nein, das ist kostenlos. Nicht 2 Euro und nicht 5 Euro, Luft ist umsonst."),
            L("Mann", "m", "Super, dann kostenlos. Danke."),
        ],
        [
            L("Kunde", "m", "Kann ich mit Karte zahlen? Auch einen kleinen Betrag, oder erst ab zehn Euro, oder gar nicht?"),
            L("Kassiererin", "f", "Ja, natürlich. Gar nicht wäre falsch, und ab zehn Euro müssen Sie nicht warten."),
            L("Kunde", "m", "Auch einen kleinen Betrag? Ab einem Euro, oder wirklich ab zehn?"),
            L("Kassiererin", "f", "Ja, ab einem Euro geht das. Nicht erst ab zehn Euro und nicht gar nicht."),
            L("Kunde", "m", "Perfekt, dann zahle ich mit Karte. Danke."),
        ],
        [
            L("Frau", "f", "Haben Sie auch Kaffee zum Mitnehmen? Oder nur Getränke, oder nur Süßigkeiten?"),
            L("Verkäufer", "m", "Ja, an der Maschine dort. Nicht nur Getränke und nicht nur Süßigkeiten."),
            L("Frau", "f", "Und etwas zu essen? Also Kaffee und belegte Brötchen?"),
            L("Verkäufer", "m", "Belegte Brötchen liegen in der Vitrine. Kaffee und Brötchen, nicht nur Getränke, nicht nur Süßigkeiten."),
            L("Frau", "f", "Dann einen Kaffee und ein Brötchen, bitte. Danke."),
        ],
    ],
    t4=None,
)

print("89-94 applied")

