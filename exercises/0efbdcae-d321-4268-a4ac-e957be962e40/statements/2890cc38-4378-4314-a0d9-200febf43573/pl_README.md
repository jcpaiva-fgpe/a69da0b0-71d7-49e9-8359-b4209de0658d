Mrożony Dorsz
====================

![Obraz 220px-Portret_Cod_Cod](./220px-Portret_Cod_Cod.jpg)


Na początku grudnia 2012 roku trzydzieści dorszy z Norwegii zmierzających do pierwszego w kraju akwarium z dorszami w Íhavo przybyło zamrożone. Według źródła wiadomości (tvi24) „ryby, około 30 centymetrów i 1,5 kilograma, przybyły martwe, zawinięte w bloki lodu, najwyraźniej z powodu zaniedbań w transporcie, długiej podróży z Alesund do Ílhavo, między samolotem a transportem drogowym”. Niewykluczone, że w transporcie lotniczym zostały poddane działaniu temperatur minus 50 stopni.

W odniesieniu do tego konkretnego przypadku jesteśmy zainteresowani rozważeniem sieci transportowej z informacją o spodziewanej temperaturze na każdym odcinku i określeniem dla wskazanych tras przewidywanej minimalnej i maksymalnej temperatury.


Wejście
-----

Pierwszy wiersz pokazuje liczbę węzłów w sieci oraz liczbę sekcji (odgałęzień) w sieci.

Poniżej znajduje się opis sekcji sieci. Każda sekcja jest opisana w wierszu czterema liczbami całkowitymi oddzielonymi spacjami: dwie pierwsze identyfikują końce sekcji, kolejne oczekiwaną temperaturę w tej sekcji, a ostatnia koszt związany z transportem. Każde łącze jest dwukierunkowe. Mogą występować pojedyncze węzły. Węzły identyfikowane są kolejnymi liczbami całkowitymi zaczynającymi się od 1. Jeśli jest to przydatne, można założyć, że sieć ma nie więcej niż 20000 węzłów.

Na koniec informacja o trasach. Zawsze będziesz mieć opis przynajmniej jednej trasy. Każda ścieżka jest opisana w linii i jest zdefiniowana przez odpowiednią sekwencję węzłów. Pierwsza liczba całkowita w tym wierszu to liczba węzłów w sekwencji. Musi założyć, że wszystkie podane trasy są prawidłowe, przy czym pierwszy węzeł wskazuje początek trasy, a ostatni jej koniec. Ścieżka narzędzia może zawierać powtarzające się węzły, ale nie w kolejnych pozycjach. Dane kończą się na 0.


Wyjście
------

Dla każdej trasy będzie linia z odpowiednią minimalną i maksymalną temperaturą, oddzielona spacją.


Przykład
-------

### Wejście

```txt
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
9 5 1 4 2 3 6 4 2 1
5 1 4 2 3 6
2 1 5
5 2 3 6 4 2
7 5 6 4 1 5 2 3
0
```

### Wyjście

```txt
-27 30
-15 10
30 30
-15 25
3 30
```

  
Kredyty
--------

DCC/FCUP 2013 (Test praktyczny A) — Ana Paula Tomás