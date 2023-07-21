Rodzina Vito
=================

![Ilustracja](06.jpg)

Gangster _Vito Deadstone_ ma zamiar przeprowadzić się do Porto. Ma tam dużą rodzinę, wszyscy mieszkają na Avenida da Boavista. Ponieważ zamierza wytrwale odwiedzać swoich bliskich, szuka domu blisko nich.

Vito chce zminimalizować całkowitą odległość dla wszystkich członków rodziny i szantażował cię, abyś napisał problem, który rozwiąże jego problem.

Dozwolone pozycje dla domów są określone przez numer domu. Odległość między dwoma miejscami w liczbach _i_ i _j_ jest określona wzorem **dij\=|i-j|** (różnica między _i_ a _j_).


Zadanie
------

Mając zestaw numerów domów, wskazujący, gdzie mieszka każdy z członków rodziny Vito, Twoim zadaniem jest dowiedzieć się, pod którym numerem Vito powinien mieszkać, aby zminimalizować odległość dla nich wszystkich, czyli liczbę, która minimalizuje sumę odległości do wszystkich członków rodziny. Należy jedynie wskazać wartość tej sumy.


Wejście
-----

W pierwszym wierszu wejścia znajduje się pojedyncza liczba oznaczająca **N** (1 ≤ N ≤ 20 000), czyli liczbę członków rodziny.

W drugim wierszu znajdują się numery drzwi członków rodziny, oddzielone pojedynczym odstępem. Liczby zawsze mieszczą się w przedziale od 1 do 50 000 (włącznie). Numery te mogą występować w dowolnej kolejności i może się zdarzyć, że dwóch lub więcej członków rodziny mieszka pod tym samym numerem drzwi (minimalna suma musi uwzględniać odległości do wszystkich członków rodziny).


Wyjście
------

Wyjście musi składać się z jednego wiersza z liczbą całkowitą wskazującą minimalną sumę odległości do wszystkich członków rodziny, czyli sumę numeru drzwi, w których Vito ma mieszkać.


Przykłady
--------

### Wejście 1

```txt
3
2 6 4
```

### Wyjście 1

```txt
4
```

### Wejście 2

```txt
4
6 2 4 2
```

### Wyjście 2

```txt
6
```


Kredyty
--------

Ten problem jest zasadniczo tłumaczeniem/adaptacją [problemu 10041](http://uva.onlinejudge.org/external/100/10041.html) z UVA Online Judge.