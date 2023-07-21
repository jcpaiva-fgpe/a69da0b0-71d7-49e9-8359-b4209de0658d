Elenco studenti
==============================

![Illustrazione](05.jpg)

Compito
------

Dato un elenco di studenti con 3 campi (nome, cognome e voto conseguito in una data unità curriculare), il tuo compito è ordinare l'elenco nell'ordine richiesto, che può essere crescente o decrescente da uno dei 3 campi.

Ingresso
-----

Sulla prima riga dell'input è presente un singolo numero che indica il tipo di ordine da utilizzare. Quel numero può essere:

* **1:** Ordina per voto in ordine decrescente. In caso di parità ordinare per nome e in caso di nuova parità ordinare per cognome.
* **2:** Ordina per ordine crescente (alfabetico) del nome. In caso di pareggio, ordina in base all'ordine in cui sono stati inseriti nell'input.

Nella seconda riga dell'input c'è un numero **N** (1 ≤ N ≤ 20.000) che corrisponde al numero di studenti.

Di seguito la descrizione degli studenti, uno per ogni riga, nel formato "NOME\_NOME COGNOME NOTE". Il nome e il cognome sono costituiti da una sequenza di una lettera maiuscola, seguita da lettere minuscole, senza spazi, e con un massimo di 30 lettere. Il voto è un numero intero compreso tra 0 e 20 (inclusi).

Produzione
------

L'output deve essere composto da **N** righe, elencando gli studenti nell'ordine richiesto (uno per riga, nello stesso formato dell'input).

Esempi
--------

### Ingresso 1

```txt
1
7
Joaquim Oliveira 10
Antonio Campos 17
Jorge Tavares 8
Luis Araujo 12
Carlo Pimenta 11
Carlo Araujo 11
Sonia Soares9
```

### Uscita 1

```txt
Antonio Campos 17
Luis Araujo 12
Carlo Araujo 11
Carlo Pimenta 11
Joaquim Oliveira 10
Sonia Soares9
Jorge Tavares 8
```

### Ingresso 2

```txt
due
7
Joaquim Oliveira 10
Antonio Campos 17
Jorge Tavares 8
Luis Araujo 12
Carlo Pimenta 11
Carlo Araujo 11
Sonia Soares9
```

### Uscita 2

```txt
Antonio Campos 17
Carlo Pimenta 11
Carlo Araujo 11
Joaquim Oliveira 10
Jorge Tavares 8
Luis Araujo 12
Sonia Soares9
```