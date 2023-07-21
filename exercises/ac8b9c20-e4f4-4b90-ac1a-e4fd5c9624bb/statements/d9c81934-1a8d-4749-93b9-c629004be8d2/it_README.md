Laboratorio informatico
===========================

Come responsabile dell'unità curriculare di programmazione, devi scegliere un laboratorio informatico dove svolgere le valutazioni pratiche. Nell'edificio del tuo dipartimento ci sono diversi laboratori con un numero variabile di computer. Per valutare quanti più studenti possibile, il tuo compito è trovare il laboratorio con il maggior numero di computer. Entrare fisicamente in ognuna delle stanze sarebbe molto faticoso. Per fortuna l'amministrazione ha a disposizione una mappa dei reparti, quindi è possibile calcolare il risultato in automatico.

Si consideri, ad esempio, la mappa nella figura seguente. Il miglior laboratorio è quello mostrato in grigio, con 15 computer.

![Illustrazione](image.png)


Compito
------

Data la descrizione ASCII della mappa del dipartimento, il tuo compito è trovare il laboratorio con il maggior numero di computer, riportando il numero di computer in quel laboratorio.


Ingresso
-----

Nella prima riga sono presenti due numeri **L** e **C**, che indicano rispettivamente il numero di righe e colonne della rappresentazione ASCII della mappa del dipartimento (_1 ≤ L,C ≤ 100_).

Seguono esattamente le righe **L**, ciascuna con i caratteri **C** che indicano la mappa. I caratteri possono essere:

* 'C': un computer
* 'P': una porta
*   '#': un muro
* ' ': uno spazio libero

La mappa è completamente racchiusa da muri, e ciascuno dei laboratori è completamente racchiuso da muri e/o porte.


Produzione
------

Dovrebbe essere stampata una singola riga, contenente il numero di computer nel laboratorio che ha il maggior numero di computer.


Esempio
-------

### Ingresso

```txt
12 26
############################
#C C C # # C C C C C #
# # # C C C C C #
#      #   P             #
# # # C C C C C #
##PP### #################
# #
####PP#######PP########
# C C # # #
# # # #
# DO DO # # DO #
############################
```

### Produzione

```txt
15
```