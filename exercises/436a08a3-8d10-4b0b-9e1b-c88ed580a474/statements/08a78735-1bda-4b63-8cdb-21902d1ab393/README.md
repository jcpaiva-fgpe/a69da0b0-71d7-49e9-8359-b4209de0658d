Condomínio Ideal
================

![](a.jpg)

O empreiteiro Dr. Ivan Oliver Irwin (I.O.I.) está a projectar um novo conjunto de edifícios para colocar na nova avenida da cidade. Os edíficios irão ficar dispostos contiguamente ao longo da avenida e juntos irão formar o condomínio mais luxuoso e elegante das redondezas.

Para facilitar a vida, a câmara municipal local dividiu a avenida em parcelas de terreno bem definidas e do mesmo tamanho. O Dr. IOI quer construir um condomínio com vários edifícios, que podem ocupar várias parcelas, mas em todo o caso têm de ser parcelas consecutivas, ou seja, têm de ser contíguas umas às outras. Não há restrição quanto ao número de parcelas a usar (pode ocupar apenas uma parcela ou inversamente ocupar até a avenida toda) mas a câmara só deu permissão para a construção de um único condomínio.

O problema é que certas parcelas de terreno da avenida têm rochas muito duras no solo e são bastante mais difíceis de furar para a construção dos edifícios. Nalgumas parcelas da avenida é tão complicado e caro furar que a construção nessa secção iria mesmo dar prejuízo. O Dr. IOI consegue estimar o lucro que iria obter pela construção em cada parcela e isso pode ajudá-lo a decidir quais as melhores parcelas para construir o seu condomínio.

Por exemplo, imagina que a avenida está dividida em 8 parcelas com os seguintes lucros estimados (em centenas de milhões de euros):

| -1 |  4 | -2 |  5 | -5 |  2 | -20|  6 |
|----|----|----|----|----|----|----|----|

Como o Dr. IOI só pode construir um único condomínio e este tem de ser feito em parcelas contíguas, o melhor que conseguiria fazer seria obter um lucro de 7, construindo nas parcelas contíguas 4 -2 5. Nota que as zonas com números negativos são zonas onde se obtém prejuízo.


Tarefa
------

A tua tarefa é ajudar o Dr. IOI e dizer-lhe qual o condomínio ideal que ele deve construir. Dados os lucros de cada parcela, tens de descobrir qual o conjunto de parcelas consecutivas que dá origem ao maior lucro. Obviamente, o lucro de um conjunto de parcelas é igual à soma dos lucros estimados de cada parcela.


Input
-----

Na primeira linha do input vem um número **N** (1 ≤ N ≤ 1000000) que representa o número de parcelas da avenida a considerar.

Depois vem uma outra linha contendo exactamente **N** números inteiros separados por um único espaço, indicando os lucros estimados de cada parcela. Seja **L** o lucro estimado de uma parcela. Então, é garantido que \-2000 ≤ L ≤ 2000.


Output
------

O output é constituído por uma única linha contendo o lucro máximo que o Dr. IOI pode obter.


Sample
------

### Input

```txt
8
-1 4 -2 5 -5 2 -20 6
```

### Output

```txt
7
```


Créditos
--------

Selecção dos Concorrentes Portugueses - Olimpíadas Internacionais de Informática 2005
_(12 de Agosto de 2005)_
