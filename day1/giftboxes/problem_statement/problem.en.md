# A. Gift Boxes

| Problem Name | Gift Boxes |
| --- | --- |
| Time Limit | 2 seconds |
| Memory Limit | 1 gigabyte |
This year's EGOI is organized in Bonn.
The organizers want to distribute at most one gift box to every team in the contest, with each team represented by a number from $0$ to $T-1$.
The contestants are standing in a single row. However they are mixed up such that people from the same team might not be standing next to each other. Note that there will be at least one team with more than one person in the row. 
There are $N$ people in the row.
Person $i$ is part of the team $a_i$.
The problem is: each team should only receive a maximum of one gift box.
In order to ensure the process runs smoothly - and willing to leave some teams with no gift as a consequence - the organisers wish to pause the gifting process exactly once, skipping a few contestants before resuming the gift box handouts.
In other words, they will skip one consecutive segment $[\ell, r]$ of the contestants.  

It is not necessary that every team receives a gift.
Nevertheless, the organizers want to maximize the number of teams that will receive their gifts while ensuring that no team ends up with two or more gifts, equivalent to minimizing the number of contestants that are skipped under this condition.
Please help the organizers to decide when it is best to pause and when to continue distributing gifts such that as few contestants as possible are skipped.

## Input

The first line of input contains two integers, $T$ and $N$ – the number of teams and the number of contestants in the row.

The second line contains $N$ integers, $a_i$, where the $i$th integer describes which team the person at position $i$ in the row belongs to.
It is guaranteed that every integer between $0$ and $T-1$ appears at least once.

## Output

Output two integers, $\ell$ and $r$, where $\ell$ is the index of the first person that is skipped and $r$ is the index of the last skipped person.
Note that $\ell$ and $r$ are indexed from $0$ to $N-1$.
If there is more than one solution, print any one of them.

## Constraints and Scoring

* $1 \leq T < N \leq 500\,000$.
* $0 \leq a_i \leq T-1$.

Your solution will be tested on a set of test groups, each worth a number of points.
Each test group contains a set of test cases.
To get the points for a test group, you need to solve all test cases in the test group.


| Group | Score | Limits |
| --- | --- | --- |
| 1 | 8 | $N = T + 1$, i.e. only one team will appear twice |
| 2 | 11 | $N = 2 \cdot T$ and every team will appear exactly once in the first half and exactly once in the second half of the line |
| 3 | 14 | $1 \leq T < N \leq 500$ |
| 4 | 21 | $N = 2 \cdot T$ and every team will appear twice |
| 5 | 22 | $1 \leq T < N \leq 5\,000$ |
| 6 | 24 | No additional constraints |


## Examples

The first sample satisfies the constraints of test groups 1, 3, 5 and 6. Two different outputs are possible: ``1 1`` corresponding to the solid blue line and ``4 4`` corresponding to the red dotted line, as described in the picture below. Either way, all four teams receive gifts and no team receives more than one gift.


<div style="zoom: 200%;">![](giftboxes-sample1.svg)</div>


The second sample satisfies the constraints of test groups 2, 3, 4, 5 and 6. Again, two different outputs are possible: ``0 2`` and ``3 5``, as described in the picture below. In both cases, all three teams receive gifts.


<div style="zoom: 200%;">![](giftboxes-sample2.svg)</div>


The third sample satisfies the constraints of test groups 3, 4, 5, 6. The optimal solution is that three teams receive a gift, as shown below. The contestants with indices $0$, $1$ and $7$, who are in teams $0$, $2$ and $3$, respectively, receive gifts. This is the only possible solution.


<div style="zoom: 200%;">![](giftboxes-sample3.svg)</div>


The fourth sample satisfies the constraints of test groups 3, 5 and 6. Again two different outputs are possible: ``0 3`` and ``1 4``, as described in the picture below. In both cases, exactly two teams (team $0$ and team $1$) receive gifts. Team $2$ does not receive a gift as doing so would require giving team $0$ or $1$ two gifts, which is strictly forbidden.


<div style="zoom: 200%;">![](giftboxes-sample4.svg)</div>


The fifth sample satisfies the constraints of test groups 3, 5 and 6. The only possible answer is ``2 3``, as described in the picture below. All four teams receive gifts.


<div style="zoom: 200%;">![](giftboxes-sample5.svg)</div>


The sixth sample satisfies the constraints of test groups 3, 5 and 6. A maximum of four out of five teams can receive a gift, as shown below. The contestants with indices $0$, $910$, $1011$ and $1112$, who are in teams $3$, $4$, $1$ and $0$, respectively, receive gifts. This is the only possible solution.


<div style="zoom: 200%;">![](giftboxes-sample6.svg)</div>





| <span style="display: inline-block; width: 150px;">Input</span> | <span style="display: inline-block; width: 150px;">Output</span> |
|-------|--------|
| <pre>4 5<br>1 3 0 2 3</pre> | <pre>1 1<br><br></pre> |
| <pre>3 6<br>1 0 2 2 1 0</pre> | <pre>0 2<br><br></pre> |
| <pre>4 8<br>0 2 0 1 2 1 3 3</pre> | <pre>2 6<br><br></pre> |
| <pre>3 6<br>1 1 2 0 1 0</pre> | <pre>0 3<br><br></pre> |
| <pre>4 6<br>0 1 2 0 3 2</pre> | <pre>2 3<br><br></pre> |
| <pre>5 13<br>3 3 3 1 2 0 3 3 2 1 4 1 0</pre> | <pre>1 9<br><br></pre> |
