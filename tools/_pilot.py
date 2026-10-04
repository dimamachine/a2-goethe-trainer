"""Pilot: new-genre T2 for tests 3, 28, 40 — TWO speakers discuss the five persons."""
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

D[3] = [
("Anna","f","Also, morgen ist das Familienfest! Freust du dich schon, Markus, sehr?"),
("Markus","m","Sehr! Ich freue mich schon, seit Wochen, auf alle."),
("Anna","f","Ich auch! Backe ich wieder meinen Schokokuchen, mit viel Kakao, dunklem?"),
("Markus","m","Ja, bitte! Alle lieben deinen Schokoladenkuchen, wie jedes Jahr."),
("Anna","f","Gut, ich backe einen Schokoladenkuchen! Bringst du Wein mit, wie immer?"),
("Markus","m","Klar, ich bringe Wein mit, roten und weißen, vom guten Laden an der Ecke."),
("Anna","f","Schön! Was ist mit Brot, bringt jemand Brot mit, frisches, vom Bäcker?"),
("Markus","m","Brot haben wir genug zu Hause, das fällt weg. Aber Getränke, wer bringt die Getränke?"),
("Anna","f","Tim bringt alkoholfreie Getränke, zwei Kästen, für die Kinder und die Oma."),
("Markus","m","Super! Und das Hauptgericht, wer kocht, du oder deine liebe Mutter?"),
("Anna","f","Meine Mutter kocht das Hauptgericht, wie immer, mit viel Liebe."),
("Markus","m","Herrlich! Und Salat, wer macht Salat, frischen, zum Festessen?"),
("Anna","f","Sara macht einen großen Salat, frisch aus dem Garten. Eis lassen wir weg, Kuchen reicht, wirklich."),
("Markus","m","Stimmt! Also, bis morgen, um drei, bei euch, pünktlich!"),
]

D[28] = [
("Mutter","f","Schau mal, die Post ist da! Ein ganzer Stapel, heute Morgen."),
("Vater","m","Oh, viel! Komm, wir sortieren zusammen, in Ruhe."),
("Mutter","f","Gern! Sag mal, ist das Paket da, mit der Tasche, aus Berlin, endlich?"),
("Vater","m","Ja, hier! Ein Paket mit einer Tasche, von Tante, das ist deins."),
("Mutter","f","Hurra, das ist meins! Und sonst, nur Werbung, oder auch teure Rechnungen?"),
("Vater","m","Leider eine Steuer-Rechnung, für mich, zweihundert Euro."),
("Mutter","f","Mist! Ist etwas für Lisa dabei, eine Karte, oder ein dicker Brief?"),
("Vater","m","Ja, schau! Eine Postkarte aus dem Ausland, aus Spanien, von ihrer besten Freundin."),
("Mutter","f","Toll! Keine Mahnung, nur ein Werbeprospekt, nichts Wichtiges. Aber Markus hat Post!"),
("Vater","m","Wirklich? Was denn, eine Rechnung, oder ein wichtiger Brief?"),
("Mutter","f","Nein, eine neue Kreditkarte, endlich da, nach langen Wochen."),
("Vater","m","Praktisch! Und Anna, hat sie etwas bekommen, ein Buch, vielleicht, ein Krimi?"),
("Mutter","f","Ja, ein bestelltes Buch, zum Lesen am Abend, sehr spannend."),
("Vater","m","Alles da! Ich räume die Post weg, in den Schrank, sofort, in Ordnung."),
("Mutter","f","Danke! Und die Rechnung zahlst du morgen, einverstanden?"),
("Vater","m","Ja, morgen, versprochen, ehrlich!"),
]

D[40] = [
("Lukas","m","Endlich Strand, das Wetter ist perfekt, oder, was meinst du?"),
("Lisa","f","Perfekt! Sonne, Meer, keine Wolken, was wollen wir mehr, herrlich?"),
("Lukas","m","Ich surfe zuerst, mit dem Brett, die Wellen sind super, heute."),
("Lisa","f","Viel Spaß! Und ich fahre Wasserski, hinter dem Boot, um elf."),
("Lukas","m","Cool! Kommt Tom auch, liegt er wieder nur rum, faul, wie immer?"),
("Lisa","f","Er liegt in der Sonne und will nur lesen, den ganzen Tag, mit Buch."),
("Lukas","m","Typisch Tom! Und Sara, baut sie wieder Burgen, wie immer?"),
("Lisa","f","Ja, sie baut Sandburgen, mit Turm, am Wasser, stundenlang."),
("Lukas","m","Schön! Ist das Wasser warm, oder kalt, heute?"),
("Lisa","f","Angenehm, nicht zu kalt! Gehst du auch tauchen, später?"),
("Lukas","m","Vielleicht! Geht jemand tauchen, zu den Fischen, heute, bei dem Wetter?"),
("Lisa","f","Tim taucht, mit Brille, heute Nachmittag, tief unten."),
("Lukas","m","Toll! Und surft noch jemand, außer mir, vielleicht Tom, oder du?"),
("Lisa","f","Nein, Tom liest nur. Surfen ist deins, allein!"),
("Lukas","m","Schade! Und schwimmt jemand Bahnen, morgens, im kalten Wasser?"),
("Lisa","f","Nein, Bahnen schwimmt keiner, zu viele Wellen, heute, viel zu wild."),
]

for n, lines in D.items():
    assert 12 <= len(lines) <= 16, (n, len(lines))
    set_lines(n, lines)
