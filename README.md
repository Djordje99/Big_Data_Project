Analiza podataka, njihovih veza i mogućnosti smanjena dimenzionalnosti
i primena algoritma mašinskog učenja nad skupom podataka


• Opis problema

Problem koje je izabran da se rešava je analiza podataka ankete američkih
stanovnika o fizičkim i psihičkim stanjima kako bi se pronašla veza tih stanja i bolesti
dijabetes. Razlog izabranog problema je taj što se život savremenog čoveka
poprilično oštetio po pitanju zdravstvenog stanja. Štetu po zdravlje nam čini hrana
koju unosimo ,koja je nutritivno osiromašena shodno masovnoj proizvodnji, vazduh,
koji zagađen zbog industrije, nezdrave navike koje čovek poseduje koje predstavljaju
manjak aktivnosti, konzumiranje alkohola i cigara. Sve to može da utiče na
progresiju i stvaranje bolesti dijabetes. Nakon analize podataka potrebno je naći
vezu između njih i pokušati pronaći povezanosti među njima. Kao poslednju fazu
projekata treba napraviti model koji će moći da predvidi postojanje bolesti uz
pomoć podataka.


• Skup podataka

Skup podataka koji će se koristiti u projektu je anketa iz 2015 godine sa teritorije
Severne Amerike. Zavistan podatak ovog skupa podataka je da li osoba ima
dijabetes, pre-dijabetes ili nema. Zavisni podaci su:

    • HighBP – visok krvni pritisak, visok pritisak se smatra kada je gornji
    pritisak veći od 130 ili donji pritisak veći od 80.
    • HighChol – visok holesterol, visokim holesterolom se smatra kada je 240
    mg/dl.
    • CholCheck – provera holesterola u poslednjih 5 godina
    • BMI – index telesne mase, računa se po formuli BMI = kg/m2. Gde je kg
    telesna masa u kilogramima, a m visina u metrima.
    • Smoker – da li je osoba pušač. Ako je osoba za života konzumirala više od
    100 cigareta smatra se da jeste.
    • Stroke – da li je osoba imala moždani udar.
    • HeartDiseaseorAttack – da li osoba ima problema sa srcem
    • PhysActivity – da li je osoba imala fizičku aktivnost u poslednjih 30 dana,
    ne uključujući posao.
    • Fruits – da li osoba konzumira barem jedno voće dnevno.
    • Veggies – da li osoba konzumira barem jedno povrće dnevno.
    • HvyAlcoholConsump – da li osoba konzumira veću količinu alkohola. Za
    muškarce 14 ili više pića nedeljno, za žene 7 ili više.
    • AnyHealthcare – da li osoba poseduje zdravstveno osiguranje.
    • NoDocbcCost – da li je osoba imala potrebu da ide kod doktora u
    poslednjih 12 meseci ali nije zbog cene pregleda.
    • GenHlth – procena sveukupnog zdravstvenog stanja na skali od 1 –5.
    • MentHlth – da li je osoba u poslednjih 30 dana bila pod stresom,
    depresijom ili imala problema sa emocijama. Na skali od 1 do 30.
    • PhysHlth – da li je osoba u poslednjih 30 dana ima neku povredu. Na skali
    od 1 do 30.
    • DiffWalk – da li osoba ima problema sa hodanjem
    • Sex – pol osobe
    • Age – starost osobe. Na skali od 1 – 13. Uz pomoć skale 1 = 18-24 9 = 60-
    64 13 = 80.
    • Education – koja je edukativna sprema osobe na skali od 1 – 6.
    • Income - godišnji prihod osobe. Od 1 – 8.

Adresa sa kog su preuzeti podaci se na nalazi na sledećem linku: anketa.


• Algoritmi

Kako bi se odradilo smanjenje dimenzionalnosti, potrebno je koristiti algoritme koji
su izrađeni za taj posao. Neki od alkoritama koji će se koristiti su:

    • Neighborhood Components Analysis - ovaj algoritam predstavlja masiski
    algoritam učenja za metričko učenje. Uči linearnu transformaciju i pokušava
    da poboljša klasifikaciju.

    • Principal Component Analysis - je najpopularnmiji algoritam za smanjenje
    dimenzionalnosti. Radi na principu osmatranja varijacaija vrednosti i uz
    pomoć visine vrednosti utvrđuje odvajanje od ostalih klasa i na taj način
    smanjuje dinemzionalnost.

    • Principal Component Analysis - algoritam pokušava da razdvoji odbirke po
    vrednosti i na taj način pronađe linearnu kombinaciju variabli koje ostvaruju
    maksimalno odvajanje od ostalih klasa i minimalno odvajanje od istih
    odbiraka u jednoj klasi.

    Kako bi se utvrdilo koje smanjenje dimenzionalnosti daje najbolje rezultate na ovom
    primeru podataka potrebno ih je sve primeniti i uporediti rezultate.
    Nakon što se uradi uspešno smanjenje dimezionalnosti postrebno je da se kreira
    model koji će uraditi predikciju ,na osnovu priloženih podataka, da li osoba pati od
    bolesti dijabetes ili ne.


• Tehnologije

Programski jezik koji je odlučen da se koristi je python. Ralog njegovog biranja jeste
taj što pruža mnogobrojne biblioteke koje omogućavaju da se ovaj projekat
implementira. Neke od tih biblioteka su pandas i sklearn. Pandas kao biblioteka
pruža da se podaci u čitaju i da se kreira data frame. Dok sklearn omogućava
smanjenje dimenzionalnosti sa gore navedenim algoritmima. Takođe omogućava da
se kreira model koji će vršiti predikciju. Okruženje koje će se koristiti za izradu
projekta je Visual Studio Code.


• Cilj

Cilj projekta je da se analiziraju podaci i prikažu. Potrebno je da se pronaće
povezanost nezavisnih podataka sa zavisnim. Nakon analize podataka i pronalaženja
veza koje se pojavljuju lsedeci korak je grafički prikaz dobijenih rezultata. Aplikacija
će posedovati UI koji će omogućiti korisniku da pronađe željene analize podataka i
grafički ih prikaže. Nakon prikaza podataka potrebno je odraditi smanjenje
dimentionalnosti. Smanjenje dimenzionalnosti će se raditi po algoritmima
navedenim u predašnjem tekstu. Potrebno je utvrditi najbolji način da se smanji
dimenzionalnost i prikazati dobijene rezultate u vidu efikasnosti. Nakon
pronalaženja najefikasnije algoritma za smanjenje dimenzionalnosti potrebno je
kreirati model i odrediti nmjegovu tačnost predikcije.