"""Batch H rewrite: tests 89-100 — natural direct speech, full lines."""
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
("Lukas","m","Also, unser Umzug! Ich packe Kartons, im Wohnzimmer, mit Zeitung, vorsichtig, viele."),
("Lisa","f","Stark! Ich trage Möbel, mit Handschuhen, stark und mutig, die Couch, zuerst."),
("Tom","m","Und ich fahre den Lkw, groß und laut, durch die Stadt, mit Plan, sicher."),
("Sara","f","Ich baue Möbel auf, mit Schrauben, in der neuen Wohnung, nach Plan, gern."),
("Tim","m","Und ich sorge fürs Essen, mit Pizza, für alle, abends, nach der Arbeit, lecker."),
("Lukas","m","Perfekt! Lisa, ist Couch schwer, zu tragen, wirklich?"),
("Lisa","f","Sehr schwer, zu viert, mit Gurten, dann geht es, gut."),
("Tom","m","Und Pizza, Tim, reicht sie für alle, nach der Arbeit?"),
("Sara","f","Bestimmt! Und Aufbau, Sara, also meiner, dauert er lange, Stunden?"),
("Tim","m","Sara, du fragst dich selbst! Also, dein Aufbau, wie lange dauert er?"),
("Sara","f","Drei Stunden! Also, ich baue Möbel auf, nach Plan!"),
("Lukas","m","Ich packe Kartons, vorsichtig!"),
("Lisa","f","Ich trage Möbel, zuerst die Couch!"),
("Tom","m","Ich fahre den Lkw, sicher!"),
("Tim","m","Und ich sorge fürs Essen, lecker!"),
("Lukas","m","Viel Erfolg allen, beim Umzug!"),
]
# fix self-address 9/10
D[89][8] = ("Sara","f","Bestimmt, Pizza reicht! Und mein Aufbau, dauert er lange, Stunden?")
D[89][9] = ("Tim","m","Drei Stunden, etwa! Und wer putzt noch, am Ende, alles?")

D[90] = [
("Lukas","m","Also, unser Sport! Ich kaufe ein Fahrrad, schnell und leicht, für Touren, am Wochenende."),
("Lisa","f","Toll! Ich kaufe eine Schwimmbrille, dicht und klar, fürs Training, morgens, im Bad."),
("Tom","m","Und ich kaufe Skier, lang und scharf, für den Winter, in den Alpen, super."),
("Sara","f","Ich kaufe Wanderschuhe, fest und hoch, für die Berge, mit Profil, robust."),
("Tim","m","Und ich kaufe einen Fußball, rund und neu, für den Park, mit Freunden, abends."),
("Lukas","m","Schön! Lisa, schwimmst du oft, morgens, im Bad, wirklich?"),
("Lisa","f","Dreimal pro Woche, vor der Arbeit, fit und wach, super."),
("Tom","m","Und Berge, Sara, wie hoch geht ihr, im Sommer, tausend Meter?"),
("Sara","f","Tausend Meter! Und Fußball, Tim, wie viele seid ihr, abends?"),
("Tim","m","Zehn Leute! Also, ich kaufe einen Fußball, für den Park!"),
("Lukas","m","Ich kaufe ein Fahrrad, für Touren!"),
("Lisa","f","Ich kaufe eine Schwimmbrille, fürs Training!"),
("Tom","m","Ich kaufe Skier, für die Alpen!"),
("Sara","f","Ich kaufe Wanderschuhe, robust!"),
("Tim","m","Und ich kaufe einen Fußball, mit Freunden!"),
("Lukas","m","Viel Spaß allen, beim Sport!"),
]

D[91] = [
("Lukas","m","Also, unsere Erkältung! Ich brauche Hustensaft, süß und dick, für nachts, gegen Husten."),
("Lisa","f","Gute Besserung! Ich brauche Schmerztabletten, gegen Kopf, stark und schnell, seit gestern."),
("Tom","m","Und ich brauche Salbe, für den Rücken, warm und gut, abends, mit Massage."),
("Sara","f","Ich brauche Pflaster und Verband, für den Finger, nach dem Kochen, klein, aber tief."),
("Tim","m","Und ich brauche Vitamine, für den Winter, täglich, mit Saft, gesund."),
("Lukas","m","Arme alle! Lisa, hilft die Tablette, gegen Kopf, schnell?"),
("Lisa","f","In einer Stunde, dann geht es, zum Glück, wirklich."),
("Tom","m","Und Finger, Sara, blutet er noch, nach dem Kochen?"),
("Sara","f","Nein, nur ein Schnitt! Und Vitamine, Tim, nimmst du sie täglich?"),
("Tim","m","Jeden Morgen! Also, ich brauche Vitamine, gesund!"),
("Lukas","m","Ich brauche Hustensaft, für nachts!"),
("Lisa","f","Ich brauche Schmerztabletten, seit gestern!"),
("Tom","m","Ich brauche Salbe, mit Massage!"),
("Sara","f","Ich brauche Pflaster und Verband, klein!"),
("Tim","m","Und ich brauche Vitamine, täglich!"),
("Lukas","m","Gute Besserung allen, schnell gesund!"),
]

D[92] = [
("Lukas","m","Also, unser Eis! Ich nehme Schokolade, dunkel und süß, in der Waffel, doppelt, lecker."),
("Lisa","f","Lecker! Ich nehme Erdbeere, frisch und rot, im Becher, mit Sahne, herrlich."),
("Tom","m","Und ich nehme Vanille, klassisch und gut, in der Waffel, mit Streuseln, einfach."),
("Sara","f","Ich nehme Zitrone, sauer und frisch, im Becher, bei Hitze, perfekt."),
("Tim","m","Und ich nehme Pistazie, grün und fein, in der Waffel, aus Italien, edel."),
("Lukas","m","Lecker! Lisa, ist Erdbeere frisch, wirklich, aus Früchten?"),
("Lisa","f","Sehr frisch, vom Markt, morgens, man schmeckt es, sofort."),
("Tom","m","Und Zitrone, Sara, nicht zu sauer, bei Hitze, ehrlich?"),
("Sara","f","Genau richtig! Und Pistazie, Tim, echt aus Italien, wirklich?"),
("Tim","m","Echt! Also, ich nehme Pistazie, edel!"),
("Lukas","m","Ich nehme Schokolade, doppelt!"),
("Lisa","f","Ich nehme Erdbeere, herrlich!"),
("Tom","m","Ich nehme Vanille, einfach!"),
("Sara","f","Ich nehme Zitrone, perfekt!"),
("Tim","m","Und ich nehme Pistazie, aus Italien!"),
("Lukas","m","Guten Appetit allen, beim Eis!"),
]

D[93] = [
("Lukas","m","Also, unsere Kinder! Ich brauche eine Impfung, für den Kleinen, am Montag, gegen Masern."),
("Lisa","f","Gut! Ich brauche Hilfe bei Fieber, hoch und heiß, seit gestern, der Arme, klein."),
("Tom","m","Und ich brauche eine Vorsorgeuntersuchung, jährlich, für die Große, mit Wiegen, normal."),
("Sara","f","Ich brauche Hilfe bei Hautausschlag, rot und wild, am Bauch, seit Tagen, schlimm."),
("Tim","m","Und ich brauche Hilfe bei Ohrenschmerzen, nachts, mit Weinen, seit Freitag, schlimm."),
("Lukas","m","Arme Kinder! Lisa, wie hoch ist Fieber, über vierzig, wirklich?"),
("Lisa","f","Neununddreißig, mit Saft, seit gestern, wir warten, noch."),
("Tom","m","Und Ausschlag, Sara, juckt er sehr, am Bauch, nachts?"),
("Sara","f","Sehr! Und Ohren, Tim, warst du schon da, beim Arzt, heute?"),
("Tim","m","Heute Morgen! Also, ich brauche Hilfe bei Ohrenschmerzen, seit Freitag!"),
("Lukas","m","Ich brauche eine Impfung, am Montag!"),
("Lisa","f","Ich brauche Hilfe bei Fieber, seit gestern!"),
("Tom","m","Ich brauche eine Vorsorgeuntersuchung, normal!"),
("Sara","f","Ich brauche Hilfe bei Hautausschlag, schlimm!"),
("Tim","m","Und ich brauche Hilfe bei Ohrenschmerzen, nachts!"),
("Lukas","m","Gute Besserung allen Kindern!"),
]

D[94] = [
("Lukas","m","Also, unsere Tankstelle! Ich tanke nur, voll, super, weiter geht es, schnell."),
("Lisa","f","Gut! Ich wasche das Auto, mit Schaum, blitzblank, für den Urlaub, glänzend."),
("Tom","m","Und ich prüfe den Reifendruck, an allen vier, mit Gerät, wichtig, vor der Reise."),
("Sara","f","Ich kaufe im Shop ein, Kaffee und Snack, für unterwegs, schnell, lecker."),
("Tim","m","Und ich fülle Luft und Wasser nach, für die Reise, sicher, mit Ruhe, gratis."),
("Lukas","m","Praktisch! Lisa, glänzt es sehr, nach der Wäsche, wirklich?"),
("Lisa","f","Wie neu, mit Wachs, für den Urlaub, perfekt, strahlend."),
("Tom","m","Und Kaffee, Sara, schmeckt er gut, an der Tanke, ehrlich?"),
("Sara","f","Ganz gut! Und Luft, Tim, stimmt der Druck, an allen vier?"),
("Tim","m","Stimmt! Also, ich fülle Luft und Wasser nach, gratis!"),
("Lukas","m","Ich tanke nur, schnell!"),
("Lisa","f","Ich wasche das Auto, glänzend!"),
("Tom","m","Ich prüfe den Reifendruck, wichtig!"),
("Sara","f","Ich kaufe im Shop ein, lecker!"),
("Tim","m","Und ich fülle Luft und Wasser nach, sicher!"),
("Lukas","m","Gute Fahrt allen, vollgetankt!"),
]

D[95] = [
("Lukas","m","Also, unsere Hunde! Ich lasse ihn waschen, mit Shampoo, groß und schmutzig, nach dem Wald."),
("Lisa","f","Süß! Ich lasse ihr die Haare schneiden, kurz und hübsch, für den Sommer, mit Schleife."),
("Tom","m","Und ich lasse ihm die Krallen schneiden, vorsichtig, mit Zange, er hat Angst, der Arme."),
("Sara","f","Ich lasse sie bürsten, lang und weich, das Fell, jeden Monat, gründlich."),
("Tim","m","Und ich lasse ihm die Ohren reinigen, sanft, mit Öl, nach dem Baden, wichtig."),
("Lukas","m","Feine Hunde! Lisa, steht die Schleife, wirklich, zum Fell?"),
("Lisa","f","Sehr süß, rot und klein, alle lachen, freundlich."),
("Tom","m","Und Bürsten, Sara, dauert es lange, jeden Monat, eine Stunde?"),
("Sara","f","Eine Stunde! Und Ohren, Tim, tut es weh, mit Öl, ehrlich?"),
("Tim","m","Gar nicht! Also, ich lasse ihm die Ohren reinigen, wichtig!"),
("Lukas","m","Ich lasse ihn waschen, nach dem Wald!"),
("Lisa","f","Ich lasse ihr die Haare schneiden, mit Schleife!"),
("Tom","m","Ich lasse ihm die Krallen schneiden, vorsichtig!"),
("Sara","f","Ich lasse sie bürsten, gründlich!"),
("Tim","m","Und ich lasse ihm die Ohren reinigen, sanft!"),
("Lukas","m","Viel Spaß allen, mit Hunden!"),
]

D[96] = [
("Lukas","m","Also, unsere Blumen! Ich kaufe für eine Hochzeit, weiß und edel, Rosen, hundert Stück."),
("Lisa","f","Schön! Ich kaufe für einen Geburtstag, bunt und lustig, mit Karte, für Mama."),
("Tom","m","Und ich kaufe Topfpflanzen für den Balkon, grün und stark, drei Stück, für den Sommer."),
("Sara","f","Ich kaufe, um mich zu bedanken, mit Herzen, für die Nachbarin, lieb."),
("Tim","m","Und ich kaufe für ein Grab, still und weiß, am Sonntag, zum Gedenken, leise."),
("Lukas","m","Schöne Anlässe! Lisa, freut sich Mama, über die Blumen, sehr?"),
("Lisa","f","Sehr, sie liebt bunte, mit Karte, jedes Jahr, zum Geburtstag."),
("Tom","m","Und Danke, Sara, wofür dankst du, der Nachbarin, genau?"),
("Sara","f","Für Hilfe! Und Grab, Tim, gehst du oft, sonntags, zum Gedenken?"),
("Tim","m","Jeden Sonntag! Also, ich kaufe für ein Grab, leise!"),
("Lukas","m","Ich kaufe für eine Hochzeit, Rosen!"),
("Lisa","f","Ich kaufe für einen Geburtstag, für Mama!"),
("Tom","m","Ich kaufe Topfpflanzen für den Balkon, drei Stück!"),
("Sara","f","Ich kaufe, um mich zu bedanken, lieb!"),
("Tim","m","Und ich kaufe für ein Grab, zum Gedenken!"),
("Lukas","m","Viel Freude allen, mit Blumen!"),
]

D[97] = [
("Lukas","m","Also, unsere Hosen! Ich lasse die Hose kürzen, zu lang, um fünf Zentimeter, schnell."),
("Lisa","f","Gut! Ich lasse das Kleid enger machen, für die Party, in der Taille, perfekt."),
("Tom","m","Und ich lasse den Reißverschluss wechseln, kaputt, an der Jacke, seit Wochen, nervig."),
("Sara","f","Ich lasse ein Loch stopfen, am Ärmel, klein und rund, nach dem Fest, ärgerlich."),
("Tim","m","Und ich lasse Knöpfe annähen, zwei Stück, am Mantel, lose, vor dem Winter."),
("Lukas","m","Viel Stoff! Lisa, wann ist die Party, am Samstag, schon?"),
("Lisa","f","Am Samstag, mit Tanz, ich freue mich, sehr, aufs Kleid."),
("Tom","m","Und Loch, Sara, sieht man es sehr, am Ärmel?"),
("Sara","f","Kaum! Und Knöpfe, Tim, nähst du selbst, oder die Schneiderin?"),
("Tim","m","Die Schneiderin! Also, ich lasse Knöpfe annähen, vor dem Winter!"),
("Lukas","m","Ich lasse die Hose kürzen, schnell!"),
("Lisa","f","Ich lasse das Kleid enger machen, perfekt!"),
("Tom","m","Ich lasse den Reißverschluss wechseln, nervig!"),
("Sara","f","Ich lasse ein Loch stopfen, ärgerlich!"),
("Tim","m","Und ich lasse Knöpfe annähen, zwei Stück!"),
("Lukas","m","Viel Erfolg allen, beim Schneider!"),
]

D[98] = [
("Lukas","m","Also, unser Wellness! Ich gehe in die Sauna, heiß und lang, mit Aufguss, abends, herrlich."),
("Lisa","f","Toll! Ich bekomme eine Massage, für den Rücken, eine Stunde, dringend, wohltuend."),
("Tom","m","Und ich schwimme im Pool, morgens, zwanzig Bahnen, vor dem Frühstück, fit."),
("Sara","f","Ich bekomme eine Gesichtsbehandlung, mit Maske, entspannt, am Nachmittag, sanft."),
("Tim","m","Und ich mache Yoga, draußen, bei Sonne, mit Blick, morgens, ruhig."),
("Lukas","m","Herrlich! Lisa, hilft Massage gut, beim Rücken, wirklich?"),
("Lisa","f","Sehr gut, wie neu, nach einer Stunde, entspannt, locker."),
("Tom","m","Und Gesicht, Sara, strahlt die Haut, nach der Maske?"),
("Sara","f","Total! Und Yoga, Tim, draußen, ist es nicht kalt, morgens?"),
("Tim","m","Angenehm! Also, ich mache Yoga, morgens, ruhig!"),
("Lukas","m","Ich gehe in die Sauna, herrlich!"),
("Lisa","f","Ich bekomme eine Massage, wohltuend!"),
("Tom","m","Ich schwimme im Pool, fit!"),
("Sara","f","Ich bekomme eine Gesichtsbehandlung, sanft!"),
("Tim","m","Und ich mache Yoga, bei Sonne!"),
("Lukas","m","Viel Erholung allen, im Hotel!"),
]

D[99] = [
("Lukas","m","Also, unser Sprachcafé! Ich spreche Englisch, fließend, mit Gästen, jeden Dienstag, gern."),
("Lisa","f","Toll! Ich spreche Spanisch, mit Freunden, im Urlaub, am Strand, bald, im Sommer."),
("Tom","m","Und ich spreche Französisch, für die Arbeit, mit Kunden, am Telefon, täglich."),
("Sara","f","Ich spreche Italienisch, mit Oma, am Sonntag, beim Essen, mit Liebe."),
("Tim","m","Und ich spreche Deutsch, als Muttersprache, klar, mit allen, immer, gern."),
("Lukas","m","Viele Sprachen! Lisa, sprichst du fließend, Spanisch, wirklich?"),
("Lisa","f","Fast, nach dem Kurs, im Sommer, am Strand, dann ja."),
("Tom","m","Und Oma, Sara, spricht sie gut, Italienisch, nur Dialekt?"),
("Sara","f","Nur Dialekt! Und Deutsch, Tim, als Muttersprache, einfach?"),
("Tim","m","Einfach! Also, ich spreche Deutsch, immer, gern!"),
("Lukas","m","Ich spreche Englisch, gern!"),
("Lisa","f","Ich spreche Spanisch, bald!"),
("Tom","m","Ich spreche Französisch, täglich!"),
("Sara","f","Ich spreche Italienisch, mit Liebe!"),
("Tim","m","Und ich spreche Deutsch, klar!"),
("Lukas","m","Viel Spaß allen, im Café!"),
]
# fix: Tim's question to self — rewrite turn 9
D[99][9] = ("Tim","m","Klar, einfach! Also, ich spreche Deutsch, immer, gern!")

D[100] = [
("Lukas","m","Also, unsere Zukunft! Ich wähle ein Studium, Medizin, ab Herbst, in Berlin, spannend."),
("Lisa","f","Toll! Ich wähle eine Ausbildung, als Köchin, mit Praxis, ab August, lecker."),
("Tom","m","Und ich gehe ins Ausland, für ein Jahr, nach Kanada, mit Arbeit, Abenteuer."),
("Sara","f","Ich arbeite sofort, im Büro, mit Gehalt, ab Juli, erwachsen, cool."),
("Tim","m","Und ich mache ein Soziales Jahr, im Krankenhaus, mit Menschen, sinnvoll, gut."),
("Lukas","m","Spannend! Lisa, kochst du gern, wirklich, jeden Tag?"),
("Lisa","f","Sehr gern, seit der Kindheit, mit Oma, in der Küche, immer."),
("Tom","m","Und Kanada, wie kalt wird es, im Winter, minus dreißig?"),
("Sara","f","Kalt! Und Büro, Sara, also meines, ist es langweilig, manchmal?"),
("Tim","m","Sara, du fragst dich selbst! Also, dein Büro, langweilig manchmal?"),
("Sara","f","Manchmal! Also, ich arbeite sofort, ab Juli!"),
("Lukas","m","Ich wähle ein Studium, spannend!"),
("Lisa","f","Ich wähle eine Ausbildung, lecker!"),
("Tom","m","Ich gehe ins Ausland, Abenteuer!"),
("Tim","m","Und ich mache ein Soziales Jahr, gut!"),
("Lukas","m","Viel Glück allen, für die Zukunft!"),
]
# fix self-address 9/10
D[100][8] = ("Sara","f","Kalt, sehr kalt! Und mein Büro, ist es langweilig, manchmal?")
D[100][9] = ("Tim","m","Bestimmt nicht! Mein Krankenhaus ist spannend, mit Menschen, sinnvoll.")

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
