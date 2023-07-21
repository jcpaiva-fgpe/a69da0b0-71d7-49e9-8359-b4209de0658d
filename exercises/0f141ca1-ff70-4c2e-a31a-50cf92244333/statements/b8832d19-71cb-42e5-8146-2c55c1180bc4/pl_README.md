Odbijanie
==========

![Ilustracja](obraz.jpg)

W najpiękniejszym ogrodzie w mieście można znaleźć kilka ciągów ponumerowanych kamieni. Grupa dzieci spędza niekończące się godziny, skacząc z kamienia na kamień w zabawnej grze, którą wymyślili. Pojedynczo przyjaciele przechodzą przez sekwencję kamieni, dodając liczby, na które „nadepnęli” prawą stopą i odejmując liczby, na które „nadepnęli” lewą stopą. Wygrywa dziecko, któremu uda się przebyć trasę, która da początek największej „ilości”.

Oczywiście dzieci nie zawsze idą najlepszą drogą, wśród tak wielu śmiechu i tak wielu prób rozproszenia się nawzajem. Jednak patrząc na ścieżkę, nie można oprzeć się wrażeniu, że byłbyś w stanie dokładnie obliczyć najlepszy wynik (ilość) możliwy do osiągnięcia. I właśnie to proponujesz zrobić.

Kamienie można traktować jako ciąg dodatnich liczb całkowitych, na przykład:

| 7 | 14| 8| 2| 19| 20| 17| 13| 4| 8| 5|
|---|---|---|---|---|---|---|---|---|---|---|

Aby nie przynosić korzyści wyższym dzieciom, które mają dłuższe nogi i dzięki temu mogą skakać dalej, dzieci określają z góry największy rozmiar **K** możliwych skoków. Skok mierzony jest liczbą mówiącą o tym, ile kamieni „postępuje naprzód”. Na przykład, jeśli są na kamieniu numer 14, skok o rozmiarze 1 prowadzi ich do kamienia o numerze 8, skok o rozmiarze 2 prowadzi ich do kamienia o numerze 2, a skok o rozmiarze 3 prowadzi ich do kamienia o numerze 19.

Ścieżka zawsze zaczyna się w miejscu bezpośrednio przed pierwszym kamieniem, a dziecko może zdecydować, czy zacząć prawą, czy lewą stopą i może przeskoczyć dowolny kamień w zasięgu najwyższego skoku. Na przykład, jeśli **K** wynosi 3, dziecko decyduje się skoczyć jedną nogą na pierwszy kamień (z numerem 7), na drugi kamień (z numerem 14) lub na trzeci kamień (z numerem 8). Następnie dziecko musi użyć drugiej stopy, to znaczy, jeśli skakało lewą nogą, przechodzi do prawej stopy i odwrotnie, i znowu może skoczyć maksymalnie **K** kamieni (i minimum 1 kamień). Trwa to tak długo, aż uda ci się "wylądować" w przestrzeni poza kamieniami, przy czym skoki wykonuje się obowiązkowo do przodu (od lewej do prawej), nie ma możliwości wykonania skoku "do tyłu".

Poniższe rysunki wskazują trzy możliwe ścieżki, którymi można podążać, jeśli rozmiar najwyższego możliwego skoku wynosi 3, oraz odpowiedni wynik, przy czym ostatnia ścieżka odpowiada rozpoczęciu od prawej stopy i zawsze przy użyciu najwyższego możliwego skoku.

| -7| 14| +8| -2| 19|+20| 17|-13| 4| 8| +5|
|---|---|---|---|---|---|---|---|---|---|---|

Wynik = 11

| 7|+14| -8| +2| 19| 20|-17|+13| 4| -8| 5|
|---|---|---|---|---|---|---|---|---|---|---|

Wynik = -4

| 7| 14| +8| 2| 19|-20| 17| 13| +4| 8| 5|
|---|---|---|---|---|---|---|---|---|---|---|

Wynik = -8

Z tych trzech ścieżek pierwsza jest najlepsza, ponieważ ma najwyższy wynik, 11 = -7+8-2+20-13+5. Ale jakie byłoby najlepsze wyjście ze wszystkich możliwych sposobów?


Zadanie
------

Biorąc pod uwagę liczbę całkowitą **K**, oznaczającą rozmiar największego możliwego skoku, oraz ciąg **N** dodatnich liczb całkowitych zapisanych na kamieniach, Twoim zadaniem jest znalezienie najlepszego wyniku, jaki może osiągnąć dziecko podążając ścieżką zgodnie z zasadami opisanymi powyżej.


Wejście
-----

W pierwszym wierszu _input_ znajduje się liczba całkowita **K**, wskazująca rozmiar największego możliwego skoku.

W drugim wierszu znajduje się liczba całkowita **N** wskazująca liczbę kamieni do rozważenia (to znaczy rozmiar sekwencji).

Następuje dokładnie **N** linii, każda z pojedynczą liczbą całkowitą **Vi**, wskazującą wartość zapisaną na i-tym kamieniu. Kamienie pojawiają się w kolejności, w jakiej pojawiają się w sekwencji, od lewej do prawej (czyli od początku do końca).

Przykładowe dane wejściowe odpowiadają liczbom użytym w opisie problemu.


Wyjście
------

_Wyjście_ musi składać się z jednego wiersza zawierającego liczbę całkowitą wskazującą najlepszy możliwy wynik do osiągnięcia.

Dzieci zaczynają skakać tuż przed pierwszym kamieniem i kończą po minięciu ostatniego kamienia. Pamiętaj, że skacząc, dzieci dodają numery, na które nadepną prawą nogą i odejmują te, na które nadepną lewą nogą, i mogą zdecydować, którą stopą użyją w pierwszym skoku. W każdym skoku mogą przeskoczyć od 1 do K kamieni do przodu.


Ograniczenia
----------

Następujące limity są gwarantowane we wszystkich przypadkach testowych, które zostaną wprowadzone do programu:

**1 ≤ K ≤ 200**

Największy rozmiar skoku

**1 ≤ N ≤ 1000**

Liczba kamieni na ścieżce

**1 ≤ Vi ≤ 1000**

Wartości zapisane na kamieniach


Przykład
-------

### Wejście

```txt
3
11
7
14
8
dwa
19
20
17
13
4
8
5
```

### Wyjście

```txt
36
```


Kredyty
--------

Jest to wersja z bardzo obniżonymi limitami zadania z **Ogólnopolskiego Finału ONI'2012** (w prawdziwym finale N mogło wzrosnąć do 1 miliona). Wydział Informatyki Wydziału Nauk Uniwersytetu w Porto. _(18 maja 2012)_