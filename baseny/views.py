import locale
from django.shortcuts import render

locale.setlocale(locale.LC_COLLATE, ("PL_pl", "UTF-8"))

# Create your views here.

def baseny(request):
    vals = (
        "Gdynia	Akademia Morska	25m	al. Jana Pawła II 3, 81-345 Gdynia	Pomorskie	glebokosc 3m od drugiej polowy basenu zalamanie	https://umg.edu.pl/basen	54.51835/18.55582",
        "Jaworzno	viasport Jaworzno	50 m / baby pool / 	Inwalidów Wojennych 22, 40-360 Jaworzno	Śląskie	zaleca się wynająć tor, pomocni i uprzejmi ratownicy, zagadać i zgłosić co się będzie robić. 	https://www.viasport.pl/basen-jaworzno-najlepsza-kryta-plywalnia.html	50.22191/19.23038",
        "Jelenia Góra	Kryta pływalnia KANS	25m 29stopni	Lwówecka 18 Jelenia Góra	Dolnośląskie	koniecznie trzeba sprawdzić harmonogram na stronie. Ratownicy w tygodniu są wspaniali i pomocni. Omijać w weekendy	http://www.kpswjg.pl/pl/centrum-sportowo-rehabilitacyjne	50.91392/15.73231",
        "Kórnik	Oaza Kórnickie centrum sportu i rekreacji	25m 28' + basen rekreacyjny 32'	ul. Ignacego Krasickiego 1 62-035 Kórnik	Wielkopolskie	19zł/h Ratownicy przyzwyczajeni to treningów free, wystarczy się przywitać z ratownikami	https://www.oaza.kornik.pl/plywalnia	52.25343/17.09137",
        "Łomianki (okolice Warszawy)	ICDS	25 m	UL.STASZICA 2, 05-092 ŁOMIANKI	Mazowieckie	Przywitanie, wyjaśnienie co robisz, że masz buddy - nikt nie robi problemów. Wieczorem można być całkowicie samemu. 	https://icds.pl/index.php/plywalnia-footer	52.34382/20.87494",
        "Mszczonów / okolice Warszawy	DeepSpot	głębokościowy 45 , tory - 20m / 32 stopnie	Warszawska 50, 96-320 Mszczonów	Mazowieckie	freediving bardzo friendly :) ale tu dopiero drogo! Niezbędny certyfikat freedivera do wejścia (albo dopłata za instruktora z DeepSpot lub wejście z instruktorem niezależnym na B2B)	https://www.deepspot.com/pl/	51.97784/20.52480",
        "Oborniki	Centrum Rekreacji Oborniki	25m	Czarnkowska 84, 64-600 Oborniki	Wielkopolskie	ratownik zgodził się na 50m pod wodą	www.centrumrekreacjioborniki.pl	52.65327/16.80620",
        "Płock	Kobylanka	only 25m, brak malego basenu, niecka od polowy płytka	aleja Floriana Kobylińskiego 28, 09-400 Płock	Mazowieckie	Tu Łukasz też może być buddy.  Basen stary, zielono na dnie ale ratownicy na lajcie pozwalaja trenowac.	http://www.mosirplock.pl/pl/kobylanka	52.55184/19.67826",
        "Płock	Podolanka	25m+ mały basen z woda 31 stopni dobry do STA	Czwartaków 6, 09-410 Płock	Mazowieckie	Jeśli potrzebny buddy to pracuje tam Łukasz Szypryt tel 797293999, ok 60zł/50min treningu. jest on trenerem pływania/ratownikiem, zna wszystkie procedury do postepowania przy BO i LMC free, umie poproswadzic trening STA i DYN, odlicza time z official top itp. Wyszkolony przez Zu Orca.	http://www.mosirplock.pl/pl/podolanka2	52.53391/19.75153",
        "Siemianowice Śląskie	Kompleks Sportowy Michał , MOSiR Pszczelnik	25m	ul. Elizy Orzeszkowej 1 , 41-103 Siemianowice Śl. 	Śląskie	przyjazny klimat, trzeba zgłosić ratownikowi i upewnić się, że można na free. 	http://www.mosir.siemianowice.pl/?kompleks-sportowy-michal-,736	50.32069/19.00853",
        "Siemianowice Śląskie	Zabytkowa pływalnia Miejska 	25m	ul. Śniadeckiego 11, 41-100 Siem-ce Śl.	Śląskie	mało zorientowani ratownicy, ale serdeczni, trzeba zgłosić i opisać co się będzie robiło i uważać na pozostałych użytkowników pływalni	pmsiemianowice.pl	50.30184/19.02856",
        "Sopot	Haffnera	25m	Jana Jerzego Haffnera 57	Pomorskie	25m, zimno, stary basen ale z klimatem :D 	https://mosir.sopot.pl/plywalnia.html	54.44967/18.56202",
        "Śrem	Śremski Sport .	25m 27' + 12,5m 32'	ul. Staszica 1a, 63-100 Śrem	Wielkopolskie	16zł/h dużo wolnych torów - poza godzinami 14-18 wtedy nauka pływania	https://sremskisport.pl/	52.07700/17.02454",
        "Warszawa	Centrum Sportu i Rekreacji Warszawskiego Uniwersytetu Medycznego (CSR WUM) 	50 m  oraz 25 m  	ul. Księcia Trojdena 2C-G, 02-109 Warszawa	Warszawa	można wszystko! ratownicy bardzo pilnują czy masz buddyego i są zorientowani w temacie, serdeczni. 	https://csr.wum.edu.pl/en	52.20582/20.98196",
        "Warszawa	Ośrodek sportowy Inflancka	50m oraz niecka do zabawy + jacuzzi, oraz odzielne płatne wejście na siłownię i sauny, parking płatny	ul. Inflancka 8, 00-189 Warszawa	Mazowieckie	konieczny czepek, przebywanie w strefie płatnej powyżej 60 minut dodatkowo płatne;-( używanie płetw, masek, fajek i innego sprzętu pływackiego oraz nurkowanie oraz wykonywanie ćwiczeń bezdechowych tylko za zgodą i nadzorem ratownika/ów (regulamin), lepiej mieć drugą osobę do asekuracji (mile widziane przez ratowników;-). 	https://aktywnawarszawa.waw.pl/pl/osrodki-sportowe/inflancka	52.25544/20.98970",
        "Warszawa	Warszawianka	50m + mały basen z ciepłą wodą	Dominika Merliniego 4, 02-511 Warszawa	Mazowieckie	Drogo w h***j 30zł ok za godz / ale akceptują multisporta plus mają fajne sauny	https://www.wodnypark.com.pl/	52.19499/21.02643",
        "Wrocław	Orbita	50m w weekendy oraz w godzinach 6:00-8:00 w dni powszednie. 2.5m głębokości. Po godzinie 8:00 basen jest dzielony na dwie częscie po 25m. Jedna część zostaje na głebokości 2.5m a druga jest podnoszona do 1.4m. Temperatura 27°C. Jest również basen rozgrzewkowy. 25m, 31°C, głębokość 1.2m.	Wejherowska 34, 54-239 Wrocław	Dolnośląskie	Zakaz używania typowego balastu na pasie. Poza tym nigdy nie było z niczym problemów. Ratownicy bardzo przychylnie podchodzą do freediverów.	https://plywalniaorbita.spartan.wroc.pl/index.php/plywalnia	51.13265/16.98847",
        "Wągrowiec	Aquapark Wągrowiec	25 m	Kościuszki 49, 62-100 Wągrowiec	Wielkopolskie	16zł/h / 28zł/2h / ratownicy zgadzili się na 50m pod wodą	http://www.aquapark.wagrowiec.eu/	52.81704/17.20073",
        "Żyrardów	AQUA Żyrardów	25m oraz niecka do zabawy, bicze wodne itd, w niej 30 stopni	Rotmistrza Witolda ileckiego 25, 96 3 Żyrardów	Mazowieckie	super przyjaźni ratownicy, zorientowani w temacie, pomogą i będą Cię szczególnie obserwować dla bezpieczeństwa, zgłosić, że będzie się robiło APNOE	aqua.zyrardow.pl	52.06763/20.44727",
        )
    # make sure cities are sorted and according to Polish alphabet
    vals = sorted(vals, key=locale.strxfrm)
    keys = ('miasto', 'nazwa', 'szczegoly', 'adres', 'wojewodztwo', 'uwagi', 'www', 'geo')
    # OSM zoom level, 19 max, 14 city level
    zoom = 17
    table = list()
    for item in vals:
        elements = dict((k, v) for k, v in zip(keys, item.split('\t')))
        # additional reprocessing of geo to get proper OSM marker
        # leaving in data simple lat/lon due to possible interoperability
        mark = elements["geo"].split("/")
        elements["geo"] = f"?mlat={mark[0]}&mlon={mark[1]}#map={zoom}/{elements['geo']}"
        table.append(elements)

    my_var = { 'pools': table, 'zoom': zoom }


    return render(request, 'baseny/baseny.html', context=my_var)
