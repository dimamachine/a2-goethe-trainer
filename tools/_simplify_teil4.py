#!/usr/bin/env python3
"""Replace the Teil-4 interview (transcript + 5 Ja/Nein items) of the 25 most
B1-heavy tests with shorter, A2-level versions.

- Same interviewee name/role (so the existing 'instruction' line stays valid).
- ~110-140 words instead of ~210-308; simple A2 vocabulary and short sentences.
- First Ja/Nein answer kept at its current polarity to preserve the ~50/50
  first-item balance across the bank.
- Only Teil 4 changes, so only each test's t4.mp3 must be regenerated.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / 'tools'

# (reporter_label, reporter_gender, expert_label, expert_gender, [texts R,E,R,E...], [(stmt,ans)*5])
DATA = {
 'ai-63': ('Reporterin','f','Wolf','m',[
    'Herr Wolf, wie lange arbeiten Sie schon als Mechaniker?',
    'Schon seit zwanzig Jahren. Ich repariere jeden Tag Autos. Die Arbeit macht mir Spaß.',
    'Was reparieren Sie am häufigsten?',
    'Meistens Bremsen und Reifen. Im Winter sind oft die Batterien leer.',
    'Müssen die Kunden lange warten?',
    'Manchmal ja. Aber bei einem Notfall helfe ich sofort.',
    'Wie können die Kunden Geld sparen?',
    'Sie sollen früh kommen. Ein kleines Problem ist billig, ein großes ist teuer.',
    'Was wünschen Sie sich von den Kunden?',
    'Dass sie mir vertrauen. Ich zeige ihnen immer die kaputten Teile. Ich bin ehrlich.'],
   [('Herr Wolf arbeitet seit zwanzig Jahren als Mechaniker.','ja'),
    ('Er repariert am häufigsten die Fenster.','nein'),
    ('Bei einem Notfall hilft er sofort.','ja'),
    ('Er rät, erst spät in die Werkstatt zu kommen.','nein'),
    ('Er zeigt den Kunden die kaputten Teile.','ja')]),

 'ai-57': ('Reporter','m','Lange','f',[
    'Frau Lange, wie ist der Wohnungsmarkt heute?',
    'Sehr schwer für Mieter. Es gibt wenige Wohnungen und die Mieten sind hoch.',
    'Was ist für die Mieter wichtig?',
    'Sie sollen alle Papiere dabei haben. Und sie müssen schnell sein.',
    'Haben Familien mit Kindern Probleme?',
    'Ja, oft. Viele Vermieter suchen lieber ruhige Mieter. Das finde ich schade.',
    'Was raten Sie bei einer Besichtigung?',
    'Kommen Sie pünktlich und seien Sie freundlich. Das ist sehr wichtig.',
    'Wird es in Zukunft besser?',
    'Ich glaube nicht so schnell. Man baut zu wenige neue Wohnungen.'],
   [('Es gibt heute wenige Wohnungen und hohe Mieten.','ja'),
    ('Mieter sollen ihre Papiere zu Hause lassen.','nein'),
    ('Familien mit Kindern haben oft Probleme.','ja'),
    ('Bei einer Besichtigung soll man pünktlich und freundlich sein.','ja'),
    ('Frau Lange glaubt, der Markt wird schnell besser.','nein')]),

 'ai-91': ('Reporter','m','Roth','f',[
    'Frau Roth, warum ist die Apotheke vor Ort wichtig?',
    'Weil wir die Kunden beraten. Im Internet bekommt man keinen Rat.',
    'Kommen die Leute auch ohne Arzt zu Ihnen?',
    'Ja, oft. Bei einer leichten Erkältung kann ich gut helfen.',
    'Und bei starken Schmerzen?',
    'Dann schicke ich die Leute zum Arzt. Das ist sicherer.',
    'Nehmen die Menschen zu viele Tabletten?',
    'Manche schon. Oft helfen auch Ruhe, Schlaf und viel Wasser.',
    'Was ist bei Tabletten wichtig?',
    'Lesen Sie immer den Zettel. Und nehmen Sie nicht mehr als erlaubt.'],
   [('Frau Roth findet die Beratung in der Apotheke wichtig.','ja'),
    ('Bei starken Schmerzen schickt sie die Leute zum Arzt.','ja'),
    ('Sie sagt, man soll bei jeder Kleinigkeit eine Tablette nehmen.','nein'),
    ('Oft helfen auch Ruhe, Schlaf und Wasser.','ja'),
    ('Sie findet, man muss den Zettel im Medikament nicht lesen.','nein')]),

 'ai-83': ('Reporter','m','Klein','f',[
    'Frau Dr. Klein, warum kommen die Patienten zu Ihnen?',
    'Viele junge Leute kommen wegen Pickeln. Andere haben Probleme mit der Sonne.',
    'Ist Bräune gesund?',
    'Nein, das ist ein Irrtum. Jeder Sonnenbrand schadet der Haut.',
    'Wie wichtig ist der Schutz vor der Sonne?',
    'Sehr wichtig. Bitte benutzen Sie eine Creme, auch im Frühling.',
    'Helfen teure Cremes besser?',
    'Nicht immer. Eine einfache Creme ist oft genauso gut.',
    'Was raten Sie für eine gesunde Haut?',
    'Trinken Sie viel Wasser, essen Sie gesund und schlafen Sie genug.'],
   [('Frau Dr. Klein findet, Bräune ist gesund.','nein'),
    ('Viele junge Leute kommen wegen Pickeln.','ja'),
    ('Sie sagt, jeder Sonnenbrand schadet der Haut.','ja'),
    ('Teure Cremes sind immer besser.','nein'),
    ('Sie rät, viel Wasser zu trinken und gesund zu essen.','ja')]),

 'ai-99': ('Reporter','m','Stark','f',[
    'Frau Stark, warum haben Sie das Sprachcafé gemacht?',
    'Beim Sprachenlernen muss man reden. Ich wollte einen Ort ohne Druck und ohne Prüfung.',
    'Wer kommt zu Ihnen?',
    'Menschen aus vielen Ländern. Manche lernen Deutsch, andere Englisch oder Spanisch.',
    'Was ist der größte Vorteil?',
    'Die Leute verlieren die Angst zu reden. Und sie finden neue Freunde.',
    'Hilft das auch beim Einleben?',
    'Ja, sehr. Wer die Sprache spricht, findet leichter Arbeit und Freunde.',
    'Was raten Sie beim Sprachenlernen?',
    'Reden Sie viel und haben Sie keine Angst vor Fehlern. Bleiben Sie dran.'],
   [('Frau Stark wollte einen Ort zum Üben ohne Druck.','ja'),
    ('Ins Sprachcafé kommen nur Studenten.','nein'),
    ('Viele Gäste verlieren dort die Angst zu reden.','ja'),
    ('Wer die Sprache spricht, findet leichter Arbeit.','ja'),
    ('Sie rät, aus Angst vor Fehlern lieber zu schweigen.','nein')]),

 'ai-1': ('Reporter','m','Bauer','m',[
    'Herr Bauer, was sind Ihre Aufgaben als Schaffner?',
    'Ich kontrolliere die Tickets und helfe den Fahrgästen. Ich gebe auch Auskunft.',
    'Was fragen die Leute am häufigsten?',
    'Wo sie umsteigen müssen und wann der Zug ankommt. Viele fragen nach dem Weg.',
    'Ist der Zug oft zu spät?',
    'Manchmal leider ja. Bei schlechtem Wetter gibt es oft Verspätungen.',
    'Macht Ihnen die Arbeit Spaß?',
    'Ja, sehr. Ich treffe jeden Tag neue Menschen. Das gefällt mir.',
    'Was wünschen Sie sich von den Fahrgästen?',
    'Etwas mehr Geduld bei Verspätungen. Wir können nichts dafür.'],
   [('Herr Bauer findet seine Arbeit langweilig.','nein'),
    ('Er kontrolliert die Tickets und hilft den Fahrgästen.','ja'),
    ('Bei schlechtem Wetter gibt es oft Verspätungen.','ja'),
    ('Die Fahrgäste fragen nie nach dem Weg.','nein'),
    ('Er wünscht sich mehr Geduld von den Fahrgästen.','ja')]),

 'ai-100': ('Reporter','m','Wagner','f',[
    'Frau Wagner, was bedeutet dieser Tag für die Schüler?',
    'Es ist ein großer Tag. Sie haben viele Jahre gelernt. Jetzt beginnt etwas Neues.',
    'Sind die jungen Leute unsicher wegen der Zukunft?',
    'Manche schon. Ich sage ihnen: Ihr müsst nicht heute schon alles wissen.',
    'Müssen alle studieren?',
    'Nein. Eine Ausbildung ist genauso gut. Wir brauchen auch Handwerker und Pfleger.',
    'Was geben Sie den Schülern mit?',
    'Lernt weiter, euer ganzes Leben lang. Bleibt neugierig und helft einander.',
    'Was wünschen Sie sich für die Schüler?',
    'Dass sie glücklich werden und einen Beruf finden, der ihnen gefällt.'],
   [('Frau Wagner sagt, die Schüler müssen heute schon alles wissen.','nein'),
    ('Für sie ist dieser Tag ein großer Tag.','ja'),
    ('Sie findet, eine Ausbildung ist genauso gut wie ein Studium.','ja'),
    ('Sie rät den Schülern, nach der Schule nicht mehr zu lernen.','nein'),
    ('Sie wünscht sich, dass die Schüler glücklich werden.','ja')]),

 'ai-68': ('Reporter','m','Becker','f',[
    'Frau Becker, wie viele Essen kochen Sie am Tag?',
    'Etwa achthundert. Wir fangen früh am Morgen an, damit alles um zwölf fertig ist.',
    'Hat sich das Essen verändert?',
    'Ja. Früher wollten alle Fleisch. Heute essen viele lieber vegetarisch.',
    'Was ist für Sie am schwersten?',
    'Es allen recht zu machen. Jeder mag etwas anderes.',
    'Was machen Sie mit den Resten?',
    'Wir werfen sie nicht weg. Wir geben das Essen an arme Menschen.',
    'Was wünschen Sie sich von den Gästen?',
    'Dass sie uns sagen, was gut war und was nicht. Kritik hilft uns.'],
   [('Die Kantine kocht etwa achthundert Essen am Tag.','ja'),
    ('Heute wollen alle Gäste jeden Tag Fleisch.','nein'),
    ('Frau Becker findet es schwer, es allen recht zu machen.','ja'),
    ('Die Reste werden weggeworfen.','nein'),
    ('Sie möchte von den Gästen wissen, was gut war.','ja')]),

 'ai-73': ('Reporter','m','Wagner','f',[
    'Frau Wagner, wie viele Tiere leben hier?',
    'Im Moment etwa zweihundert. Im Sommer werden es leider mehr.',
    'Warum mehr im Sommer?',
    'Viele Leute fahren in den Urlaub und geben ihr Tier ab. Das ist traurig.',
    'Wie bekommen Sie Geld?',
    'Vor allem durch Spenden. Die Stadt gibt nur wenig. Viele Helfer arbeiten gratis.',
    'Worauf achten Sie bei einer Adoption?',
    'Dass das Tier zur Familie passt. Ein großer Hund braucht viel Platz.',
    'Was möchten Sie den Menschen sagen?',
    'Überlegen Sie gut, bevor Sie ein Tier nehmen. Ein Tier ist kein Spielzeug.'],
   [('Im Sommer kommen weniger Tiere ins Heim.','nein'),
    ('Das Tierheim bekommt das meiste Geld durch Spenden.','ja'),
    ('Bei einer Adoption soll das Tier zur Familie passen.','ja'),
    ('Frau Wagner findet, ein Tier ist ein Spielzeug.','nein'),
    ('Sie rät, vor der Anschaffung gut zu überlegen.','ja')]),

 'ai-70': ('Reporter','m','Richter','f',[
    'Frau Richter, welche Versicherung braucht man wirklich?',
    'Nicht so viele. Wichtig ist eine Versicherung für Schäden. Sie kostet wenig und hilft viel.',
    'Haben die Leute oft zu viele Versicherungen?',
    'Ja, leider. Manche haben fünf oder sechs. Viele brauchen sie gar nicht.',
    'Was ist der häufigste Fehler?',
    'Die Leute lesen den Vertrag nicht. Dann sind sie überrascht.',
    'Soll man die Versicherung oft wechseln?',
    'Nicht jedes Jahr. Aber man soll die Preise ab und zu vergleichen.',
    'Was raten Sie jungen Leuten?',
    'Fangen Sie einfach an und denken Sie früh an später. Aber kaufen Sie nicht zu viel.'],
   [('Frau Richter findet eine Versicherung für Schäden wichtig.','ja'),
    ('Sie meint, viele Leute haben zu viele Versicherungen.','ja'),
    ('Sie sagt, man soll den Vertrag nicht lesen.','nein'),
    ('Sie rät, die Preise ab und zu zu vergleichen.','ja'),
    ('Sie meint, junge Leute sollen so viel wie möglich kaufen.','nein')]),

 'ai-64': ('Reporter','m','Sommer','f',[
    'Frau Sommer, warum geht man noch ins Reisebüro?',
    'Wegen der Beratung. Im Internet ist man allein. Bei uns hilft ein Mensch.',
    'Welche Reiseziele sind beliebt?',
    'Spanien und Italien immer. Aber auch ferne Länder wie Thailand kommen wieder.',
    'Was ist der häufigste Fehler?',
    'Die Leute buchen zu spät. Dann ist alles teuer. Wer früh bucht, spart Geld.',
    'Reisen Sie selbst gern?',
    'Ja, sehr. Am liebsten dorthin, wo wenige Touristen sind.',
    'Was raten Sie für die nächste Reise?',
    'Probieren Sie etwas Neues. Und nehmen Sie nicht zu viel Gepäck mit.'],
   [('Frau Sommer findet, man soll möglichst spät buchen.','nein'),
    ('Im Reisebüro bekommt man eine persönliche Beratung.','ja'),
    ('Wer früh bucht, spart Geld.','ja'),
    ('Sie reist am liebsten dort, wo viele Touristen sind.','nein'),
    ('Sie rät, nicht zu viel Gepäck mitzunehmen.','ja')]),

 'ai-98': ('Reporter','m','Adler','f',[
    'Frau Adler, warum kommen die Menschen ins Wellnesshotel?',
    'Vor allem, um sich zu erholen. Viele arbeiten zu viel und sind müde.',
    'Sind solche Hotels sehr teuer?',
    'Nicht alle. Unter der Woche gibt es oft günstige Angebote.',
    'Was ist bei den Gästen am beliebtesten?',
    'Die Massagen. Danach kommen Sauna und Pool. Auch Yoga mögen viele.',
    'Kommen auch Firmen zu Ihnen?',
    'Ja, immer mehr. Sie schicken ihre Mitarbeiter zur Erholung.',
    'Was raten Sie gestressten Menschen?',
    'Nehmen Sie sich auch zu Hause Zeit für sich. Ein Bad oder ein Spaziergang hilft schon.'],
   [('Frau Adler sagt, Wellnesshotels sind immer sehr teuer.','nein'),
    ('Die meisten Gäste kommen, um sich zu erholen.','ja'),
    ('Massagen sind bei den Gästen am beliebtesten.','ja'),
    ('Sie meint, Erholung gibt es nur im teuren Hotel.','nein'),
    ('Immer mehr Firmen schicken ihre Mitarbeiter zur Erholung.','ja')]),

 'ai-79': ('Reporterin','f','Roth','m',[
    'Herr Roth, heute hat jeder eine Kamera im Handy. Braucht man noch einen Fotografen?',
    'Ja, finde ich. Ein gutes Foto ist mehr als ein schnelles Bild.',
    'Was ist das Schwierigste an Ihrer Arbeit?',
    'Die Menschen zum Lächeln zu bringen. Viele sind vor der Kamera nervös.',
    'Welche Aufträge mögen Sie am liebsten?',
    'Hochzeiten. Es ist der schönste Tag, und ich darf ihn festhalten.',
    'Ändern Sie die Fotos viel am Computer?',
    'Nur ein bisschen. Die Menschen sollen echt aussehen, nicht wie in der Werbung.',
    'Was raten Sie Hobby-Fotografen?',
    'Achten Sie auf das Licht. Und machen Sie viele Bilder, dann ist ein gutes dabei.'],
   [('Herr Roth ändert seine Fotos sehr stark am Computer.','nein'),
    ('Er findet, ein gutes Foto ist mehr als ein schnelles Bild.','ja'),
    ('Viele Menschen sind vor der Kamera nervös.','ja'),
    ('Er fotografiert am liebsten bei Hochzeiten.','ja'),
    ('Er rät Hobby-Fotografen, nicht auf das Licht zu achten.','nein')]),

 'ai-86': ('Reporterin','f','Krämer','m',[
    'Herr Krämer, mit welchem Problem kommen die Leute am häufigsten?',
    'Mit dem Rücken. Wir sitzen einfach zu viel, im Büro und im Auto.',
    'Wie wichtig ist die Mithilfe der Patienten?',
    'Sehr wichtig. Sie müssen die Übungen auch zu Hause machen.',
    'Kann man Rückenschmerzen vermeiden?',
    'Ja. Stehen Sie öfter auf, bewegen Sie sich und machen Sie Sport. Schwimmen ist gut.',
    'Sind die Geräte besser als Ihre Hände?',
    'Nein. Meine Hände bleiben das wichtigste Werkzeug. Ich spüre, wo das Problem ist.',
    'Was raten Sie den Menschen?',
    'Bleiben Sie aktiv. Haben Sie keine Angst vor Bewegung.'],
   [('Herr Krämer findet, die Übungen zu Hause sind nicht wichtig.','nein'),
    ('Die meisten Patienten kommen mit Rückenproblemen.','ja'),
    ('Er sagt, man kann Rückenschmerzen vermeiden.','ja'),
    ('Für ihn sind die Geräte besser als seine Hände.','nein'),
    ('Er rät, aktiv zu bleiben.','ja')]),

 'ai-97': ('Reporter','m','Yilmaz','f',[
    'Frau Yilmaz, wie hat sich Ihre Arbeit verändert?',
    'Früher kauften die Leute oft neu. Jetzt lassen sie Kleidung wieder reparieren.',
    'Was sind die häufigsten Aufträge?',
    'Hosen kürzen, das mache ich jeden Tag. Auch Reißverschlüsse wechseln.',
    'Lohnt sich das Reparieren immer?',
    'Nicht immer. Bei billiger Kleidung ist es manchmal zu teuer. Bei guter lohnt es sich.',
    'Können junge Leute noch nähen?',
    'Leider immer weniger. Manche kommen nur, um einen Knopf annähen zu lassen.',
    'Was wünschen Sie sich?',
    'Dass die Menschen Kleidung wieder mehr schätzen. Reparieren ist gut für die Umwelt.'],
   [('Heute lassen die Leute Kleidung wieder mehr reparieren.','ja'),
    ('Hosen kürzen ist ein häufiger Auftrag.','ja'),
    ('Frau Yilmaz sagt, das Reparieren lohnt sich immer.','nein'),
    ('Immer weniger junge Leute können nähen.','ja'),
    ('Sie findet Reparieren schlecht für die Umwelt.','nein')]),

 'ai-96': ('Reporter','m','Blum','f',[
    'Frau Blum, wann haben Sie am meisten zu tun?',
    'Am Valentinstag, am Muttertag und an Weihnachten. Dann ist sehr viel los.',
    'Was soll man beim Blumenkauf beachten?',
    'Kaufen Sie Blumen der Jahreszeit. Sie sind frischer und halten länger.',
    'Verschenken Männer und Frauen andere Blumen?',
    'Ein bisschen. Männer kaufen oft rote Rosen, Frauen lieber bunte Sträuße.',
    'Ist Ihr Beruf anstrengend?',
    'Ja, schon. Ich stehe früh auf und trage schwere Eimer mit Wasser.',
    'Was ist das Schönste an Ihrem Beruf?',
    'Ich mache die Menschen glücklich. Mit Blumen kann man Danke sagen.'],
   [('Frau Blum sagt, ihr Beruf ist gar nicht anstrengend.','nein'),
    ('Am Muttertag hat sie besonders viel zu tun.','ja'),
    ('Sie rät, Blumen der Jahreszeit zu kaufen.','ja'),
    ('Männer kaufen oft rote Rosen.','ja'),
    ('Sie findet ihren Beruf nicht schön.','nein')]),

 'ai-92': ('Reporterin','f','Conti','m',[
    'Herr Conti, was ist Ihr Geheimnis beim Eis?',
    'Gute, frische Zutaten. Echte Früchte und echte Milch. Das schmeckt man.',
    'Welche Sorte verkaufen Sie am meisten?',
    'Schokolade und Vanille. Aber die Leute probieren auch neue Sorten.',
    'Ist es ein hartes Geschäft?',
    'Ja, sehr. Wir hängen vom Wetter ab. Ein nasser Sommer ist schlecht für uns.',
    'Essen die Leute viel Eis?',
    'Oh ja, vor allem im Sommer. Eis macht einfach glücklich.',
    'Was lieben Sie an Ihrem Beruf?',
    'Die glücklichen Gesichter. Ein Kind mit einem Eis lacht über das ganze Gesicht.'],
   [('Herr Conti sagt, das Eisgeschäft ist nicht vom Wetter abhängig.','nein'),
    ('Er nimmt frische Zutaten wie echte Früchte.','ja'),
    ('Schokolade und Vanille verkauft er am meisten.','ja'),
    ('Im Sommer essen die Leute viel Eis.','ja'),
    ('Er findet seinen Beruf nicht schön.','nein')]),

 'ai-62': ('Reporter','m','Hofer','f',[
    'Frau Hofer, was verkaufen Sie auf dem Markt?',
    'Alles von meinem Hof. Gemüse, Salate und im Sommer auch Beeren.',
    'Wie sieht Ihr Tag aus?',
    'Sehr früh. Ich stehe um vier Uhr auf und fahre in die Stadt.',
    'Warum kaufen die Leute bei Ihnen?',
    'Wegen der Frische. Mein Gemüse ist von gestern, nicht von letzter Woche.',
    'Ist es schwer, von einem kleinen Hof zu leben?',
    'Ja, das ist es. Ohne den Markt würden wir es nicht schaffen.',
    'Was wünschen Sie sich für die Zukunft?',
    'Dass mehr junge Leute wieder auf dem Markt einkaufen.'],
   [('Frau Hofer steht erst um sieben Uhr auf.','nein'),
    ('Sie verkauft nur Sachen von ihrem eigenen Hof.','ja'),
    ('Die Leute kaufen bei ihr wegen der Frische.','ja'),
    ('Ohne den Markt könnte ihr Hof gut leben.','nein'),
    ('Sie wünscht sich mehr junge Kunden auf dem Markt.','ja')]),

 'ai-88': ('Reporterin','f','Lang','m',[
    'Herr Lang, warum kaufen die Leute gern im Internet?',
    'Weil es bequem ist. Man kann zu jeder Zeit bestellen, auch nachts.',
    'Schicken die Leute viel zurück?',
    'Ja, sehr viel, vor allem Kleidung. Das ist schlecht für die Umwelt.',
    'Schadet das Online-Shopping den Geschäften?',
    'Leider ja. Viele kleine Läden haben Probleme. Das ist schade.',
    'Worauf soll man beim Bestellen achten?',
    'Lesen Sie die Beschreibung genau und schauen Sie auf die Größe.',
    'Was raten Sie noch?',
    'Bestellen Sie nicht zu viel auf einmal. Dann müssen Sie weniger zurückschicken.'],
   [('Herr Lang findet viele Rücksendungen kein Problem.','nein'),
    ('Online-Shopping ist bequem, weil man immer bestellen kann.','ja'),
    ('Er sagt, kleine Läden haben durch das Internet Probleme.','ja'),
    ('Er rät, die Größe vor dem Bestellen zu prüfen.','ja'),
    ('Er meint, man soll möglichst viel auf einmal bestellen.','nein')]),

 'ai-87': ('Reporter','m','Berg','f',[
    'Frau Berg, hat sich das Spielzeug verändert?',
    'Ja, sehr. Früher gab es einfaches Holzspielzeug. Heute hat alles Elektronik.',
    'Was kaufen die Leute am häufigsten?',
    'Vor Weihnachten ist am meisten los. Beliebt sind Baukästen und Brettspiele.',
    'Worauf achten Sie bei Ihrem Spielzeug?',
    'Auf gute Qualität und Sicherheit. Billiges Spielzeug geht schnell kaputt.',
    'Geben die Eltern zu viel Geld aus?',
    'Manchmal ja. Kinder brauchen nicht so viel. Wenige gute Sachen sind besser.',
    'Was ist das Schönste an Ihrem Beruf?',
    'Die glücklichen Kinder. Wenn ein Kind staunt, freue ich mich.'],
   [('Heute hat das Spielzeug oft Elektronik.','ja'),
    ('Vor Weihnachten ist am meisten los.','ja'),
    ('Frau Berg achtet nicht auf Qualität und Sicherheit.','nein'),
    ('Sie sagt, wenige gute Sachen sind besser als viele.','ja'),
    ('Sie findet die glücklichen Kinder nicht wichtig.','nein')]),

 'ai-60': ('Reporter','m','Walter','f',[
    'Frau Walter, was sind Ihre Aufgaben im Park?',
    'Ich kümmere mich um die Pflanzen und die Wege. Viele Gärtner arbeiten bei mir.',
    'Wie viele Besucher kommen?',
    'Im Sommer sehr viele, im Winter weniger. Unser Park ist sehr beliebt.',
    'Was sind die Probleme?',
    'Der Müll. Manche Leute werfen alles auf den Boden. Das ärgert mich.',
    'Welche Feste gibt es im Park?',
    'Im Sommer ein großes Fest mit Musik. Auch ein Lauf geht durch den Park.',
    'Wie sehen Sie die Zukunft?',
    'Parks werden immer wichtiger. Wir pflanzen jedes Jahr mehr Bäume.'],
   [('Im Sommer und Winter kommen gleich viele Besucher.','nein'),
    ('Frau Walter kümmert sich um Pflanzen und Wege.','ja'),
    ('Müll ist ein Problem im Park.','ja'),
    ('Sie findet, Parks werden in Zukunft weniger wichtig.','nein'),
    ('Im Park gibt es im Sommer ein großes Fest.','ja')]),

 'ai-95': ('Reporter','m','Kraus','f',[
    'Frau Kraus, was machen Sie genau?',
    'Ich pflege das Fell von Hunden und Katzen. Ich wasche, schneide und bürste sie.',
    'Ist die Arbeit mit den Tieren schwer?',
    'Manchmal. Viele Tiere haben Angst. Ich brauche viel Geduld und Ruhe.',
    'Sollen die Besitzer das Fell selbst pflegen?',
    'Das Bürsten ja. Aber das Schneiden ist schwer. Dafür kommen Sie besser zu mir.',
    'Wollen die Leute manchmal seltsame Sachen?',
    'Ja. Manche wollen den Hund bunt färben. Das mache ich nicht. Ein Tier ist kein Spielzeug.',
    'Was lieben Sie an Ihrem Beruf?',
    'Ich liebe Tiere. Aus einem traurigen Tier wird ein glückliches.'],
   [('Frau Kraus wäscht, schneidet und bürstet die Tiere.','ja'),
    ('Sie sagt, man kann mit ängstlichen Tieren hektisch sein.','nein'),
    ('Das Bürsten sollen die Besitzer selbst machen.','ja'),
    ('Sie färbt Hunde gern bunt.','nein'),
    ('Sie arbeitet gern mit Tieren.','ja')]),

 'ai-67': ('Reporter','m','Vogel','f',[
    'Frau Vogel, wie sieht Ihr Tag aus?',
    'Ich fange früh an, um sechs Uhr. Erst füttere ich die Tiere, dann mache ich sauber.',
    'Welche Tiere betreuen Sie?',
    'Vor allem die Affen. Sie sind sehr klug. Ich kenne alle mit Namen.',
    'Ist die Arbeit gefährlich?',
    'Bei manchen Tieren ja. Zu den großen Affen gehe ich nie allein.',
    'Was wünschen Sie sich von den Besuchern?',
    'Bitte füttern Sie die Tiere nicht. Falsches Essen macht sie krank. Und seien Sie leise.',
    'Warum sind Zoos wichtig?',
    'Wir schützen Tiere, die es bald nicht mehr gibt. Und Kinder lernen viel über Tiere.'],
   [('Frau Vogel kennt ihre Affen alle mit Namen.','ja'),
    ('Sie geht allein zu den großen Affen.','nein'),
    ('Sie fängt früh am Morgen mit der Arbeit an.','ja'),
    ('Sie findet es gut, wenn Besucher die Tiere füttern.','nein'),
    ('Zoos schützen Tiere, die es bald nicht mehr gibt.','ja')]),

 'ai-65': ('Reporterin','f','Krause','m',[
    'Herr Krause, was wünschen sich die Kunden heute?',
    'Die meisten wollen einfache Geräte, die sofort funktionieren. Nicht kompliziert.',
    'Kaufen die Leute lieber teuer oder günstig?',
    'Das ist gemischt. Beim Handy geben viele viel Geld aus, bei Kabeln wollen sie sparen.',
    'Was ist der häufigste Fehler?',
    'Die Leute kaufen zu viel. Geräte mit vielen Funktionen, die sie nie nutzen.',
    'Wie ist es mit dem Online-Handel?',
    'Online ist oft billiger. Aber bei uns kann man die Geräte anfassen und fragen.',
    'Was raten Sie den Kunden?',
    'Überlegen Sie, was Sie wirklich brauchen. Und werfen Sie alte Geräte nicht weg.'],
   [('Die meisten Kunden wollen heute einfache Geräte.','ja'),
    ('Beim Handy sparen die Leute am meisten.','nein'),
    ('Herr Krause sagt, viele Leute kaufen zu viel.','ja'),
    ('Im Geschäft kann man die Geräte anfassen.','ja'),
    ('Er rät, alte Geräte einfach wegzuwerfen.','nein')]),

 'ai-85': ('Reporter','m','Hofmann','f',[
    'Frau Hofmann, ab welchem Alter sollen Kinder ein Instrument lernen?',
    'Mit sechs oder sieben Jahren ist ein guter Start. Aber das Kind muss Lust haben.',
    'Wie wichtig ist das Üben?',
    'Sehr wichtig. Besser jeden Tag fünfzehn Minuten als einmal in der Woche lang.',
    'Lernen auch Erwachsene bei Ihnen?',
    'Ja, immer mehr. Man ist nie zu alt für Musik.',
    'Ist Musik gut für Kinder?',
    'Ja, sehr. Sie hilft beim Lernen und macht glücklich.',
    'Was raten Sie Eltern, wenn ein Kind aufhören will?',
    'Nicht gleich aufgeben. Vielleicht passt ein anderes Instrument besser.'],
   [('Frau Hofmann sagt, mit sechs oder sieben ist ein guter Start.','ja'),
    ('Sie meint, einmal pro Woche lang üben ist am besten.','nein'),
    ('Auch immer mehr Erwachsene lernen bei ihr.','ja'),
    ('Musik hilft Kindern beim Lernen.','ja'),
    ('Sie rät, sofort aufzugeben, wenn ein Kind aufhören will.','nein')]),
}


def num_path(tid):
    return TOOLS / f"_test{int(tid.split('-')[1])}_data.json"


def main():
    changed = 0
    for tid, (rl, rg, el, eg, texts, items) in DATA.items():
        p = num_path(tid)
        d = json.loads(p.read_text(encoding='utf-8'))
        t4 = d['teile'][3]
        lines = []
        for i, txt in enumerate(texts):
            if i % 2 == 0:
                lines.append({'speaker': rl, 'gender': rg, 'text': txt})
            else:
                lines.append({'speaker': el, 'gender': eg, 'text': txt})
        t4['transcript'] = lines
        t4['items'] = [{'q': q, 'correct': a} for q, a in items]
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        changed += 1
    print(f"Simplified Teil 4 in {changed} tests.")


if __name__ == '__main__':
    main()
