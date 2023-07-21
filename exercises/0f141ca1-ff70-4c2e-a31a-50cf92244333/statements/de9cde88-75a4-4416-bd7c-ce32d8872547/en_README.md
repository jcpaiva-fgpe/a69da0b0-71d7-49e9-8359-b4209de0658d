bouncing
==========

![Illustration](image.jpg)

In the most beautiful garden in the city you can find several sequences of numbered stones. A group of children spend endless hours hopping from stone to stone, in a fun game they invented. One at a time, the friends go through the sequence of stones, adding the numbers they "step on" with their right foot, and subtracting the numbers they "step on" with their left foot. The child who manages to make the route that gives rise to the greatest "quantity" wins the game.

Of course, children don't always go the best way, amid so much laughter and so many attempts to distract each other. However, looking at the path, you can't help but think that you would be able to calculate precisely the best result (quantity) possible to achieve. And that's exactly what you propose to do.

Stones can be thought of as a sequence of positive integers, such as the following:

| 7 | 14| 8| 2| 19| 20| 17| 13| 4| 8| 5|
|---|---|---|---|---|---|---|---|---|---|---|

In order not to benefit taller children, who have longer legs and therefore can jump further, children define in advance the largest **K** size of possible jumps. A jump is measured by a number saying how many stones "step forward". For example, if they are on the number 14 stone, a size 1 jump takes them to the number 8 stone, a size 2 jump takes them to the number 2 stone, and a size 3 jump takes them to the number 19 stone.

A path always starts in the space immediately before the first stone and the child can decide whether to start with the right or left foot, and can jump any of the stones within reach of the highest jump. For example, if **K** is 3, the child decides to jump with one foot to the 1st stone (with the number 7), to the 2nd stone (with the number 14) or to the 3rd stone (with the number 8). Then, the child has to use the other foot, that is, if he jumped with his left foot, he passes to the right foot, and vice versa, and again he can only jump a maximum of **K** stones (and a minimum of 1 stone). This continues until you manage to "land" in a space outside the stones, with the jumps made obligatorily forwards (from left to right), not being possible to jump "backwards".

The following figures indicate three possible paths to follow if the size of the highest possible jump is 3, and the respective result, with the last path corresponding to starting with the right foot and always using the highest possible jump.

| -7| 14| +8| -2| 19|+20| 17|-13| 4| 8| +5|
|---|---|---|---|---|---|---|---|---|---|---|

Result = 11

| 7|+14| -8| +2| 19| 20|-17|+13| 4| -8| 5|
|---|---|---|---|---|---|---|---|---|---|---|

Result = -4

| 7| 14| +8| 2| 19|-20| 17| 13| +4| 8| 5|
|---|---|---|---|---|---|---|---|---|---|---|

Result = -8

Of these three paths, the first is the best, as it has the highest result, 11 = -7+8-2+20-13+5. But what would be the best way out of all the possible ways?


Task
------

Given an integer **K**, indicating the size of the biggest possible jump, and a sequence of **N** positive integers written on stones, your task is to find the best result that a child can obtain following a path according to the rules described above.


Input
-----

On the first line of _input_ comes an integer **K**, indicating the size of the largest possible jump.

On the second line comes an integer **N** indicating the number of stones to be considered (that is, the size of the sequence).

Exactly **N** lines follow, each with a single integer **Vi**, indicating the value written on the i-th stone. The stones come in the order in which they appear in the sequence, from left to right (that is, from beginning to end).

The input example corresponds to the figures used in the problem statement.


Output
------

The _output_ must consist of a single line containing an integer indicating the best possible result to be achieved.

Children start jumping just before the first stone and finish when they pass the last stone. Remember that, when jumping, children add the numbers they step on with their right foot and subtract those they step on with their left foot, and they can decide which foot they use in the first jump. In each jump they can jump between 1 and K stones forward.


Restrictions
----------

The following limits are guaranteed in all test cases that will be put to the program:

**1 ≤ K ≤ 200**

Biggest jump size

**1 ≤ N ≤ 1,000**

Number of stones on the path

**1 ≤ Vi ≤ 1000**

Values ​​written on stones


Example
-------

### Input

```txt
3
11
7
14
8
two
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


Credits
--------

This is a version with very reduced limits of a problem from the **ONI'2012 National Final** (in the real final N could go up to 1 million). Department of Computer Science, Faculty of Sciences of the University of Porto. _(May 18, 2012)_