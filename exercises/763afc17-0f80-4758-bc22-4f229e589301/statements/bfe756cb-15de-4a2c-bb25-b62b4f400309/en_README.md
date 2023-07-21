Vacation plan
======================

![Image holiday_period_503505](./holiday_period_503505.jpg) ![Image calendar3](./calendar3.png)

People from the north who intended to go to the beach in the Algarve and Andalusia over the Easter holidays, were surprised by winds, showers and a very cold weather. _"Blancos llegaron y más blancos come back"_, so they already dream of a week or fifteen days of vacation that they plan to enjoy in June, July, August or September, if the vacation subsidy is not in the flood. It looks like it won't... So, a group of optimistic friends is already trying to choose a week of vacation, according to each one's preferences and unavailability. That week (seven days of vacation) must start on a Monday and end on the following Sunday or, alternatively, start on a Saturday and end on the following Friday. Each group member indicated a sequence of non-overlapping periods and classified each period using integers: `-1` to indicate unavailability and values ​​from `1` to `5` to express preferences, with `5` being the maximum level. In the periods not included, it is also available but with a zero preference level, if friends think it's a good idea or if there is no alternative. The classification serves to similarly score each day of the referred period. The chosen week will be one that everyone can go to, after June 1 (Wednesday) and ending before September 12, 2011, and which has the maximum score, considering the sum of the scores accumulated over the seven days, after processing everyone's preferences. If there is more than one possible week, they will choose the closest one, lest the cold come back in force.


Task
------

We want a program to process the information provided and indicate the date on which the group will start the vacation (or detect the inconsistency if there is no possibility of them going together).


Input
-----

A first line with the number of group members. An equal number of blocks follow, each containing the preferences or unavailability of a member of the group. A block starts with a positive integer denoting the number of periods that the member referred and then, on each line, has a quintet in the format _"day month day month preference"_, for example, `16 6 30 6 3` (which would represent the period from June 16 to June 30 with preference 3 on each of the days of that period; if it were `16 6 30 6 -1`, it would indicate that the member could not go in that period).


Output
------

If there is a week where everyone can, indicate the start date of the vacation in the format: day number followed by a space followed by `June`, `July`, `August` or `September`. Otherwise the word `inconsistent`.


Examples
--------

### Input 1

```sh
3
two
10 7 7 9 -1
10 6 23 6 5
two
1 6 15 7 -1
25 7 26 7 4
1
23 6 25 6 -1
```

### Output 1

```sh
inconsistent
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
two
3 7 20 8 4
1 9 9 9 -1
3
15 6 8 7 5
15 8 31 8 -1
7 9 10 9 5
```

### Output 2

```sh
July 9
```


Credits
--------

ToPAS'2011 (F) - Ana Paula Tomás