# D. Wind Turbines

| Problem Name | Wind Turbines |
| --- | --- |
| Time Limit | 4 seconds |
| Memory Limit | 1 gigabyte |
Anna has been tasked with designing the wiring for a new offshore wind farm in the North Sea consisting of $N$ turbines, numbered $0, 1, \ldots, N-1$. Her goal is to ensure that all turbines are connected to the shore as cheaply as possible.

Anna has a list of $M$ potential connections, each linking two wind turbines and having a specific cost. Additionally, the nearby city has agreed to cover the costs of connecting a consecutive interval $[\ell, r]$ of turbines to the shore. That is, each turbine $t$ in this range ($\ell\le t\le r$) is directly connected to the shore for free. 
If all potential connections are built, there is a way to reach any wind turbine from any other wind turbine.
That implies that as soon as one of the wind turbines is connected to the shore, it is possible to build connections such that the power from all the turbines can be transferred to the shore. Of course, more connections to the shore may allow for a cheaper total cost.
Note that the free connections are the only direct ones to the shore.

It is Anna's job to select a subset of the potential connections in a way that minimizes the sum of their costs, while ensuring that every wind turbine can reach the shore (possibly via other wind turbines).

In order to make an informed decision, the city provides Anna with $Q$ possible options for the interval $[\ell, r]$. The city asks Anna to compute the minimum cost for each of these scenarios.

## Input

The first line of the input contains three integers, $N$, $M$ and $Q$.

The following $M$ lines contain three integers each, $u_i$, $v_i$ and $c_i$. The $i$th line describes a potential connection between wind turbines $u_i$ and $v_i$ that has the cost $c_i$. These connections are undirected and connect two different turbines. No two connections are between the same pair of turbines.
It is guaranteed that, if all potential connections are built, any wind turbine is reachable from any other (directly or indirectly).

The next $Q$ lines contain two integers each, $\ell_i$ and $r_i$, describing the scenario where the shore directly connects to the wind turbines $\ell_i,\ell_i+1,\ldots,r_i$. Note that we can have $r_i = \ell_i$ when the shore directly connects to a single wind turbine. 

## Output

Output $Q$ lines, one line per scenario, containing one integer each, the minimum cost of connecting the turbines such that every turbine can deliver its power to the shore.

## Constraints and Scoring

* $2 \le N\le 100\,000$.
* $1 \le M\le 100\,000$.
* $1 \le Q\le 200\,000$.
* $0 \le u_i,v_i \le N-1$.
* $u_i \ne v_i$, and there is at most one direct connection between each pair of wind turbines.
* $1 \le c_i \le 1\,000\,000\,000$.
* $0 \le \ell_i\le r_i \le N-1$.

Your solution will be tested on a set of test groups, each worth a number of points. Each test group contains a set of test cases. To get the points for a test group, you need to solve all the test cases in the test group.


| Group | Score | Limits |
| --- | --- | --- |
| 1 | 8 | $M=N-1$ and the $i$th connection has $u_i=i$ and $v_i=i+1$, i.e. if all connections are built, they form a path $0 \leftrightarrow 1 \leftrightarrow 2 \leftrightarrow \ldots \leftrightarrow N-1$ |
| 2 | 11 | $N,M,Q\le 2\,000$ and $\sum(r_i-\ell_i+1) \le 2\,000$ |
| 3 | 13 | $r_i=\ell_i+1$ for all $i$ |
| 4 | 17 | $1\le c_i \le 2$ for all $i$, i.e., everyeach connection has costscost either $1$ or $2$ |
| 5 | 16 | $\sum(r_i-\ell_i+1)\le 400\,000$ |
| 6 | 14 | $\ell_i=0$ for all $i$ |
| 7 | 21 | No additional constraints |


## Examples

In the first example, we are given the following graph of potential connections.

<div style="zoom: 55%;">![](windturbines-sample1.svg)</div>


We are given three scenarios.
In the first scenario, turbine 1 is the only one with a connection to the shore. In this case, we need to keep all connections except for the connection between turbine $0$ and turbine $2$, giving a total cost of $2+3+6+3=14$.
In the next scenario, the turbines 3 and 4 are connected to the shore. In this case, we keep the connections $(1,0)$, $(1,2)$ and $(2,4)$, giving a cost of 8.
In the third scenario, all but turbine 0 are connected to the shore. In this case, we only need to connect this one to another turbine, which we do by choosing the connection $(0,1)$.
The solutions to the scenarios are depicted below:

<table><tr>
<td style="zoom: 60%;">![](windturbines-sample1q1.svg)</td>  <td style="zoom: 60%;">![](windturbines-sample1q2.svg)</td> <td style="zoom: 60%;">![](windturbines-sample1q3.svg)</td> 
</tr></table>

The first and the sixth samples satisfy the constraints of test groups 2, 5 and 7. The second and the seventh samples satisfy the constraints of test groups 1, 2, 5 and 7. The third sample satisfies the constraints of test groups 2, 3, 5 and 7. The fourth sample satisfies the constraints of test groups 2, 4, 5 and 7. The fifth sample satisfies the constraints of test groups 2, 5, 6 and 7.

<style>div { page-break-inside: auto !important; } td { page-break-inside: avoid; } </style>

| <span style="display: inline-block; width: 150px;">Input</span> | <span style="display: inline-block; width: 150px;">Output</span> |
|-------|--------|
| <pre>5 5 3<br>1 0 2<br>0 2 5<br>1 2 3<br>3 0 6<br>2 4 3<br>1 1<br>3 4<br>1 4</pre> | <pre>14<br>8<br>2<br><br><br><br><br><br><br></pre> |
| <pre>5 4 4<br>0 1 3<br>1 2 1<br>2 3 5<br>3 4 2<br>0 4<br>2 3<br>2 4<br>2 2</pre> | <pre>0<br>6<br>4<br>11<br><br><br><br><br><br></pre> |
| <pre>7 7 4<br>6 4 3<br>1 4 5<br>3 2 4<br>0 3 2<br>5 2 3<br>4 0 1<br>1 3 1<br>0 1<br>2 3<br>4 5<br>5 6</pre> | <pre>12<br>10<br>10<br>10<br><br><br><br><br><br><br><br><br></pre> |
| <pre>7 7 3<br>2 6 1<br>1 0 1<br>0 5 1<br>1 2 2<br>3 4 1<br>5 3 1<br>5 4 1<br>5 6<br>1 3<br>3 4</pre> | <pre>5<br>4<br>6<br><br><br><br><br><br><br><br><br></pre> |
| <pre>7 7 4<br>6 4 3<br>1 4 5<br>3 2 4<br>0 3 2<br>5 2 3<br>4 0 1<br>1 3 1<br>0 3<br>0 6<br>0 1<br>0 4</pre> | <pre>7<br>0<br>12<br>6<br><br><br><br><br><br><br><br><br></pre> |
| <pre>9 13 4<br>0 1 1<br>2 0 3<br>1 2 4<br>5 4 4<br>2 5 6<br>3 1 7<br>8 1 4<br>6 3 9<br>0 3 5<br>3 5 3<br>4 3 2<br>6 2 4<br>7 8 5<br>1 8<br>4 7<br>6 7<br>1 2</pre> | <pre>1<br>14<br>22<br>24<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></pre> |
| <pre>6 5 1<br>0 1 1000000000<br>1 2 1000000000<br>2 3 1000000000<br>3 4 1000000000<br>4 5 1000000000<br>1 1</pre> | <pre>5000000000<br><br><br><br><br><br><br></pre> |
