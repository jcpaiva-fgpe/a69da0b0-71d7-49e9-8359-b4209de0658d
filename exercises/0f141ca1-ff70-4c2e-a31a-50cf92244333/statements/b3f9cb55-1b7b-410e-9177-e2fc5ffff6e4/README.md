Saltitando
==========

![Illustration](image.jpg)

No mais belo jardim da cidade podem encontrar-se várias sequências de pedras numeradas. Um grupo de crianças passa tempos intermináveis a saltitar de pedra em pedra, num divertido jogo que inventaram. Um de cada vez, os amigos percorrem a sequência de pedras, somando os números que "calcam" com o pé direito, e subtraindo os números que "calcam" com o pé esquerdo. A criança que conseguir fazer o percurso que dá origem à maior "quantidade" ganha o jogo.

Claro que as crianças nem sempre percorrem o melhor caminho, no meio de tantas risadas e tantas tentativas de se distraírem uns aos outros. No entanto, olhando para o caminho, não consegues deixar de pensar que conseguirias calcular precisamente qual o melhor resultado (quantidade) possível de atingir. E é isso mesmo que te propões a fazer.

As pedras podem ser pensadas como uma sequência de números inteiros positivos, como por exemplo a seguinte:

| 7 | 14|  8|  2| 19| 20| 17| 13|  4|  8|  5|
|---|---|---|---|---|---|---|---|---|---|---|

Para não beneficiar as crianças de maior estatura, que têm pernas maiores, e por isso mesmo podem saltar mais longe, as crianças definem antecipadamente qual o maior tamanho **K** dos saltos possíveis. Um salto é medido por um número dizendo quantas pedras "avançam". Por exemplo, se estiverem na pedra com número 14, um salto de tamanho 1 leva-as para a pedra com o número 8, um salto de tamanho 2 leva-as para a pedra com o número 2 e um salto de tamanho 3 leva-as para a pedra com o número 19.

Um caminho é iniciado sempre no espaço imediatamente antes da primeira pedra e a criança pode decidir se começa pelo pé direito ou esquerdo, sendo que pode saltar qualquer uma das pedras ao alcance do maior salto. Por exemplo, se **K** for 3, a criança decidir saltar com um dos pés para a 1ª pedra (com o número 7), para a 2ª pedra (com o número 14) ou para a 3ª pedra (com o número 8). De seguida, a criança tem de usar o outro pé, ou seja, se saltou com o pé esquerdo, passa para o pé direito, e vice-versa, sendo que novamente só pode saltar um máximo de **K** pedras (e um mínimo de 1 pedra). Isto continua até conseguir "aterrar" num espaço fora das pedras, com os saltos feitos obrigatoriamente para a frente (da esquerda para a direita), não sendo possível saltar "para trás".

As figuras seguintes indicam três caminhos possíveis de seguir se o tamanho da maior salto possível for 3, e o respetivo resultado, sendo que o último caminho corresponde a começar com o pé direito e usar sempre o maior salto possível.

| -7| 14| +8| -2| 19|+20| 17|-13|  4|  8| +5|
|---|---|---|---|---|---|---|---|---|---|---|

Resultado = 11

|  7|+14| -8| +2| 19| 20|-17|+13|  4| -8|  5|
|---|---|---|---|---|---|---|---|---|---|---|

Resultado = -4

|  7| 14| +8|  2| 19|-20| 17| 13| +4|  8|  5|
|---|---|---|---|---|---|---|---|---|---|---|

Resultado = -8

De entre estes três caminhos, o melhor é o primeiro, pois tem o maior resultado, 11 = -7+8-2+20-13+5. Mas qual seria o melhor caminho, de entre todos os caminhos possíveis?


Tarefa
------

Dado um número inteiro **K**, indicando o tamanho do maior salto possível, e uma sequência de **N** números inteiros positivos escritos em pedras, a tua tarefa é encontrar qual o melhor resultado que uma criança pode obter seguindo um caminho de acordo com as regras atrás descritas.


Input
-----

Na primeira linha do _input_ vem um número inteiro **K**, indicando o tamanho do maior salto possível.

Na segunda linha vem um número inteiro **N** indicando o número de pedras a considerar (ou seja, o tamanho da sequência).

Seguem-se exatamente **N** linhas, cada uma com um único inteiro **Vi**, indicando o valor escrito na i-ésima pedra. As pedras vêm pela ordem em que aparecem na sequência, da esquerda para a direita (ou seja, do início para o fim).

O exemplo de input corresponde às figuras usadas no enunciado do problema.


Output
------

O _output_ deve ser constituído por uma única linha contendo um inteiro indicando o melhor resultado possível de atingir.

As crianças começam a saltar exatamente antes da primeira pedra e terminam quando ultrapassam a última pedra. Recorda que, ao saltar, as crianças somam os números que pisam com o pé direito e subtraem os que pisam com o pé esquerdo, sendo que podem decidir qual o pé que usam no primeiro salto. Em cada salto podem saltar entre 1 e K pedras para a frente.


Restrições
----------

São garantidos os seguintes limites em todos os casos de teste que irão ser colocados ao programa:

**1 ≤ K ≤ 200**

Tamanho do maior salto

**1 ≤ N ≤ 1 000**

Número de pedras no caminho

**1 ≤ Vi ≤ 1000**

Valores escritos nas pedras


Exemplo
-------

### Input

```txt
3
11
7
14
8
2
19
20
17
13
4
8
5
```

### Output

```txt
36
```


Créditos
--------

Esta é uma versão com os limites muito reduzidos de um problema da **Final Nacional das ONI'2012** (na final real N podia ir até 1 milhão). Departamento de Ciência de Computadores, Faculdade de Ciências da Universidade do Porto. _(18 de Maio de 2012)_
