O Carteiro Paulo
================

![Illustration](image.jpg)

O Carteiro Paulo e o seu gato preto e branco vão todos os dias de manhã distribuir o correio na sua carrinha vermelha. Todos na cidade acenam à sua passagem.

A carrinha do Paulo tem uma capacidade limitada e por vezes os sacos de correio ultrapassam o limite de carga. Quando isso acontece, o Paulo quer encher o máximo possível a sua carrinha, levando tanto peso quanto possível. No entanto, o Paulo não pode retirar cartas e encomendas de um saco para outro e apenas pode decidir se um determinado saco vai ou não ser transportado na carrinha.

Imagina por exemplo que o Paulo tinha no correio 4 sacos com os pesos de 4Kg, 5Kg, 7Kg e 8Kg. Se a capacidade de carga é de 10Kg de correio, qual é o máximo peso de correio que o Paulo consegue levar numa viagem? Neste caso, o melhor que consegue fazer é levar 9Kg, que correspondem a transportar os dois sacos de 4Kg e 5Kg. E no caso geral? Tens de ajudar o Paulo!


Tarefa
------

Dado um conjunto de sacos de correio e os seus respectivos pesos, bem como o limite de carga da carrinha vermelha do Paulo, a tua tarefa é calcular o máximo peso que o Paulo consegue levar na carrinha, sabendo que um saco de correio não poder ser dividido (ou é transportado na carrinha ou fica na estação de correios).


Input
-----

Na primeira linha do _input_ vem uma única linha contendo dois inteiros **S** e **C**, separados por um espaço, sendo que **S** indica o número de sacos de correio e **C** indica a capacidade de carga máxima da carrinha (_1 ≤ S ≤ 5000, 1 ≤ C ≤ 10000_).

Seguem-se exactamente **S** linhas, cada uma contendo um número inteiro contendo o peso **Pi** de um saco de correio (_1 ≤ Pi ≤ 500_). Os sacos podem vir em qualquer ordem e podem existir vários sacos com o mesmo peso.


Output
------

O _output_ é constituído uma única linha, indicando o peso máximo que a carrinha consegue transportar, ou seja, qual a maior soma de pesos de um conjunto de sacos de correio que é inferior ou igual à capacidade de carga de carrinha.


Exemplos
--------

### Input 1

```txt
4 10
4
5
7
8
```

### Output 1

```txt
9
```

### Input 2

```txt
6 15
10
2
4
2
1
1
```

### Output 2

```txt
15
```


Créditos
--------

Problema inicialmente usado na **Qualificação para a final das ONI'2008** _(17/04 a 19/04 de 2008)_. **Nota:** Os testes usados neste treino não são necessariamente os mesmo que foram usados na qualificação real de 2008.
