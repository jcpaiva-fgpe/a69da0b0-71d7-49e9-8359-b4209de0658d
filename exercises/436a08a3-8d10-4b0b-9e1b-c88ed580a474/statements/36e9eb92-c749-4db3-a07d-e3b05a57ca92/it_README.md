Condominio ideale
================

![](a.jpg)

Committente Dott. Ivan Oliver Irwin (I.O.I.) sta progettando una nuova serie di edifici da collocare sul nuovo viale della città. Gli edifici saranno disposti contigui lungo il viale e insieme formeranno il condominio più lussuoso ed elegante delle vicinanze.

Per facilitare la vita, il consiglio comunale locale ha suddiviso il viale in lotti ben definiti della stessa dimensione. Il dottore. IOI vuole realizzare un condominio con più fabbricati, che possono occupare più lotti, ma in ogni caso devono essere lotti consecutivi, cioè devono essere contigui tra loro. Non c'è limite al numero di lotti da utilizzare (può occupare un solo lotto o al contrario occupare fino all'intero viale) ma il Comune ha autorizzato solo la costruzione di un unico condominio.

Il problema è che certi appezzamenti di terreno sul viale hanno al suolo rocce molto dure e sono molto più difficili da trivellare per la costruzione di edifici. In alcuni tratti del viale è così complicato e costoso trivellare che la costruzione in quel tratto sarebbe addirittura costosa. Il dottore. IOI può stimare il profitto che otterresti costruendo su ogni lotto e questo può aiutarti a decidere su quali lotti è meglio costruire il tuo condominio.

Ad esempio, immagina che il viale sia suddiviso in 8 lotti con i seguenti profitti stimati (in centinaia di milioni di euro):

| -1 | 4 | -2 | 5 | -5 | 2 | -20| 6 |
|----|----|----|----|----|----|----|----|

Come il Dott. IOI può costruire un solo condominio e questo deve essere fatto in lotti contigui, il massimo che potrebbe fare sarebbe fare un profitto di 7, costruendo 4 -2 5 in lotti contigui.


Compito
------

Il tuo compito è aiutare il Dr. IOI e digli il condominio ideale che dovrebbe costruire. Dati i profitti per ogni divisione, devi capire quale serie di divisioni consecutive dà il profitto più alto. Ovviamente l'utile di un insieme di rate è pari alla somma degli utili stimati di ciascuna rata.


Ingresso
-----

Nella prima riga dell'input è presente un numero **N** (1 ≤ N ≤ 1000000) che rappresenta il numero di lotti del viale da considerare.

Segue un'altra riga contenente esattamente **N** numeri interi separati da un unico spazio, che indicano i profitti stimati per ogni rata. Sia **L** il profitto stimato di una rata. Quindi \-2000 ≤ L ≤ 2000 è garantito.


Produzione
------

L'output è costituito da una singola riga contenente il profitto massimo che Dr. IOI può ottenere.


campione
------

### Ingresso

```txt
8
-1 4 -2 5 -5 2 -20 6
```

### Produzione

```txt
7
```


Crediti
--------

Selezione dei concorrenti portoghesi - Olimpiadi internazionali di informatica 2005
_(12 agosto 2005)_