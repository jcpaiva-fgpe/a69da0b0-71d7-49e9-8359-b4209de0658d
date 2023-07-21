Vito's Family
=================

![Illustration](06.jpg)

Gangster _Vito Deadstone_ is about to move to Porto. He has a big family there, all living on Avenida da Boavista. Since he intends to visit his relatives assiduously, he is looking for a house close to them.

Vito wants to minimize the total distance for all family members and has blackmailed you into writing a problem to solve his problem.

The allowed positions for the houses are given by the number of the house. The distance between two places in numbers _i_ and _j_ is given by **dij\=|i-j|** (difference between _i_ and _j_).


Task
------

Given a set of house numbers, indicating where each of Vito's family members lives, your task is to figure out which number Vito should live in in order to minimize the distance for all of them, that is, the number that minimizes the sum of distances to all family members. You must only indicate the value of this sum.


Input
-----

In the first line of the input there is a single number indicating **N** (1 ≤ N ≤ 20,000), the number of family members.

On the second line are the door numbers of the family members, separated by a single space. Numbers are always between 1 and 50,000 (inclusive). These numbers can come in any order and it can happen that two or more family members live on the same door number (the minimum sum must include the distances to all family members).


Output
------

The output must consist of a single line with an integer indicating the minimum sum of distances to all family members, that is, the sum of the door number where Vito must live.


Examples
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


Credits
--------

This problem is essentially a translation/adaptation of [problem 10041](http://uva.onlinejudge.org/external/100/10041.html) from the UVA Online Judge.