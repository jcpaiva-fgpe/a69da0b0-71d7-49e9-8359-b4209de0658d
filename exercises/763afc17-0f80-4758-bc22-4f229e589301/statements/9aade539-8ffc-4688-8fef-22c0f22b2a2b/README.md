Plano de Férias
===============

![Image holiday_period_503505](./holiday_period_503505.jpg) ![Image calendar3](./calendar3.png)

Gente do norte que tencionava fazer praia no Algarve e Andaluzia nas férias da Páscoa, foi surpreendida por ventos, aguaceiros e um muito frio. _"Blancos llegaron y más blancos volvieron"_, pelo que já sonham com uma semana ou quinze dias de férias que planeiam gozar em Junho, Julho, Agosto ou Setembro, se o subsídio de férias não for na enxurrada. Parece que não irá...Assim, um grupo de amigos optimistas está já a tentar escolher uma semana de férias, de acordo com as preferências e indisponibilidades de cada um. Essa semana (sete dias de férias) tem de começar numa segunda-feira e terminar no domingo seguinte ou, em alternativa, começar num sábado e terminar na sexta-feira seguinte. Cada membro do grupo indicou uma sequência de períodos que não se sobrepõem e classificou cada período usando inteiros: `-1` para assinalar indisponibilidade e valores de `1` a `5` para manifestar preferências, sendo `5` o nível máximo. Nos períodos que não incluiu, também está disponível mas com nível de preferência zero, se os amigos acharem boa ideia ou se não existir alternativa. A classificação serve para pontuar analogamente cada dia do período referido. A semana escolhida será uma em que todos possam ir, após 1 de Junho (quarta-feira) e com fim antes de 12 de Setembro de 2011, e que tenha a pontuação máxima, considerando a soma das pontuações acumuladas nos sete dias, após processamento das preferências de todos. Se existir mais do que uma semana possível, escolherão a mais próxima, não vá o frio voltar em força.


Tarefa
------

Pretende-se um programa para processar a informação fornecida e indicar a data em que o grupo iniciará as férias (ou detectar a inconsistência se não existir nenhuma possibilidade de irem juntos).


Input
-----

Uma primeira linha com o número de membros do grupo. Segue-se igual número de blocos, cada um contendo as preferências ou indisponibilidades de um membro do grupo. Um bloco começa por um inteiro positivo que denota o número de períodos que o membro referiu e depois, em cada linha, tem um quinteto no formato _"dia mês dia mês preferência"_, por exemplo, `16 6 30 6 3` (que representaria o período de 16 de Junho a 30 de Junho com preferência 3 em cada um dos dias desse período; se fosse `16 6 30 6 -1`, indicaria que o membro não poderia ir nesse período).


Output
------

Se existir uma semana em que todos possam, indicará a data de início das férias no formato: número do dia seguido de um espaço seguido de `de Junho`, `de Julho`, `de Agosto` ou `de Setembro`. Caso contrário, a palavra `inconsistente`.


Exemplos
--------

### Input 1

```sh
3
2
10 7 7 9 -1
10 6 23 6 5
2
1 6 15 7 -1
25 7 26 7 4
1
23 6 25 6 -1
```

### Output 1

```sh
inconsistente
```

### Input 2

```sh
5
6
16 6 30 6 3
8 7 8 7 -1
9 7 31 7 5
5 8 12 8 5
23 8 31 8 2
7 6 8 6 -1
1
1 6 31 7 4
1
1 8 5 9 1
2
3 7 20 8 4
1 9 9 9 -1
3
15 6 8 7 5
15 8 31 8 -1
7 9 10 9 5
```

### Output 2

```sh
9 de Julho
```


Créditos
--------

ToPAS'2011 (F) - Ana Paula Tomás