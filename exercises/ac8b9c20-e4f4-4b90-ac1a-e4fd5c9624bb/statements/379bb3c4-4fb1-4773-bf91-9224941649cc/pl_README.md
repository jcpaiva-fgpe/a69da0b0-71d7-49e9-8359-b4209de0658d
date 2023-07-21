Laboratorium komputerowe
===========================

Jako osoba odpowiedzialna za programową jednostkę programową musisz wybrać pracownię komputerową, w której będziesz mógł przeprowadzać ewaluacje praktyczne. W budynku Twojego wydziału znajduje się kilka laboratoriów ze zróżnicowaną liczbą komputerów. Aby ocenić jak najwięcej uczniów, Twoim zadaniem jest znalezienie pracowni z największą liczbą komputerów. Fizyczne wchodzenie do każdego z pomieszczeń byłoby bardzo męczące. Na szczęście administracja dysponuje mapą działów, więc możliwe jest automatyczne obliczenie wyniku.

Rozważmy na przykład mapę na poniższym rysunku. Najlepsze laboratorium to to pokazane na szaro, z 15 komputerami.

![Ilustracja](obraz.png)


Zadanie
------

Biorąc pod uwagę opis ASCII mapy działu, Twoim zadaniem jest znalezienie laboratorium z największą liczbą komputerów, podając liczbę komputerów w tym laboratorium.


Wejście
-----

W pierwszym wierszu znajdują się dwie liczby **L** i **C**, oznaczające odpowiednio liczbę wierszy i kolumn reprezentacji ASCII mapy departamentu (_1 ≤ L,C ≤ 100_).

Następują dokładnie linie **L**, każda ze znakami **C** wskazującymi mapę. Postacie mogą być:

* „C”: komputer
* „P”: port
*   '#': ściana
* ' ': wolne miejsce

Mapa jest całkowicie otoczona ścianami, a każde z laboratoriów jest całkowicie otoczone ścianami i/lub drzwiami.


Wyjście
------

Należy wydrukować jedną linię zawierającą liczbę komputerów w laboratorium, które ma najwięcej komputerów.


Przykład
-------

### Wejście

```txt
12 26
###########################
#C C C # # C C C C C #
# # # C C C C C #
#      #   P             #
# # # C C C C C #
###PP### ################
# #
###PP### #####PP########
# C C # # #
# # # #
# C C # # C #
###########################
```

### Wyjście

```txt
15
```