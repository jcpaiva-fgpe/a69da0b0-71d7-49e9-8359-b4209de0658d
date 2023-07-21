rimbalzare
==========

![Illustrazione](image.jpg)

Nel giardino più bello della città si trovano diverse sequenze di pietre numerate. Un gruppo di bambini trascorre interminabili ore saltando di pietra in pietra, in un divertente gioco che hanno inventato. Uno alla volta, gli amici ripercorrono la sequenza delle pietre, sommando i numeri su cui "calpestano" con il piede destro e sottraendo i numeri su cui "calpestano" con il piede sinistro. Vince la partita il bambino che riesce a compiere il percorso che dà luogo alla maggior "quantità".

Certo, non sempre i bambini vanno nel migliore dei modi, tra tante risate e tanti tentativi di distrarsi a vicenda. Tuttavia, guardando il percorso, non puoi fare a meno di pensare che saresti in grado di calcolare con precisione il miglior risultato (quantità) possibile ottenere. Ed è esattamente quello che ti proponi di fare.

Le pietre possono essere pensate come una sequenza di numeri interi positivi, come i seguenti:

| 7 | 14| 8| 2| 19| 20| 17| 13| 4| 8| 5|
|---|---|---|---|---|---|---|---|---|---|---|

Per non avvantaggiare i bambini più alti, che hanno le gambe più lunghe e quindi possono saltare più lontano, i bambini definiscono in anticipo la dimensione **K** massima dei salti possibili. Un salto è misurato da un numero che dice quante pietre "fanno un passo avanti". Ad esempio, se si trovano sulla pietra numero 14, un salto di dimensione 1 li porta alla pietra numero 8, un salto di dimensione 2 li porta alla pietra numero 2 e un salto di dimensione 3 li porta alla pietra numero 19.

Un percorso inizia sempre nello spazio immediatamente prima della prima pietra e il bambino può decidere se iniziare con il piede destro o sinistro, e può saltare qualsiasi delle pietre alla portata del salto più alto. Ad esempio, se **K** è 3, il bambino decide di saltare con un piede alla prima pietra (con il numero 7), alla seconda pietra (con il numero 14) o alla terza pietra (con il numero 8). Poi, il bambino deve usare l'altro piede, cioè se ha saltato con il piede sinistro, passa al piede destro, e viceversa, e di nuovo può saltare solo un massimo di **K** pietre (e un minimo di 1 pietra). Si continua così fino a quando si riesce ad "atterrare" in uno spazio esterno alle pietre, con i salti fatti obbligatoriamente in avanti (da sinistra a destra), non potendo saltare "all'indietro".

Le figure seguenti indicano tre possibili percorsi da seguire se la dimensione del salto più alto possibile è 3, e il rispettivo risultato, con l'ultimo percorso corrispondente a partire con il piede destro e utilizzando sempre il salto più alto possibile.

| -7| 14| +8| -2| 19|+20| 17|-13| 4| 8| +5|
|---|---|---|---|---|---|---|---|---|---|---|

Risultato = 11

| 7|+14| -8| +2| 19| 20|-17|+13| 4| -8| 5|
|---|---|---|---|---|---|---|---|---|---|---|

Risultato = -4

| 7| 14| +8| 2| 19|-20| 17| 13| +4| 8| 5|
|---|---|---|---|---|---|---|---|---|---|---|

Risultato = -8

Di questi tre percorsi, il primo è il migliore, in quanto ha il risultato più alto, 11 = -7+8-2+20-13+5. Ma quale sarebbe la migliore via d'uscita tra tutte le vie possibili?


Compito
------

Dato un intero **K**, che indica la dimensione del salto più grande possibile, e una sequenza di **N** interi positivi scritti su pietre, il tuo compito è trovare il miglior risultato che un bambino può ottenere seguendo un percorso secondo le regole sopra descritte.


Ingresso
-----

Sulla prima riga di _input_ compare un numero intero **K**, che indica la dimensione del salto più grande possibile.

Sulla seconda riga compare un intero **N** che indica il numero di pietre da considerare (ovvero la dimensione della sequenza).

Seguono esattamente **N** righe, ciascuna con un solo intero **Vi**, indicante il valore scritto sulla pietra i-esima. Le pietre arrivano nell'ordine in cui appaiono nella sequenza, da sinistra a destra (cioè dall'inizio alla fine).

L'esempio di input corrisponde alle cifre utilizzate nella dichiarazione del problema.


Produzione
------

L'_output_ deve essere costituito da una singola riga contenente un numero intero che indica il miglior risultato possibile da ottenere.

I bambini iniziano a saltare poco prima della prima pietra e finiscono quando superano l'ultima pietra. Ricorda che, quando saltano, i bambini sommano i numeri che calpestano con il piede destro e sottraggono quelli che calpestano con il piede sinistro, e possono decidere quale piede usare nel primo salto. In ogni salto possono saltare tra 1 e K pietre in avanti.


Restrizioni
----------

I seguenti limiti sono garantiti in tutti i casi di test che verranno inseriti nel programma:

**1 ≤ K ≤ 200**

La dimensione del salto più grande

**1 ≤ N ≤ 1.000**

Numero di pietre sul percorso

**1 ≤ Vi ≤ 1000**

Valori scritti su pietre


Esempio
-------

### Ingresso

```txt
3
11
7
14
8
due
19
20
17
13
4
8
5
```

### Produzione

```txt
36
```


Crediti
--------

Questa è una versione con limiti molto ridotti di un problema della **Finale Nazionale ONI'2012** (nella finale reale il N potrebbe arrivare fino a 1 milione). Dipartimento di Informatica, Facoltà di Scienze dell'Università di Porto. _(18 maggio 2012)_