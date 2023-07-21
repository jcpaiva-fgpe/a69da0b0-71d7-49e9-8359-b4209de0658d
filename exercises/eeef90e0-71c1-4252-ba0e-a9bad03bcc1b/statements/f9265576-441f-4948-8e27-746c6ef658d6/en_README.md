Luxury Transportation
==================

![Image shuttle](./ shuttle.jpeg)


Usually, live animals have to be transported in air-conditioned holds but, in the case of cod destined for the Maritime Museum of Ílhavo, there may also have been some misunderstanding given the proximity of the Christmas season. The truth is that new copies were eventually sent, and these arrived safe and sound. It is intended to verify whether it is possible to transport an animal of a certain species from a source node to a certain destination node and, if so, indicate the **minimum length** of a possible route. The length is defined by the number of sections of the route. The species has restrictions on the minimum and maximum temperature it supports, so only routes compatible with these restrictions can be considered.

  

Input
-----

At the beginning there is a line with four integers: the first two designate the minimum and maximum temperature supported by the animal to be transported, and the next two, the origin node and the destination node (these nodes are different). A line follows with the number of nodes in the network and the number of sections (branches) in the network. Below is a description of the network sections. Each section is described on a line by four integers separated by spaces: the first two identify the ends of the section, the next the expected temperature in that section and the last a cost associated with transport. Any link is bidirectional. There may be isolated nodes. Nodes are identified by consecutive integers starting from 1. If it is useful, you can assume that the network has no more than 20000 nodes.
  

Output
------

A line with the word `Yes` followed by a space and the length of the minimum journey, if the network allows transporting the animal between origin and destination. Otherwise, a line with the word `Nao` (not accented).


Examples
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
Yes 2
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
No
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
Yes 3
```
  
Credits
--------

DCC/FCUP 2013 (Practical Test B) - Ana Paula Tomás