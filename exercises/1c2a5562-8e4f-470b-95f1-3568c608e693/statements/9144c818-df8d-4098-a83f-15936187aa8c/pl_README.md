Cięcia budżetowe
==================

![Obraz skarbonki](./pigbox.jpg)

Ze względu na cięcia budżetowe unikanie długich podróży nie ma już sensu. Tak więc w kontynuacji problemu „luksusowego transportu” celem jest raczej ustalenie, czy możliwe jest przewiezienie zwierzęcia z węzła źródłowego do węzła docelowego bez wydawania więcej niż określona kwota. Kwota do zapłaty dla każdego odcinka to koszt wskazany dla tego odcinka (który jest zawsze liczbą całkowitą i podawany w euro). Pod uwagę mogą być brane tylko trasy, które gwarantują warunki narzucone w zakresie temperatur tolerowanych przez zwierzę.


Wejście
-----
  
Na początku znajduje się wiersz z czterema liczbami całkowitymi: pierwsze dwie oznaczają minimalną i maksymalną temperaturę utrzymywaną przez transportowane zwierzę, a kolejne dwie węzeł początkowy i docelowy (węzły te są różne). Następnie jest liczba węzłów w sieci i liczba sekcji (rozgałęzień) w sieci, po których następuje liczba całkowita reprezentująca liczbę scenariuszy do rozważenia, a następnie taka sama liczba linii. Każda z tych linii zawiera maksymalną kwotę, jaką możesz wydać (wiadomo, że ta kwota jest zawsze mniejsza niż 10 000 euro). Zawsze jest przynajmniej jeden scenariusz.


Wyjście
------

Przy każdym scenariuszu słowo Tak, jeśli możliwe jest wykonanie transportu bez przekroczenia wskazanej kwoty. W przeciwnym razie będzie miał Nao (nie zaakcentowany).


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
8
5000
50
101
400
300
112
111
110
```

### Wyjście 1

```txt
Tak
NIE
NIE
Tak
Tak
Tak
Tak
NIE
```


### Wejście 2

```txt
\-3 10 4 6
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
1
3000
```

### Wyjście 2

```txt
NIE
```

  
Kredyty
--------

DCC/FCUP 2013 (egzamin praktyczny C) - Ana Paula Tomás