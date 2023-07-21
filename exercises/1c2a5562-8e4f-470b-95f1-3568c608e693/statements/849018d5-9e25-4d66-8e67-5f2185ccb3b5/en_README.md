Budget Cuts
==================

![Image piggy bank](./pigbox.jpg)

Due to budget cuts, it is no longer relevant to avoid long journeys. Thus, in the continuation of the "Luxury Transport" Problem, the aim is rather to know whether or not it is possible to get the animal from a source node to a destination node without spending more than a certain amount. For each section, the amount to be paid is the cost indicated for that section (which is always an integer and given in euros). Only routes that guarantee the conditions imposed regarding the temperatures tolerated by the animal can be considered.


Input
-----
  
At the beginning there is a line with four integers: the first two designate the minimum and maximum temperature supported by the animal to be transported, and the next two, the origin node and the destination node (these nodes are different). Then there is the number of nodes in the network and the number of sections (branches) in the network, followed by an integer representing the number of scenarios to be considered, and then an equal number of lines. Each of these lines contains the maximum amount you could spend (it is known that this amount is always less than 10000 euros). There is always at least one scenario.


Output
------

For each scenario, the word Yes if it is possible to carry out the transport without exceeding the indicated amount. Otherwise, it will have Nao (not accentuated).


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
Yes
No
No
Yes
Yes
Yes
Yes
No
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
No
```

  
Credits
--------

DCC/FCUP 2013 (practical test C) - Ana Paula Tomás