Laboratório de Computadores
===========================

Como responsável pela unidade de curricular de programação, tem de escolher um laboratório de computaores onde fazer as avaliações práticas. No edifício do seu departamento, existem vários laboratórios com um número variado de computadores. Para pode avaliar o maior número de alunos, a sua tarefa é descobrir o laboratório com mais computadores. Entrar fisicamente em cada uma das salas seria muito cansativo. Felizmente, a administração tem disponível um mapa do departamento, pelo que é possível calcular automaticamente o resultado.

Considere por exemplo o mapa da figura seguinte. O melhor laboratório é o indicado a cinzento, com 15 computadores.

![Illustration](image.png)


Tarefa
------

Dada descrição em ASCII do mapa do departmaneto, a tua tarefa é descobrir o laboratório com o maior número de computadores, reportando o número de computadores desse laboratório.


Input
-----

Na primeira linha vêm dois números **L** e **C**, indicando respetivamente o número de linha e colunas da representação em ASCII do mapa do departamento (_1 ≤ L,C ≤ 100_).

Seguem-se exactamente **L** linhas, cada uma com **C** caracteres indicando o mapa. Os caracteres podem ser:

*   'C': um computador
*   'P': uma porta
*   '#': uma parede
*   ' ': um espaço livre

O mapa está completamente delimitado por paredes, e cada um dos laboratórios está completamente delimitado por paredes e/ou portas.


Output
------

Deve ser imprimida uma única linha, contendo o número de computadores do laboratório que tenha mais computadores.


Exemplo
-------

### Input

```txt
12 26
##########################
#C C C #   # C C C C C   #
#      #   # C C C C C   #
#      #   P             #
#      #   # C C C C C   #
###PP###   ###############
#                        #
###PP###   #####PP########
# C  C #   #             #
#      #   #             #
# C  C #   #     C       #
##########################
```

### Output

```txt
15
```
