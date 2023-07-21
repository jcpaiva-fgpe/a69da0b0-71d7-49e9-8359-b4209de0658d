Luksusowy transport
==================

![Transfer obrazu](./ shuttle.jpeg)


Zwykle żywe zwierzęta muszą być transportowane w klimatyzowanych ładowniach, ale w przypadku dorsza przeznaczonego do Muzeum Morskiego w Ílhavo mogło dojść do nieporozumienia, biorąc pod uwagę bliskość okresu Bożego Narodzenia. Prawda jest taka, że ​​w końcu wysłano nowe kopie, które dotarły całe i zdrowe. Ma na celu zweryfikowanie, czy możliwy jest transport zwierzęcia określonego gatunku z węzła źródłowego do określonego węzła docelowego, a jeśli tak, wskazanie **minimalnej długości** możliwej trasy. Długość jest określona liczbą odcinków trasy. Gatunek ma ograniczenia dotyczące minimalnej i maksymalnej temperatury, którą obsługuje, więc można brać pod uwagę tylko trasy zgodne z tymi ograniczeniami.

  

Wejście
-----

Na początku znajduje się wiersz z czterema liczbami całkowitymi: pierwsze dwie oznaczają minimalną i maksymalną temperaturę utrzymywaną przez transportowane zwierzę, a kolejne dwie węzeł początkowy i docelowy (węzły te są różne). Następuje linia z liczbą węzłów w sieci i liczbą sekcji (odgałęzień) w sieci. Poniżej znajduje się opis sekcji sieci. Każda sekcja jest opisana w wierszu czterema liczbami całkowitymi oddzielonymi spacjami: dwie pierwsze identyfikują końce sekcji, kolejne oczekiwaną temperaturę w tej sekcji, a ostatnia koszt związany z transportem. Każde łącze jest dwukierunkowe. Mogą występować pojedyncze węzły. Węzły identyfikowane są kolejnymi liczbami całkowitymi zaczynającymi się od 1. Jeśli jest to przydatne, można założyć, że sieć ma nie więcej niż 20000 węzłów.
  

Wyjście
------

Wiersz ze słowem „Tak”, po którym następuje spacja i długość minimalnej podróży, jeśli sieć zezwala na transport zwierzęcia między miejscem pochodzenia a miejscem przeznaczenia. W przeciwnym razie wiersz ze słowem „Nao” (bez akcentu).


Przykłady
--------

### Wejście 1

```txt
-2 25 1 6
6 10
1 4 10 35
3 5 -22 30
1 2 -27 50
5 2 20 51
3 2 3 27
2 4 -1 5
5 6 9 20
1 5 30 20
4 6 25 450
6 3 -15 40
```

### Wyjście 1

```txt
Tak 2
```

### Wejście 2

```txt
-3 10 4 6
6 10
1 4 10 35
3 5 -22 30
1 2 -27 50
5 2 20 51
3 2 3 27
2 4 -1 5
5 6 9 20
1 5 30 20
4 6 25 450
6 3 -15 40
```

### Wyjście 2

```txt
NIE
```

### Wejście 3

```txt
-2 21 6 4
6 10
1 4 10 35
3 5 -22 30
1 2 -27 50
5 2 20 51
3 2 3 27
2 4 -1 5
5 6 9 20
1 5 30 20
4 6 25 450
6 3 -15 40
```

### Wyjście 3

```txt
Tak 3
```
  
Kredyty
--------

DCC/FCUP 2013 (Test praktyczny B) — Ana Paula Tomás