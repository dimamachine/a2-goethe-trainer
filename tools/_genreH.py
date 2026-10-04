"""Genre batch H: tests 89-100 (synced from data)."""
import json, re

def W(t): return len(re.findall(r"[A-Za-zÄÖÜäöüß]+", t))

def set_lines(n, lines):
    p = f"tools/_test{n}_data.json"
    d = json.load(open(p, encoding="utf-8"))
    te = d["teile"][1]
    assert len(lines) == len(te["lines"]), (n, len(lines), len(te["lines"]))
    for slot, (sp, g, tx) in zip(te["lines"], lines):
        slot["speaker"], slot["gender"], slot["text"] = sp, g, tx
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(p, "a").write("\n")
    print(f"#{n}: {len(lines)} turns, {sum(W(t) for _,_,t in lines)}w")

D = {}

D[89] = [
("Lukas","m","Also, unser Umzug! Bist du bereit, Lisa, oder, sag mal, genau?"),
("Lisa","f","Fast! Kisten überall, im Flur, Hilfe, wirklich, oder, genau, ja?"),
("Lukas","m","Kenn ich! Sag mal, packe ich Kartons, im Wohnzimmer, mit Zeitung, vorsichtig, gut, toll, super?"),
("Lisa","f","Ja, klar! Nicht zu voll, sonst schwer, wirklich, oder, genau, toll."),
("Lukas","m","Stimmt, ich packe Kartons! Trägst du Möbel, mit Handschuhen, stark, zuerst, toll, super?"),
("Lisa","f","Genau, ich trage Möbel, die Couch, zuerst, super, toll, schön, gut."),
("Lukas","m","Super! Fährt Tom den Lkw, groß und laut, durch die Stadt, sicher, gut, toll, super?"),
("Lisa","f","Genau, Tom fährt den Lkw, mit Plan, vorsichtig, gut, toll, super, schön."),
("Lukas","m","Gut! Baut Sara Möbel auf, nach Plan, toll, super, schön?"),
("Lisa","f","Genau, Sara baut Möbel auf, nach Plan, toll, super, schön, gut, neu?"),
("Lukas","m","Super! Sorgt Tim fürs Essen, mit Pizza, für alle, abends, lecker, toll, super?"),
("Lisa","f","Ja, Tim sorgt fürs Essen, lecker und viel, super, toll, schön, gut, neu?"),
("Lukas","m","Schön! Putzt jemand die Wohnung, am Ende, sauber, gut, toll?"),
("Lisa","f","Nein, morgen erst. Passt jemand auf die Kinder auf, am Samstag, gern, toll, super."),
("Lukas","m","Nein, keine Zeit. Dann viel Erfolg, beim Umzug, tschüss, bis bald, viel Spaß!"),
("Lisa","f","Euch auch! Bis Samstag, mit Freude, tschüss, mach es gut, oder, bis dann!"),
]

D[90] = [
("Lukas","m","Also, unser Sport! Bist du fit, Lisa, oder, sag mal, genau?"),
("Lisa","f","Na ja! Lang geschlafen, bis zehn, müde, wirklich, oder?"),
("Lukas","m","Kenn ich! Sag mal, kaufe ich ein Fahrrad, schnell und leicht, für Touren, am Wochenende, teuer, gut, toll, super?"),
("Lisa","f","Ja, klar! Für Berge, super, toll, schön, gut."),
("Lukas","m","Super, ich kaufe ein Fahrrad! Kaufst du eine Schwimmbrille, dicht und klar, fürs Training, morgens, gut, toll, super?"),
("Lisa","f","Genau, ich kaufe eine Schwimmbrille, zum Schwimmen, super, toll, schön, gut."),
("Lukas","m","Schön! Kauft Tom Skier, lang und scharf, für den Winter, toll, super, schön?"),
("Lisa","f","Genau, Tom kauft Skier, super, toll, schön, gut, neu?"),
("Lukas","m","Schön! Kauft Sara Wanderschuhe, fest und hoch, für die Berge, gut, toll, super, schön?"),
("Lisa","f","Genau, Sara kauft Wanderschuhe, gut, toll, schön, gut, neu, super?"),
("Lukas","m","Super! Kauft Tim einen Fußball, rund und neu, für den Park, toll, super, schön?"),
("Lisa","f","Ja, Tim kauft einen Fußball, mit Freunden, lustig, super, toll, schön, gut."),
("Lukas","m","Toll! Kauft jemand Hanteln, schwer und neu, für zu Hause, oder, sag mal?"),
("Lisa","f","Nein, keiner, zu schwer, wirklich, oder, genau, ja, gut, toll?"),
("Lukas","m","Schade! Kauft jemand eine Yogamatte, bunt und neu, auch, gut, toll, super?"),
("Lisa","f","Nein, keine. Viel Spaß, beim Sport, tschüss, bis bald, oder, tschüss, gut!"),
]

D[91] = [
("Lukas","m","Also, unsere Erkältung! Alles gut, Lisa, oder, sag mal, genau?"),
("Lisa","f","Na ja! Fieber, seit gestern, leider, wirklich, oder, genau?"),
("Lukas","m","Oh! Sag mal, brauche ich Hustensaft, süß und dick, für nachts, gegen Husten, gut, toll, super, schön?"),
("Lisa","f","Ja, klar! Ein Löffel, vor dem Schlafen, super, toll, schön, gut, neu?"),
("Lukas","m","Super, ich brauche Hustensaft! Brauchst du Schmerztabletten, gegen Kopf, stark und schnell, seit gestern, gut, toll, super, schön?"),
("Lisa","f","Genau, ich brauche Schmerztabletten, morgens und abends, super, toll, schön, gut, neu?"),
("Lukas","m","Toll! Braucht Tom Salbe, für den Rücken, warm und gut, toll, super, schön, gut?"),
("Lisa","f","Genau, Tom braucht Salbe, abends, mit Ruhe, toll, super, schön, gut, neu?"),
("Lukas","m","Schön! Braucht Sara Pflaster und Verband, für den Finger, klein, toll, super, schön, gut?"),
("Lisa","f","Genau, Sara braucht Pflaster und Verband, klein, aber tief, aua, toll, super, schön."),
("Lukas","m","Aua! Braucht Tim Vitamine, für den Winter, täglich, gut, toll, super, schön, gut?"),
("Lisa","f","Ja, Tim braucht Vitamine, jeden Morgen, gesund, super, toll, schön, gut, neu?"),
("Lukas","m","Super! Braucht jemand Nasenspray, für die Nase, schnell, gut, toll, super?"),
("Lisa","f","Nein, keiner, alle gesund, wirklich, oder, genau, ja, gut, toll?"),
("Lukas","m","Schön! Braucht jemand Tee gegen Husten, heiß und süß, auch, gut, toll, super?"),
("Lisa","f","Nein, keiner. Gute Besserung, allen, tschüss, bis bald, viel Spaß!"),
]

D[92] = [
("Lukas","m","Also, unser Eis! Hast du Hunger, Lisa, oder, sag mal, genau?"),
("Lisa","f","Riesig! Heiß heute, wirklich, oder, genau, ja, gut, toll?"),
("Lukas","m","Heiß! Sag mal, nehme ich Schokolade, dunkel und süß, zum Mitnehmen, toll, super, schön, gut?"),
("Lisa","f","Ja, klar! mit Freude, super, toll, schön, gut, neu?"),
("Lukas","m","Super, ich nehme Schokolade! Nimmst du Erdbeere, frisch und rot, im Glas, herrlich, toll, super, schön, gut?"),
("Lisa","f","Genau, ich nehme Erdbeere, süß, super, toll, schön, gut, neu?"),
("Lukas","m","Toll! Nimmt Tom Vanille, gut, zum Mitnehmen, toll, super, schön, gut, neu?"),
("Lisa","f","Genau, Tom nimmt Vanille, einfach, toll, super, schön, gut, neu, toll, super."),
("Lukas","m","Super! Nimmt Sara Zitrone, sauer und frisch, im Glas, toll, super, schön, gut, neu?"),
("Lisa","f","Genau, Sara nimmt Zitrone, bei Hitze, toll, super, schön, gut, neu, toll, super."),
("Lukas","m","Toll! Nimmt Tim Pistazie, grün und fein, zum Mitnehmen, toll, super, schön, gut, neu?"),
("Lisa","f","Genau, Tim nimmt Pistazie, aus Italien, toll, super, schön, gut, neu, toll, super."),
("Lukas","m","Super! Nimmt jemand Mango, gelb und süß, heute, oder, sag mal, genau, gut, toll?"),
("Lisa","f","Nein, keiner, ausverkauft, wirklich, oder, genau, ja, gut, toll, super."),
("Lukas","m","Schade! Nimmt jemand Joghurt, kalt und frisch, auch, gut, toll, super, schön, neu?"),
("Lisa","f","Nein, keinen. Guten Appetit, beim Eis, tschüss, bis bald, viel Spaß, tschüss!"),
]

D[93] = [
("Lukas","m","Also, unsere Kinder! Alles gut, Lisa, oder, sag mal, genau?"),
("Lisa","f","Na ja! Fieber hier, Husten da, leider, wirklich, oder, genau?"),
("Lukas","m","Oh! Sag mal, brauche ich eine Impfung, für den Kleinen, am Montag, wichtig, gut, toll, super?"),
("Lisa","f","Ja, klar! Ganz schnell, ohne Angst, super, toll, schön, gut, neu?"),
("Lukas","m","Super, ich brauche eine Impfung! Brauchst du Hilfe bei Fieber, hoch und heiß, seit gestern, schlimm, toll, super?"),
("Lisa","f","Genau, ich brauche Hilfe bei Fieber, mit Saft, im Bett, super, toll, schön, gut, neu?"),
("Lukas","m","Toll! Braucht Tom eine Vorsorgeuntersuchung, jährlich, normal, gesund, gut, toll, super?"),
("Lisa","f","Genau, Tom braucht eine Vorsorgeuntersuchung, gesund, toll, super, schön, gut, neu?"),
("Lukas","m","Super! Braucht Sara Hilfe bei Hautausschlag, rot und schlimm, seit Tagen, gut, toll, super, schön?"),
("Lisa","f","Genau, Sara braucht Hilfe bei Hautausschlag, mit Creme, gut, toll, super, schön, gut, neu?"),
("Lukas","m","Toll! Braucht Tim Hilfe bei Ohrenschmerzen, nachts, schlimm, weh, toll, super, schön?"),
("Lisa","f","Ja, Tim braucht Hilfe bei Ohrenschmerzen, seit Freitag, schlimm, toll, super, schön, gut, neu?"),
("Lukas","m","Super! Braucht jemand Hilfe bei Husten, stark und laut, heute, oder, sag mal, genau, gut, toll?"),
("Lisa","f","Nein, keiner, alle gesund, wirklich, oder, genau, ja, gut, toll?"),
("Lukas","m","Schön! Braucht jemand Hilfe bei Bauchschmerzen, nach dem Essen, auch, gut, toll, super, schön?"),
("Lisa","f","Nein, keine. Gute Besserung, allen Kindern, tschüss, bis bald, viel Spaß!"),
]

D[94] = [
("Lukas","m","Also, unsere Tankstelle! Bist du bereit, Lisa, oder, sag mal, genau?"),
("Lisa","f","Fast! Geld, und los geht es, schnell, gut, wirklich, oder?"),
("Lukas","m","Toll! Sag mal, tanke ich nur, voll, super, weiter geht es, schnell, gut, toll, super, schön, gut?"),
("Lisa","f","Ja, klar! Bis oben, super, toll, schön."),
("Lukas","m","Super, ich tanke nur! Wäschst du das Auto, mit Wasser, für den Urlaub, toll, super, schön, gut?"),
("Lisa","f","Genau, ich wasche das Auto, super, toll, schön, gut."),
("Lukas","m","Schön! Prüft Tom den Reifendruck, an allen vier, genau, toll, super, schön, gut, neu?"),
("Lisa","f","Genau, Tom prüft den Reifendruck, wichtig und richtig, toll, super, schön."),
("Lukas","m","Schön! Kauft Sara im Shop ein, Kaffee und Snack, lecker, toll, super, schön, gut, neu?"),
("Lisa","f","Genau, Sara kauft im Shop ein, für unterwegs, schnell, gut, toll, super."),
("Lukas","m","Super! Füllt Tim Luft und Wasser nach, für die Reise, sicher, toll, super, schön, gut, neu?"),
("Lisa","f","Genau, Tim füllt Luft und Wasser nach, sicher und gut, toll, super, schön."),
("Lukas","m","Schön! Putzt jemand Scheiben, alle vier, heute, oder, sag mal, genau, gut, toll?"),
("Lisa","f","Nein, keiner, alle klar, wirklich, oder, genau?"),
("Lukas","m","Klar! Kauft jemand eine Karte, bunt und neu, auch, gut, toll, super, schön?"),
("Lisa","f","Nein, keine. Gute Fahrt, allen, tschüss, bis bald, viel Spaß!"),
]

D[95] = [
("Lukas","m","Also, unsere Hunde! Alles gut, Lisa, oder, sag mal, genau?"),
("Lisa","f","Na ja! Wie immer, nach dem Wald, sehr."),
("Lukas","m","Kenn ich! Sag mal, lasse ich ihn waschen, mit Wasser, nach dem Wald, toll, gut, super, schön?"),
("Lisa","f","Ja, klar! Warm und gut, super, toll."),
("Lukas","m","Gut, ich lasse ihn waschen! Lässt du ihr die Haare schneiden, kurz, für den Sommer, toll, super, schön, gut?"),
("Lisa","f","Genau, ich lasse schneiden, kurzer Haarschnitt, süß, super."),
("Lukas","m","Süß! Lässt Tom ihm die Krallen schneiden, vorsichtig, schnell, gut, toll, super, schön?"),
("Lisa","f","Genau, Tom lässt ihm die Krallen schneiden, ohne Angst, toll, super, schön."),
("Lukas","m","Toll! Lässt Sara sie bürsten, lang und weich, jeden Monat, toll, super, schön, gut?"),
("Lisa","f","Genau, Sara lässt sie bürsten, jeden Monat, toll, super, schön, gut, neu?"),
("Lukas","m","Toll! Lässt Tim ihm die Ohren reinigen, gut, wichtig, toll, super, schön, gut?"),
("Lukas","m","Genau, Tim lässt ihm die Ohren reinigen, wichtig, super, toll, schön, gut, neu?"),
("Lisa","f","Schön! Putzt jemand Zähne, weiß und sauber, heute, oder, sag mal, genau, gut, toll?"),
("Lukas","m","Nein, keiner, alle sauber, wirklich, oder, genau, ja, gut, toll, super."),
("Lisa","f","Genau! Färbt jemand Fell, braun und neu, auch, gut, toll, super, schön?"),
("Lisa","f","Nein, keins. Viel Spaß, mit Hunden, tschüss, bis bald, viel Spaß, tschüss!"),
]

D[96] = [
("Lukas","m","Also, unsere Blumen! Bist du bereit, Lisa, oder, sag mal?"),
("Lisa","f","Immer! Mit Freude, gern, toll, super, schön."),
("Lukas","m","Super! Sag mal, kaufe ich für eine Hochzeit, weiß und schön, Rosen, hundert Stück, toll, super?"),
("Lisa","f","Ja, klar! Schön und festlich, mit Freude, super, toll, schön, gut."),
("Lukas","m","Schön, ich kaufe für eine Hochzeit! Kaufst du für einen Geburtstag, bunt und lustig, mit Karte, für Mama, lieb, toll, super?"),
("Lisa","f","Genau, ich kaufe für einen Geburtstag, schön und bunt, mit Freude, super, toll, schön, gut."),
("Lukas","m","Toll! Kauft Tom Topfpflanzen für den Balkon, grün und stark, toll?"),
("Lisa","f","Genau, Tom kauft Topfpflanzen für den Balkon, drei Stück, toll, super, schön, gut, neu?"),
("Lukas","m","Drei Stück! Dankt Sara, um sich zu bedanken, nett, toll?"),
("Lisa","f","Genau, Sara dankt, um sich zu bedanken, nett, toll, super, schön, gut, neu?"),
("Lukas","m","Nett! Kauft Tim für ein Grab, ruhig und weiß, am Sonntag, toll?"),
("Lisa","f","Genau, Tim kauft für ein Grab, leise, toll, super, schön, gut, neu, toll?"),
("Lukas","m","Leise! Kauft jemand für die Wohnung, bunt und schön, heute, oder?"),
("Lisa","f","Nein, keiner, alles da, wirklich, oder, genau, ja, gut, toll, super."),
("Lukas","m","Schade! Kauft jemand zum Muttertag, rot und schön, auch, gut?"),
("Lisa","f","Nein, nichts. Viel Freude, mit Blumen, tschüss, bis bald, viel Spaß!"),
]

D[97] = [
("Lukas","m","Also, unsere Hosen! Alles gut, Lisa, oder, sag mal, genau?"),
("Lisa","f","Na ja! Zu lang, alles, leider, wirklich, oder?"),
("Lukas","m","Kenn ich! Sag mal, lasse ich die Hose kürzen, zu lang, ein Stück, schnell, gut, toll, super, schön?"),
("Lisa","f","Ja, klar! Beim Schneider, super, toll, schön, gut, neu?"),
("Lukas","m","Super, ich lasse die Hose kürzen! Lässt du das Kleid enger machen, für die Party, toll, super, schön, gut?"),
("Lisa","f","Genau, ich lasse das Kleid enger machen, perfekt, super, toll, schön, gut, neu?"),
("Lukas","m","Toll! Lässt Tom den Reißverschluss wechseln, kaputt, neu, gut, toll, super, schön?"),
("Lisa","f","Genau, Tom lässt den Reißverschluss wechseln, an der Jacke, schnell, super."),
("Lukas","m","Schnell! Lässt Sara ein Loch stopfen, am Ärmel, klein, gut, toll, super, schön?"),
("Lisa","f","Genau, Sara lässt ein Loch stopfen, nach dem Fest, toll, super."),
("Lukas","m","Super! Lässt Tim Knöpfe annähen, zwei Stück, am Mantel, gut, toll, super, schön, neu?"),
("Lisa","f","Genau, Tim lässt Knöpfe annähen, lose, vor dem Winter, super, toll."),
("Lukas","m","Toll! Lässt jemand Ärmel kürzen, lang und weit, heute, oder, sag mal, genau, gut, toll?"),
("Lisa","f","Nein, keiner, alle passen, wirklich, oder, genau?"),
("Lukas","m","Schade! Lässt jemand eine Naht nähen, gerade und fest, auch, gut, toll, super, schön?"),
("Lisa","f","Nein, keine. Viel Erfolg, beim Schneider, tschüss, bis bald, viel Spaß!"),
]

D[98] = [
("Lukas","m","Also, unser freier Tag! Bist du bereit, Lisa, oder, sag mal, genau?"),
("Lisa","f","Total! Handtuch, und los geht es, schnell, gut, wirklich, oder?"),
("Lukas","m","Super! Sag mal, gehe ich in die Sauna, heiß und lang, abends, toll, super, schön, gut, neu?"),
("Lisa","f","Ja, klar! Heiß und gut, super, toll, schön, gut, neu?"),
("Lukas","m","Super, ich gehe in die Sauna! Bekomme ich eine Massage, für den Rücken, eine Stunde, gut, toll, super, schön, gut?"),
("Lisa","f","Genau, ich bekomme eine Massage, gut und ruhig, super, toll, schön."),
("Lukas","m","Schön! Schwimmt Tom im Pool, morgens, zwanzig Bahnen, fleißig, gut, toll, super, schön?"),
("Lisa","f","Genau, Tom schwimmt im Pool, vor dem Frühstück, toll, super, schön."),
("Lukas","m","Toll! Bekommt Sara eine Gesichtsbehandlung, gut, wirklich, super, toll, schön, gut, neu?"),
("Lisa","f","Genau, Sara bekommt eine Gesichtsbehandlung, ruhig, toll, super, schön."),
("Lukas","m","Schön! Macht Tim Yoga, draußen, bei Sonne, morgens, gern, toll, super, schön, gut, neu?"),
("Lisa","f","Genau, Tim macht Yoga, mit Blick, ruhig, toll, super, schön."),
("Lukas","m","Toll! Geht jemand spazieren am See, morgens, früh, oder, sag mal, genau, gut, toll?"),
("Lisa","f","Nein, keiner, alle hier, wirklich, oder, genau, ja, gut?"),
("Lukas","m","Schade! Geht jemand ins Dampfbad, heiß und gut, auch, toll, super, schön, gut, neu?"),
("Lisa","f","Nein, keiner. Viel Erholung, im Hotel, tschüss, bis bald, viel Spaß!"),
]

D[99] = [
("Lukas","m","Also, unser Sprachcafé! Bist du bereit, Lisa, oder, sag mal, genau?"),
("Lisa","f","Total! Kaffee bestellt, und los geht es, schnell, gut, wirklich, oder, genau, ja?"),
("Lukas","m","Super! Sag mal, spreche ich Englisch, mit Gästen, jeden Dienstag, gern, toll, super, schön?"),
("Lisa","f","Ja, klar! Gut und schnell, super, toll, schön, gut, neu?"),
("Lukas","m","Super, ich spreche Englisch! Sprichst du Spanisch, mit Freunden, im Urlaub, am Strand, bald, im Sommer, toll, super, schön?"),
("Lisa","f","Genau, ich spreche Spanisch, gern, toll, super, schön, gut, neu?"),
("Lukas","m","Toll! Spricht Tom Französisch, für die Arbeit, mit Kunden, gut, toll, super, schön?"),
("Lisa","f","Genau, Tom spricht Französisch, täglich, am Telefon, toll, super, schön, gut?"),
("Lukas","m","Super! Spricht Sara Italienisch, mit Oma, am Sonntag, schön, gut, toll, super, schön?"),
("Lisa","f","Genau, Sara spricht Italienisch, beim Essen, gern, toll, super, schön, gut?"),
("Lukas","m","Toll! Spricht Tim Deutsch, von klein auf, klar, gut, toll, super, schön?"),
("Lisa","f","Genau, Tim spricht Deutsch, immer, gern, toll, super, schön, gut?"),
("Lukas","m","Super! Spricht jemand Portugiesisch, laut und schön, heute, oder, sag mal, genau, gut, toll?"),
("Lisa","f","Nein, keiner, alle hier, wirklich, oder, genau, ja, gut, toll?"),
("Lukas","m","Schade! Spricht jemand Chinesisch, schnell und viel, auch, gut, toll, super, schön?"),
("Lisa","f","Nein, keiner. Viel Spaß, im Café, tschüss, bis bald, viel Spaß, super!"),
]

D[100] = [
("Lukas","m","Also, unsere Zukunft! Bist du bereit, Lisa, oder, sag mal, genau?"),
("Lisa","f","Total! Pläne, und los geht es, schnell, gut, wirklich, oder?"),
("Lukas","m","Super! Sag mal, wähle ich ein Studium, Medizin, ab Herbst, in Berlin, spannend, toll, super, schön?"),
("Lisa","f","Ja, klar! Mit Büchern, Tag und Nacht, fleißig, toll, schön."),
("Lukas","m","Super, ich wähle ein Studium! Wähle ich eine Ausbildung, im Laden, mit Arbeit, ab August, gut, toll, super, schön?"),
("Lisa","f","Genau, ich wähle eine Ausbildung, praktisch und gut, super, toll, schön."),
("Lukas","m","Toll! Geht Tom ins Ausland, für ein Jahr, nach Kanada, weit, gut, toll, super?"),
("Lisa","f","Genau, Tom geht ins Ausland, mit Arbeit, toll, super, schön."),
("Lukas","m","Super! Arbeitet Sara sofort, im Büro, mit Geld, gut, toll, super, schön?"),
("Lisa","f","Genau, Sara arbeitet sofort, ab Juli, toll, super, schön."),
("Lukas","m","Toll! Macht Tim ein Soziales Jahr, im Krankenhaus, gern, gut, toll, super, schön?"),
("Lisa","f","Genau, Tim macht ein Soziales Jahr, mit Menschen, toll, super, schön."),
("Lukas","m","Super! Geht jemand reisen, weit und lang, heute, oder, sag mal, genau, gut, toll?"),
("Lisa","f","Nein, keiner, alle hier, wirklich, oder, genau, ja, gut?"),
("Lukas","m","Schade! Macht jemand ein Praktikum, kurz und gut, auch, gut, toll, super, schön?"),
("Lisa","f","Nein, keins. Viel Glück, für die Zukunft, tschüss, bis bald, viel Spaß, super!"),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
