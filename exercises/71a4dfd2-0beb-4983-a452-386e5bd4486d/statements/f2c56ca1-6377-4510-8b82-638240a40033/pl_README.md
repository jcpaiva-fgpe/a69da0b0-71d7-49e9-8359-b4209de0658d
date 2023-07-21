Listonosz Paweł
================

![Ilustracja](obraz.jpg)

Listonosz Paulo i jego czarno-biały kot jadą każdego ranka, aby dostarczyć pocztę w swojej czerwonej furgonetce. Wszyscy w mieście machają, gdy przechodzi.

Furgonetka Paulo ma ograniczoną pojemność i czasami torby z pocztą przekraczają limit ładowności. Kiedy tak się dzieje, Paulo chce maksymalnie wypełnić swoją furgonetkę, biorąc na siebie jak najwięcej ciężaru. Jednak Paulo nie może przenosić listów i paczek z jednej torby do drugiej i może jedynie zdecydować, czy dana torba będzie przewożona furgonetką.

Wyobraź sobie na przykład, że Paulo miał w poczcie 4 torby o wadze 4Kg, 5Kg, 7Kg i 8Kg. Jeśli ładowność poczty wynosi 10 kg, jaka jest maksymalna waga poczty, którą Paulo może zabrać w podróż? W takim przypadku najlepsze, co możesz zrobić, to przewieźć 9 kg, co odpowiada przewożeniu dwóch toreb 4 kg i 5 kg. A w przypadku ogólnym? Trzeba pomóc Pawłowi!


Zadanie
------

Mając zestaw toreb pocztowych i ich wagę, a także dopuszczalną ładowność czerwonej furgonetki Paulo, Twoim zadaniem jest obliczenie maksymalnego ciężaru, jaki Paulo może przewozić furgonetką, wiedząc, że paczki pocztowej nie można podzielić (ani przewieźć furgonetką, ani zostawić na poczcie).


Wejście
-----

W pierwszym wierszu _wejścia_ znajduje się pojedynczy wiersz zawierający dwie liczby całkowite **S** i **C** oddzielone spacją, gdzie **S** oznacza liczbę worków pocztowych, a **C** oznacza maksymalną ładowność furgonetki (_1 ≤ S ≤ 5000, 1 ≤ C ≤ 10000_).

Następują dokładnie **S** wierszy, z których każdy zawiera liczbę całkowitą zawierającą **Pi** wagę worka pocztowego (_1 ≤ Pi ≤ 500_). Worki mogą być dostarczane w dowolnej kolejności i może być wiele worków o tej samej wadze.


Wyjście
------

Pole _wyjście_ składa się z pojedynczej linii, wskazującej maksymalną masę, jaką może przewozić furgonetka, czyli najwyższą sumę mas zestawu worków pocztowych, która jest mniejsza lub równa ładowności furgonetki.


Przykłady
--------

### Wejście 1

```txt
4 10
4
5
7
8
```

### Wyjście 1

```txt
9
```

### Wejście 2

```txt
6 15
10
dwa
4
dwa
1
1
```

### Wyjście 2

```txt
15
```


Kredyty
--------

Problem pierwotnie użyty w **Kwalifikacjach do finału ONI'2008** _(17.04 do 19.04.2008)_. **Uwaga:** Testy użyte w tym szkoleniu niekoniecznie są takie same, jak te użyte w rzeczywistych kwalifikacjach w 2008 roku.