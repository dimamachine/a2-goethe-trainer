"""Manual round 2: salads, test2 day-prompts, closing piles.
Asserts exact match + comma budget. Idempotent (skips already-applied)."""
import json

FIXES = [
 # salads
 (14, 'Also die Hochzeit! Bist du froh sehr findest, Mama du auch?',
      'Also die Hochzeit! Bist du froh, Mama? Findest du auch?'),
 (25, 'Also unsere Bücher! Liest du viel du, Vater auch oder. Was meinst du und genau?',
      'Also unsere Bücher! Liest du viel, Vater? Du auch, oder was meinst du?'),
 (29, 'Also unsere Vereine! Bist du aktiv du, Mutter auch oder?',
      'Also unsere Vereine! Bist du aktiv, Mutter? Du auch, oder?'),
 (41, 'Also unser Wintertag! Bist du warm genug heute, Lisa und gut?',
      'Also unser Wintertag! Bist du warm genug heute, Lisa?'),
 (60, 'Also unser Parktag! Bist du fit heute, Lisa oder. Sag mal und genau?',
      'Also unser Parktag! Bist du fit heute, Lisa, oder? Sag mal!'),
 (61, 'Also unser Training! Na Training, Lisa heute oder. Sag mal genau und los ja?',
      'Also unser Training! Heute Training, Lisa, oder? Sag mal! Geht es los?'),
 # test2: flesh out bare day-prompts (days stay in same lines)
 (2, 'Markus: Dienstag?', 'Markus: Verstehe. Und wie sieht es am Dienstag aus?'),
 (2, 'Markus: Klingt nett. Donnerstag?', 'Markus: Klingt nett. Und was machst du am Donnerstag?'),
 (2, 'Markus: Und Freitag?', 'Markus: Und wie ist es am Freitag?'),
 (2, 'Markus: Und am Samstag?', 'Markus: Und was ist am Samstag?'),
 (2, 'Markus: Oh, gratuliere ihr! Und Sonntag?', 'Markus: Oh, gratuliere ihr! Und wie sieht der Sonntag aus?'),
 (2, 'Anna: Hallo Markus, lass mich überlegen. Am Montag bin ich frei — aber ich wollte ein Buch zu Ende lesen. Sehr ruhig bleiben.',
      'Anna: Hallo Markus, lass mich überlegen. Am Montag bin ich frei, aber ich wollte ein Buch zu Ende lesen. Ich bleibe ganz ruhig.'),
 (2, 'Anna: Donnerstag treffe ich Clara zum gemeinsamen Kochen — italienisch. Sie wollte zuerst ins Schwimmbad aber jetzt machen wir lieber Pasta.',
      'Anna: Donnerstag treffe ich Clara zum gemeinsamen Kochen, italienisch. Sie wollte zuerst ins Schwimmbad, aber jetzt machen wir lieber Pasta.'),
 (2, 'Anna: Nein, kein Schwimmen. Und mein Bruder spielt jeden Sonntag Fußball aber das ist nicht mein Sport.',
      'Anna: Nein, kein Schwimmen. Und mein Bruder spielt jeden Sonntag Fußball, aber das ist nicht mein Sport.'),
 (2, 'Anna: Sonntag bin ich frei. Lass uns dann Kaffee trinken — sagen wir um drei im Café Mozart.',
      'Anna: Sonntag bin ich frei. Lass uns dann Kaffee trinken, sagen wir um drei im Café Mozart.'),
 # closing piles (user-quoted)
 (29, 'Dir auch! Bis Dienstag, beim Schach, viel Glück. Tschüss. Bis bald und viel Spaß!',
      'Dir auch! Bis Dienstag, beim Schach, viel Glück. Tschüss! Bis bald!'),
 (32, 'Verstehe! Dann viel Spaß, im Bad, allen und tschüss bis morgen!',
      'Verstehe! Dann viel Spaß im Bad, allen! Tschüss, bis morgen!'),
 (41, 'Keine Angst! Bis morgen im Schnee, tschüss! Viel Spaß!',
      'Keine Angst! Bis morgen im Schnee, tschüss! Viel Spaß!'),
 (41, 'Bis morgen! Fahr vorsichtig, viel Spaß! Danke!',
      'Bis morgen! Fahr vorsichtig, viel Spaß! Danke!'),
 (52, 'Verstehe! Dann viel Spaß, im Bad, allen. Tschüss. Bis bald bis morgen!',
      'Verstehe! Dann viel Spaß im Bad, allen! Tschüss, bis morgen!'),
 (52, 'Dir auch! Bis morgen, tschüss, mach es gut und gute Nacht!',
      'Dir auch! Bis morgen, tschüss! Mach es gut, gute Nacht!'),
 (67, 'Nein, beides nicht. Schade! Dann viel Spaß, im Zoo. Tschüss. Bis bald!',
      'Nein, beides nicht. Schade! Dann viel Spaß im Zoo, tschüss! Bis bald!'),
]

if __name__ == '__main__':
    import sys
    apply = '--apply' in sys.argv
    n = 0
    for t, old, new in FIXES:
        # old may include "Speaker: " prefix or be bare text
        assert new.count(',') <= 2, (t, new)
        p = f'tools/_test{t}_data.json'
        d = json.load(open(p, encoding='utf-8'))
        hit = [l for l in d['teile'][1]['lines']
               if l['text'] == old or (l['speaker'] + ': ' + l['text']) == old]
        done = [l for l in d['teile'][1]['lines']
                if l['text'] == new or (l['speaker'] + ': ' + l['text']) == new]
        if not hit and done:
            continue
        assert len(hit) == 1, (t, 'match=%d: %s' % (len(hit), old[:70]))
        h = hit[0]
        h['text'] = new if ': ' not in new[:len(h['speaker'])+2] or not new.startswith(h['speaker']+': ') else new[len(h['speaker'])+2:]
        # simpler: if new contains speaker prefix strip it
        if new.startswith(h['speaker'] + ': '):
            h['text'] = new[len(h['speaker'])+2:]
        else:
            h['text'] = new
        n += 1
        if apply:
            json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
            open(p, 'a', encoding='utf-8').write('\n')
    print('pairs to apply:', n)
