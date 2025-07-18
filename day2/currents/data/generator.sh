#!/usr/bin/env bash
. ../../../testdata_tools/gen.sh

use_solution ac.cpp

compile gen_random.cpp
compile gen_line.cpp
compile gen_dag.cpp
compile gen_almost_line.cpp
compile gen_special.py
compile gen_manual.py

MAXN=200000
MAXM=500000

samplegroup
limits maxn=$MAXN maxm=$MAXM acyclic=0 line=0 all_to_N=0
sample 1
sample 2
sample 3
sample 4

group group1 12
limits maxn=$MAXN maxm=$MAXM acyclic=0 line=1 all_to_N=0
tc line-1 gen_line 5
tc 3
tc line-2 gen_line 199997
tc line-3 gen_line $MAXN
tc line-4 gen_line 2000

group group2 15
limits maxn=$MAXN maxm=$MAXM acyclic=0 line=0 all_to_N=1
tc bfs-1 gen_random 5 2 $MAXM 1
tc 3
tc bfs-2 gen_random $MAXN 0 $MAXM 1
tc bfs-3 gen_random $MAXN 100 $MAXM 1
tc bfs-4 gen_random $MAXN 200000 $MAXM 1
tc bfs-5 gen_random 2000 400000 $MAXM 1
tc bfs-6 gen_random 2000 10 $MAXM 1

# group group3 15
# limits maxn=10 maxm=10 acyclic=1 line=0 all_to_N=0
# tc 1
# tc 2
# tc 3
# tc tiny-1 gen_dag 6 9
# tc line-1
# tc tiny-2 gen_dag 10 10
# tc tiny-3 gen_dag 9 10
# tc tiny-4 gen_dag 7 10
# tc tiny-5 gen_dag 5 10
# tc tiny-6 gen_almost_line 10

group group3 20
limits maxn=2000 maxm=2000 acyclic=0 line=0 all_to_N=0
tc 1
tc 2
tc 4
tc line-4
tc small-1 gen_random 7 3 2000 0
tc small-2 gen_random 1000 3 2000 0
tc small-3 gen_random 1000 500 2000 0
tc dag-1 gen_dag 1800 2000
tc small-4 gen_random 900 10 $MAXM 1
tc medium-1p5-path gen_special n=999 mode=one_and_half_path
tc medium-ladder-dag gen_special n=1202 mode=ladder_dag
tc dag-2 gen_dag 10 15
tc small-5 gen_almost_line 2000

group group4 29
limits maxn=$MAXN maxm=$MAXM acyclic=1 line=0 all_to_N=0
include_group group1
tc dag-1
tc dag-2
tc 1
tc 2
tc medium-ladder-dag
tc dag-3 gen_dag $MAXN $MAXM
tc dag-4 gen_dag $MAXN 300000
tc dag-5 gen_dag $MAXN 230000
tc dag-6 gen_almost_line $MAXN
tc large-ladder-dag gen_special n=$MAXN mode=ladder_dag
tc manual gen_manual n=199996 0

group group5 24
limits maxn=$MAXN maxm=$MAXM acyclic=0 line=0 all_to_N=0
include_group group2
include_group group4
include_group group5
include_group sample
tc full-1 gen_random 10 5 $MAXM 0
tc full-2 gen_random $MAXN 10 $MAXM 0
tc full-3 gen_random $MAXN 0 $MAXM 0
tc full-4 gen_random $MAXN 100000 $MAXM 0
tc full-5 gen_random $MAXN 10000 $MAXM 0
tc full-6 gen_random 2000 400000 $MAXM 0
tc large-1p5-path gen_special n=$MAXN mode=one_and_half_path


