Computer Lab
===========================

As responsible for the programming curricular unit, you have to choose a computer laboratory where you can carry out the practical evaluations. In your department building, there are several laboratories with a varied number of computers. In order to assess as many students as possible, your task is to find the lab with the most computers. Physically entering each of the rooms would be very tiring. Fortunately, the administration has a department map available, so it is possible to calculate the result automatically.

Consider, for example, the map in the following figure. The best lab is the one shown in grey, with 15 computers.

![Illustration](image.png)


Task
------

Given the ASCII description of the department map, your task is to find the lab with the most computers, reporting the number of computers in that lab.


Input
-----

In the first line there are two numbers **L** and **C**, respectively indicating the number of lines and columns of the ASCII representation of the department map (_1 ≤ L,C ≤ 100_).

Exactly **L** lines follow, each with **C** characters indicating the map. Characters can be:

* 'C': a computer
* 'P': a port
*   '#': a wall
* ' ': a free space

The map is completely enclosed by walls, and each of the labs is completely enclosed by walls and/or doors.


Output
------

A single line should be printed, containing the number of computers in the laboratory that has the most computers.


Example
-------

### Input

```txt
12 26
###########################
#C C C # # C C C C C #
# # # C C C C C #
#      #   P             #
# # # C C C C C #
###PP### ################
# #
###PP### #####PP########
# C C # # #
# # # #
# C C # # C #
###########################
```

### Output

```txt
15
```