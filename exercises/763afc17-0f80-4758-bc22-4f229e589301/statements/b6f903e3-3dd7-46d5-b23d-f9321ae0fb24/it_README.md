Piano vacanze
===============

![Immagine holiday_period_503505](./holiday_period_503505.jpg) ![Immagine calendar3](./calendar3.png)

Le persone del nord che intendevano andare in spiaggia in Algarve e in Andalusia durante le vacanze di Pasqua, sono state sorprese da venti, rovesci e un clima molto freddo. _"Blancos llegaron y más blancos tornano"_, quindi sognano già una settimana o quindici giorni di ferie che intendono godersi a giugno, luglio, agosto o settembre, se il sussidio ferie non è in piena. Sembra proprio di no... Così, un gruppo di amici ottimisti sta già cercando di scegliere una settimana di vacanza, secondo le preferenze e le indisponibilità di ciascuno. Tale settimana (sette giorni di ferie) deve iniziare di lunedì e terminare la domenica successiva o, in alternativa, iniziare di sabato e terminare il venerdì successivo. Ogni membro del gruppo ha indicato una sequenza di periodi non sovrapposti e ha classificato ciascun periodo utilizzando numeri interi: `-1` per indicare l'indisponibilità e valori da `1` a `5` per esprimere preferenze, con `5` come livello massimo. Nei periodi non compresi è disponibile anche ma con gradino zero, se gli amici lo ritengono una buona idea o se non ci sono alternative. La classifica serve a segnare in modo analogo ogni giorno del periodo di riferimento. La settimana prescelta sarà quella frequentabile da tutti, dopo il 1 giugno (mercoledì) e che terminerà prima del 12 settembre 2011, e che avrà il punteggio massimo, considerando la somma dei punteggi accumulati nei sette giorni, dopo aver elaborato le preferenze di tutti. Se c'è più di una settimana possibile, sceglieranno quella più vicina, per timore che il freddo torni in vigore.


Compito
------

Vogliamo un programma che elabori le informazioni fornite e indichi la data in cui il gruppo inizierà la vacanza (o rilevi l'incoerenza se non c'è possibilità che vadano insieme).


Ingresso
-----

Una prima riga con il numero di membri del gruppo. Seguono un numero uguale di blocchi, ciascuno contenente le preferenze o l'indisponibilità di un membro del gruppo. Un blocco inizia con un numero intero positivo che denota il numero di periodi a cui il membro ha fatto riferimento e poi, su ogni riga, ha un quintetto nel formato _"giorno mese giorno mese preferenza"_, ad esempio, `16 6 30 6 3` (che rappresenterebbe il periodo dal 16 giugno al 30 giugno con preferenza 3 su ciascuno dei giorni di quel periodo; se fosse `16 6 30 6 -1`, indicherebbe che il membro non potrebbe andare in quel periodo).


Produzione
------

Se c'è una settimana in cui tutti possono, indicare la data di inizio della vacanza nel formato: numero del giorno seguito da uno spazio seguito da `giugno`, `luglio`, `agosto` o `settembre`. Altrimenti la parola "incoerente".


Esempi
--------

### Ingresso 1

```sh
3
due
10 7 7 9 -1
10 6 23 6 5
due
1 6 15 7 -1
2572674
1
23 6 25 6 -1
```

### Uscita 1

```sh
incoerente
```

### Ingresso 2

```sh
5
6
16 6 30 6 3
8 7 8 7 -1
973175
5 8 12 8 5
23 8 31 8 2
7 6 8 6 -1
1
1 6 31 7 4
1
18591
due
372084
1 9 9 9 -1
3
15 6 8 7 5
15 8 31 8 -1
7 9 10 9 5
```

### Uscita 2

```sh
9 luglio
```


Crediti
--------

ToPAS'2011 (F) - Ana Paula Tomás