Transporte de Luxo
==================

![Image vaivem](./vaivem.jpeg)


Habitualmente, os animais vivos têm de ser transportados em porões climatizados mas, no caso dos bacalhaus destinados ao Museu Marítimo de Ílhavo, pode também ter havido algum equívoco dada a proximidade da quadra natalícia. A verdade é que acabaram por ser enviados novos exemplares, e esses chegaram sãos e salvos. Pretende-se verificar se é possível transportar um animal de uma certa espécie de um nó origem para um certo nó destino e, se for, indicar o **comprimento mínimo** de um percurso possível. O comprimento é definido pelo número de troços do percurso. A espécie tem restrições quanto à temperatura mínima e máxima que suporta, pelo que só poderão ser considerados percursos compatíveis com essas restrições.

  

Input
-----

No início tem uma linha com quatro inteiros: os dois primeiros designam a temperatura mínima e máxima suportadas pelo animal a transportar e, os dois seguintes, o nó origem e o nó destino (estes nós são distintos). Segue-se uma linha com o número de nós da rede e o número de troços (ramos) da rede. A seguir tem a descrição dos troços da rede. Cada troço é descrito numa linha por quatro inteiros separados por espaços: os dois primeiros identificam os extremos do troço, o seguinte a temperatura esperada nesse troço e o último um custo associado ao transporte. Qualquer ligação é bidirecional. Pode haver nós isolados. Os nós são identificados por inteiros consecutivos a partir de 1. Se for útil, pode assumir que a rede não tem mais do que 20000 nós.
  

Output
------

Uma linha com a palavra `Sim` seguida de um espaço e do comprimento do percurso mínimo, se a rede permitir o transporte do animal entre a origem e o destino. Caso contrário, uma linha com a palavra `Nao` (não acentuada).


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
```

### Output 1

```txt
Sim 2
```

### Input 2

```txt
-3 10 4 6
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
```

### Output 2

```txt
Nao
```

### Input 3

```txt
-2 21 6 4
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
```

### Output 3

```txt
Sim 3
```
  
Créditos
--------

DCC/FCUP 2013 (Prova Prática B) - Ana Paula Tomás
