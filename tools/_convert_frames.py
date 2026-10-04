"""Convert 6 T2 tests from name-frames to day/month-frames (user-approved).
Rewrites items + instruction + full dialogue. Speakers/options untouched.
Usage: python3 tools/_convert_frames.py [--apply]"""
import json, re

def L(sp, g, t):
    return {"speaker": sp, "gender": g, "text": t}

CONV = {}

CONV[11] = {
 "instruction": "Sie hören ein Gespräch. Sie hören den Text einmal. Welcher Termin ist an welchem Tag? Wählen Sie für jeden Tag einen Buchstaben (a–i).",
 "items": [("Montag", "h"), ("Dienstag", "b"), ("Mittwoch", "f"), ("Donnerstag", "a"), ("Freitag", "e")],
 "lines": [
  L("Vater", "m", "Also unsere Termine! Hast du den Zettel, Mutter? Die Woche wird voll."),
  L("Mutter", "f", "Ja, hier! Fünf Termine in einer Woche. Am besten alles der Reihe nach."),
  L("Vater", "m", "Stimmt, am Montag geht es los. Ich habe den Arzt-Termin für die Impfung. Um neun beim Hausarzt."),
  L("Mutter", "f", "Um neun, alles klar. Und was ist am Dienstag? Ich schreibe es auf."),
  L("Vater", "m", "Am Dienstag habe ich den Bank-Termin. Zum Geldwechseln für den Urlaub."),
  L("Mutter", "f", "Und was machen wir am Mittwoch? Und danach Kaffee?"),
  L("Vater", "m", "Am Mittwoch ist TÜV-Termin fürs Auto. Um acht in der Werkstatt. Die Bremsen sind neu."),
  L("Mutter", "f", "Hoffentlich! Wie wäre es mit dem Friseur? Gehen wir auch zum Friseur?"),
  L("Vater", "m", "Nein, Friseur erst nächste Woche. Diese Woche keine Zeit. Das passt gut."),
  L("Mutter", "f", "Schade, am Donnerstag muss ich zum Bürgeramt. Für den Reisepass. Der alte ist fast voll."),
  L("Vater", "m", "Stimmt, der Pass läuft bald ab. Und die Katze? Muss sie zum Tierarzt? Sie frisst gut."),
  L("Mutter", "f", "Nein, die Katze ist gesund. Wir brauchen keinen Tierarzt. Sie ist jung und fit."),
  L("Vater", "m", "Und was ist am Freitag? Dann sind wir fertig."),
  L("Mutter", "f", "Am Freitag habe ich den Zahnarzt-Termin. Um zehn. Aber nur Kontrolle. Das geht schnell."),
  L("Vater", "m", "Dann viel Erfolg! Alles klar bis Freitag! Wir schaffen das."),
  L("Mutter", "f", "Bis dann! Leg den Zettel auf den Tisch!"),
 ],
}

CONV[30] = {
 "instruction": "Sie hören ein Gespräch. Sie hören den Text einmal. Welcher Termin ist an welchem Tag? Wählen Sie für jeden Tag einen Buchstaben (a–i).",
 "items": [("Montag", "e"), ("Dienstag", "i"), ("Mittwoch", "a"), ("Donnerstag", "g"), ("Freitag", "h")],
 "lines": [
  L("Vater", "m", "Also die Ämter! Hast du die Liste, Mutter? Die Woche wird voll."),
  L("Mutter", "f", "Ja, hier! Fünf Gänge in einer Woche. Am besten alles der Reihe nach."),
  L("Vater", "m", "Genau, am Montag gehen wir zum Bürgeramt. Für den Personalausweis. Mit Foto und Geburtsurkunde."),
  L("Mutter", "f", "Um acht, alles klar. Und was ist am Dienstag? Ich schreibe es auf."),
  L("Vater", "m", "Am Dienstag gehen wir zum Finanzamt. Die Steuern für letztes Jahr. Das ist viel Geld. Ich freue mich schon."),
  L("Mutter", "f", "Und was machen wir am Mittwoch? Und danach Mittagessen?"),
  L("Vater", "m", "Am Mittwoch hat das Auto TÜV. Die Hauptuntersuchung. Um halb neun in der Werkstatt."),
  L("Mutter", "f", "Verstanden. Müssen wir auch zum Arbeitsamt? Wegen der Rente? Ich frage nur."),
  L("Vater", "m", "Nein, Arbeitsamt erst nächsten Monat. Diese Woche nicht. Ganz sicher."),
  L("Mutter", "f", "Am Donnerstag gehen wir zum Standesamt. Für die Geburtsurkunde vom Baby. Das Baby ist klein."),
  L("Vater", "m", "Schön, das Baby braucht die Urkunde. Und die Ausländerbehörde? Brauchen wir ein Visum? Das dauert lange."),
  L("Mutter", "f", "Wir brauchen kein Visum. Die Ausländerbehörde fällt weg."),
  L("Vater", "m", "Prima, und was ist am Freitag? Dann sind wir fertig. Mach es gut."),
  L("Mutter", "f", "Am Freitag gehen wir zur Krankenkasse. Für die neue Karte. Das freut mich."),
  L("Vater", "m", "Dann viel Erfolg! Alles klar bis Freitag! Wir schaffen das."),
  L("Mutter", "f", "Bis dann! Und nimm die Mappe mit!"),
 ],
}

CONV[49] = {
 "instruction": "Sie hören ein Gespräch. Sie hören den Text einmal. Welche Vorstellung läuft an welchem Tag? Wählen Sie für jeden Tag einen Buchstaben (a–i).",
 "items": [("Dienstag", "c"), ("Mittwoch", "g"), ("Donnerstag", "d"), ("Freitag", "a"), ("Samstag", "e")],
 "lines": [
  L("Lukas", "m", "Also der Spielplan! Hast du die Zeitung, Lisa? Die Woche wird toll."),
  L("Lisa", "f", "Ja, hier! Fünf Abende Theater. Ich freue mich schon. Das wird super."),
  L("Lukas", "m", "Stimmt, am Dienstag läuft das Kinderstück. Um sechs für die Kleinen. Die Kinder lieben es."),
  L("Lisa", "f", "Schön, für die Kinder. Und was läuft am Mittwoch? Ich schreibe es auf."),
  L("Lukas", "m", "Am Mittwoch tanzen sie Ballett. Schwanensee mit Musik. Anna kommt mit. Das wird schön."),
  L("Lisa", "f", "Herrlich. Und was gibt es am Donnerstag? Erzähl mehr."),
  L("Lukas", "m", "Am Donnerstag gibt es das Comedy-Stück. Zum Lachen mit Freunden. Kommst du mit?"),
  L("Lisa", "f", "Lustig! Und das Musical Cats? Läuft es auch?"),
  L("Lukas", "m", "Nein, Cats ist ausverkauft. Leider keine Karten. Das ist schade. Im Herbst vielleicht."),
  L("Lisa", "f", "Schade, am Freitag spielen sie Faust. Das wird toll. Ich freue mich schon."),
  L("Lukas", "m", "Stark, Faust ist super. Und Krimi-Theater? Magst du Krimis? Das freut mich."),
  L("Lisa", "f", "Nein, Krimis mag ich nicht. Lieber etwas Lustiges."),
  L("Lukas", "m", "Verstanden. Und was läuft am Samstag? Für alle."),
  L("Lisa", "f", "Am Samstag spielen sie Romeo und Julia. Liebe mit Musik. Das wird toll. Ich freue mich."),
  L("Lukas", "m", "Dann viel Spaß! Alles klar bis Samstag! Wir schaffen das."),
  L("Lisa", "f", "Bis dann! Und kauf die Karten heute! Tschüss! Mach es gut."),
 ],
}

CONV[81] = {
 "instruction": "Sie hören ein Gespräch. Sie hören den Text einmal. Welcher Kurs läuft an welchem Tag? Wählen Sie für jeden Tag einen Buchstaben (a–i).",
 "items": [("Montag", "g"), ("Dienstag", "f"), ("Mittwoch", "d"), ("Donnerstag", "b"), ("Freitag", "i")],
 "lines": [
  L("Lukas", "m", "Also die Kurse! Hast du das Heft, Lisa? Der Plan ist neu."),
  L("Lisa", "f", "Ja, hier! Fünf Kurse in einer Woche. Ich freue mich schon. Das wird super."),
  L("Lukas", "m", "Am Montag beginnt der Sprachkurs. Englisch für den Urlaub. Das ist praktisch. Mit Anna."),
  L("Lisa", "f", "Praktisch. Und was läuft am Dienstag? Ich schreibe es auf."),
  L("Lukas", "m", "Am Dienstag ist Computerkurs. Mit Laptop und Internet. Mit eigenem Laptop. Das ist neu."),
  L("Lisa", "f", "Nützlich. Und was gibt es am Mittwoch? Erzähl mehr."),
  L("Lukas", "m", "Am Mittwoch ist Yoga-Kurs. Ruhe am Abend. Ganz ruhig und langsam. Das tut gut."),
  L("Lisa", "f", "Schön! Und Gitarre? Gibt es Gitarrenkurs? Für den Anfang?"),
  L("Lukas", "m", "Nein, Gitarre ist voll. Leider kein Platz mehr. Das ist schade. Im Herbst vielleicht."),
  L("Lisa", "f", "Schade, am Donnerstag ist Fotokurs. Mit Kamera durch die Stadt. Durch den Park. Das klingt toll."),
  L("Lukas", "m", "Fotos sind super. Und Malkurs? Malst du gern? Anna kommt mit."),
  L("Lisa", "f", "Nein, Malen erst nächstes Jahr. Jetzt keine Zeit. Vielleicht später."),
  L("Lukas", "m", "Alles klar. Und was läuft am Freitag? Für alle."),
  L("Lisa", "f", "Am Freitag ist Kochkurs. Italienisch kochen mit Freunden. Für alle. Das wird lecker."),
  L("Lukas", "m", "Dann viel Spaß! Alles klar bis Freitag! Wir schaffen das."),
  L("Lisa", "f", "Bis dann! Und meld uns heute an! Tschüss! Mach es gut."),
 ],
}

CONV[24] = {
 "instruction": "Sie hören ein Gespräch. Sie hören den Text einmal. Welches Training ist an welchem Tag? Wählen Sie für jeden Tag einen Buchstaben (a–i).",
 "items": [("Montag", "f"), ("Dienstag", "c"), ("Mittwoch", "i"), ("Donnerstag", "d"), ("Freitag", "h")],
 "lines": [
  L("Lisa", "f", "Also die Trainingswoche! Hast du den Plan, Lukas? Der Plan ist neu."),
  L("Lukas", "m", "Ja, hier! Fünf Trainings in einer Woche. Ich freue mich schon. Das wird super."),
  L("Lisa", "f", "Genau, am Montag ist Fußball im Verein. Mit Freunden auf dem Platz. Tim spielt mit. Das ist wichtig."),
  L("Lukas", "m", "Und was ist am Dienstag? Ich schreibe es auf."),
  L("Lisa", "f", "Am Dienstag tanzt Marie Ballett. In der Tanzschule. Sie übt viel. Das ist schön."),
  L("Lukas", "m", "Schön. Und was gibt es am Mittwoch? Erzähl mehr."),
  L("Lisa", "f", "Am Mittwoch singt der Kinderchor. In der Schule am Abend. Mit Anna. Das klingt schön."),
  L("Lukas", "m", "Toll! Und Reiten? Reitet Marie auch?"),
  L("Lisa", "f", "Nein, Reiten ist zu teuer. Das geht nicht. Vielleicht später. Das ist schade."),
  L("Lukas", "m", "Verstanden. Am Donnerstag ist Karate. Mit Sportkleidung. Das ist stark. Kommst du mit?"),
  L("Lisa", "f", "Karate ist gut. Und Sprachen? Lernt jemand Sprachen? Das freut mich."),
  L("Lukas", "m", "Nein, Sprachen nur in der Schule. Nicht im Verein. Ganz sicher. Das ist klar."),
  L("Lisa", "f", "Alles klar. Und was ist am Freitag? Für alle."),
  L("Lukas", "m", "Am Freitag spielt Tim Schach. Im Klub mit Freunden. Um vier. Das wird toll."),
  L("Lisa", "f", "Dann viel Spaß! Alles klar bis Freitag! Wir schaffen das."),
  L("Lukas", "m", "Bis dann! Und hol die Taschen heute! Tschüss! Mach es gut."),
 ],
}

CONV[64] = {
 "instruction": "Sie hören ein Gespräch. Sie hören den Text einmal. Wohin fahren sie in welchem Monat? Wählen Sie für jeden Monat einen Buchstaben (a–i).",
 "items": [("Mai", "h"), ("Juni", "i"), ("Juli", "c"), ("August", "g"), ("September", "e")],
 "lines": [
  L("Lisa", "f", "Also der Reiseplan! Hast du den Kalender, Lukas? Der Plan ist neu."),
  L("Lukas", "m", "Ja, hier! Fünf Reisen in einem Jahr. Ich freue mich schon."),
  L("Lisa", "f", "Super, im Mai machen wir eine Städtereise. Nach Prag mit dem Zug. Das wird schön."),
  L("Lukas", "m", "Herrlich. Und wohin geht es im Juni? Erzähl mehr. Ich schreibe es auf."),
  L("Lisa", "f", "Im Juni machen wir Strandurlaub. Sonne und Meer in Spanien. Mit Anna."),
  L("Lukas", "m", "Wunderbar. Und was machen wir im Juli? Erzähl mehr."),
  L("Lisa", "f", "Im Juli ist Camping. Mit Zelt an den See. Das klingt gut."),
  L("Lukas", "m", "Cool! Und Safari in Afrika? Wäre das was?"),
  L("Lisa", "f", "Nein, Safari ist zu teuer. Vielleicht später. Das ist schade. Das ist klar."),
  L("Lukas", "m", "Schade, im August wandern wir in den Bergen. Mit Rucksack und Karte. Mit Tom. Das wird schön."),
  L("Lisa", "f", "Toll, Berge sind schön. Und Skiurlaub? Fahren wir Ski? Anna kommt mit."),
  L("Lukas", "m", "Nein, Ski erst im Winter. Jetzt ist Sommer. Ganz sicher. Das steht fest."),
  L("Lisa", "f", "Und wohin geht es im September? Dann sind wir fertig. Für alle."),
  L("Lukas", "m", "Im September ist Wellness-Urlaub. Hotel mit Frühstück. Das wird ruhig."),
  L("Lisa", "f", "Dann viel Spaß! Alles klar bis September! Wir schaffen das."),
  L("Lukas", "m", "Bis dann! Und buch das Hotel heute! Tschüss!"),
 ],
}

if __name__ == "__main__":
    import sys
    apply = "--apply" in sys.argv
    for n, c in CONV.items():
        p = f"tools/_test{n}_data.json"
        d = json.load(open(p, encoding="utf-8"))
        te = d["teile"][1]
        assert len(c["lines"]) == 16, n
        assert sorted(set(l["speaker"] for l in c["lines"])) == sorted(set(l["speaker"] for l in te["lines"])), (n, "speakers changed!")
        for l in c["lines"]:
            assert l["text"].count(",") <= 2, (n, l["text"])
        import re
        w = sum(len(re.findall(r"[A-Za-zÄÖÜäöüß]+", l["text"])) for l in c["lines"])
        print(f"test{n}: {w} words")
        if apply:
            te["instruction"] = c["instruction"]
            te["items"] = [{"person": p_, "correct": c_} for p_, c_ in c["items"]]
            te["lines"] = c["lines"]
            json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            open(p, "a", encoding="utf-8").write("\n")
    print("done")
