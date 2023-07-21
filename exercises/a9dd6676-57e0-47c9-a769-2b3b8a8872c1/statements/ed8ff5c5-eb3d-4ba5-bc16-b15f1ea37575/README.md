A Família de Vito
=================

![Ilustração](06.jpg)

O gangster _Vito Deadstone_ está prestes a mudar-se para o Porto. Ele tem uma grande família por lá, todos a viverem na Avenida da Boavista. Uma vez que ele pretende visitar assiduamente os seus familiares, ele está à procura de uma casa próxima deles.

Vito quer minimizar a distância total para todos os familiares e fez chantagem contigo para que escrevas um problema para resolver o seu problema.

As posições permitidas para as casas são dadas pelo número da porta. A distância entre duas casas nos números _i_ e _j_ é dada por **dij\=|i-j|** (diferença entre _i_ e _j_).


Tarefa
------

Dada um conjunto de números de porta, indicando onde mora cada um dos familiares de Vito, a tua tarefa é descobrir qual o número onde Vito deve morar de movo a minimizar a distância para todos eles, ou seja, o número que minimiza a soma das distâncias a todos os familiares. Deves apenas indicar qual o valor desta soma.


Input
-----

Na primeira linha do input vem um único número indicando **N** (1 ≤ N ≤ 20,000), a quantidade de familiares.

Na segunda linha vêm os números de porta dos familiares, separados por um único espaço. Os números estão sempre entre 1 e 50,000 (inclusive). Estes números pode vir por qualquer ordem e pode acontecer que dois ou mais familiares vivam no mesmo número de porta (sendo a soma mínima deve incluir as distâncias a todos os familiares).


Output
------

O output deve ser constituído por uma única linha com um número inteiro indicando a soma mínima das distâncias a todos os familiares, ou seja, a soma do número de porta onde Vito deve passar a morar.


Exemplos
--------

### Input 1

```txt
3
2 6 4
```

### Output 1

```txt
4
```

### Input 2

```txt
4
6 2 4 2
```

### Output 2

```txt
6
```


Créditos
--------

Este problema é essencialmente uma tradução/adaptação do [problema 10041](http://uva.onlinejudge.org/external/100/10041.html) do UVA Online Judge.
