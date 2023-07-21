Famiglia di Vito
=================

![Illustrazione](06.jpg)

Il gangster _Vito Deadstone_ sta per trasferirsi a Porto. Ha una grande famiglia lì, tutti vivono in Avenida da Boavista. Siccome intende visitare assiduamente i suoi parenti, cerca una casa vicino a loro.

Vito vuole ridurre al minimo la distanza totale per tutti i membri della famiglia e ti ha ricattato per farti scrivere un problema per risolvere il suo problema.

Le posizioni consentite per le case sono date dal numero della casa. La distanza tra due posizioni nei numeri _i_ e _j_ è data da **dij\=|i-j|** (differenza tra _i_ e _j_).


Compito
------

Dato un insieme di numeri civici, che indicano dove vive ciascuno dei membri della famiglia di Vito, il tuo compito è capire in quale numero dovrebbe vivere Vito per minimizzare la distanza per tutti loro, cioè il numero che minimizza la somma delle distanze a tutti i membri della famiglia. Devi solo indicare il valore di questa somma.


Ingresso
-----

Nella prima riga dell'input c'è un unico numero che indica **N** (1 ≤ N ≤ 20.000), il numero dei membri della famiglia.

Sulla seconda riga sono riportati i numeri di porta dei membri della famiglia, separati da un unico spazio. I numeri sono sempre compresi tra 1 e 50.000 (inclusi). Questi numeri possono essere in qualsiasi ordine e può succedere che due o più membri della famiglia vivano sullo stesso numero di porta (la somma minima deve includere le distanze da tutti i membri della famiglia).


Produzione
------

L'output deve essere costituito da un'unica riga con un numero intero indicante la somma minima delle distanze da tutti i componenti della famiglia, ovvero la somma del numero della porta dove Vito deve abitare.


Esempi
--------

### Ingresso 1

```txt
3
264
```

### Uscita 1

```txt
4
```

### Ingresso 2

```txt
4
6 2 4 2
```

### Uscita 2

```txt
6
```


Crediti
--------

Questo problema è essenzialmente una traduzione/adattamento del [problema 10041](http://uva.onlinejudge.org/external/100/10041.html) del giudice online UVA.