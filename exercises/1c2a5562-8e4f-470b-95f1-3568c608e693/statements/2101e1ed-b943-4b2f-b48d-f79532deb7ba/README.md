Cortes Orçamentais
==================

![Image cofre-porquinho](./cofre-porquinho.jpg)

Em virtude dos cortes orçamentais, deixou de ser relevante evitar percursos longos. Assim, na continuação do Problema "Transporte de Luxo", pretende-se antes saber se é ou não possível fazer chegar o animal de um nó origem até um nó destino sem gastar mais do que uma certa quantia. Em cada troço, o valor a pagar é o custo indicado para esse troço (o qual é sempre um inteiro e dado em euros). Só poderão ser considerados percursos que garantam as condições impostas quanto às temperaturas suportadas pelo animal.


Input
-----
  
No início tem uma linha com quatro inteiros: os dois primeiros designam a temperatura mínima e máxima suportadas pelo animal a transportar e, os dois seguintes, o nó origem e o nó destino (estes nós são distintos). Depois, tem o número de nós da rede e o número de troços (ramos) da rede, seguido de um inteiro que representa o número de cenários a considerar, e depois, igual número de linhas. Cada uma dessas linhas contém o valor máximo que poderia despender (sabe-se que esse valor é sempre inferior a 10000 euros). Existe sempre pelo menos um cenário.


Output
------

Para cada cenário, a palavra Sim se for possível efetuar o transporte sem ultrapassar o montante indicado. Caso contrário, terá Nao (não acentuada).


Exemplos
--------

### Input 1

```txt
-2 25 1 6
6 10
1 4 10 35
3 5 -22 30
1 2 -27 50
5 2 20 51
3 2 3 27
2 4 -1 5
5 6 9 20
1 5 30 20
4 6 25 450
6 3 -15 40
8
5000
50
101
400
300
112
111
110
```

### Output 1

```txt
Sim
Nao
Nao
Sim
Sim
Sim
Sim
Nao
```


### Input 2

```txt
\-3 10 4 6
6 10
1 4 10 35
3 5 -22 30
1 2 -27 50
5 2 20 51
3 2 3 27
2 4 -1 5
5 6 9 20
1 5 30 20
4 6 25 450
6 3 -15 40
1
3000
```

### Output 2

```txt
Nao
```

  
Créditos
--------

DCC/FCUP 2013 (prova prática C) - Ana Paula Tomás
