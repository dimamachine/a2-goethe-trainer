# Hören-Test-Schema und Generation

Dieser Ordner enthält Skripte und Dokumentation, um Hören-Tests im Goethe-A2-Format zu erzeugen.

## Hauptkonzept

Jeder Hörtest folgt der offiziellen Goethe-Zertifikat-A2-Struktur (Fit in Deutsch 2):

| Teil | Format | Anzahl | Wird gehört | Antwortform |
|------|--------|--------|------------|-------------|
| 1 | 5 kurze Texte (Durchsage, Anrufbeantworter, Wetterbericht, Verkehrsfunk, kurze Mitteilung) | 5 Aufgaben | jeder Text 2× | MC a/b/c |
| 2 | 1 längeres Gespräch zwischen 2 Personen | 5 Aufgaben | 1× | Zuordnung: 5 Tage/Personen/Orte → 9 Aktivitäten/Optionen (a–i) |
| 3 | 5 kurze Gespräche (Restaurant, Geschäft, Schule, Arzt, Telefon usw.) | 5 Aufgaben | jedes Gespräch 1× | MC a/b/c |
| 4 | 1 längeres Interview | 5 Aufgaben | 2× | Ja / Nein |

**20 Aufgaben pro Test. Maximale Punktzahl: 20.**

## Längenrichtlinien (Goethe-Modellsatz / Übungssatz, nicht B1)

Offizielle A2-Hörtexte sind kürzer als frühere interne Vorgaben. Richtwerte nach Modellsatz Erwachsene und DW-A2-Transkripten:

| Teil | Wörter | Sprecherwechsel | Audio (einmal gehört) |
|------|--------|-----------------|------------------------|
| 1 | 45–65 pro Text | Monolog | ~20–25 Sek. |
| 2 | 160–220 gesamtes Gespräch | 12–16 | ~70–90 Sek. |
| 3 | 45–70 pro Dialog | 4–6 | ~20–25 Sek. |
| 4 | 170–240 Interview gesamt | 10–14 | ~70–90 Sek. |

Für edge-tts: keine Punkt-Fragmente (`Ja. Ich…`). Komma + Kleinbuchstabe (`Ja, ich…`), oder den Satz zusammenziehen (`Seit acht Jahren habe ich…`).

## Goethe-typische Aufgaben-Tricks

Die richtige Antwort ist **fast nie wörtlich** im Text. Ein paar typische Muster:

1. **Alle drei Optionen werden im Text erwähnt**, aber nur eine antwortet auf die konkrete Frage.
   - Text: "Heute Hähnchen. Gestern hatten wir Fisch, vorgestern Burger."
   - Frage: "Was hat sie gestern gegessen?"
   - a) Fisch ✓ b) Burger c) Hähnchen — alle drei sind erwähnt!

2. **Umformulierung**: Antwort steht im Text mit anderen Wörtern.
   - Text: "Die Tür funktioniert nicht mehr — kommt nicht auf."
   - Frage: "Was ist kaputt?"
   - Lösung: "Tür" — direkt zu "funktioniert nicht / kommt nicht auf" verlinkt.

3. **Sondern**-Konstruktion: einer der Sprecher korrigiert.
   - "Wir treffen uns nicht um sechs, sondern erst um sieben."
   - Distraktor: 6 Uhr. Lösung: 7 Uhr.

4. **Negation**: "Sie hat keine Zeit am Samstag, aber Sonntag passt."
   - Distraktor: Samstag.

5. **Zeitform-Trick**: Vergangenheit vs. Gegenwart vs. Zukunft.
   - Text: "Ich bin früher viel gereist. Jetzt bleibe ich lieber zu Hause."
   - Frage: "Was macht die Person?" — Lösung: "bleibt zu Hause", nicht "reist".

6. **Bestätigung statt direkter Aussage**: Sprecher A schlägt vor, B akzeptiert oder lehnt ab.
   - "Sollen wir um 14 Uhr?" "Nein, lieber um 15." → Lösung: 15 Uhr.

## Daten-Schema

```js
{
  id: 'ai-1',               // stabile, kurze ID (für Audio-Pfade)
  name: 'Themenname',       // Titel im Picker
  teile: [
    // — Teil 1 —
    {
      type: 'mc',
      title: 'Teil 1: Fünf kurze Texte',
      instruction: 'Du hörst fünf kurze Texte. Du hörst jeden Text zweimal. Wähle a, b oder c.',
      items: [
        {
          transcript: '...80–120 Wörter Text...',
          gender: 'm',     // 'm' oder 'f' — bestimmt Sprecher-Geschlecht
          q: 'Wo/Was/Wann/Wie ...?',
          opts: ['Option a', 'Option b', 'Option c'],
          correct: 1       // Index 0/1/2
        },
        // ... 5 items insgesamt
      ]
    },
    // — Teil 2 —
    {
      type: 'match',
      title: 'Teil 2: Ein Gespräch',
      instruction: 'Du hörst ein Gespräch. Du hörst den Text einmal. Wähle für jede Person/jeden Tag den passenden Buchstaben (a–i).',
      lines: [             // Gespräch zwischen 2+ Personen
        { speaker: 'Anna',   gender: 'f', text: '...' },
        { speaker: 'Markus', gender: 'm', text: '...' },
        // ... 10–18 Sprecher-Wechsel insgesamt
      ],
      options: [           // 9 Optionen a–i (5 richtig + 3 Distraktoren + 1 Beispiel)
        { letter: 'a', text: '...' },
        // ... 9 insgesamt
      ],
      items: [             // 5 Aufgaben (Beispiel-0 nicht enthalten)
        { person: 'Anna',           correct: 'c' },
        { person: 'Markus',         correct: 'a' },
        // ... 5 insgesamt
      ]
    },
    // — Teil 3 —
    {
      type: 'mc',
      title: 'Teil 3: Fünf kurze Gespräche',
      instruction: 'Du hörst fünf kurze Gespräche. Du hörst jedes Gespräch einmal. Wähle a, b oder c.',
      items: [
        {
          lines: [         // 5–7 Wechsel zwischen 2 Sprechern
            { speaker: 'Kundin',     gender: 'f', text: '...' },
            { speaker: 'Verkäufer',  gender: 'm', text: '...' },
            // ...
          ],
          q: 'Was bestellt die Kundin?',
          opts: ['Pizza', 'Pasta', 'Salat'],
          correct: 0
        },
        // ... 5 items insgesamt
      ]
    },
    // — Teil 4 —
    {
      type: 'jn',
      title: 'Teil 4: Interview',
      instruction: 'Du hörst ein Interview. Du hörst den Text zweimal. Ja oder Nein?',
      transcript: [        // Interview zwischen 2 Personen
        { speaker: 'Reporter', gender: 'm', text: '...' },
        { speaker: 'Schmidt',  gender: 'f', text: '...' },
        // ... 10–14 Wechsel insgesamt
      ],
      items: [             // 5 Aussagen
        { q: 'Sie arbeitet seit 5 Jahren als Lehrerin.', correct: 'ja' },
        // ... 5 insgesamt
      ]
    }
  ]
}
```

## Sprecher-Geschlecht (`gender`)

Pflicht-Feld in:
- Teil 1 monologue items (`item.gender`)
- Allen `speaker`-Einträgen in `lines` und `transcript`

Werte: `'m'` (männlich) oder `'f'` (weiblich).

Das Audio-Skript wählt:
- Männlicher Sprecher → eine zufällige männliche Stimme (Conrad oder Florian)
- Weiblicher Sprecher → eine zufällige weibliche Stimme (Katja oder Seraphina)
- Bei 2 Sprechern desselben Geschlechts → 2 verschiedene Stimmen dieses Geschlechts

## Audio-Generation

```bash
# Audio für alle Tests erzeugen (nur fehlende):
python3 tools/generate_audio.py

# Bestimmten Test erzeugen:
python3 tools/generate_audio.py --test ai-5

# Erzwingen (überschreibt vorhandene Dateien):
python3 tools/generate_audio.py --force
```

Ausgabe: `assets/audio/{test_id}/`:
- `t1-1.mp3` … `t1-5.mp3` (Teil 1, 5 Monologe)
- `t2.mp3` (Teil 2, langes Gespräch)
- `t3-1.mp3` … `t3-5.mp3` (Teil 3, 5 Dialoge)
- `t4.mp3` (Teil 4, Interview)

**Audio-Dateien werden nicht in git committed** (siehe `.gitignore`). Jeder muss sie lokal generieren.

## Voraussetzungen

```bash
pip install edge-tts                 # TTS-Engine (Azure Neural über Edge)
brew install ffmpeg                  # MP3-Konkatenation
brew install node                    # Test-Daten-Extraktion aus HTML
```

## Inhaltliche Variation pro Test

Damit 100 Tests abwechslungsreich bleiben, sollten Themen rotieren:

- **Teil 1 Quellen**: Bahnhofs-/Flughafendurchsage, Anrufbeantworter (Familie, Arzt, Firma), Wetterbericht, Verkehrsfunk, Werbung, Lautsprecherdurchsage im Geschäft/Hotel/Krankenhaus, Schulnachricht, Sportnachricht, Veranstaltungsansage.
- **Teil 2 Themen**: Wochenplanung, Familienausflug, Urlaubsplanung, Geburtstag organisieren, Klassenfahrt, Umzug, WG-Aufgaben verteilen, Hochzeit vorbereiten, Vereinsaktivität, Schulprojekt.
- **Teil 3 Settings**: Restaurant/Café, Geschäft (Mode/Schuhe/Buch), Apotheke/Arzt, Schule (Lehrer–Schüler, Eltern–Lehrer), Hotel-Rezeption, Bahnhof/Auskunft, Telefongespräch (Reservierung, Termin), Sprachschule, Sportverein.
- **Teil 4 Interview-Themen**: Beruf (Köchin, Pilot, Lehrer, Arzt, Bauer, Designer …), Hobby (Sport, Musik, Reisen, Kunst …), Ausbildung, Lebensgeschichte, Initiative/Verein.

## Inhalts-Checkliste pro Test

- [ ] Alle 5 Teil-1-Texte sind 80–120 Wörter und enthalten alle 3 Antwort-Optionen
- [ ] Teil-2-Gespräch hat 10–18 Sprecherwechsel und ein klares 5+Beispiel Matching-Schema
- [ ] Teil-3-Dialoge haben 5–7 Wechsel und realistische Settings
- [ ] Teil-4-Interview ist 12–16 Wechsel zwischen 2 Personen mit klaren Fakten
- [ ] Mindestens 2–3 Aufgaben pro Teil nutzen Goethe-Tricks (siehe oben)
- [ ] Jeder Sprecher hat `gender` gesetzt
- [ ] Vokabular bleibt im A2-Wortschatzbereich
- [ ] Keine politischen, religiösen oder kontroversen Themen
