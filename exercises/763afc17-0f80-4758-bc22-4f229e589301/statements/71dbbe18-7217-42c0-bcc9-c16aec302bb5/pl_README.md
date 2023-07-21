Plan urlopowy
===============

![Obrazek holiday_period_503505](./holiday_period_503505.jpg) ![Obraz kalendarz3](./calendar3.png)

Ludzi z północy, którzy w okresie Świąt Wielkanocnych zamierzali wybrać się na plażę w Algarve i Andaluzji, zaskoczyły wiatry, przelotne opady i bardzo zimna pogoda. _„Blancos llegaron y más blancos come back”_, więc marzą już o tygodniu lub piętnastu dniach wakacji, którymi planują się cieszyć w czerwcu, lipcu, sierpniu lub wrześniu, jeśli dofinansowanie do wakacji nie będzie zalewać. Wygląda na to, że nie... Tak więc grupa optymistycznych przyjaciół już próbuje wybrać tydzień wakacji, zgodnie z preferencjami i niedostępnością każdego z nich. Ten tydzień (siedem dni urlopu) musi zaczynać się w poniedziałek i kończyć w następną niedzielę lub alternatywnie zaczynać się w sobotę i kończyć w następny piątek. Każdy członek grupy wskazał sekwencję nienakładających się na siebie okresów i sklasyfikował każdy okres za pomocą liczb całkowitych: `-1` oznacza niedostępność oraz wartości od `1` do `5` określające preferencje, przy czym `5` oznacza poziom maksymalny. W okresach nieuwzględnionych jest również dostępny, ale z zerowym poziomem preferencji, jeśli znajomi uznają to za dobry pomysł lub jeśli nie ma alternatywy. Klasyfikacja służy do podobnej punktacji każdego dnia okresu, o którym mowa. Wybranym tygodniem będzie ten, do którego każdy będzie mógł się udać, po 1 czerwca (środa) i kończący się przed 12 września 2011 r., i który ma maksymalną liczbę punktów, biorąc pod uwagę sumę punktów zebranych w ciągu siedmiu dni, po przetworzeniu preferencji wszystkich. Jeśli jest więcej niż jeden możliwy tydzień, wybiorą najbliższy, żeby mrozy nie wróciły ze zdwojoną siłą.


Zadanie
------

Chcemy, aby program przetworzył podane informacje i wskazał datę rozpoczęcia wakacji przez grupę (lub wykrył niezgodność, jeśli nie ma możliwości wspólnego wyjazdu).


Wejście
-----

Pierwszy wiersz z liczbą członków grupy. Następuje taka sama liczba bloków, z których każdy zawiera preferencje lub niedostępność członka grupy. Blok zaczyna się dodatnią liczbą całkowitą oznaczającą liczbę okresów, do których odnosi się członek, a następnie w każdym wierszu znajduje się kwintet w formacie _"dzień miesiąc dzień miesiąc preferencja"_, na przykład `16 6 30 6 3` (co oznaczałoby okres od 16 czerwca do 30 czerwca z preferencją 3 w każdym dniu tego okresu; gdyby to było `16 6 30 6 -1`, oznaczałoby to, że członek nie mógł iść w tym okresie okres).


Wyjście
------

Jeśli istnieje tydzień, w którym każdy może podać datę rozpoczęcia urlopu w formacie: numer dnia, po którym następuje spacja, po której następuje „czerwiec”, „lipiec”, „sierpień” lub „wrzesień”. W przeciwnym razie słowo „niespójne”.


Przykłady
--------

### Wejście 1

```sz
3
dwa
10 7 7 9 -1
10 6 23 6 5
dwa
1 6 15 7 -1
25 7 26 7 4
1
23 6 25 6 -1
```

### Wyjście 1

```sz
niespójny
```

### Wejście 2

```sz
5
6
16 6 30 6 3
8 7 8 7 -1
9 7 31 7 5
5 8 12 8 5
23 8 31 8 2
7 6 8 6 -1
1
1 6 31 7 4
1
1 8 5 9 1
dwa
3 7 20 8 4
1 9 9 9 -1
3
15 6 8 7 5
15 8 31 8 -1
7 9 10 9 5
```

### Wyjście 2

```sz
9 lipca
```


Kredyty
--------

ToPAS'2011 (F) - Ana Paula Tomás