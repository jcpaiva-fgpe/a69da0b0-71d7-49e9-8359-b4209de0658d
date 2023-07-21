Tagli del budget
==================

![Immagine salvadanaio](./pigbox.jpg)

A causa dei tagli al budget, non è più rilevante evitare lunghi viaggi. Pertanto, nella continuazione del problema del "trasporto di lusso", l'obiettivo è piuttosto sapere se sia possibile o meno portare l'animale da un nodo di origine a un nodo di destinazione senza spendere più di una certa cifra. Per ogni tratta l'importo da pagare è il costo indicato per quella tratta (che è sempre un numero intero ed espresso in euro). Possono essere presi in considerazione solo percorsi che garantiscano le condizioni imposte in merito alle temperature tollerate dall'animale.


Ingresso
-----
  
All'inizio c'è una linea con quattro numeri interi: i primi due designano la temperatura minima e massima sopportata dall'animale da trasportare, e i due successivi, il nodo di origine e il nodo di destinazione (questi nodi sono diversi). Poi c'è il numero di nodi nella rete e il numero di sezioni (rami) nella rete, seguito da un numero intero che rappresenta il numero di scenari da considerare, e quindi un numero uguale di linee. Ognuna di queste righe contiene l'importo massimo che potresti spendere (si sa che tale importo è sempre inferiore a 10000 euro). C'è sempre almeno uno scenario.


Produzione
------

Per ogni scenario, la parola Sì se è possibile effettuare il trasporto senza superare l'importo indicato. Altrimenti avrà Nao (non accentuato).


Esempi
--------

### Ingresso 1

```txt
-2 25 1 6
6 10
1 4 10 35
35-2230
1 2 -27 50
5 2 20 51
3 2 3 27
24-15
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

### Uscita 1

```txt
SÌ
NO
NO
SÌ
SÌ
SÌ
SÌ
NO
```


### Ingresso 2

```txt
\-3 10 4 6
6 10
1 4 10 35
35-2230
1 2 -27 50
5 2 20 51
3 2 3 27
24-15
5 6 9 20
1 5 30 20
4 6 25 450
6 3 -15 40
1
3000
```

### Uscita 2

```txt
NO
```

  
Crediti
--------

DCC/FCUP 2013 (prova pratica C) - Ana Paula Tomás