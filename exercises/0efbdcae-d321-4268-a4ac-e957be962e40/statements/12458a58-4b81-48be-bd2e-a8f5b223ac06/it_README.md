Baccalà surgelato
====================

![Immagine 220px-Portrait_of_Cod](./220px-Portrait_of_Cod.jpg)


All'inizio di dicembre 2012, trenta merluzzi norvegesi diretti al primo acquario di merluzzo del paese a Íhavo sono arrivati ​​congelati. Secondo una fonte di notizie (tvi24), "il pesce, circa 30 centimetri e 1,5 chili, è arrivato morto, avvolto in blocchi di ghiaccio, apparentemente per negligenza nel trasporto, un lungo viaggio da Alesund a Ílhavo, tra aereo e trasporto su gomma". È possibile che siano stati sottoposti a temperature di meno 50 gradi durante il trasporto aereo.

Per quanto riguarda questo caso specifico, ci interessa considerare una rete di trasporto con informazioni sulla temperatura prevista in ogni tratta e determinare, per i percorsi indicati, la temperatura minima e massima prevista.


Ingresso
-----

La prima riga mostra il numero di nodi nella rete e il numero di sezioni (rami) nella rete.

Di seguito la descrizione delle sezioni di rete. Ogni tratto è descritto su una riga da quattro numeri interi separati da spazi: i primi due identificano le estremità del tratto, il successivo la temperatura prevista in quel tratto e l'ultimo un costo associato al trasporto. Qualsiasi collegamento è bidirezionale. Potrebbero esserci nodi isolati. I nodi sono identificati da numeri interi consecutivi a partire da 1. Se è utile, puoi presumere che la rete non abbia più di 20000 nodi.

Infine, ci sono informazioni sui percorsi. Avrai sempre la descrizione di almeno un percorso. Ogni percorso è descritto in una linea ed è definito dalla corrispondente sequenza di nodi. Il primo numero intero su quella riga è il numero di nodi nella sequenza. Deve presumere che tutti i percorsi dati siano validi, con il primo nodo che indica l'origine del percorso e l'ultimo la sua fine. Un percorso utensile può contenere nodi ripetuti ma non in posizioni consecutive. I dati terminano con 0.


Produzione
------

Per ogni percorso sarà presente una riga con la corrispondente temperatura minima e massima, separate da uno spazio.


Esempio
-------

### Ingresso

```txt
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
9 5 1 4 2 3 6 4 2 1
5 1 4 2 3 6
2 1 5
5 2 3 6 4 2
7 5 6 4 1 5 2 3
0
```

### Produzione

```txt
-27 30
-15 10
30 30
-15 25
3 30
```

  
Crediti
--------

DCC/FCUP 2013 (Prova pratica A) - Ana Paula Tomás