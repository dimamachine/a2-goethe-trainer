# Журнал проверки Hören T2 картинок (900 шт, 100 тем)

Правила: watermark/текст на картинке = REGEN; картинка соответствует ДРУГОЙ букве той же темы = SWAP (переименовать); не тот смысл = REGEN; не тот стиль (не flat-cartoon-white-bg) = REGEN.
Эталон: scratchpad/t2_expected.json (буква → текст опции) + tools/_image_concepts.json (текст → концепт).
Листы: scratchpad/sheets/NNN-slug.png. Свап делать НЕ сразу — копить в plan, применить после подтверждения структуры. REGEN-список → tools-совместимый формат "slug letter | prompt".

Статус: | # | slug | вердикт |
- 001 reisen-mit-der-bahn: REGEN b (текст «A2» на билетах), REGEN h (ожидался человек с собакой, а нарисована сервировка стола — дубль g; собаки в сете нет, свап невозможен). MINOR i (слово «BUCHEN» на кнопке — по смыслу ок).
- 002 wochenende-und-freizeit: OK все 9.
- 003 im-restaurant-und-cafe: OK. MINOR h (надписи «FANT»/«SAFT» на бутылках — по смыслу ок).
- 004 schule-und-sprachkurs: REGEN b (ожидалась «Wahrscheinlichkeit» — вероятность/кубики, а нарисован поднос со снеками = дубль c). d OK (концепт = «tidy study room», совпадает), f OK (концепт сам требует «drawn on paper»).
- 005 wohnen-und-umzug: OK. MINOR d («FRAGILE» на коробке), MINOR f («NEU!» ценник).
- 006 beim-arzt-und-in-der-apotheke: OK все 9 (тема wellness — подписи совпадают).
- 007 im-buero-und-arbeitsleben: REGEN d (ожидался DJ с пультом, а нарисован конверт = дубль e). SWAP h←i (текущая i = зал с накрытыми столами = концепт h «event hall»; текущая h — странная «книжка» — выбросить). REGEN i (ящик с бутылками напитков). MINOR b («ON» на камере).
- 008 urlaub-und-reisen-planen: SWAP e↔f (отель и стиральная машина перепутаны местами). Остальное OK.
- 016 kochen-und-essen: SWAP e↔f (мясо и букет перепутаны). MOVE d→g (чистый хлеб с d поставить на g «bringt Brot mit»; текущая g с ТЕКСТОМ «Goethe-Zertifikat A2 Hören (Modellsatz/Übungssatz)» — выбросить). REGEN d («dekoriert den Tisch» — украшенный стол). REGEN h («macht einen Salat» — нарисован хлеб, 3-й дубль хлеба; нужен салат). Остальное OK.
- 017 garten-und-pflanzen: SWAP a↔b (полив и удобрение перепутаны), SWAP c↔d (обрезка дерева и отдых в саду перепутаны), SWAP g↔h (посадка томатов и прополка перепутаны). Остальное OK.
- 018 internet-und-technik: SWAP a↔b (камера и наушники перепутаны), SWAP c↔d (e-reader и планшет перепутаны). REGEN h («ein Laptop» — нарисован второй смартфон, дубль g; нужен ноутбук). MINOR e («12:45» на часах — уместно).
- 019 bank-und-geld: SWAP e↔i (счёт за электричество и банковские карты перепутаны). REGEN b («Online-Banking» — нарисована вторая продуктовая тележка, дубль a; нужен «online banking on a laptop screen»). REGEN h («zahlt die Miete» — нарисованы документы со щитом = дубль g-страховки; нужен «дом + наличные»). Остальное OK.
- 020 sprachen-lernen: OK все 9 (флаги).
- 021 auto-und-fahren: REGEN c («Kein Benzin mehr» — нарисован аккумулятор с проводами, почти дубль d; нужна пустая канистра/датчик топлива на нуле). SWAP e↔f (замок двери и тормозной диск перепутаны). Остальное OK.
- 022 kleidung-und-mode: SWAP a↔b (деньги в конверте и spa-сертификат перепутаны), SWAP c↔d (вино и кулинарная книга перепутаны), SWAP g↔h (фотоальбом и дорожная сумка перепутаны). Остальное OK.
- 023 wetter-und-jahreszeiten: OK все 9.
- 024 kinder-und-erziehung: SWAP b↔c (балет и верховая езда перепутаны). REGEN f («Fußball im Verein» — нарисован ребёнок с гигантским смартфоном). REGEN g («malt und zeichnet» — фотореалистичная игрушка, брак Grok; нужен рисующий ребёнок). MINOR e (каракули на учебнике).
- 025 bibliothek-und-lesen: MOVE d→e (романтика на скамейке = Liebesromane; текущая e — тревел-бук с ТЕКСТОМ «Goethe-Zertifikat A2 Hören…» — выбросить). REGEN d («Reiseberichte» — чистая книга-путешествий с картой). SWAP f↔g (кулинарная книга и биографии перепутаны; «BIOGRAFIE» на обложке — уместно, minor). MOVE i→h (страница комикса = Comics und Manga; текущая h — макет экзаменационной страницы Hören с A/B/C — выбросить). REGEN i («Krimis» — детектив/лупа). 
- 026 friseur-und-schoenheit: SWAP g↔h (сауна и маска для лица перепутаны). REGEN i («Maniküre» — нарисован массаж спины, дубль e; нужны руки с накрашенными ногтями). Остальное OK.
- 027 hotel-und-uebernachten: REGEN a, b, e, f, i — на всех ТЕКСТ «Goethe-Zertifikat A2 Hören…» (a Pension, e Ferienwohnung, f Camping, i bei Verwandten — сцены верные, но текст; b Bauernhof — ещё и контент неверный: дом с вывеской «Pension» вместо фермы с амбаром и животными). d (автобус у отеля) — ок по концепту. c, g, h OK.
- 028 post-und-pakete: REGEN b («Werbeprospekt» — нарисована вторая открытка, дубль a; нужен рекламный буклет). SWAP c↔d (подарок и кредитка перепутаны). SWAP e↔f (счёт и заказанная книга перепутаны; «SUMME/BEZAHLT» на счёте — уместно). MOVE h→g (сцена с «EILT!»-письмом = Mahnung; текущая g — свадебная открытка с ТЕКСТОМ «Goethe-Zertifikat…» — выбросить) + REGEN h (чистая свадебная открытка). MINOR i («FRAGILE»).
- 029 vereine-und-hobbys: REGEN a (Theaterverein — сцена верная, но ТЕКСТ «Goethe-Zertifikat…» сверху). REGEN b (Tanzverein — нарисован второй театр + ТЕКСТ; нужны танцующие пары). MOVE c→d (фотографы с камерами = Foto-Club; текущая d — музыкальная группа с ТЕКСТОМ — выбросить) + REGEN c (Musikverein — оркестр/группа без текста). SWAP g↔h (хор и футбол перепутаны). e, f, i OK.
- 030 behoerden-und-dokumente: MOVE a→b (сцена «бюро находок/заявление о пропаже» подходит к Polizei—Verlustanzeige; текущая b с ТЕКСТОМ «Goethe-Zertifikat A2 Hören» — выбросить) + REGEN a (TÜV — осмотр машины). SWAP e↔f (суд и Bürgeramt перепутаны). REGEN h («Krankenkasse» — фотореалистичный металлический предмет, брак). c, d, g, i OK.
- 031 beim-zahnarzt: SWAP a↔c (отбеливание и коронка перепутаны). REGEN f («Karies-Behandlung/Plombe» — фотореалистичная МАШИНА, брак Grok). Остальное OK (i брекеты — стиль чуть реалистичнее, но приемлемо).
- 032 im-schwimmbad: REGEN b («trinkt etwas im Café» — вторая горка, дубль a; нужно кафе у бассейна). REGEN e («Aqua-Fitness» — фотореалистичный чёрный предмет, брак). REGEN h («Sprungbrett» — человек просто плывёт по дорожкам, дубль g; нужен прыжок с трамплина). Остальное OK.
- 033 camping-und-wandern: REGEN b (сцена готовки верная, но ТЕКСТ «Goethe-Zertifikat A2…»). SWAP c↔d (гриль-дрова и игры-книги перепутаны). MOVE h→g (карта маршрута = Wanderpläne; текущая g — коврики с ТЕКСТОМ — выбросить) + REGEN h (спальники и коврики без текста). Остальное OK.
- 034 im-krankenhaus: SWAP c↔g (рентген лёгких = Lungenentzündung, забинтованное колено = Knie). REGEN i (сцена контроля верная, но ТЕКСТ «Goethe-Zertifikat A2 Hören»). Остальное OK.
- 035 moebel-und-einrichtung: MOVE b→a (садовые стулья = Outdoor-Stühle; текущая a — письменный стол с ТЕКСТОМ — выбросить) + REGEN b (Schreibtisch без текста). REGEN d («Bett» — нарисован второй диван, дубль c; нужна кровать). SWAP e↔f (шкаф и обеденный стол перепутаны). REGEN h («Kommode» — нарисован зеркальный шкафчик, дубль g; нужен комод с ящиками). c, g, i OK.
- 036 studium-und-universitaet: OK все 9. MINOR b (цветная полоса-артефакт сверху).
- 037 bewerbung-und-job-suchen: SWAP a↔c (учительница и программист перепутаны). Остальное OK.
- 038 babys-und-kleinkinder: REGEN d («Puppen» — нарисован плюшевый мишка с лейкой, дубль темы c; нужны куклы). REGEN f («Bücher» — динозавры пьют чай + ТЕКСТ «Goethe-Zertifikat…»; нужны детские книги). MOVE g→h (гитара+труба = Musik; текущая h — фотореалистичный чёрный предмет — выбросить) + REGEN g («Malen» — рисующий ребёнок). REGEN i (игрушечные машинки — сцена верная, но ТЕКСТ «Goethe-Zertifikat…»). a, b, c, e OK.
- 039 am-flughafen: SWAP a↔b (Вена и Рим перепутаны). REGEN i («Madrid» — дворец верный, но ТЕКСТ «Goethe-Zertifikat…»). Остальное OK.
- 040 sommer-und-strand: REGEN a («Kajak» — нарисован второй сноркелинг, дубль c; нужна байдарка). ROTATE d→f (акваланг = Tauchen), f→e (парусник = Segeln), e→d (замок из песка = Sandburgen). REGEN i («Surfen» — второй пляжный волейбол, дубль g; нужен сёрфер). Остальное OK.
- 041 winter-und-skifahren: SWAP b↔c (прыжки с трамплина и коньки перепутаны). MOVE d→e (сноубордист = Snowboarden; текущая e — фотореалистичная чёрная маска — выбросить) + REGEN d («Ski fahren» — горнолыжник). SWAP g↔i (ледолазание и санки перепутаны). a, f, h OK.
- 042 geburtstag-und-geschenke: REGEN c («Geld» — нарисован мальчик с гигантским CD, дубль a; нужны деньги/купюры). Остальное OK.
- 043 reise-mit-dem-auto: REGEN f («Mercedes» — машина верная, но ТЕКСТ «Goethe-Zertifikat…»). MINOR d/e (обе синие седаны — визуально похожи, но допустимо). Остальное OK.
- 044 musik-und-konzerte: MOVE c→a (саксофонист = Jazz; текущая a — второй скрипичный оркестр, дубль b — выбросить) + REGEN c («Country» — банджо/ковбойская гитара). SWAP d↔e (микрофон с цепочкой = Hip-Hop, гитара с пальмовыми листьями = Reggae — перепутаны). SWAP h↔i (DJ-пульт = Elektro, аккордеон = Volksmusik — перепутаны). f, g OK.
- 045 im-museum: REGEN a (Sport — кубки верные, но ТЕКСТ). REGEN d («Naturkunde» — нарисована женщина с лейкой на холсте, не то). REGEN e («Moderne Kunst» — нарисован скелет динозавра (= Naturkunde) + ТЕКСТ). REGEN f («Musik» — фотореалистичная чёрная рамка, брак). REGEN h («Mode» — вторые пирамиды с маской, дубль g; нужна мода). REGEN i (Geschichte — витрины верные, но ТЕКСТ). Только b, c, g OK.
- 046 am-bahnhof (города): ROTATE e→c (Frauenkirche = München), c→d (Эльбфилармония/порт = Hamburg), d→e (небоскрёбы = Frankfurt). MOVE g→f (Бранденбургские ворота = Berlin; текущая f — Кёльнский собор, дубль h — выбросить). REGEN g («Dresden» — Frauenkirche/Semperoper). h (собор с краном = Köln) OK, a, b, i OK.
- 047 computer-und-probleme: REGEN b («Videos schneiden» — ТЕКСТ + не тот сюжет). REGEN c («App programmieren» — нарисован видеомонтаж + ТЕКСТ-баннер). MOVE d→e (рисунок с таймлайном = Animationen; текущая e — фоторедактор с ТЕКСТОМ — выбросить) + REGEN d («Fotos bearbeiten» без текста). REGEN h («E-Mails» — ТЕКСТ сверху). a, f, g, i OK.
- 048 im-supermarkt: SWAP a↔b (рыба и напитки). ROTATE d→f (мясо = Fleisch), e→d (сыр = Käse), f→e (десерт = Nachtisch). ROTATE g→h (вино = Wein), h→i (хлеб = Brot), i→g (овощи = Gemüse). Все картинки на месте, только перемешаны. c OK.
- 049 im-theater: REGEN a («Faust» — сцена ок, но ТЕКСТ). SWAP b↔c (кукольный театр = Kinderstück, кот с микрофоном = Musical Cats). MOVE d→e (балкон = Romeo und Julia; текущая e — фотореалистичный серый предмет — выбросить) + REGEN d (Comedy-Stück). SWAP g↔h (оперная певица и балерина перепутаны). REGEN i (детектив ок, но ТЕКСТ-баннер). f OK.
- 050 beim-tierarzt: SWAP a↔b (попугай и хомяк). REGEN d («Schildkröte» — фотореалистичная жуткая фигура, брак). MOVE h→i (кот = Katze), MOVE g→h (змея = Schlange), REGEN g («Fische» — текущая i-аквариум с ТЕКСТОМ — выбросить). c, e, f OK.
- 051 beim-augenarzt: ROTATE a→c (очки на книге = Lesebrille), c→b (спортивные очки = Sportbrille), b→a (глаз без очков = Keine Sehhilfe). ROTATE d→e (простые очки = Normale Brille), e→f (очки у монитора = Computer-Brille), f→d (двухзонные линзы = Bifokal). SWAP g↔h (лазерная операция и контактные линзы перепутаны). i OK.
- 010 einkaufen-und-geschaefte: SWAP c↔d (уборка и пирожные перепутаны). Остальное OK.
- 011 termine-und-telefon: OK. MINOR c («FORM» на документе; буквы на таблице у оптика i — уместны).
- 012 tiere-und-haustiere: REGEN f («kontrolliert die Wohnung und holt die Post» — вместо этого распаковка корма, дубль g; нужен концепт «проверяет квартиру/достаёт почту из ящика»). Остальное OK.
- 013 verkehr-und-stadt: OK все 9.
- 014 familienfeste: REGEN f (НА КАРТИНКЕ ТЕКСТ «Goethe-Zertifikat A2 Hören (Modellsatz, Übungssatz)» — утечка стиль-промпта; сцена подходит, но текст недопустим). REGEN i («spielt Musik» — фотореалистичный чёрный предмет, брак Grok; нужен «person playing guitar with speakers»). Остальное OK.
- 015 kino-theater-und-konzert: REGEN b («Filmfestival» — второй кинозал, дубль c; нужен clapperboard + red carpet). REGEN d («Tanz-Aufführung» — фотореалистичный чёрный аппарат, брак; нужны танцоры на сцене). REGEN e («Open-Air-Konzert» — нарисована галерея, дубль f; нужна уличная сцена с толпой). Остальное OK.
- 009 sport-und-fitness: REGEN c («Yoga» — сгенерирована фотореалистичная чёрная машина с буквой «P», полный брак Grok). SWAP g↔h (джоггинг и велосипед перепутаны). d (Pilates, поза воина на коврике) — ок, концепты yoga/pilates почти одинаковы. Остальное OK.

## 052 im-schwimmbad-und-sauna
- ROTATE a→c, b→a, c→b (на a — аква-фитнес с гантелями → c; на b — прыжок с вышки → a; на c — джакузи → b)
- MOVE e→d (на e — сцена массажа → d); REGEN e (Bahnen schwimmen; текущая d — бассейн с дорожками, но с ТЕКСТОМ «Goethe-Zertifikat A2 Hören» — выбросить)
- SWAP g↔i (на g — сауна с печкой → i; на i — детский лягушатник → g)
- f, h OK

## 053 familienfeier-und-hochzeit
- SWAP a↔b (на a — DJ за пультами → b; на b — женщина с тортом → a)
- MOVE d→c (на d — открытка-приглашение с шариками → c); REGEN d (Auto schmücken; текущая c — свадебная машина, но с ТЕКСТОМ «Goethe-Zertifikat A2 Hören (Modellsatz/Übungssatz)» — выбросить)
- SWAP e↔f (на e — оратор с микрофоном → f; на f — букет цветов → e)
- g, h, i OK

## 054 beim-optiker
- Цепочка: b→c (на b — спортивные очки-маска → Sportbrille), a→b (на a — красные очки → Rote farbige Brille), REGEN a (Runde Brille — круглые очки; текущая c — ФОТОРЕАЛ тёмный футляр, мусор — выбросить)
- ROTATE d→f, e→d, f→e (на d — чёрные роговые очки → f; на e — очки на книге → Lesebrille d; на f — тонкие безободковые очки → Randlose e)
- ROTATE g→h, h→i, i→g (на g — очки с двухзонными линзами → Bifokal h; на h — золотые очки в руках → Goldene i; на i — золотые авиаторы → Pilotenbrille g)

## 055 beim-fussball
- ROTATE a→b, b→c, c→a (на a — зелёно-белая = Werder → b; на b — сине-белая полосатая = Hertha → c; на c — жёлто-чёрная = Dortmund → a)
- d–i OK (Köln бело-красная, Schalke синяя, RB Leipzig красно-белая, HSV бело-синяя, Frankfurt чёрно-красная, Bayern красная)

## 056 beim-baecker
- SWAP a↔b (на a — чизкейк → Käsekuchen; на b — зерновой хлеб с семечками → Vollkornbrot)
- SWAP d↔f (на d — круассан → f; на f — яблочный штрудель → d)
- REGEN e (Berliner = пончик с начинкой БЕЗ дырки; на картинке кольцевой донат с дыркой — дублирует h)
- c, g, h, i OK

## 057 wohnungssuche-und-makler
- REGEN a (Bauernhaus: сцена правильная — ферма с трактором, но крупный ТЕКСТ «Goethe-Zertifikat A2 Hören» — выбросить)
- MOVE c→b (на c — семья на кухне + сад за дверью = Familie-Wohnung mit Garten); REGEN c (Haus zum Kaufen — дом с табличкой продажи; текущая b — ФОТОРЕАЛ тёмный мусор — выбросить)
- d, e, f OK (концепты почти неразличимы по ТЗ: single room / studio / one-room; все три сцены различны и уместны)
- MOVE h→g (на h — пентхаус с бассейном на крыше = Penthouse); REGEN h (Loft — индустриальный лофт; текущая g — лофт-сцена, но с ТЕКСТОМ — выбросить)
- i OK

## 058 beim-friseur-und-beauty
- Все 9 OK

## 059 beim-friseur-maenner
- SWAP b↔c (на b — пучок/Dutt → c; на c — синий ирокез → b)
- SWAP d↔e (на d — дреды → e; на e — длинные прямые волосы с пробором → d)
- ROTATE g→i, i→h, h→g (на g — undercut с фиолетовой чёлкой → i; на i — лысый бреет голову = Glatze → h; на h — короткий ёжик = Bürstenschnitt → g)
- a, f OK

## 060 im-park-und-erholung
- SWAP a↔b (на a — велосипедист → b; на b — тайцзи в фиолетовом костюме → a)
- MOVE d→e (на d — прогулка с собакой на поводке = Gassi gehen); MOVE f→d (на f — пикник на пледе = Picknick); REGEN f (Frisbee spielen; текущая e — фрисби, но с ТЕКСТОМ «Goethe-Zertifikat A2 Hören» — выбросить)
- REGEN i (Spazieren: на картинке женщина гуляет С СОБАКОЙ — дублирует e/Gassi gehen; нужна прогулка без собаки; концепт «a person taking a walk in a park»)
- c, g, h OK

## 061 im-fitnessstudio
- MOVE b→a (на b — скручивания на коврике = Pilates); MOVE c→b (на c — групповой танец = Zumba); REGEN c (Klettern; текущая a — скалодром, но с ТЕКСТОМ — выбросить)
- SWAP d↔e (на d — беговая дорожка → e; на e — пловец → d)
- ROTATE g→i, h→g, i→h (на g — боксёрская груша → Boxen i; на h — гантели = Krafttraining → g; на i — йога-поза дерева → Yoga h)
- f OK

## 062 auf-dem-wochenmarkt
- ROTATE c→e, e→d, d→c (на c — букет цветов → Blumen e; на e — мясная витрина → Fleisch und Wurst d; на d — сыр → Käse c)
- SWAP f↔g (на f — рыба на тарелке → Fisch g; на g — стол с овощами → Gemüse f)
- a, b, h, i OK

## 063 in-der-autowerkstatt
- ROTATE a→b, b→c, c→a (на a — разбитая фара → Licht b; на b — спущенное колесо → Platter Reifen c; на c — сломанные дворники в дождь → Scheibenwischer a)
- SWAP d↔e (на d — лужа масла под машиной → Verliert Öl e; на e — не заводится, открытый капот с красным X → Motor springt nicht an d)
- f, g, h, i OK

## 064 im-reisebuero
- SWAP a↔b (на a — сафари-джип со зверями → b; на b — круизный лайнер → a)
- ROTATE d→f, e→d, f→e (на d — лыжники → Skiurlaub f; на e — семья на велосипедах → Fahrradtour d; на f — спа-массаж → Wellness e)
- MOVE h→g (на h — турист с рюкзаком в горах = Wandern); REGEN h (Städtereise; текущая g — города/Эйфелева башня, но с ТЕКСТОМ «Goethe-Zertifikat A2 Hören» — выбросить)
- REGEN i (Strandurlaub: ФОТОРЕАЛ тёмные ночные горы, мусор — выбросить)
- c OK

## 065 im-elektronikgeschaeft
- SWAP a↔b (на a — смартфон → Handy b; на b — мальчик с приставкой и геймпадом → Spielekonsole a)
- c–i OK

## 066 handwerker-im-haus
- SWAP d↔e (на d — мойщик окон → e; на e — электрик с проводами → d)
- ROTATE g→h, h→i, i→g (на g — плиточник → Fliesenleger h; на h — пилит дерево = Tischler → i; на i — сантехник с трубами = Klempner → g)
- a, b, c, f OK

## 067 im-zoo
- MOVE a→c (на a — слон моет машинку = Elefanten); MOVE b→a (на b — попугаи купаются = Papageien); REGEN b (Tiger; текущая c — ФОТОРЕАЛ чёрный ящик, мусор — выбросить)
- REGEN g (Eisbären — ФОТОРЕАЛ чёрная панель, мусор)
- REGEN h (Giraffen — ФОТОРЕАЛ странное кресло, мусор)
- REGEN i (Affen — ФОТОРЕАЛ тёмный мусор)
- d, e, f OK

## 068 in-der-kantine
- SWAP b↔c (на b — шницель с картошкой → c; на c — рис с овощами → b)
- ROTATE d→e, e→f, f→d (на d — салат в миске → Großer Salat e; на e — рыба на тарелке → Fisch f; на f — пицца → Pizza d)
- MOVE g→i (на g — карривурст с картошкой = Currywurst); REGEN g (Nur Nachtisch — десерт; текущая i — торт, но с ТЕКСТОМ «Goethe-Zertifikat A2 Hören» — выбросить)
- a, h OK

## 069 im-fundbuero
- SWAP b↔c (на b — синяя куртка → Jacke c; на c — сумочка → Tasche b)
- SWAP d↔f (на d — мальчик за ноутбуком → Laptop f; на f — связка ключей → Schlüssel d)
- SWAP h↔i (на h — кошелёк с деньгами → Geldbeutel i; на i — наручные часы → Uhr h)
- a, e, g OK

## 070 bei-der-versicherung
- SWAP h↔i (концепт Rechtsschutz = «scales of justice with a shield» — это картинка на i (весы+щит+документы); концепт Haftpflicht = «a protective shield» — это картинка на h (щит с галочкой))
- a–g OK

## 071 im-baumarkt
- ROTATE a→c, c→b, b→a (на a — плитка/мытьё плитки → Fliesen c; на c — замок с ключом → Schloss und Schlüssel b; на b — штабель досок → Holz a)
- ROTATE d→f, f→e, e→d (на d — банки с краской → Farbe f; на f — молоток и ключ → Werkzeug e; на e — полив растений → Pflanzen d)
- SWAP g↔i (на g — лампа → Lampe i; на i — рулоны обоев → Tapeten g)
- h OK

## 072 muelltrennung-und-recycling
- SWAP d↔f (на d — кран с каплей и лист = Spart Wasser → f; на f — велосипед + зачёркнутая машина = Fährt nur Fahrrad → d)
- ROTATE g→i, i→h, h→g (на g — вешалка одежды с ценником 3€ = Second-Hand → i; на i — выброс очистков в компост → Kompostiert h; на h — магазин без упаковки с банками → ohne Verpackung g)
- a, b, c, e OK

## 073 im-tierheim
- SWAP a↔b (на a — морская свинка → b; на b — черепаха → a)
- ROTATE d→f, f→e, e→d (на d — мышь → Maus f; на f — птица в клетке → Vogel e; на e — кролик с лейкой → Kaninchen d)
- ROTATE g→i, i→h, h→g (на g — кошка → Katze i; на i — собака с мячом → Hund h; на h — аквариум с рыбками → Fische g)
- c OK

## 074 auf-dem-weihnachtsmarkt
- ROTATE a→b, b→c, c→a (на a — украшение ёлки → Weihnachtsbaum b; на b — карусель → Karussell c; на c — женщина с фотоаппаратом → Fotos a)
- ROTATE d→e, e→f, f→d (на d — каток → Schlittschuh e; на e — мальчик ест братвурст → f; на f — девочка слушает музыку → d)
- SWAP g↔i (на g — прилавок с подарками/покупка → Geschenke kaufen i; на i — пакет жареного миндаля → Gebrannte Mandeln g)
- h OK

## 075 in-der-reinigung
- SWAP b↔c (на b — красная зимняя куртка → Winterjacke c; на c — свёрнутый ковёр → Teppich b)
- REGEN e (Vorhänge: сцена со шторами правильная, но ТЕКСТ «Goethe-Zertifikat A2 Hören» сверху — выбросить)
- SWAP g↔i (на g — костюм на вешалке → Anzug i; на i — галстуки → Krawatten g)
- a, d, f, h OK

## 076 in-der-buchhandlung
- SWAP b↔c (на b — лупа над отпечатком/уликами = детектив → Krimis c; на c — книга с портретом пишущего человека = Biografien b)
- ROTATE d→e, e→f, f→d (на d — супергерой → Comics e; на e — открытая книга с картой/Эйфелевой башней → Reiseführer f; на f — перо и книга → Gedichte d, концепт «a poetry book with a quill pen»)
- MOVE h→g (на h — кулинарная книга с блюдами = Kochbücher); REGEN h (Kinderbücher — «colorful children's books»; текущая g — девочка поливает цветы, не соответствует ни одному концепту — выбросить)
- REGEN i (Sachbücher: сцена с книгами правильная, но ТЕКСТ «Goethe-Zertifikat A2 Hören» — выбросить)
- a OK

## 077 bei-der-polizei
- REGEN a (Fahrrad gestohlen/Anzeige: сцена правильная — участок, картинка велосипеда, но ТЕКСТ «Goethe-Zertifikat A2 Hören» — выбросить)
- REGEN e (Strafzettel bezahlen: сцена правильная, но ТЕКСТ — выбросить)
- b, c, d, f, g, h, i OK (h и i похожи, но различимы: h — звонит у аварии, i — свидетель со стороны)

## 078 in-der-tanzschule
- Все 9 OK (пары b/c/d/e/g/i стилистически различимы: cha-cha жёлтое платье, salsa красно-оранжевое, foxtrott классика, discofox 70-е клёши, walzer длинное платье, tango драматичная поза)

## 079 beim-fotografen
- REGEN b (Urlaubsfotos: сцена отпуска правильная, но крупный ТЕКСТ «Goethe-Zertifikat A2 Hören (Modellsatz)» — выбросить)
- REGEN i (Porträtfotos, концепт «a studio portrait photo»: на картинке женщина говорит по телефону за столом — не портретная съёмка)
- MINOR a (Hochzeitsfotos: сцена свадьбы правильная, но серый фон и чуть иной стиль — на усмотрение)
- MINOR e (Naturfotos: пейзаж с туристкой, но без фотоаппарата — приемлемо, однозначно «природа»)
- c, d, f, g, h OK

## 080 im-schuhgeschaeft
- REGEN f (Laufschuhe: кроссовки правильные, но ТЕКСТ «Goethe-Zertifikat A2 Hören» сверху — выбросить)
- остальные 8 OK

## 081 in-der-volkshochschule
- REGEN b (Fotokurs: сцена с фотоаппаратами правильная, но ТЕКСТ сверху — выбросить)
- остальные 8 OK

## 082 bei-der-autovermietung
- REGEN d (Motorrad: на картинке ТАКСИ — чужая тема)
- REGEN e (Familienwagen: на картинке ПОЛИЦЕЙСКАЯ машина — чужая тема)
- REGEN f (Transporter: на картинке ПОЕЗД — чужая тема)
- REGEN g (Sportwagen: на картинке САМОЛЁТ — чужая тема)
- REGEN h (Kleinwagen: на картинке ВЕЛОСИПЕД — чужая тема)
- a, b, c, i OK
- ПРИМЕЧАНИЕ: такси/полиция/поезд/самолёт/велосипед похожи на набор «Verkehrsmittel» другого теста — при применении проверить, не пригодятся ли эти файлы другой теме (маловероятно, все темы уже имеют свои картинки)

## 083 beim-hautarzt
- REGEN b (Insektenstich: на картинке температура/градусник — симптомы простуды, чужой набор)
- REGEN c (Warzen: на картинке перебинтованная рука)
- REGEN d (Haarausfall: на картинке головная боль)
- REGEN e (Nagelpilz: на картинке боль в животе)
- REGEN f (Trockene Haut: на картинке сморкается/чихает)
- REGEN g (Pickel/Akne: на картинке кашель)
- REGEN h (Muttermal-Kontrolle: на картинке насморк/красный нос)
- REGEN i (Sonnenbrand: на картинке принимает таблетку)
- a OK
- ПРИМЕЧАНИЕ: почти весь набор — картинки «простуда/симптомы» из чужой темы; сверить с 091 in-der-apotheke и 093 beim-kinderarzt при просмотре

## 084 in-der-tourist-information
- a OK (парк)
- REGEN b (Bootsfahrt: на картинке детская площадка + ТЕКСТ)
- REGEN c (Zoo: на картинке бассейн + ТЕКСТ)
- REGEN d (Museum: на картинке библиотека)
- REGEN e (Aussichtsturm: на картинке почта — марки, конверт)
- REGEN f (Stadtführung: на картинке касса/Schalter)
- REGEN g (Markt: на картинке магазинная касса с «OPEN» — не рынок)
- REGEN h (Theater: на картинке аптека)
- REGEN i (Shopping: на картинке кафе)
- ПРИМЕЧАНИЕ: почти весь набор — чужая тема «места в городе» (площадка, бассейн, библиотека, почта, касса, аптека, кафе)

## 085 in-der-musikschule
- Цепочка MOVE: b→i (пианино → Klavier; бонго на i выбросить), d→b (ударная установка → Schlagzeug), e→d (скрипка → Geige), c→e (мальчик с гитарой → Gitarre)
- REGEN c (Gesang — пение, картинки нет)
- REGEN h (Cello: на картинке губная гармошка)
- a, f, g OK

## 086 beim-physiotherapeuten
- MOVE c→g (на c — мальчик на костылях с перебинтованной стопой = Verstauchter Fuß; текущая g — боль в горле, чужая тема — выбросить)
- REGEN b (Hüftschmerzen: на картинке нога в гипсе с костылями — не бедро; выбросить)
- REGEN c (Verletztes Knie — колено с повязкой)
- REGEN d (Kopfschmerzen: ФОТОРЕАЛ тёмный круглый предмет, мусор)
- REGEN f (Steifer Nacken: на картинке ЗУБНАЯ боль)
- REGEN h (Ellbogenschmerzen: на картинке боль в УХЕ)
- REGEN i (Schulterschmerzen: на картинке пациент на вытяжке ноги в больнице)
- a, e OK
- ПРИМЕЧАНИЕ: зуб/горло/ухо — чужой набор (симптомы для лора/зубного)

## 087 im-spielzeugladen
- MOVE b→h (на b — пазл = Puzzle; воздушный змей на h выбросить)
- MOVE c→i (на c — настольная игра с кубиками = Brettspiel; сборная модель самолёта на i выбросить)
- REGEN b (Auto — игрушечная машинка; текущего нет)
- REGEN c (Eisenbahn — игрушечная железная дорога)
- REGEN d (Puppe: на картинке игральные карты — выбросить)
- REGEN e (Fahrrad: на картинке шахматы — выбросить)
- REGEN f (Kuscheltier: на картинке домино — выбросить)
- REGEN g (Ball: на картинке волчок/юла — выбросить)
- a OK

## 088 online-shopping-und-ruecksendung
- a OK (пакет продуктов = Lebensmittel)
- REGEN b (Medikamente: на картинке корзина фруктов)
- REGEN c (Elektronik: на картинке хлеб/булочки)
- REGEN d (Spielzeug: на картинке молоко в холодильник)
- REGEN e (Möbel: на картинке сумка овощей)
- REGEN f (Bücher: на картинке лоток яиц)
- REGEN g (Schuhe: на картинке штопор и вино)
- REGEN h (Kleidung: ФОТОРЕАЛ тёмный мусор)
- REGEN i (Werkzeug: на картинке шоколад/сладости)
- ПРИМЕЧАНИЕ: весь набор кроме a — «еда» из чужой темы

## 089 beim-umzugsunternehmen
- MOVE f→i (на f — мытьё окна = Putzen; сгребание листьев на i выбросить)
- REGEN b (Fürs Essen sorgen: на картинке полив цветов)
- REGEN c (Möbel aufbauen: на картинке стрижка газона)
- REGEN d (Den Lkw fahren: на картинке покраска забора)
- REGEN e (Kinder betreuen: на картинке развешивание белья)
- REGEN f (Kartons packen — после переноса мытья окна на i)
- REGEN g (Parkplatz freihalten: на картинке мойка машины + ТЕКСТ)
- REGEN h (Möbel tragen: на картинке гриль/BBQ)
- a OK
- ПРИМЕЧАНИЕ: набор кроме a — «работа в саду/по дому» из чужой темы

## 090 im-sportgeschaeft
- Все 9 OK

## 091 in-der-apotheke
- SWAP e↔f (на e — травяной чай → Tee gegen Husten f; на f — тюбик мази → Salbe e)
- SWAP h↔i (на h — сироп с ложкой → Hustensaft i; на i — градусник и больной → Fieberthermometer h)
- a, b, c, d, g OK

## 092 in-der-eisdiele
- Все 9 OK

## 093 beim-kinderarzt
- SWAP d↔f (на d — болит живот → Bauchschmerzen f; на f — кашель → Husten d)
- остальные 7 OK

## 094 an-der-tankstelle
- Все 9 OK

## 095 beim-tierfriseur
- Все 9 OK
- MINOR e (Fell färben: окраска видна слабо — кисть с цветными прядями; отличимо от f Bürsten, но на грани)
- MINOR d/g (Baden mit Spezial-Shampoo и Waschen сюжетно близки — оба «купание в тазу»; d отличается бутылкой шампуня; это заложено в самих опциях)

## 096 im-blumenladen
- Все 9 OK (букеты c/e/h/i различаются деталями: жёлтый бант/облачко-извинение/розовая упаковка/вручение с голубым бантом; венки b и g — заложенная близость опций, различимы: b у могилы, g с чёрным траурным бантом)

## 097 in-der-aenderungsschneiderei
- Все 9 OK

## 098 im-wellnesshotel
- REGEN i (Im Pool schwimmen: ФОТОРЕАЛ зелёный предмет с зеркальным псевдотекстом, мусор — выбросить)
- остальные 8 OK

## 099 im-sprachcafe
- Все 9 OK (флаги все правильные)

## 100 abschlussfeier-und-zukunftsplaene
- Все 9 OK

# ПРОСМОТР ЗАВЕРШЁН: 100/100 листов

# ВТОРОЙ ПРОХОД (2026-07-04): Grok Build повторно применил мои renames поверх уже применённых (swap'ы откатились, циклы сдвинулись) и заполнил 149 regen-слотов. Все листы пересобраны с текущего диска, проверка заново. Вердикты ниже перекрывают первый проход.

## 001 reisen-mit-der-bahn (2й проход)
REGEN h (hütet den Hund — сгенерирована сервировка стола, не собака; дубль смысла g). MINOR b (новые музейные билеты с мелкими «A2»). Остальные 7 OK.

## 002 wochenende-und-freizeit (2й проход)
Все 9 OK.

## 003 im-restaurant-und-cafe (2й проход)
Все 9 OK.

## 004 schule-und-sprachkurs (2й проход)
REGEN b (macht Wahrscheinlichkeit — Grok опять сгенерировал поднос снеков, дубль c; нужен концепт с кубиками/монетой). MINOR f (Statistik — карандашный стиль, приемлемо). Остальные OK.

## 005 wohnen-und-umzug (2й проход)
Все 9 OK.

## 006 beim-arzt-und-in-der-apotheke (2й проход)
Все 9 OK (опции теста — wellness: акупунктура, фризёр, сауна и т.д.; картинки соответствуют).

## 007 im-buero-und-arbeitsleben (2й проход)
REGEN d (ist DJ und bringt die Musikanlage — сейчас конверт с почтовым ящиком). MOVE i->h (текущая i — зал с флажками и столами = organisiert die Location; старую h — белую «книжку» с картинкой праздника — в карантин). REGEN i (besorgt die Getränke — ящики/бутылки напитков). Остальные OK.

## 008 urlaub-und-reisen-planen (2й проход)
SWAP e<->f (свап откатился: у e стиральная машина, у f отель). Остальные 7 OK.

## 009 sport-und-fitness (2й проход)
SWAP g<->h (откатился: g=велосипед, h=бег). REGEN c (Yoga — сейчас фотореал: чёрная машина с буквой P, мусор; концепт: человек в позе лотоса/медитации на коврике, НЕ warrior pose — она уже у d Pilates). Остальные OK.

## 010 einkaufen-und-geschaefte (2й проход)
SWAP c<->d (откатился: c=уборка, d=пирожные). Остальные 7 OK.

## 011 termine-und-telefon (2й проход)
Все 9 OK.

## 012 tiere-und-haustiere (2й проход)
REGEN f (kontrolliert die Wohnung und holt die Post — Grok сгенерировал распаковку корма, дубль g; концепт: человек у двери квартиры вынимает письма из почтового ящика). Остальные OK.

## 013 verkehr-und-stadt (2й проход)
Все 9 OK.

## 014 familienfeste (2й проход)
REGEN f (organisiert die Location — новая генерация с текстом «Goethe-Zertifikat A2 Hören (Modellsatz, Übungssatz)» на картинке). REGEN i (spielt Musik — фотореал: чёрный кожаный футляр, мусор; концепт: человек играет на гитаре у праздничного стола). Остальные OK.

## 015 kino-theater-und-konzert (2й проход)
REGEN d (Tanz-Aufführung — фотореал чёрной техники). REGEN e (Open-Air-Konzert — сгенерирована картинная галерея, дубль f; концепт: уличная сцена с музыкантами и толпой вечером). REGEN b (Filmfestival — новая генерация = обычный кинозал, неотличим от c Kino-Besuch; концепт: open-air кино вечером, экран на улице, гирлянды, публика на стульях). Остальные OK.

## 016 kochen-und-essen (2й проход)
SWAP e<->f (откатился: e=тарелка жаркого, f=букет). MOVE d->g (d=хлеб в руке — это bringt Brot mit; старую g — хлеб с текстом «Goethe-Zertifikat A2 Hören (Modellsatz/Übungssatz)» — в карантин). DISCARD h (женщина несёт хлеб — не салат). REGEN d (dekoriert den Tisch — сервировка: свечи, салфетки, тарелки). REGEN h (macht einen Salat — миска салата, человек перемешивает). Остальные OK.

## 017 garten-und-pflanzen (2й проход)
SWAP a<->b (a=полив лейкой, b=разбрасывание удобрений). SWAP c<->d (c=отдых в шезлонге, d=обрезка ветки). SWAP g<->h (g=выдёргивание сорняков, h=посадка томатов). Остальные OK.

## 018 internet-und-technik (2й проход)
SWAP a<->b (a=фотоаппарат, b=наушники). SWAP c<->d (c=планшет с фото, d=ридер с текстом и закладкой). REGEN h (ein Laptop — Grok сгенерировал смартфон в руке; концепт: открытый ноутбук с клавиатурой на столе). Остальные OK.

## 019 bank-und-geld (2й проход)
SWAP e<->i (e=кошелёк с картами -> на i kümmert sich um die Bank-Karten; i=счёт с лампочкой/молнией -> на e zahlt die Stromrechnungen). REGEN b (verwaltet das Online-Banking — Grok снова сгенерировал тележку продуктов, дубль a; концепт: человек за ноутбуком, на экране банковская страница с евро, БЕЗ покупок). REGEN h (zahlt die Miete — сгенерирован щит с галочкой, дубль страховки; концепт: человек передаёт наличные купюры перед маленьким домом). Остальные OK.

## 020 sprachen-lernen (2й проход)
Все 9 OK.

## 021 auto-und-fahren (2й проход)
SWAP e<->f (e=ключ ломается в замке двери, f=разбитый тормозной диск). REGEN c (Kein Benzin mehr — Grok сгенерировал аккумулятор с проводами, дубль d; концепт: стрелка топлива на нуле / пустая канистра у машины, БЕЗ аккумулятора). Остальные OK.

## 022 kleidung-und-mode (2й проход; тема — подарки)
SWAP a<->b (a=деньги в конверте, b=спа-ваучер). SWAP c<->d (c=бутылка вина, d=кулинарная книга). SWAP g<->h (g=дорожная сумка, h=фотоальбом). Остальные OK.

## 023 wetter-und-jahreszeiten (2й проход)
Все 9 OK.

## 024 kinder-und-erziehung (2й проход; подтверждение жалобы пользователя)
SWAP b<->c (b=балерина, c=верховая езда — своп откатился). REGEN f (spielt Fußball im Verein — Grok сгенерировал ребёнка с гигантским смартфоном; концепт: дети в одинаковых футболках играют в футбол на поле). REGEN g (malt und zeichnet — фотореал: пластиковая водяная игрушка; концепт: ребёнок рисует карандашами за столом). MINOR i (загнутый уголок страницы). Остальные OK.

## 025 bibliothek-und-lesen (2й проход)
MOVE d->e (d=пара на скамейке с сердцем = Liebesromane; старую e — тревел-книгу с картой и текстом «Goethe-Zertifikat A2 Hören» — в карантин, текст-лик). MOVE i->h (i=комикс-панели с бабблами = Comics und Manga; старую h — рендер экзаменационного листа с текстом «Hören», A/B/C — в карантин). DISCARD g (книги «BIOGRAFIE» с портретами — дубль f). REGEN d (Reiseberichte — открытая книга с картой и компасом, чемодан, БЕЗ текста). REGEN g (Kochbücher — стопка кулинарных книг с кастрюлей/ложкой на обложке). REGEN i (Krimis — детективная книга с лупой/следами). Остальные OK.

## 026 friseur-und-schoenheit (2й проход)
SWAP g<->h (g=маска для лица, h=сауна — своп откатился). REGEN i (macht eine Maniküre — Grok сгенерировал массаж спины, дубль e; концепт: покраска ногтей на руках крупным планом). Остальные OK.

## 027 hotel-und-uebernachten (2й проход)
REGEN a, b, e, f, i — Grok перегенерировал все 5, но НА ВСЕХ снова текст «Goethe-Zertifikat A2 Hören (Modellsatz/Übungssatz)» сверху. Контент под текстом в целом верный (пансион, дом, гостиная, палатка, приезд к родственникам) — нужно перегенерировать с жёстким «no text». Плюс у b на двери висит табличка «Pension» — для Bauernhof лучше двор с трактором/животными. c, d, g, h OK.

## 028 post-und-pakete (2й проход)
SWAP c<->d (c=кредитка, d=подарок). SWAP e<->f (e=книга в коробке, f=большой счёт SUMME/BEZAHLT). MOVE h->g (h=женщина с конвертом EILT! и восклицательным знаком = Mahnung; старую g — свадебную открытку с текстом «Goethe-Zertifikat A2 Hören» — в карантин). REGEN b (Werbeprospekt — Grok сгенерировал вторую открытку, дубль a; концепт: рекламный листок супермаркета с продуктами и ценниками-процентами, без читаемого текста). REGEN h (Hochzeitseinladung — открытка с женихом и невестой, сердечки, БЕЗ текста). Остальные OK.

## 029 vereine-und-hobbys (2й проход)
MOVE c->d (c=три фотографа с камерами = Foto-Club; старую d — музыкальную группу с текстом «Goethe-Zertifikat A2 Hören» — в карантин). SWAP g<->h (g=поющий хор, h=мальчик с футбольным мячом). REGEN a (Theaterverein — сцена верная, но сверху текст «Goethe-Zertifikat A2 Hören» + артефактная строка). REGEN b (Tanzverein — сгенерирован театр с масками и Goethe-текстом; концепт: пары танцуют в зале). REGEN c (Musikverein — духовой оркестр/группа с инструментами, БЕЗ текста). Остальные OK.

## 030 behoerden-und-dokumente (2й проход)
MOVE a->b (a=стол полиции с найденными вещами и зонтом = Verlustanzeige; старую b — POLIZEI-стойку с текстом «Goethe-Zertifikat A2» — в карантин). SWAP e<->f (e=судья с молотком=Gericht, f=выдача Personalausweis=Bürgeramt). REGEN a (TÜV — Hauptuntersuchung: механик осматривает машину на подъёмнике с чек-листом). REGEN h (Krankenkasse — фотореал металлической детали; концепт: стойка мед. страховки, человек получает страховую карту, зелёный крест). Остальные OK.

## 031 beim-zahnarzt (2й проход)
SWAP a<->c (a=установка коронки, c=чистка/отбеливание зуба до блеска — своп откатился). REGEN f (Karies-Behandlung / Plombe — фотореал: женщина с серебристой машиной; концепт: зуб с тёмным пятном кариеса + бормашина/пломба). Остальные OK.

## 032 im-schwimmbad (2й проход)
REGEN b (trinkt etwas im Café — Grok снова сгенерировал водную горку, дубль a; концепт: человек в купальнике за столиком у бассейна пьёт напиток через трубочку). REGEN e (macht Aqua-Fitness — фотореал чёрного кожаного предмета; концепт: группа в воде делает упражнения с нудлами, инструктор у бортика). REGEN h (springt vom Sprungbrett — сгенерирован пловец на дорожках, дубль g; концепт: человек прыгает с трамплина в бассейн, в полёте). Остальные OK.

## 033 camping-und-wandern (2й проход)
SWAP c<->d (c=настольные игры и книги, d=мальчик с дровами у гриля). MOVE h->g (h=карта пешего маршрута = Wanderpläne; старую g — свёрнутые коврики с текстом «Goethe-Zertifikat A2 Hören» — в карантин). REGEN b (kümmert sich um das Essen — сцена верная, но сверху текст «Goethe-Zertifikat A2 (Modellsatz/Übungssatz)»). REGEN h (bringt Schlafsäcke und Isomatten — спальные мешки и свёрнутые коврики, БЕЗ текста). Остальные OK.

## 034 im-krankenhaus (2й проход)
SWAP c<->g (c=рентген лёгких с воспалением = Lungenentzündung, g=перевязанное колено с костылём = Knie-OP). REGEN i (ist im Krankenhaus für eine Kontrolle — сцена верная, но сверху текст «Goethe-Zertifikat A2 Hören (Modellsatz,Übungssatz)»). Остальные OK.

## 035 moebel-und-einrichtung (2й проход)
MOVE b->a (b=садовые складные стулья = Outdoor-Stühle; старую a — мальчик за письменным столом с текстом «Goethe-Zertifikat A2 Hören» — в карантин). SWAP e<->f (e=обеденный стол с едой, f=платяной шкаф). REGEN b (Schreibtisch — письменный стол с лампой и стулом, БЕЗ текста). REGEN d (Bett — Grok сгенерировал второй диван, дубль c; концепт: кровать с подушкой и одеялом). REGEN h (Kommode — сгенерирован зеркальный шкафчик ванной, дубль g; концепт: комод с выдвижными ящиками в спальне). Остальные OK.

## 036 studium-und-universitaet (2й проход)
Все 9 OK (MINOR: у b цветная полоска сверху, приемлемо).

## 037 bewerbung-und-job-suchen (2й проход)
SWAP a<->c (a=программист за монитором с кодом, c=учительница у доски). Остальные OK.

## 038 babys-und-kleinkinder (2й проход)
MOVE g->h (g=папа с гитарой и девочка с трубой = Musik; старую h — фотореал чёрной металлической детали — в карантин). REGEN d (Puppen — сейчас мишка поливает цветок из лейки, не куклы; концепт: две куклы в платьях). REGEN f (Bücher — динозавры за чаепитием с текстом «Goethe-Zertifikat A2 Hören»; концепт: стопка детских книжек с картинками, ребёнок листает). REGEN g (Malen — ребёнок рисует кисточкой за мольбертом). REGEN i (Autos — сцена верная, но сверху текст «Goethe-Zertifikat A2 Hören»). Остальные OK.

## 039 am-flughafen (2й проход; тема — города)
SWAP a<->b (a=Вена: Бельведер+Штефансдом, b=Колизей). REGEN i (Madrid — королевский дворец нарисован верно, но сверху текст «Goethe-Zertifikat A2 Hören (Modellsatz/Übungssatz)»). Остальные OK.

## 040 sommer-und-strand (2й проход)
ROTATE: e->d (мальчик строит замок из песка = Sandburgen), f->e (парусник = Segeln), d->f (аквалангист = Tauchen). REGEN a (Kajak fahren — Grok сгенерировал сноркелера, дубль c; концепт: человек гребёт веслом в каяке по воде). REGEN i (Surfen — сгенерирован пляжный волейбол, дубль g; концепт: человек стоит на доске для сёрфинга на волне). Остальные OK.

## 041 winter-und-skifahren (2й проход)
SWAP b<->c (b=прыгун с трамплина, c=фигурист на коньках). SWAP g<->i (g=ледолазание с ледорубами, i=дети на санках). MOVE d->e (d=сноубордист = Snowboarden; старую e — фотореал чёрной маски — в карантин). REGEN d (Ski fahren — горнолыжник спускается по склону; НЕ беговые лыжи, они у h). Остальные OK.

## 042 geburtstag-und-geschenke (2й проход)
REGEN c (Geld — Grok сгенерировал мальчика с гигантским CD, дубль a; концепт: банкноты и монеты евро в руке/конверте). Остальные OK.

## 043 reise-mit-dem-auto (2й проход; марки машин)
REGEN f (Mercedes — чёрный седан нарисован, но сверху текст «Goethe-Zertifikat A2 Hören (Modellsatz, Übungssatz)»; концепт: чёрный элегантный седан, БЕЗ текста). Остальные OK.

## 044 musik-und-konzerte (2й проход)
MOVE c->a (c=саксофонист = Jazz; старую a — скрипачку с детским оркестром, дубль b — в карантин). SWAP d<->e (d=микрофон с золотой цепью и наушниками = Hip-Hop -> на e; e=гитара с пальмовыми листьями и раста-браслетами = Reggae -> на d). SWAP h<->i (h=пульт с эквалайзером = Elektro, i=аккордеонист = Volksmusik). REGEN c (Country — акустическая гитара/банджо и ковбойская шляпа). Остальные OK.

## 045 im-museum (2й проход)
REGEN a (Sport — витрина с кубками верная, но сверху текст «Goethe-Zertifikat A2 Hören»). REGEN d (Naturkunde — сгенерирован полив цветов на холсте; концепт: витрина музея природы — бабочки/минералы/чучела животных, БЕЗ динозавра — динозавр пойдёт в e? нет: динозавр тоже Naturkunde; см. e). REGEN e (Moderne Kunst — сгенерирован скелет динозавра с Goethe-текстом; концепт: зал с абстрактными яркими картинами и скульптурами). REGEN f (Musik — фотореал чёрного устройства; концепт: витрина со старинными инструментами — скрипка, граммофон). REGEN h (Mode — сгенерированы пирамиды с маской фараона, дубль g; концепт: манекены в исторических платьях). REGEN i (Geschichte — витрина с античными вазами верная, но сверху текст «Goethe-Zertifikat A2 Hören»). b, c, g OK.
Примечание: для d уместен скелет динозавра (как раньше) — но БЕЗ текста; для e строго без динозавра.

## 046 am-bahnhof (2й проход; города Германии)
ROTATE: e->c (Frauenkirche с зелёными куполами = München), c->d (Эльбфилармония с гаванью = Hamburg), d->e (скайлайн небоскрёбов = Frankfurt). MOVE g->f (Бранденбургские ворота = Berlin; старую f — второй Кёльнский собор, дубль h — в карантин). REGEN g (Dresden — Frauenkirche с каменным куполом / Цвингер, БЕЗ текста). a, b, h, i OK.

## 047 computer-und-probleme (2й проход; творческие задачи на ПК)
MOVE d->e (d=рисунок на экране с таймлайном воспроизведения = Animationen erstellen; старую e — фоторедактор с баннером «Goethe-Zertifikat A2 Hören» — в карантин). MOVE g->h (g=ноутбук с конвертами на экране = E-Mails beantworten; старую h — веб-страницу с текстом «Goethe-Zertifikat A2 Hören» — в карантин). REGEN b (Videos schneiden — с Goethe-текстом; концепт: экран с видеодорожкой и ножницами, БЕЗ текста). REGEN c (App programmieren — с Goethe-текстом; концепт: экран с блоками кода, человек за клавиатурой). REGEN d (Fotos bearbeiten — экран с фотографией и ползунками яркости/цвета). REGEN g (Texte schreiben — человек печатает текстовый документ на ноутбуке, страница с абзацами). i MINOR (абстрактные цветные блоки как «дизайн сайта» — оставляю). a, f OK.

## 048 im-supermarkt (2й проход)
SWAP a<->b (a=бутылки напитков, b=рыба на тарелке). ROTATE: e->d (сыр = Käse), f->e (девочка с десертом = Nachtisch), d->f (сырое мясо = Fleisch). ROTATE: i->g (овощи и салатница = Gemüse für Salat), g->h (винные бутылки = Wein), h->i (женщина с хлебами = Brot und Brötchen). Остальные OK.

## 049 im-theater (2й проход)
SWAP b<->c (b=кукольный театр с зайцем и мишкой = Kinderstück, c=кот с микрофоном = Musical Cats). SWAP g<->h (g=оперная певица, h=балерина). MOVE d->e (d=сцена с балконом и розой = Romeo und Julia; старую e — фотореал серебристых наушников — в карантин). REGEN a (Faust — сцена верная, но сверху текст «Goethe-Zertifikat A2 Hören»). REGEN d (Comedy-Stück — комик на сцене, смеющийся зал, БЕЗ масок — маски у f). REGEN i (Krimi-Theater — детектив с лупой верный, но сверху баннер «Goethe-Zertifikat A2 HÖREN»). f OK.

## 050 beim-tierarzt (2й проход)
SWAP a<->b (a=попугай, b=хомяк). ЦЕПОЧКА: g->h (змея с зубной щёткой = Schlange), h->i (кот пьёт из стакана = Katze), старую i — аквариум с текстом «Goethe-Zertifikat A2 Hören» — в карантин. REGEN g (Fische — аквариум с рыбками, БЕЗ текста). REGEN d (Schildkröte — фотореал странной куклы; концепт: черепаха с панцирем). c, e, f OK.

## 051 beim-augenarzt
- ROTATE a→c (очки на книге = Lesebrille), c→b (спортивные очки-маска = Sportbrille), b→a (здоровый глаз + читающая женщина = Keine Sehhilfe)
- ROTATE d→e (протирает обычные очки = Normale Brille), e→f (очки перед монитором = Computer-Brille), f→d (линзы с двумя зонами = Bifokal-Brille)
- SWAP g↔h (лазерная операция на глазу = Augen-Operation ↔ контейнер с линзами = Kontaktlinsen)
- i OK (Rx-солнцезащитные)

## 052 im-schwimmbad-und-sauna
- ROTATE a→c (гантели в бассейне = Aqua-Fitness), c→b (круглый джакузи = Whirlpool), b→a (вышка с прыгуном = Vom Turm springen)
- MOVE e→d (массаж = Massage); старая d (пловец на дорожках с Goethe-текстом) в карантин
- REGEN e (Bahnen schwimmen — пловец кролем на дорожках, БЕЗ текста)
- SWAP g↔i (сауна с печкой = Sauna ↔ детский лягушатник = Kinderbecken)
- f,h OK

## 053 familienfeier-und-hochzeit
- SWAP a↔b (DJ за пультом = Musik/DJ ↔ женщина с тортом = Torte backen)
- MOVE d→c (открытка-приглашение с шариками = Einladungen); старая c (свадебная машина Just Married с Goethe-текстом) в карантин
- REGEN d (Auto schmücken — украшенная свадебная машина с лентами и цветами, БЕЗ текста)
- SWAP e↔f (женщина у микрофона = Rede halten ↔ букет в руке = Blumen)
- g,h,i OK

## 054 beim-optiker
- ROTATE a→b (большие КРАСНЫЕ очки = Rote farbige Brille), b→c (девочка надевает спортивную маску = Sportbrille); старая c (фотореал тёмно-синий кожаный футляр) в карантин
- REGEN a (Runde Brille — круглые очки)
- ROTATE d→f (огромные чёрные роговые очки = Schwarze Hornbrille), e→d (красные очки на книге = Lesebrille), f→e (тонкие безободковые очки = Randlose Brille)
- ROTATE g→h (двухзонные линзы = Bifokal-Brille), h→i (золотая оправа в руках = Goldene Brille), i→g (золотые авиаторы на лице = Pilotenbrille)

## 055 beim-fussball
- ROTATE a→b (зелёно-белая футболка = Werder Bremen), b→c (сине-белая полосатая = Hertha Berlin), c→a (жёлто-чёрная = Dortmund)
- d,e,f,g,h,i OK (цвета клубов совпадают)

## 056 beim-baecker
- SWAP a↔b (ломтик чизкейка = Käsekuchen ↔ буханка с семечками = Vollkornbrot)
- SWAP d↔f (круассан = Croissants ↔ штрудель с яблочной начинкой = Apfelstrudel)
- DISCARD e + REGEN e (Berliner — Grok опять нарисовал пончик С ДЫРКОЙ и джемом; концепт: круглый берлинер БЕЗ дырки, с сахарной пудрой и каплей джема сбоку)
- c,g,h,i OK

## 057 wohnungssuche-und-makler
- DISCARD a (ферма с трактором — контент верный, но Goethe-текст сверху) + REGEN a (Bauernhaus — фермерский дом с трактором и огородом, БЕЗ текста)
- MOVE c→b (семья на кухне + сад за дверью = Familie-Wohnung mit Garten); старая b (фотореал: тёмный тканевый конус с палкой, хлам) в карантин
- REGEN c (Haus zum Kaufen — маклер передаёт ключи семье перед домиком, БЕЗ текста и табличек)
- MOVE h→g (стеклянный верхний этаж с бассейном на крыше = Penthouse); старая g (лофт с кирпичными стенами, НО с Goethe-текстом) в карантин
- REGEN h (Loft — индустриальное открытое пространство, кирпич, трубы, высокие окна, БЕЗ текста)
- d,e,f — взаимозаменяемые комнаты (WG/Studio/Ein-Zimmer), оставляю как есть (MINOR); i OK

## 058 beim-friseur-und-beauty
- все 9 OK

## 059 beim-friseur-maenner
- SWAP b↔c (пучок = Dutt ↔ синий ирокез = Iro/Mohawk)
- SWAP d↔e (дреды = Dreadlocks ↔ длинные волосы с прямым пробором = Mittelscheitel)
- ROTATE g→i (фиолетовый выбритый висок + наушники = Undercut), h→g (короткий ёжик, чистит зубы = Bürstenschnitt), i→h (лысый бреет голову = Glatze)
- a,f OK

## 060 im-park-und-erholung
- SWAP a↔b (велосипедист = Fahrrad fahren ↔ тай-чи в фиолетовом костюме = Tai Chi)
- MOVE d→e (выгул собаки на поводке = Mit Hund Gassi gehen); старая e (дети с фрисби, НО Goethe-текст) в карантин
- MOVE f→d (пикник на пледе = Picknick mit Freundinnen)
- REGEN f (Frisbee spielen — двое кидают фрисби в парке, БЕЗ текста)
- DISCARD i + REGEN i (Spazieren — Grok опять нарисовал прогулку С СОБАКОЙ = дубль e; концепт: пара неспешно гуляет по дорожке парка, БЕЗ собаки)
- c,g,h OK

## 061 im-fitnessstudio
- MOVE b→a (скручивания на коврике = Pilates), c→b (группа танцует = Zumba)
- DISCARD a (скалодром — контент верный, но Goethe-текст сверху)
- REGEN c (Klettern — человек на скалодроме с цветными зацепами, БЕЗ текста)
- SWAP d↔e (беговая дорожка = Laufband ↔ пловец = Schwimmen)
- ROTATE g→i (боксёрская груша = Boxen), h→g (гантели = Krafttraining), i→h (поза дерева = Yoga)
- f OK

## 062 auf-dem-wochenmarkt
- ROTATE c→e (букет = Blumen), e→d (мясная витрина = Fleisch und Wurst), d→c (сыр = Käse)
- SWAP f↔g (рыба на тарелке = Fisch ↔ овощной прилавок = Gemüse)
- a,b,h,i OK

## 063 in-der-autowerkstatt
- ROTATE a→b (разбитая фара с фонариком = Licht funktioniert nicht), b→c (спущенная шина = Platter Reifen), c→a (сломанные дворники под дождём = Scheibenwischer kaputt)
- SWAP d↔e (лужа масла под машиной = Verliert Öl ↔ открытый капот с красным X = Motor springt nicht an)
- f,g,h,i OK

## 064 im-reisebuero
- SWAP a↔b (сафари с жирафом и львом = Safari in Afrika ↔ круизный лайнер = Kreuzfahrt)
- ROTATE d→f (семья на лыжах = Skiurlaub), e→d (семья на велосипедах = Fahrradtour), f→e (массаж = Wellness-Urlaub)
- MOVE h→g (турист с рюкзаком в горах = Wandern in den Bergen); старая g (Эйфелева башня + чемодан, НО Goethe-текст) в карантин
- REGEN h (Städtereise — туристка с чемоданом у известных зданий, БЕЗ текста)
- DISCARD i (фотореал: тёмный ночной пейзаж, хлам) + REGEN i (Strandurlaub — пляж, зонт, море)
- c OK

## 065 im-elektronikgeschaeft
- SWAP a↔b (смартфон = Handy ↔ приставка с геймпадом = Spielekonsole)
- остальные 7 OK

## 066 handwerker-im-haus
- SWAP d↔e (провода в руках = Elektriker ↔ скребок для окон = Fensterputzer)
- ROTATE g→h (укладка плитки = Fliesenleger), h→i (пилит доску = Tischler), i→g (трубы и разводной ключ = Klempner)
- a,b,c,f OK

## 067 im-zoo
- MOVE a→c (слон моет машинку = Elefanten); старая c (фотореал: чёрная коробка, хлам) в карантин
- MOVE b→a (попугаи купаются = Papageien)
- REGEN b (Tiger — тигр в зоопарке)
- DISCARD g (фотореал: чёрная металлическая панель), h (фотореал: чёрная скульптура), i (фотореал: тёмная ткань)
- REGEN g (Eisbären — белые медведи у воды), h (Giraffen — жирафы едят листья), i (Affen — обезьяны на канатах)
- d,e,f OK

## 068 in-der-kantine
- SWAP b↔c (шницель с картошкой фри = Schnitzel ↔ рис с овощами = Reis mit Gemüse)
- ROTATE d→e (миска салата = Großer Salat), e→f (рыба на тарелке = Fisch), f→d (пицца = Pizza)
- MOVE g→i (карривурст с фри = Currywurst); старая i (кусок торта с клубникой — контент верный, но Goethe-текст) в карантин
- REGEN g (Nur Nachtisch — кусок торта/десерт на тарелке, БЕЗ текста)
- a,h OK

## 069 im-fundbuero
- SWAP b↔c (куртка надевается = Jacke ↔ сумочка = Tasche)
- SWAP d↔f (ноутбук = Laptop ↔ связка ключей = Schlüssel)
- SWAP h↔i (кошелёк с купюрами = Geldbeutel ↔ наручные часы = Uhr)
- a,e,g OK

## 070 bei-der-versicherung
- SWAP h↔i (весы с документами и юристом = Rechtsschutzversicherung ↔ щит с галочкой, женщина и машинка = Haftpflichtversicherung)
- остальные 7 OK

## 071 im-baumarkt
- ROTATE a→c (мытьё плитки = Fliesen), c→b (замок с ключом = Schloss und Schlüssel), b→a (штабель досок = Holz)
- ROTATE d→f (банки с краской = Farbe), f→e (молоток и гаечный ключ = Werkzeug), e→d (полив растений в горшках = Pflanzen)
- SWAP g↔i (лампа = Lampe ↔ рулоны обоев = Tapeten)
- h OK

## 072 muelltrennung-und-recycling
- SWAP d↔f (кран с каплей и лист = Spart Wasser ↔ велосипед и зачёркнутая машина = Fährt nur Fahrrad)
- ROTATE g→i (вешалка одежды с ценником 3€ = Kauft Second-Hand-Kleidung), i→h (компост = Kompostiert Bioabfälle), h→g (магазин без упаковки, банки = Kauft ohne Verpackung ein)
- a,b,c,e OK

## 073 im-tierheim
- SWAP a↔b (морская свинка с морковкой = Meerschweinchen ↔ черепаха с сумкой = Schildkröte)
- ROTATE d→f (мышь = Maus), f→e (птица в клетке = Vogel), e→d (кролик с лейкой = Kaninchen)
- ROTATE g→i (кот умывается = Katze), i→h (пёс с мячом = Hund), h→g (аквариум = Fische)
- c OK

## 074 auf-dem-weihnachtsmarkt
- ROTATE a→b (украшение ёлки = Den Weihnachtsbaum ansehen), b→c (карусель = Karussell fahren), c→a (фотографирует ярмарку = Fotos machen)
- ROTATE d→e (каток = Schlittschuh laufen), e→f (ест братвурст = Bratwurst essen), f→d (девочка слушает рождественскую музыку = Weihnachtsmusik hören)
- SWAP g↔i (продавец вручает свёрток, прилавок с подарками = Geschenke kaufen ↔ пакет жареного миндаля = Gebrannte Mandeln essen)
- h OK

## 075 in-der-reinigung
- SWAP b↔c (красная зимняя куртка = Winterjacke ↔ свёрнутый ковёр = Teppich)
- DISCARD e (шторы — контент верный, но Goethe-текст сверху) + REGEN e (Vorhänge — оконные шторы, БЕЗ текста)
- SWAP g↔i (тёмный костюм на вешалке = Anzug ↔ галстуки = Krawatten)
- a,d,f,h OK

## 076 in-der-buchhandlung
- SWAP b↔c (лупа над уликами = Krimis ↔ книга с портретом на обложке = Biografien)
- ROTATE d→e (супергерой = Comics), e→f (книга-карта с путешественником и Эйфелевой башней = Reiseführer), f→d (перо и блокнот = Gedichte)
- MOVE h→g (кулинарная книга с пастой и салатом = Kochbücher); старая g (девочка поливает цветы — вообще не книга) в карантин
- REGEN h (Kinderbücher — стопка ярких детских книжек)
- DISCARD i (книги — контент верный, но Goethe-текст) + REGEN i (Sachbücher — научно-популярные книги с глобусом/лупой, БЕЗ текста)
- a OK

## 077 bei-der-polizei
- DISCARD a (заявление о краже велосипеда у стойки POLIZEI — контент верный, но Goethe-текст) + REGEN a (Fahrrad gestohlen — женщина у стойки полиции показывает картинку велосипеда, БЕЗ текста; надпись POLIZEI на стойке допустима? НЕТ — просить вообще без надписей)
- DISCARD e (оплата штрафа у стойки — контент верный, но Goethe-текст) + REGEN e (Strafzettel bezahlen — человек передаёт квитанцию и деньги кассиру, БЕЗ текста)
- остальные 7 OK

## 078 in-der-tanzschule
- все 9 OK

## 079 beim-fotografen
- DISCARD b (селфи в отпуске с пальмой — контент верный, но Goethe-текст на «открытке») + REGEN b (Urlaubsfotos — турист фотографирует пляж с пальмой, БЕЗ текста)
- DISCARD i (женщина говорит по телефону за столом — это не портретное фото) + REGEN i (Porträtfotos — фотограф снимает портрет человека на фоне студийного фона)
- a,c,d,e,f,g,h OK

## 080 im-schuhgeschaeft
- DISCARD f (беговые кроссовки — контент верный, но Goethe-текст сверху) + REGEN f (Laufschuhe — пара спортивных беговых кроссовок в движении, БЕЗ текста)
- остальные 8 OK

## 081 in-der-volkshochschule
- DISCARD b (женщина с камерой и фотопринадлежностями — контент верный, но Goethe-текст сверху) + REGEN b (Fotokurs — группа с фотоаппаратами слушает преподавателя, БЕЗ текста)
- остальные 8 OK

## 082 bei-der-autovermietung
- SWAP a↔b (красный кабриолет с парой = Cabrio ↔ городской автобус = Bus)
- MOVE f→g (красный спорткар = Sportwagen); старая g (маленькая красная машинка у паркомата — контент Kleinwagen, но Goethe-текст + тарабарщина «Gabbgetendscht LaePir Menerwelt») в карантин
- MOVE h→f (жёлтый фургон доставки с коробками = Transporter)
- REGEN h (Kleinwagen — маленькая компактная машинка, БЕЗ текста)
- c,d,e,i OK

## 083 beim-hautarzt
- все 9 OK (полная регенерация Grok здесь удалась)

## 084 in-der-tourist-information
- DISCARD c (зоопарк со львом и слоном — контент верный, но Goethe-текст сверху) + REGEN c (Zoo — животные в вольерах, посетители, БЕЗ текста)
- DISCARD h (сцена с певцами — контент верный, но Goethe-текст сверху) + REGEN h (Theater — театральная сцена с занавесом и актёрами, БЕЗ текста)
- остальные 7 OK

## 085 in-der-musikschule
- ROTATE b→i (клавиши/пианино = Klavier), d→b (барабанная установка = Schlagzeug), e→d (скрипка со смычком = Geige), c→e (мальчик с акустической гитарой = Gitarre); старая i (бонго — нет подходящего слота) в карантин автоматически
- DISCARD h (губная гармошка — нет такого варианта)
- REGEN c (Gesang — человек поёт в микрофон), h (Cello — ребёнок играет на виолончели со смычком)
- a,f,g OK

## 086 beim-physiotherapeuten
- все 9 OK (регенерация Grok удалась)

## 087 im-spielzeugladen
- ROTATE a→f (мишка с лейкой = Kuscheltier), f→i (семья за настольной игрой = Brettspiel), i→a (сборная модель самолёта = Baukasten)
- DISCARD h (второй мишка с лейкой — дубль a) и e (пазл — контент верный, но Goethe-текст)
- REGEN e (Fahrrad — детский велосипед), h (Puzzle — собирают пазл, БЕЗ текста)
- b,c,d,g OK

## 088 online-shopping-und-ruecksendung
- все 9 OK (регенерация Grok удалась)

## 089 beim-umzugsunternehmen
- DISCARD f (женщина пакует коробки — контент верный, но Goethe-текст сверху) + REGEN f (Kartons packen — человек складывает вещи в картонные коробки со скотчем, БЕЗ текста)
- остальные 8 OK

## 090 im-sportgeschaeft
- все 9 OK

## 091 in-der-apotheke
- SWAP e↔f (кружка травяного чая = Tee gegen Husten ↔ тюбик мази = Salbe)
- SWAP h↔i (фиолетовая бутылка с ложкой сиропа = Hustensaft ↔ градусник и больная с термометром = Fieberthermometer)
- a,b,c,d,g OK

## 092 in-der-eisdiele
- все 9 OK

## 093 beim-kinderarzt
- SWAP d↔f (держится за живот = Bauchschmerzen ↔ кашляет = Husten)
- остальные 7 OK

## 094 an-der-tankstelle
- все 9 OK

## 095 beim-tierfriseur
- DISCARD e (собака в тазу с шампунем — дубль d/g, окрашивания нет) + REGEN e (Fell färben — грумер красит шерсть собаки в яркий розовый/фиолетовый цвет, кисточка/краска, БЕЗ текста)
- остальные 8 OK (d = купание с бутылкой шампуня, g = простое мытьё губкой — различимы)

## 096 im-blumenladen
- все 9 OK (b = венок у могилы, g = траурный венок с чёрным бантом — различимы)

## 097 in-der-aenderungsschneiderei
- все 9 OK

## 098 im-wellnesshotel
- DISCARD i (фотореал: тёмно-зелёная арка с зеркальной тарабарщиной «IAIADD.L» — хлам, повтор ошибки первого прохода) + REGEN i (Im Pool schwimmen — человек плывёт в бассейне отеля, голубая вода, БЕЗ текста)
- остальные 8 OK

## 099 im-sprachcafe
- все 9 OK (флаги соответствуют языкам)

## 100 abschlussfeier-und-zukunftsplaene
- все 9 OK

# ВТОРОЙ ПРОХОД ЗАВЕРШЁН: 100/100 тем просмотрено

# ТРЕТИЙ ПРОХОД (2026-07-05)
Контекст: пользователь расставил 108 регенераций + Grok перезаписал 66 лишних файлов (целиком темы beim-hautarzt, beim-physiotherapeuten, online-shopping-und-ruecksendung, beim-umzugsunternehmen, bei-der-autovermietung, im-spielzeugladen, in-der-tourist-information и одиночные). OCR-скан (Vision) всех 900: 49 файлов с текстом, 3 с водяным знаком Goethe. Ниже вердикты по темам.
001 reisen-mit-der-bahn: i REGEN (кнопка «BUCHEN» на экране). Остальное OK.
002 wochenende-und-freizeit: OK.
003 im-restaurant-und-cafe: OK (новая h хороша).
004 schule-und-sprachkurs: OK (новая b — кубики+монета — хороша; f статистика на «бумаге» — стиль терпимый, смысл ясен).
005 wohnen-und-umzug: f REGEN (надписи «NEU» на полке и ярлыке). a: цифры 237 на счётчике — контекстная деталь, OK.
006 beim-arzt-und-in-der-apotheke: OK.
007 im-buero-und-arbeitsleben: OK (новые d DJ и i напитки хороши).
008 urlaub-und-reisen-planen: OK.
009 sport-und-fitness: OK (новая c йога-лотос отличима от d пилатес).
010 einkaufen-und-geschaefte: OK.
011 termine-und-telefon: OK (новая c страховка хороша; буквы на таблице зрения в i — контекст, OK).
012 tiere-und-haustiere: OK (новая f почта из ящика хороша).
013 verkehr-und-stadt: OK.
014 familienfeste: OK (новые f Location и i музыка хороши).
015 kino-theater-und-konzert: MOVE e→d (танцоры на сцене = Tanz-Aufführung); DISCARD d (сервировка стола — не в тему); REGEN e (Open-Air-Konzert: уличная сцена, группа, публика, вечер). b Filmfestival OK.
015/016 ПОПРАВКА (кросс-темная путаница Grok):
  kino-theater-und-konzert/d (сервировка стола) → kochen-und-essen/d (dekoriert den Tisch) ✓
  kochen-und-essen/d (опен-эйр концерт) → kino-theater-und-konzert/e (Open-Air-Konzert) ✓
  kino-theater-und-konzert/e (танцоры на сцене) → kino-theater-und-konzert/d (Tanz-Aufführung) ✓
  (прежний вердикт 015 «discard d, regen e» отменён — все три картинки пригодны, просто стояли не там)
016 kochen-und-essen: h DISCARD+REGEN (девочка за ноутбуком — не салат). Остальное OK.
017 garten-und-pflanzen: OK.
018 internet-und-technik: OK (новая h ноутбук хороша).
019 bank-und-geld: b (салат!) → ПЕРЕМЕСТИТЬ в kochen-und-essen/h (macht einen Salat); REGEN b (Online-Banking). Прежний вердикт «016h discard+regen» отменён — салат нашёлся. Новая h (деньги+домик) OK.
020 sprachen-lernen: OK.
021 auto-und-fahren: OK (новая c «Kein Benzin» — стрелка на E — отлично).
022 kleidung-und-mode: OK (цифры на евро-купюрах — контекст).
023 wetter-und-jahreszeiten: OK.
024 kinder-und-erziehung: OK (новые f футбол-дети-у-ворот и g девочка-рисует — хороши; e с «PONFRUN» на учебнике — мелочь, оставил).
025 bibliothek-und-lesen: g REGEN (книга «BIOGRAFIE» с портретом — дубль f и текст; нужны поваренные книги); i REGEN (дубль комикс-панелей из h; нужен детектив: лупа+следы). d карта+компас+чемодан OK.
026 friseur-und-schoenheit: i REGEN (снова массаж спины — дубль e; нужен крупный план покраски ногтей на руках). Остальное OK.
027 hotel-und-uebernachten: a REGEN (водяной знак «Goethe-Zertifikat A2 Hören (Modellsatz/Übungssatz» сверху). b/e/f/i новые — хороши, d Bus-Hotel терпимо.
028 post-und-pakete: e REGEN (надписи «SUMME», «BEZAHLT» на счёте — счёт с цифрами € без слов); g REGEN (наклейка «EILT!» на конверте — конверт с красным восклицательным знаком без слов). b/h новые хороши, i сумка в коробке OK.
029 vereine-und-hobbys: OK (новые a/b/c хороши; «9» на футболке — мелочь).
030 behoerden-und-dokumente: d REGEN (английское «JOB» на столе); e REGEN (штамп «FERTIG»). g вывеска «Standesamt» и c «PASSPORT» на обложке — функциональный контекст, оставил. Новые a TÜV и h Krankenkasse хороши.
031 beim-zahnarzt: OK (новая f кариес+бормашина отличная).
ПОЛИТИКА ТЕКСТА (3-й проход): REGEN — водяные знаки, тарабарщина, заметные декоративные слова (JOB, FERTIG, NEU, BUCHEN, EILT, SUMME/BEZAHLT, BIOGRAFIE, FOUND, START, OPEN); ОСТАВЛЯЮ — корректные функциональные надписи (вывеска Standesamt, PASSPORT на паспорте, буквы таблицы зрения, цифры на счётчике/купюрах/часах).
032 im-schwimmbad: OK (новые b/e/h хороши).
033 camping-und-wandern: OK (новые b/h хороши).
034 im-krankenhaus: OK (новая i хороша).
035 moebel-und-einrichtung: OK (новые b/d/h хороши).
036 studium-und-universitaet: OK.
037 bewerbung-und-job-suchen: OK.
038 babys-und-kleinkinder: g REGEN (готовка вместо рисования; нужен малыш, рисующий красками/мелками). d/f/i новые хороши.
039 am-flughafen: OK (новая i Мадрид хороша).
040 sommer-und-strand: SWAP a↔i (сёрфер и каякер лежат наоборот). Остальное OK.
041/042 КРОСС-СВОП: winter-und-skifahren/d (конверт с деньгами) ↔ geburtstag-und-geschenke/c (горнолыжник). Обе картинки правильные, лежат в чужих темах.
043 reise-mit-dem-auto: OK (новый Mercedes хорош, звезда-логотип допустима).
044 musik-und-konzerte: OK (новая c Country хороша).
045 im-museum: SWAP a↔d (динозавр лежит в Sport, кубки — в Naturkunde). Новые e/f/h/i хороши.
046/047 КРОСС-СВОП: am-bahnhof/g (планшет с видеомонтажом) ↔ computer-und-probleme/b (Фрауэнкирхе Дрезден). Обе правильные, лежат в чужих темах.
047 computer-und-probleme: c REGEN (просто клавиатура — не «программирует приложение»; нужен человек за ноутбуком + телефон с приложением); i REGEN (сетка блоков неотличима от c; нужен экран с макетом сайта — шапка/блоки). d/e/g хороши.
048 im-supermarkt: OK. OCR-хиты a «UUUU» (чешуя рыбы) и d «=00» (дырки сыра) — ложные, текста нет.
049 im-theater: a REGEN — «Faust» сгенерирован как жанровая комедия (женщина с метёлкой из перьев, мужчина у вазы), не Фауст; override: old scholar in dark robe with a big old book and a small red devil figure on a theater stage. d (стендап-комик) и i (детектив у кресла) — хороши. Остальное OK.
050 beim-tierarzt: OK. d (черепаха у ветеринара) и g (аквариум с рыбками) — регены встали хорошо. Животные все узнаваемы.
051 beim-augenarzt: OK. На i крошечное «Rx» на линзе — функциональная маркировка рецепта, по политике KEEP.
052 im-schwimmbad-und-sauna: OK. e (пловец по дорожкам) — реген встал отлично.
053/095/087/084/089 КРОСС-ЦЕПОЧКА (5 топиков, Grok разложил регены со сдвигом):
  - familienfeier-und-hochzeit/d («Auto schmücken») содержит покраску собаки в розовый = концепт beim-tierfriseur/e «Fell färben» → MOVE в tierfriseur/e.
  - beim-tierfriseur/e содержит пазл (мама+ребёнок) = концепт im-spielzeugladen/h «Puzzle» → MOVE в spielzeugladen/h.
  - im-spielzeugladen/h содержит упаковку коробок = концепт beim-umzugsunternehmen/f «Kartons packen» → MOVE в umzug/f.
  - beim-umzugsunternehmen/f содержит детский велосипед с доп. колёсами = концепт im-spielzeugladen/e «Fahrrad» → MOVE в spielzeugladen/e.
  - im-spielzeugladen/e содержит театральную сцену с кланяющимися актёрами = концепт in-der-tourist-information/h «Theater» → MOVE в tourist-info/h.
  - in-der-tourist-information/h — ВАТЕРМАРКА «Goethe-Zertifikat A2 Hören» (OCR подтверждён) → DISCARD (карантин pass3__).
  - familienfeier-und-hochzeit/d → REGEN: white wedding car decorated with ribbons, flowers and cans on strings (переиспользовать override из pass-2).
  Итого цепочка закрывает все 5 слотов без регена, кроме familienfeier/d.
087 im-spielzeugladen (остальное): i «Brettspiel» — на поле игры текст «START» (OCR) → по политике REGEN; override: family playing a colorful board game with dice and pawns, winding path of colored squares, no text anywhere. Остальные клетки OK.
084 in-der-tourist-information (остальное): OK; c (вход в зоопарк с силуэтами) — реген хорош.
089 beim-umzugsunternehmen (остальное): OK; g «P» на асфальте парковки — функциональная разметка, KEEP.
095 beim-tierfriseur (остальное): OK.
050 см. выше; 053 остальное: OK (d разобран в цепочке).
054 beim-optiker: a REGEN — реген-слот «Runde Brille» заполнен дубликатом b (красные ПРЯМОУГОЛЬНЫЕ очки, та же композиция); override: a single pair of perfectly ROUND circular eyeglasses with thin gold wire frames, lying on a plain table, nothing else. Остальное OK (b красные, h бифокальные, i золотые — различимы).
055 beim-fussball: OK. Цифры «9» на футболках — функциональные, KEEP. Клубные цвета соответствуют (Dortmund жёлто-чёрный, Werder зелёный, Hertha сине-белый, Köln бело-красный, Schalke синий, RB Leipzig красно-белый, HSV бело-синий, Frankfurt чёрно-красный, Bayern красный).
056 beim-baecker: e REGEN (повторно) — Grok опять нарисовал пончик С ДЫРКОЙ (конфликт с h «Donuts»); override усилить: a German Berliner: a solid round filled bun with absolutely NO hole in the middle, thick and puffy, dusted with white powdered sugar, red strawberry jam oozing out of a small opening on the SIDE, lying on a small plate. Остальное OK (a светло-коричневый цельнозерновой с семечками vs c чёрный Schwarzbrot — различимы).
057 wohnungssuche-und-makler: a DISCARD+REGEN — ватермарка «Goethe-Zertifikat A2 Hören (Modellsatz, Übungssatz)», Grok использовал СТАРЫЙ промпт; override (из pass-2): cozy farmhouse in the countryside with a tractor and a barn, no signs or text. c DISCARD+REGEN — точный дубликат b (та же кухня+сад); override: real-estate agent handing house keys to a happy family in front of a house, SOLD-style red ribbon but no text. h DISCARD+REGEN — точный дубликат g (пентхаус с бассейном); override: loft apartment interior with high ceiling, exposed red brick wall, metal pipes, big industrial windows. Остальное OK.
058 beim-friseur-und-beauty: OK, все 9 различимы.
059 beim-friseur-maenner: OK. b (синий ирокез, мальчик завязывает шнурок — причёска читается), g (короткий ёжик, чистит зубы — причёска читается). Приемлемо, причёски различимы.
060/061 КРОСС-3-ЦИКЛ (без регенов):
  - im-fitnessstudio/c («Klettern») содержит двух детей с красным фрисби = концепт im-park-und-erholung/f → MOVE в park/f.
  - im-park-und-erholung/f («Frisbee») содержит прогулку пожилой пары по дорожке = концепт park/i «Spazieren» → MOVE в park/i.
  - im-park-und-erholung/i («Spazieren») содержит скалодром = концепт fitnessstudio/c «Klettern» → MOVE в fitnessstudio/c.
060 остальное: OK. 061 остальное: OK.
062 auf-dem-wochenmarkt: OK.
063 in-der-autowerkstatt: OK (все 9 неисправностей читаются).
064 im-reisebuero: OK. h (город с собором) и i (пляж с зонтом) — регены встали отлично. OCR d/h — ложные (разметка дороги/фасады).
065 im-elektronikgeschaeft: OK. OCR g — ложный (клавиши ноутбука).
066 handwerker-im-haus: OK.
067 im-zoo: 3-ЦИКЛ внутри топика — регены встали со сдвигом: в g «Eisbären» лежат жирафы (концепт h), в h «Giraffen» — обезьяны (концепт i), в i «Affen» — белые медведи (концепт g). RENAME g→h, h→i, i→g. b «Tiger» встал верно; OCR-хит b «Vll./Dir.» — ложный (камни). Остальное OK.
068/075/076/077 КРОСС-ЦЕПОЧКИ:
  3-ЦИКЛ: in-der-kantine/g («Nur Nachtisch») содержит штору+девочку = концепт in-der-reinigung/e «Vorhänge» → MOVE в reinigung/e; in-der-reinigung/e содержит стопку детских книг с мишкой = концепт in-der-buchhandlung/h «Kinderbücher» → MOVE в buchhandlung/h; in-der-buchhandlung/h содержит красный пудинг с ванильным соусом = концепт kantine/g → MOVE в kantine/g. Цикл замкнут, без регенов.
  КРОСС-СВОП: in-der-buchhandlung/i («Sachbücher») содержит оплату штрафа в окошке = концепт bei-der-polizei/e «Strafzettel bezahlen» ↔ bei-der-polizei/e содержит книги с глобусом и лупой = концепт buchhandlung/i. SWAP между топиками.
069 im-fundbuero: OK.
075 in-der-reinigung (остальное): OK; OCR e «283» относился к старой картинке; после move проверить.
076 in-der-buchhandlung (остальное): OK (a,b,c,d,e,f,g хороши).
077 bei-der-polizei: b DISCARD+REGEN — на кошельке видна надпись «FOUND» (OCR), по политике текста; override: a woman handing a plain brown wallet to a police officer behind a police-station counter, absolutely no text or labels. Остальное OK (a с великом в облачке — хорош).
070 bei-der-versicherung: OK.
071 im-baumarkt: OK.
072 muelltrennung-und-recycling: OK. «3€» на ценнике second-hand — функциональное, KEEP.
073 im-tierheim: OK. OCR g — ложный (пузырьки аквариума).
074 auf-dem-weihnachtsmarkt: OK. OCR d «PLAY» — мелкая кнопка CD-плеера, функциональная, KEEP; «€» на ценнике i — KEEP.
078 in-der-tanzschule: OK (все 9 танцев различимы).
079 beim-fotografen: SWAP b↔i — регены встали наоборот: в b «Urlaubsfotos» студийный портрет с лампой/фоном (концепт i), в i «Porträtfotos» мальчик снимает пляж с пальмой (концепт b). Остальное OK.
080 im-schuhgeschaeft: OK. f (кроссовки) — реген встал хорошо.
081 in-der-volkshochschule: OK. b (группа с фотоаппаратами) — реген хорош.
082 bei-der-autovermietung: OK. OCR a «42» — номер маршрута автобуса, функциональный, KEEP. h (маленький круглый ситикар) — реген хорош.
083 beim-hautarzt: OK.
085 in-der-musikschule: SWAP c↔h — регены встали наоборот: в c «Gesang» виолончель у стула (концепт h), в h «Cello» поющий в микрофон мальчик (концепт c). Остальное OK.
086 beim-physiotherapeuten: OK. OCR b — ложный.
088 online-shopping-und-ruecksendung: OK.
090 im-sportgeschaeft: OK.
091 in-der-apotheke: OK.
092 in-der-eisdiele: OK (все вкусы различимы по цвету/топпингу).
093 beim-kinderarzt: OK.
094 an-der-tankstelle: c DISCARD+REGEN — жёлтая вывеска «OPEN» на двери (OCR, видное декоративное слово); override: a woman paying for snacks and a drink at a petrol-station shop counter, friendly cashier, shelves with colorful bottles behind, no signs or text anywhere. e «P AIR» на колонке подкачки — функциональная маркировка, KEEP. b мелкая этикетка канистры масла — KEEP. Остальное OK.
096 im-blumenladen: OK (b венок у могилы vs g похоронный венок с чёрным бантом — различимы контекстом).
097 in-der-aenderungsschneiderei: OK. OCR g/h — ложные (булавки/стежки).
098 im-wellnesshotel: OK. i (пловец в бассейне отеля с шезлонгами) — реген встал отлично. g Sauna vs h Dampfbad различимы (дерево+камни vs плитка+густой пар).
099 im-sprachcafe: OK. Все 9 флагов/символов корректны (мечеть для арабского, Эйфелева башня для французского).
100 abschlussfeier-und-zukunftsplaene: OK. Мелкое «Werkstatt» на ящике инструментов в g — функциональный контекст, KEEP.
ИТОГ 3-го прохода: 24 REGEN-слота; свопы внутри тем: 040 a↔i, 045 a↔d, 067 g→h→i→g, 079 b↔i, 085 c↔h; 8 кросс-темных цепочек/свопов (см. выше). Применение: apply_ops3.py, карантин pass3__.

## Пасс 3 — размещение регенераций (2026-07-05)

Grok Build сгенерировал 24 файла (31.jpg–54.jpg, сессия 019f3242) по tools/regen_prompts_t2.txt (24 строки). Список слотов был верный, но нумерация файлов перепутана у 19 из 24 — исправлено чистой перестановкой fix_grok_placement3.py (5 циклов, 19 перемещений). Итоговая проверка: 900/900 картинок на диске, OCR по всем 24 новым — ноль попаданий, визуально проверены все 18 затронутых тем (001, 005, 019, 025, 026, 027, 028, 030, 038, 047, 049, 054, 056, 057, 077, 087, 094 + wohnungssuche) — всё соответствует опциям. Регенерационных слотов не осталось. Пасс 3 закрыт.
