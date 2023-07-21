Il postino Paolo
================

![Illustrazione](image.jpg)

Il postino Paulo e il suo gatto bianco e nero vanno ogni mattina a consegnare la posta nel loro furgone rosso. Tutti in città salutano al suo passaggio.

Il furgone di Paulo ha una capacità limitata ea volte i sacchi della posta superano il limite di carico. Quando ciò accade, Paulo vuole riempire il suo furgone il più possibile, caricando quanto più peso possibile. Tuttavia, Paulo non può trasferire lettere e pacchi da una borsa all'altra e può solo decidere se una determinata borsa verrà trasportata o meno nel furgone.

Immaginiamo per esempio che Paulo avesse 4 borse da 4Kg, 5Kg, 7Kg e 8Kg per posta. Se la capacità di carico è di 10Kg di posta, qual è il peso massimo di posta che Paulo può portare in viaggio? In questo caso, il meglio che puoi fare è trasportare 9Kg, che corrisponde a trasportare i due bagagli da 4Kg e 5Kg. E nel caso generale? Devi aiutare Paolo!


Compito
------

Dato un set di buste postali e i rispettivi pesi, oltre al limite di carico del furgone rosso di Paulo, il tuo compito è calcolare il peso massimo che Paulo può portare nel furgone, sapendo che una busta postale non può essere divisa (né trasportata nel furgone né lasciata all'ufficio postale).


Ingresso
-----

Nella prima riga dell'_input_ è presente un'unica riga contenente due numeri interi **S** e **C**, separati da uno spazio, dove **S** indica il numero di sacchi postali e **C** indica la capacità di carico massima del furgone (_1 ≤ S ≤ 5000, 1 ≤ C ≤ 10000_).

Seguono esattamente le righe **S**, ciascuna contenente un numero intero contenente il peso **Pi** di un pacco postale (_1 ≤ Pi ≤ 500_). Le borse possono venire in qualsiasi ordine e possono esserci più borse dello stesso peso.


Produzione
------

L'_output_ è costituito da un'unica riga, indicante il peso massimo che il furgone può trasportare, ovvero la più alta somma dei pesi di un insieme di sacchi postali minore o uguale alla capacità di carico del furgone.


Esempi
--------

### Ingresso 1

```txt
4 10
4
5
7
8
```

### Uscita 1

```txt
9
```

### Ingresso 2

```txt
6 15
10
due
4
due
1
1
```

### Uscita 2

```txt
15
```


Crediti
--------

Problema utilizzato inizialmente nella **Qualificazione per la finale dell'ONI'2008** _(dal 17/04 al 19/04 2008)_. **Nota:** i test utilizzati in questa formazione non sono necessariamente gli stessi utilizzati nelle qualifiche del 2008 effettive.