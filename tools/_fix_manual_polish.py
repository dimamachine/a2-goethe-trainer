"""Manual polish of the worst staccato leftovers (word salads, piles).
Every pair asserts exact match; every new text must have <=2 commas."""
import json

FIXES = [
 (12, 'Wunderbar! Kümmert sich Vater um die Fische gut und gern wirklich oder?',
      'Wunderbar! Kümmert sich Vater gern um die Fische? Wirklich?'),
 (24, 'Ja, Marie tanzt Ballett. In der Tanzschule und jeden Tag und abends?',
      'Ja, Marie tanzt Ballett. In der Tanzschule jeden Tag?'),
 (25, 'Cool! Liest Marie Kinderbücher und Märchen, vor dem Schlafen, jeden Tag und abends im Bett?',
      'Cool! Liest Marie Kinderbücher und Märchen? Vor dem Schlafen jeden Tag im Bett?'),
 (25, 'Ja, Marie liest Kinderbücher und Märchen, Rotkäppchen liebt sie. Seit Jahren und jeden Tag und abends?',
      'Ja, Marie liest Kinderbücher und Märchen, Rotkäppchen liebt sie. Seit Jahren jeden Tag?'),
 (32, 'Ja, Lisa rutscht auf der Wasserrutsche schnell und sicher juhu und weiter!',
      'Ja, Lisa rutscht auf der Wasserrutsche schnell und sicher. Juhu, weiter!'),
 (36, 'Ja, Tom studiert Informatik mit Kaffee. Tag und Nacht und fleißig und jeden Tag.',
      'Ja, Tom studiert Informatik mit Kaffee. Tag und Nacht fleißig, jeden Tag.'),
 (42, 'Also die Geschenke! Hast du Ideen für, Lisa Papa schnell?',
      'Also die Geschenke! Hast du Ideen für Papa, Lisa? Schnell?'),
 (42, 'Ein paar! Er wird sechzig, ein Fest. Mit allen zusammen und gern.',
      'Ein paar! Er wird sechzig, ein Fest. Mit allen zusammen, gern.'),
 (42, 'Ja, klar! Papa liebt Uhren. Seit Jahren wirklich und sehr.',
      'Ja, klar! Papa liebt Uhren. Seit Jahren, wirklich sehr.'),
 (44, 'Ja, klar! Du spielst selbst. Seit Jahren. Im Keller laut und sehr.',
      'Ja, klar! Du spielst selbst seit Jahren im Keller. Laut und sehr.'),
 (44, 'Genau, ich mag Rock! Magst du Klassik. Mit Klavier und jeden Tag und abends?',
      'Genau, ich mag Rock! Magst du Klassik? Mit Klavier jeden Tag?'),
 (44, 'Schön! Mag Tom Jazz. Abends. In der Bar? Hört er Klassik, wie du und genau allein und wirklich.',
      'Schön! Mag Tom Jazz? Abends in der Bar? Hört er Klassik wie du? Allein und wirklich?'),
 (45, 'Na, Gold und mehr! Also Sara mag Ägypten, mit Gold sehr und wirklich.',
      'Na, Gold und mehr! Also Sara mag Ägypten mit Gold. Sehr und wirklich!'),
 (45, 'Ach so, mit Gold! Mag Tim Technik, mit Computer immer und gern.',
      'Ach so, mit Gold! Mag Tim Technik? Mit Computer, immer gern.'),
 (45, 'Ja, Tom mag Naturkunde und besonders Tiere. Schon immer gern und sehr.',
      'Ja, Tom mag Naturkunde und besonders Tiere. Schon immer sehr gern!'),
 (47, 'Toll! Designt Sara eine Webseite, für den Verein bunt und klar modern und neu und schick?',
      'Toll! Designt Sara eine Webseite? Für den Verein bunt und modern?'),
 (51, 'Genau, ich brauche Kontaktlinsen und weiche. Jeden Tag und neue super bequem.',
      'Genau, ich brauche weiche Kontaktlinsen für jeden Tag. Super bequem!'),
 (51, 'Dir auch! Und putz sie oft, die Brille, jeden Tag und morgens!',
      'Dir auch! Und putz sie oft, die Brille jeden Tag morgens!'),
 (51, 'Genau, Sara braucht eine Sonnenbrille mit Sehstärke dunkel und cool toll und schick.',
      'Genau, Sara braucht eine Sonnenbrille mit Sehstärke. Dunkel und cool.'),
 (59, 'Also unsere Haare! Alles gut bei, Lars dir und alles klar?',
      'Also unsere Haare! Alles gut bei dir, Lars? Alles klar?'),
 (59, 'Stimmt, ich habe eine Glatze! Hast du einen Iro. Bunt und jeden Tag und bunt?',
      'Stimmt, ich habe eine Glatze! Hast du einen Iro? Bunt, jeden Tag?'),
 (60, 'Genau, Tom liest auf einer Bank und stundenlang. Jeden Tag und fleißig toll und super.',
      'Genau, Tom liest auf einer Bank, stundenlang. Jeden Tag fleißig. Toll und super!'),
 (61, 'Super! Sag mal, mache ich Krafttraining und schwer. Dreimal pro Woche oft und gern?',
      'Super! Sag mal, mache ich schweres Krafttraining? Dreimal pro Woche, oft und gern?'),
 (62, 'Ja, klar! Frisch und gut. Vom Markt. Wirklich oder sehr und toll.',
      'Ja, klar! Frisch und gut vom Markt. Wirklich toll!'),
 (62, 'Genau, ich kaufe Blumen bunt und schön jeden Samstag und morgens früh und gern.',
      'Genau, ich kaufe jeden Samstag früh bunte Blumen. Gern!'),
 (62, 'Genau, Tom kauft Käse gut und frisch für alle gern und sehr.',
      'Genau, Tom kauft guten frischen Käse für alle. Sehr gern!'),
 (70, 'Kenn ich! Sag mal, brauche ich eine Autoversicherung für den Wagen. Neu. Ab Januar und teuer sehr und wirklich?',
      'Kenn ich! Sag mal, brauche ich eine Autoversicherung für den Wagen? Neu ab Januar, teuer. Sehr und wirklich?'),
 (70, 'Ja, klar! Pflicht für alle. Mit Schutz. Wirklich oder und genau ja und gut?',
      'Ja, klar! Pflicht für alle mit Schutz. Wirklich? Genau, ja!'),
 (70, 'Stimmt, ich brauche eine Autoversicherung! Brauchst du eine Hausratversicherung. Für die Wohnung. Mit Fahrrad und wichtig oder und genau?',
      'Stimmt, ich brauche eine Autoversicherung! Brauchst du eine Hausratversicherung für die Wohnung? Mit Fahrrad, wichtig und genau!'),
 (71, 'Nein, keine, weiß reicht und genau ja und wirklich?',
      'Nein, keine. Weiß reicht, wirklich?'),
 (73, 'Nein, keiner, alle weg und genau wirklich und ja.',
      'Nein, keiner alle weg. Wirklich, ja?'),
 (74, 'Also unser Marktbesuch! Bist du fertig für, Lisa den Winter oder. Sag mal und genau?',
      'Also unser Marktbesuch! Bist du fertig für den Winter, Lisa? Sag mal?'),
 (74, 'Nein, keiner, zu teuer und genau wirklich und ja.',
      'Nein, keiner zu teuer. Wirklich, ja?'),
 (75, 'Also unsere Kleidung! Alles voll bei, Lisa dir oder. Sag mal und genau?',
      'Also unsere Kleidung! Alles voll bei dir, Lisa? Sag mal?'),
 (75, 'Super! Bringt Tom die Winterjacke dick und warm leider, alt gut und wirklich?',
      'Super! Bringt Tom die dicke warme Winterjacke? Leider alt, aber gut und wirklich?'),
 (85, 'Ja, klar! Jeden Tag und fleißig toll und super.',
      'Ja, klar! Jeden Tag fleißig. Toll und super!'),
 (99, 'Ja, klar! Gut und schnell und neu und toll?',
      'Ja, klar! Gut und schnell? Neu und toll?'),
 (99, 'Genau, Tim spricht Deutsch, immer und gern?',
      'Genau, Tim spricht Deutsch. Immer gern!'),
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
            continue  # already applied in a previous partial run
        assert len(hit) == 1, (t, 'match=%d %s' % (len(hit), old[:60]))
        if apply:
            hit[0]['text'] = new
            json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
            open(p, 'a', encoding='utf-8').write('\n')
        n += 1
    print('pairs ok:', n)
