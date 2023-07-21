Listagem de Estudantes
======================

![Ilustração](05.jpg)

Tarefa
------

Dada uma lista de estudantes com 3 campos (primeiro nome, apelido e nota obtida numa dada unidade curricular), a tua tarefa é ordenar a lista por uma ordem pedida, que pode ser crescente ou decrescente de um dos 3 campos.

Input
-----

Na primeira linha do input vem um único número indicando o tipo de ordem a usar. Esse número pode ser:

*   **1:** ordenar por ordem decrescente da nota. Em caso de empate ordenar pelo primeiro nome e em caso de novo empate ordenar pelo apelido.
*   **2:** ordenar por ordem (alfabética) crescente do primeiro nome. Em caso de empate ordenar pela ordem em que vinham no input.

Na segunda linha do input vem um número **N** (1 ≤ N ≤ 20,000) que corresponde à quantidade de estudantes.

Segue-se a descrição dos estudantes, um por cada linha, no formato "PRIMEIRO\_NOME APELIDO NOTA". O primeiro nome e o apelido são constituídos por uma sequência de uma letra maiúscula, seguida de letra minúsculas, sem espaços, e com um máximo de 30 letras. A nota é um número inteiro entre 0 e 20 (inclusive).

Output
------

O output deve ser constituído **N** linhas, listando os estudantes pela ordem pedida (um por linha, no mesmo formato do input).

Exemplos
--------

### Input 1

```txt
1
7
Joaquim Oliveira 10
Antonio Campos 17
Jorge Tavares 8
Luis Araujo 12
Carlos Pimenta 11
Carlos Araujo 11
Sonia Soares 9
```

### Output 1

```txt
Antonio Campos 17
Luis Araujo 12
Carlos Araujo 11
Carlos Pimenta 11
Joaquim Oliveira 10
Sonia Soares 9
Jorge Tavares 8
```

### Input 2

```txt
2
7
Joaquim Oliveira 10
Antonio Campos 17
Jorge Tavares 8
Luis Araujo 12
Carlos Pimenta 11
Carlos Araujo 11
Sonia Soares 9
```

### Output 2

```txt
Antonio Campos 17
Carlos Pimenta 11
Carlos Araujo 11
Joaquim Oliveira 10
Jorge Tavares 8
Luis Araujo 12
Sonia Soares 9
```
