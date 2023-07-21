Ideal condominium
================

![](a.jpg)

Contractor Dr. Ivan Oliver Irwin (I.O.I.) is designing a new set of buildings to be placed on the city's new avenue. The buildings will be arranged contiguously along the avenue and together they will form the most luxurious and elegant condominium in the vicinity.

To make life easier, the local city council divided the avenue into well-defined plots of the same size. The Doctor. IOI wants to build a condominium with several buildings, which can occupy several plots, but in any case they must be consecutive plots, that is, they must be contiguous to each other. There is no restriction on the number of plots to be used (it can occupy just one plot or conversely occupy up to the entire avenue) but the council only gave permission for the construction of a single condominium.

The problem is that certain plots of land on the avenue have very hard rocks on the ground and are much more difficult to drill holes for the construction of buildings. In some parts of the avenue it is so complicated and expensive to drill that the construction in that section would even be costly. The Doctor. IOI can estimate the profit he would get by building on each plot and this can help you decide which plots are best to build your condo on.

For example, he imagines that the avenue is divided into 8 plots with the following estimated profits (in hundreds of millions of euros):

| -1 | 4 | -2 | 5 | -5 | 2 | -20| 6 |
|----|----|----|----|----|----|----|----|

Like Dr. IOI can only build a single condominium and this has to be done in contiguous plots, the best it could do would be to make a profit of 7, building 4 -2 5 in contiguous plots.


Task
------

Your task is to help Dr. IOI and tell him the ideal condominium he should build. Given the profits for each split, you have to figure out which set of consecutive splits gives the highest profit. Obviously, the profit of a set of installments is equal to the sum of the estimated profits of each installment.


Input
-----

In the first line of the input there is a number **N** (1 ≤ N ≤ 1000000) that represents the number of parcels of the avenue to be considered.

Then comes another line containing exactly **N** whole numbers separated by a single space, indicating the estimated profits for each installment. Let **L** be the estimated profit of one installment. So \-2000 ≤ L ≤ 2000 is guaranteed.


Output
------

The output consists of a single line containing the maximum profit that Dr. IOI can get.


sample
------

### Input

```txt
8
-1 4 -2 5 -5 2 -20 6
```

### Output

```txt
7
```


Credits
--------

Selection of Portuguese Competitors - International Olympiads in Informatics 2005
_(August 12, 2005)_