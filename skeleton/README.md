# Skeleton code

## Files

Any file beginning with cin will use <\<iostream\>> to do I/O. Otherwise, assume it uses <<\<stdio.h\>>>.

The reason for this is that in testing, the <<\<stdio.h\>>> headers seemed to perform better.

<read\_n.cpp> reads in an integer, n from stdin, then reads n numbers into a vector, which can later be operated on. 

<operate\_n.cpp> reads in an integer, n from stdin, then reads n number from stdin, passing each n to a function.

<knapsack .cpp> is a simple implementation of the knapsack problem. It could be adapted for any backtracking though
