Trasporto di lusso
==================

![Immagine shuttle](./ shuttle.jpeg)


Solitamente gli animali vivi devono essere trasportati in stive climatizzate ma, nel caso del merluzzo destinato al Museo Marittimo di Ílhavo, potrebbe esserci stato anche qualche malinteso data la vicinanza del periodo natalizio. La verità è che alla fine sono state inviate nuove copie e queste sono arrivate sane e salve. Si intende verificare se è possibile trasportare un animale di una determinata specie da un nodo di origine ad un determinato nodo di destinazione e, in tal caso, indicare la **lunghezza minima** di un possibile percorso. La lunghezza è definita dal numero di sezioni del percorso. La specie ha restrizioni per quanto riguarda la temperatura minima e massima che supporta, quindi possono essere considerati solo percorsi compatibili con queste restrizioni.

  

Ingresso
-----

All'inizio c'è una linea con quattro numeri interi: i primi due designano la temperatura minima e massima sopportata dall'animale da trasportare, e i due successivi, il nodo di origine e il nodo di destinazione (questi nodi sono diversi). Segue una linea con il numero di nodi nella rete e il numero di sezioni (rami) nella rete. Di seguito la descrizione delle sezioni di rete. Ogni tratto è descritto su una riga da quattro numeri interi separati da spazi: i primi due identificano le estremità del tratto, il successivo la temperatura prevista in quel tratto e l'ultimo un costo associato al trasporto. Qualsiasi collegamento è bidirezionale. Potrebbero esserci nodi isolati. I nodi sono identificati da numeri interi consecutivi a partire da 1. Se è utile, puoi presumere che la rete non abbia più di 20000 nodi.
  

Produzione
------

Una riga con la parola "Sì" seguita da uno spazio e dalla durata minima del viaggio, se la rete consente il trasporto dell'animale tra l'origine e la destinazione. Altrimenti, una riga con la parola "Nao" (non accentata).


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
```

### Uscita 1

```txt
Sì 2
```

### Ingresso 2

```txt
-3 10 4 6
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
```

### Uscita 2

```txt
NO
```

### Ingresso 3

```txt
-2 21 6 4
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
```

### Uscita 3

```txt
Sì 3
```
  
Crediti
--------

DCC/FCUP 2013 (Prova pratica B) - Ana Paula Tomás