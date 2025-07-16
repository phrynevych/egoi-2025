#!/usr/bin/env bash
. ../../../testdata_tools/gen.sh

ulimit -s 16000000

use_solution jb.cc opt

compile gen.py
compile gen_special.py

MAXN=100000
MAXM=100000
MAXQ=200000
MAXW=1000000000
MAXS=$((MAXN*MAXQ))


samplegroup
limits maxn=$MAXN maxm=$MAXM maxs=$MAXS maxq=$MAXQ maxw=$MAXW
sample 1
sample 2
sample 3
sample 4
sample 5
sample 6
sample 7


group group1 8
limits maxn=$MAXN maxm=$MAXM maxs=$MAXS maxq=$MAXQ maxw=$MAXW path=1
tc 2
tc 7
tc g1-path1 gen n=$MAXN m=$((MAXN-1)) q=$MAXQ maxw=$MAXW mode='path'  
tc g1-path2 gen n=$MAXN m=$((MAXN-1)) q=$MAXQ maxw=$MAXW mode='path'  
tc g1-path3 gen n=$MAXN m=$((MAXN-1)) q=$MAXQ maxw=$MAXW mode='path'  
tc g1-path4 gen n=$MAXN m=$((MAXN-1)) q=$MAXQ maxw=$MAXW mode='path'  
tc g1-path5 gen n=$MAXN m=$((MAXN-1)) q=$MAXQ maxw=$MAXW mode='path'  
tc g1-inc-path gen_special n=$MAXN q=$MAXQ mode='path_increasing_costs'  

group group2 11
limits maxn=2000 maxm=2000 maxs=2000 maxq=2000 maxw=$MAXW
tc 1
tc 2
tc 3
tc 4
tc 5
tc 6
tc 7
tc g2-many1 gen n=5 m=8 q=$MAXQ maxs=2000 maxw=$MAXW mode='sum_many' tree='pruefer'
tc g2-many2 gen n=1000 m=2000 q=$MAXQ maxs=2000 maxw=$MAXW  mode='sum_many' tree='caterpillar'
tc g2-many3 gen n=200 m=2000 q=$MAXQ maxs=2000 maxw=$MAXW mode='sum_many' tree='broom'
tc g2-many4 gen n=2000 m=2000 q=$MAXQ maxs=2000 maxw=$MAXW  mode='sum_many'

tc g2-random1 gen n=200 m=2000 q=$MAXQ maxs=2000 maxw=$MAXW mode='sum_random' tree='pruefer'
tc g2-random2 gen n=1000 m=2000 q=$MAXQ maxs=2000 maxw=$MAXW  mode='sum_random' tree='caterpillar'
tc g2-random3 gen n=1000 m=2000 q=$MAXQ maxs=2000 maxw=$MAXW  mode='sum_random' tree='broom'
tc g2-random4 gen n=1000 m=2000 q=$MAXQ maxs=2000 maxw=$MAXW  mode='sum_random'
tc g2-random5 gen n=2000 m=2000 q=$MAXQ maxs=2000 maxw=$MAXW  mode='sum_random' shuffle=0


group group3 13
limits maxn=$MAXN maxm=$MAXM maxs=$MAXS maxq=$MAXQ maxw=$MAXW tuple=1
tc 3
tc g3-tuple1 gen n=$MAXN m=$MAXM q=$MAXQ maxw=$MAXW  mode='tuple' tree='pruefer'
tc g3-tuple2 gen n=5000 m=$MAXM q=$MAXQ maxw=$MAXW  mode='tuple' tree='pruefer'
tc g3-tuple3 gen n=5000 m=$MAXM q=$MAXQ maxw=$MAXW  mode='tuple' tree='caterpillar'
tc g3-tuple4 gen n=$MAXN m=$MAXM q=$MAXQ maxw=$MAXW  mode='tuple' tree='caterpillar' weights='increasing'
tc g3-tuple5 gen n=$MAXN m=$MAXM q=$MAXQ maxw=$MAXW  mode='tuple' tree='broom' weights='decreasing'
tc g3-tuple6 gen n=$MAXN m=$MAXM q=$MAXQ maxw=$MAXW  mode='tuple' tree='broom'
tc g3-tuple7 gen n=$MAXN m=$MAXM q=$MAXQ maxw=$MAXW  mode='tuple'
tc g3-tuple8 gen n=$MAXN m=$MAXM q=$MAXQ maxw=$MAXW  mode='tuple' shuffle=0

group group4 17
limits maxn=$MAXN maxm=$MAXM maxs=$MAXS maxq=$MAXQ maxw=2
tc 4
tc g4-allpossible gen n=$MAXN m=$MAXM q=$MAXQ maxw=2 cc=1 mode='all_possible' 
tc g4-manyimposs1 gen n=100 m=150 q=$MAXQ maxw=2 cc=4 mode='smallw' 
tc g4-manyimposs2 gen n=5000 m=$MAXM q=$MAXQ maxw=2 cc=10 mode='smallw' 
tc g4-manyimposs3 gen n=5000 m=$MAXM q=$MAXQ maxw=2 cc=1000 mode='smallw' 
tc g4-manyimposs4 gen n=$MAXN m=$MAXM q=$MAXQ maxw=2 cc=100 mode='smallw' 
tc g4-manyimposs5 gen n=$MAXN m=$MAXM q=$MAXQ maxw=2 cc=500 mode='smallw' 
tc g4-manyimposs6 gen n=$MAXN m=$MAXM q=$MAXQ maxw=2 cc=100 mode='smallw' 
tc g4-manyimposs7 gen n=$MAXN m=$MAXM q=$MAXQ maxw=2 cc=500 mode='smallw' 
tc g4-manyimposs8 gen n=$MAXN m=$MAXM q=$MAXQ maxw=2 cc=500 mode='smallw' 

group group5 16
limits maxn=$MAXN maxm=$MAXM maxs=400000 maxq=$MAXQ maxw=$MAXW
include_group group2
include_group group3
#tc g5-pairs gen n=$MAXN m=$MAXM maxs=200000 q=$((MAXQ/2)) maxw=$MAXW mode='tuple'
tc g5-many1 gen n=5000 m=$MAXM maxs=400000 q=$MAXQ maxw=$MAXW  mode='sum_many' tree='pruefer'
tc g5-many2 gen n=$MAXN m=$MAXM maxs=400000 q=$MAXQ maxw=$MAXW  mode='sum_many' tree='caterpillar'
tc g5-many3 gen n=$MAXN m=$MAXM maxs=400000 q=$MAXQ maxw=$MAXW  mode='sum_many' tree='broom'
tc g5-many4 gen n=$MAXN m=$MAXM maxs=400000 q=$MAXQ maxw=$MAXW  mode='sum_many' size=4
tc g5-random1 gen n=$MAXN m=$MAXM maxs=400000 q=$MAXQ maxw=$MAXW  mode='sum_random' tree='pruefer'
tc g5-random2 gen n=$MAXN m=$MAXM maxs=400000 q=$MAXQ maxw=$MAXW  mode='sum_random' tree='caterpillar'
tc g5-random3 gen n=$MAXN m=$MAXM maxs=400000 q=$MAXQ maxw=$MAXW  mode='sum_random' tree='broom'
tc g5-random4 gen n=$MAXN m=$MAXM maxs=400000 q=$MAXQ maxw=$MAXW  mode='sum_random'
tc g5-random5 gen n=$MAXN m=$MAXM maxs=400000 q=$MAXQ maxw=$MAXW  mode='sum_random' shuffle=0


group group6 14
limits maxn=$MAXN maxm=$MAXM maxs=$MAXS maxq=$MAXQ maxw=$MAXW left=1
tc 5
tc g6-left1 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='left' tree='pruefer'
tc g6-left2 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='left' tree='pruefer'
tc g6-left3 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='left' tree='caterpillar'
tc g6-left4 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='left' tree='caterpillar' weights='increasing'
tc g6-left5 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='left' tree='broom' weights='decreasing'
tc g6-left6 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='left' tree='broom'
tc g6-left7 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='left'
tc g6-left8 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='left' shuffle=0

group group7 21
limits maxn=$MAXN maxm=$MAXM maxs=$MAXS maxq=$MAXQ maxw=$MAXW
include_group group1
include_group group3
include_group group4
include_group group5
include_group group6
tc g7-all1 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='all_possible' tree='pruefer'
tc g7-all2 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='all_possible' tree='pruefer'
tc g7-all3 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='all_possible' tree='caterpillar'
tc g7-all4 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='all_possible'  tree='caterpillar' weights='increasing'
tc g7-all5 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='all_possible' tree='broom' weights='decreasing'
tc g7-all6 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='all_possible' tree='broom'
tc g7-all7 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='all_possible'
tc g7-all8 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='all_possible'
tc g7-all9 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='all_possible'
tc g7-all10 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='all_possible' shuffle=0
tc g7-all11 gen n=$MAXN m=$MAXM maxw=$MAXW q=$MAXQ  mode='all_possible' shuffle=0
tc g7-bitinv gen_special n=$MAXN q=$MAXQ mode='bitinv'
tc g7-inc-path2 gen_special n=$MAXN q=$MAXQ mode='path_increasing_costs' shuffle=1


