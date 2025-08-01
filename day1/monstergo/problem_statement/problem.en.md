# C. Monster-Go

| Problem Name | Monster-Go |
| --- | --- |
| Time Limit | 1 seconds |
| Memory Limit | 1 gigabyte |
Helen and her friends have discovered an amazing new game for their phones.
The game, called *Monster-Go*, is about catching monsters by walking to different monster nests outdoors.
There are an infinite number of monsters of a single type available at each nest.
When the friends arrive at a monster nest, each of them will catch and add the monster type at that nest to their collection.
There are a total of $50$ different monster types that the friends can catch, numbered $0,1,\ldots,49$.

To make the game more exciting, the $N$ friends have decided that each player will have a personalized list of exactly $12$ monster types to collect.
The first person to catch all the monsters on their list wins the game.
They want to design the lists in such a way that, no matter the order in which they visit the monster nests, there is always a single, unique winner – never a tie.
The friends always walk around together as a group and arrive together at a monster nest.

Can you help them design the lists?
Your score will depend on the number of values of $N$, the number of people playing, for which you are able to solve the problem.

## Input

The first and only line of input contains the integer $N$, the number of players.

## Output

Output $N$ lines, where the $i$th line withhas the $12$ distinct integers $c_{i,1}, c_{i,2}, \ldots, c_{i,12}$ (where $0 \le c_{i,j} \le 49$) representing the monster types on the list of person $i$.
If there are multiple solutions, you may print any of them.

## Constraints and Scoring

* $1 \leq N \leq 50$.


Your solution will be tested on a set of test groups, each worth a number of points.
**The $i$th test group contains a single test case with $N = i$ and is worth $2$ points**. That is, there are a total of $50$ tests (one for each $N = 1, 2, \ldots, 50$), and your score on this problem is twice the number of tests your program solves.



| Group | Score | Limits |
| --- | --- | --- |
| 1 | 2 | $N = 1$ |
| 2 | 2 | $N = 2$ |
| 3 | 2 | $N = 3$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| 49 | 2 | $N = 49$ |
| 50 | 2 | $N = 50$ |


## Example

In the sample, where there are $N = 2$ friends, the program should output two lists. Indeed, for the two lists in the sample output, the friends cannot both win at the same time, no matter the order in which they visit the monster nests.
Note that there are many other valid answers.


| <span style="display: inline-block; width: 150px;">Input</span> | <span style="display: inline-block; width: 150px;">Output</span> |
|-------|--------|
| <pre>2<br><br></pre> | <pre>0 1 2 3 4 5 6 7 8 9 10 11<br>38 39 40 41 42 43 44 45 46 47 48 49</pre> |
