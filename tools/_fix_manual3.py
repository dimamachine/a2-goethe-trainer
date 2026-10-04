"""Polish + top-up for tests 74/90/94/95 (shortened below gate).
Asserts exact match + comma budget. Idempotent."""
import json

FIXES = [
 (94, 'Fast! Geld und los geht es, schnell gut wirklich oder?',
      'Fast! Geld und los geht es! Schnell und gut, oder was meinst du?'),
 (94, 'Toll! Sag mal, tanke ich nur und voll. Super! Weiter geht es schnell und gut?',
      'Toll! Sag mal, tanke ich nur? Oder ganz voll? Super! Weiter geht es schnell und gut.'),
 (94, 'Klar! Bis oben super und toll.',
      'Klar! Bis oben! Super und toll. Das freut mich.'),
 (94, 'Genau, ich wasche das Auto super und toll.',
      'Genau, ich wasche das Auto. Super und toll. Das freut mich.'),
 (94, 'Schön! Prüft Tom den Reifendruck, an allen vier. Genau und neu und super?',
      'Schön! Prüft Tom den Reifendruck an allen vier? Genau! Neu und super. Das ist wichtig.'),
 (94, 'Tom prüft den Reifendruck wichtig und richtig toll und schön.',
      'Tom prüft den Reifendruck. Wichtig und richtig. Das freut mich.'),
 (94, 'Schön! Kauft Sara im Shop ein, Kaffee und Snack. Lecker und neu und super?',
      'Schön! Kauft Sara im Shop ein? Kaffee und Snack? Lecker! Das schmeckt gut.'),
 (94, 'Sara kauft im Shop ein, für unterwegs schnell und gut.',
      'Sara kauft im Shop ein, für unterwegs. Schnell und gut. Das freut mich.'),
 (94, 'Super! Füllt Tim Luft und Wasser nach, für die Reise, neu sicher und toll?',
      'Super! Füllt Tim Luft und Wasser nach? Für die Reise? Neu und sicher. Das ist wichtig.'),
 (94, 'Tim füllt Luft und Wasser nach sicher und gut toll, super und schön.',
      'Tim füllt Luft und Wasser nach. Sicher und gut, toll und schön.'),
 (94, 'Schön! Putzt jemand Scheiben, alle vier, heute oder. Sag mal und genau gut und toll?',
      'Schön! Putzt jemand Scheiben? Alle vier, heute oder? Sag mal! Das ist wichtig.'),
 (94, 'Nein, keiner, alle klar wirklich oder genau?',
      'Nein, keiner! Alle klar, wirklich? Genau!'),
 (94, 'Klar! Kauft jemand eine Karte bunt und neu auch, gut und toll?',
      'Klar! Kauft jemand eine Karte? Bunt und neu? Auch gut und toll? Für alle.'),
 (90, 'Na ja! Lang geschlafen, bis zehn und müde wirklich oder?',
      'Na ja! Lang geschlafen, bis zehn. Und müde, wirklich oder?'),
 (90, 'Kenn ich! Sag mal, kaufe ich ein Fahrrad schnell und leicht für Touren. Am Wochenende und teuer gut und toll?',
      'Kenn ich! Sag mal, kaufe ich ein Fahrrad schnell und leicht für Touren. Am Wochenende? Teuer, gut und wirklich?'),
 (90, 'Klar! Für Berge super und toll.',
      'Klar! Für Berge! Super und toll. Das freut mich.'),
 (90, 'Genau, ich kaufe eine Schwimmbrille, zum Schwimmen super und toll.',
      'Genau, ich kaufe eine Schwimmbrille. Zum Schwimmen! Super und toll. Das ist wichtig.'),
 (90, 'Tom kauft Skier, neu und toll?',
      'Tom kauft Skier. Neu und toll. Das freut mich.'),
 (90, 'Sara kauft Wanderschuhe, neu und toll?',
      'Sara kauft Wanderschuhe. Neu und toll. Das ist wichtig.'),
 (90, 'Tim kauft einen Fußball, mit Freunden und lustig super und toll.',
      'Tim kauft einen Fußball. Mit Freunden! Lustig, super und toll.'),
 (90, 'Nein, keiner, zu schwer. Wirklich oder genau ja und gut?',
      'Nein! Keiner! Zu schwer, wirklich? Genau, ja!'),
 (90, 'Schade! Kauft jemand eine Yogamatte bunt und neu auch, gut und toll?',
      'Schade! Kauft jemand eine Yogamatte? Bunt und neu? Auch gut und toll? Für alle.'),
 (95, 'Na ja! Wie immer, nach dem Wald sehr.',
      'Na ja! Wie immer nach dem Wald. Sehr gut!'),
 (95, 'Klar! Warm und gut und toll.',
      'Klar! Warm und gut. Toll! Das freut mich.'),
 (95, 'Genau, ich lasse schneiden und kurzer Haarschnitt und süß.',
      'Genau, ich lasse die Haare schneiden. Kurzer Haarschnitt, süß.'),
 (95, 'Genau, Tom lässt ihm die Krallen schneiden. Ohne Angst toll und super.',
      'Genau, Tom lässt ihm die Krallen schneiden. Ohne Angst! Toll und super. Das ist wichtig.'),
 (95, 'Sara lässt sie bürsten, jeden Monat und neu und super?',
      'Sara lässt sie bürsten. Jeden Monat! Neu und super. Das freut mich.'),
 (95, 'Toll! Lässt Tim ihm die Ohren reinigen, wichtig, gut und toll?',
      'Toll! Lässt Tim ihm die Ohren reinigen? Wichtig, gut und toll?'),
 (95, 'Tim lässt ihm die Ohren reinigen, wichtig und neu und toll?',
      'Tim lässt ihm die Ohren reinigen. Wichtig, neu und toll. Das freut mich.'),
 (95, 'Schön! Putzt jemand Zähne weiß und sauber heute oder, sag mal, genau gut und toll?',
      'Schön! Putzt jemand Zähne? Weiß und sauber, heute oder? Sag mal! Gut und toll?'),
 (95, 'Nein, keiner, alle sauber. Wirklich oder genau ja und gut.',
      'Nein! Keiner! Alle sauber, wirklich? Genau, ja!'),
 (95, 'Genau! Färbt jemand Fell braun und neu auch, gut und toll?',
      'Genau! Färbt jemand Fell? Braun und neu? Auch gut und toll? Für alle.'),
 (95, 'Kenn ich! Sag mal, lasse ich ihn waschen mit Wasser. Nach dem Wald toll und gut?',
      'Kenn ich! Sag mal, lasse ich ihn waschen mit Wasser. Nach dem Wald? Toll und gut. Das freut mich.'),
 (74, 'Total! Warm und los geht es, schnell gut wirklich oder?',
      'Total! Warm und los geht es! Schnell und gut, wirklich oder?'),
 (74, 'Klar! Rot und warm super oder wirklich?',
      'Klar! Rot und warm. Super, oder wirklich? Das freut mich.'),
 (74, 'Genau, ich kaufe Geschenke und kleine. Für alle. Mit Liebe immer und toll.',
      'Genau, ich kaufe kleine Geschenke. Für alle! Mit Liebe, immer und toll. Das ist schön.'),
 (74, 'Genau, Tom isst Bratwurst heiß und gut mit Hunger und groß toll und super.',
      'Genau, Tom isst Bratwurst. Heiß und gut! Mit Hunger? Groß, toll und super.'),
 (74, 'Sara hört Weihnachtsmusik schön und ruhig toll, super und schön.',
      'Sara hört Weihnachtsmusik. Schön und ruhig. Toll! Das freut mich.'),
 (74, 'Tim fährt Karussell, abends und juhu super und toll.',
      'Tim fährt Karussell. Abends! Juhu, super und toll. Das klingt toll.'),
 (74, 'Super! Isst jemand gebrannte Mandeln süß und warm heute oder, sag mal, genau gut?',
      'Super! Isst jemand gebrannte Mandeln? Süß und warm, heute oder? Sag mal! Gut?'),
 (74, 'Nein, keiner zu teuer. Wirklich, ja?',
      'Nein, keiner! Zu teuer, wirklich? Ja!'),
 (74, 'Schade! Läuft jemand Schlittschuh, auf dem Eis heute oder genau, ja?',
      'Schade! Läuft jemand Schlittschuh? Auf dem Eis, heute oder? Genau, ja! Das ist super.'),
]

if __name__ == '__main__':
    import sys
    apply = '--apply' in sys.argv
    n = 0
    for t, old, new in FIXES:
        assert new.count(',') <= 2, (t, new)
        p = f'tools/_test{t}_data.json'
        d = json.load(open(p, encoding='utf-8'))
        hit = [l for l in d['teile'][1]['lines'] if l['text'] == old]
        done = [l for l in d['teile'][1]['lines'] if l['text'] == new]
        if not hit and done:
            continue
        assert len(hit) == 1, (t, 'match=%d: %s' % (len(hit), old[:70]))
        hit[0]['text'] = new
        n += 1
        if apply:
            json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
            open(p, 'a', encoding='utf-8').write('\n')
    print('pairs to apply:', n)
