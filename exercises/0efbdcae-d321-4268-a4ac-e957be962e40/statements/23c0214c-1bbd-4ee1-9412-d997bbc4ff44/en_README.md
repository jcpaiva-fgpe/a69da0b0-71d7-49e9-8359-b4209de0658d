Frozen Codfish
====================

![Image 220px-Portrait_of_Cod](./220px-Portrait_of_Cod.jpg)


In early December 2012, thirty cod from Norway bound for the country's first cod aquarium in Íhavo arrived frozen. According to a news source (tvi24), "the fish, about 30 centimeters and 1.5 kilos, arrived dead, wrapped in blocks of ice, apparently due to negligence in transport, a long journey from Alesund to Ílhavo, between plane and road transport". It is possible that they were subjected to temperatures of minus 50 degrees in air transport.

With regard to this specific case, we are interested in considering a transport network with information on the expected temperature in each section and determining, for the indicated routes, the minimum and maximum temperature expected.


Input
-----

The first line shows the number of nodes in the network and the number of sections (branches) in the network.

Below is a description of the network sections. Each section is described on a line by four integers separated by spaces: the first two identify the ends of the section, the next the expected temperature in that section and the last a cost associated with transport. Any link is bidirectional. There may be isolated nodes. Nodes are identified by consecutive integers starting from 1. If it is useful, you can assume that the network has no more than 20000 nodes.

Finally, there is information about the routes. You will always have the description of at least one route. Each path is described in a line, and is defined by the corresponding sequence of nodes. The first integer on that line is the number of nodes in the sequence. It must assume that all given routes are valid, with the first node indicating the origin of the route and the last its end. A toolpath can contain repeated nodes but not at consecutive positions. The data ends with 0.


Output
------

For each route, there will be a line with the corresponding minimum and maximum temperature, separated by a space.


Example
-------

### Input

```txt
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
9 5 1 4 2 3 6 4 2 1
5 1 4 2 3 6
2 1 5
5 2 3 6 4 2
7 5 6 4 1 5 2 3
0
```

### Output

```txt
-27 30
-15 10
30 30
-15 25
3 30
```

  
Credits
--------

DCC/FCUP 2013 (Practical Test A) - Ana Paula Tomás