Lista studentów
==============================

![Ilustracja](05.jpg)

Zadanie
------

Mając listę uczniów z 3 polami (imię, nazwisko i stopień uzyskany w danej jednostce programowej), Twoim zadaniem jest posortowanie listy w żądanej kolejności, która może być rosnąca lub malejąca z jednego z 3 pól.

Wejście
-----

W pierwszym wierszu wejścia znajduje się pojedyncza liczba wskazująca rodzaj zlecenia, którego należy użyć. Ta liczba może być:

* **1:** Sortuj według oceny w kolejności malejącej. W przypadku remisu sortuj według imienia, aw przypadku nowego remisu sortuj według nazwiska.
* **2:** Sortuj według rosnącej (alfabetycznej) kolejności imion. W przypadku remisu posortuj dane według kolejności ich wprowadzania.

W drugim wierszu wejścia znajduje się liczba **N** (1 ≤ N ≤ 20 000) odpowiadająca liczbie uczniów.

Poniżej znajduje się opis uczniów, po jednym dla każdej linii, w formacie „IMIĘ\_NAZWISKO UWAGI”. Imię i nazwisko składa się z ciągu wielkich liter, po których następują małe litery, bez spacji i maksymalnie 30 liter. Ocena jest liczbą całkowitą z przedziału od 0 do 20 (włącznie).

Wyjście
------

Dane wyjściowe muszą składać się z **N** wierszy, zawierających listę uczniów w żądanej kolejności (po jednym w wierszu, w tym samym formacie co dane wejściowe).

Przykłady
--------

### Wejście 1

```txt
1
7
Joaquim Oliveira 10
Antonio Campos 17
Jorge Tavares 8
Luis Araujo 12
Karol Pimenta 11
Carlos Araujo 11
Sonia Soares9
```

### Wyjście 1

```txt
Antonio Campos 17
Luis Araujo 12
Carlos Araujo 11
Karol Pimenta 11
Joaquim Oliveira 10
Sonia Soares9
Jorge Tavares 8
```

### Wejście 2

```txt
dwa
7
Joaquim Oliveira 10
Antonio Campos 17
Jorge Tavares 8
Luis Araujo 12
Karol Pimenta 11
Carlos Araujo 11
Sonia Soares9
```

### Wyjście 2

```txt
Antonio Campos 17
Karol Pimenta 11
Carlos Araujo 11
Joaquim Oliveira 10
Jorge Tavares 8
Luis Araujo 12
Sonia Soares9
```