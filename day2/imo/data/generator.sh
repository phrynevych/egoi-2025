#!/usr/bin/env bash
. ../../../testdata_tools/gen.sh

use_solution ng.cpp

compile generator.py

MAXN=20000
MAXM=100
MAXK=100

samplegroup
limits maxn=$MAXN maxm=$MAXM maxk=$MAXK
sample 1
sample 2
sample 3
sample 4

group group1 10
limits maxn=2 maxm=2 maxk=1 minm=2

for n in {0..5}; do
  tc tiny-$n generator mode=tiny mask=$n
done
tc 4
for n in {7..15}; do
  tc tiny-$n generator mode=tiny mask=$n
done

group group2 13
limits maxn=2 maxm=$MAXM maxk=$MAXK
include_group group1
tc 2
tc 3
tc n2-1 generator n=2 m=$MAXM k=$MAXK
tc n2-2 generator n=2 m=$MAXM k=$MAXK mode=all_max
tc n2-3 generator n=2 m=$MAXM k=$MAXK mode=all_max noise=1
tc n2-4 generator n=2 m=$MAXM k=$MAXK mode=random_subsetsum p=10 
tc n2-5 generator n=2 m=$MAXM k=$MAXK mode=mod_subsetsum p=10 
tc n2-6 generator n=2 m=$MAXM k=$MAXK ex=0.5
tc n2-7 generator n=2 m=$MAXM k=$MAXK ex=1.0
tc n2-8 generator n=2 m=$MAXM k=$MAXK mode=halves
tc n2-9 generator n=2 m=$MAXM k=$MAXK mode=halves p=10
tc_manual ../manual_tests/anti_greedy1.in
tc_manual ../manual_tests/anti_greedy2.in
tc_manual ../manual_tests/anti_greedy3.in

group group3 10
limits max_nm=16 maxn=$MAXN maxm=$MAXM maxk=$MAXK
include_group group1
tc 2
tc 3
tc anti_greedy1
tc anti_greedy3
tc nm16-1 generator n=4 m=4 k=$MAXK
tc nm16-2 generator n=4 m=4 k=$MAXK mode=all_max
tc nm16-3 generator n=4 m=4 k=$MAXK mode=all_max noise=1
tc nm16-4 generator n=4 m=4 k=$MAXK mode=random_subsetsum p=2
tc nm16-5 generator n=5 m=3 k=$MAXK
tc nm16-6 generator n=7 m=2 k=$MAXK
tc nm16-7 generator n=15 m=1 k=$MAXK
tc nm16-8 generator n=3 m=5 k=$MAXK mode=random_subsetsum p=4
tc nm16-9 generator n=4 m=4 k=$MAXK mode=random_subsetsum p=3
tc nm16-10 generator n=4 m=4 k=$MAXK mode=mod_subsetsum p=3
tc nm16-11 generator n=4 m=4 k=$MAXK mode=mod_subsetsum p=2
tc nm16-12 generator n=4 m=4 k=$MAXK ex=0.8
tc nm16-13 generator n=2 m=8 k=$MAXK
tc nm16-14 generator n=2 m=8 k=$MAXK mode=all_max
tc nm16-15 generator n=2 m=8 k=$MAXK mode=halves

group group4 18
limits maxn=$MAXN maxm=$MAXM maxk=1
include_group group1
tc 2
tc k1-1 generator n=10 m=5 k=1
tc k1-2 generator n=$MAXN m=$MAXM k=1
tc k1-3 generator n=$MAXN m=$MAXM k=1 mode=all_max
tc k1-4 generator n=$MAXN m=$MAXM k=1 mode=all_max noise=1
tc k1-5 generator n=$MAXN m=$MAXM k=1 ex=0.9
tc k1-6 generator n=$MAXN m=$MAXM k=1 mode=halves
tc k1-7 generator n=2 m=1 k=1
tc k1-8 generator n=10 m=$MAXM k=1
tc k1-9 generator n=70 m=$MAXM k=1
tc k1-10 generator n=$MAXN m=$MAXM k=1 mode=halves p=10
tc k1-11 generator n=2 m=1 k=1 mode=halves flip=1

group group5 21
limits maxn=10000 maxm=10 maxk=10
include_group group1
tc 1
tc 2
tc 3
tc anti_greedy1
tc anti_greedy3
tc original-1 generator n=10000 m=10 k=10
tc original-2 generator n=5000 m=10 k=10
tc original-3 generator n=1000 m=10 k=10
tc original-4 generator n=200 m=10 k=10
tc original-5 generator n=10000 m=10 k=10 mode=all_max
tc original-6 generator n=10000 m=10 k=10 mode=all_max noise=1
tc original-subsetsum-1 generator n=10000 m=10 k=10 mode=random_subsetsum p=3
tc original-subsetsum-2 generator n=10000 m=10 k=10 mode=mod_subsetsum p=3
tc original-7 generator n=10000 m=10 k=10 ex=0.9
tc original-8 generator n=10000 m=10 k=10 mode=halves p=3
tc original-9 generator n=2 m=10 k=10
tc original-10 generator n=5 m=10 k=10
tc original-11 generator n=10 m=10 k=10
tc original-12 generator n=10000 m=10 k=10 mode=block ss=2
tc original-spam-1 generator n=3 m=10 k=10 mode=spam
tc original-spam-2 generator n=3 m=6 k=7 mode=spam
tc original-spam-3 generator n=3 m=7 k=9 mode=spam
tc original-spam-4 generator n=2 m=7 k=9 mode=spam
tc original-force-1 generator n=10 m=10 k=10 mode=force x=7
tc original-force-2 generator n=10 m=8 k=9 mode=force x=7 am=10
tc original-force-3 generator n=10 m=8 k=9 mode=force x=5 am=10
tc original-force-4 generator n=10 m=5 k=7 mode=force x=6 am=10
tc original-force-5 generator n=10 m=6 k=10 mode=force x=7 am=10
tc original-force-6 generator n=10 m=9 k=10 mode=force x=7 am=10

group group6 28
limits maxn=$MAXN maxm=$MAXM maxk=$MAXK
include_group group2
include_group group3
include_group group4
include_group group5
tc large-1 generator n=100 m=$MAXM k=$MAXK
tc large-2 generator n=$MAXN m=$MAXM k=$MAXK
tc large-3 generator n=$MAXN m=$MAXM k=$MAXK
tc large-4 generator n=$MAXN m=$MAXM k=$MAXK
tc large-5 generator n=3000 m=$MAXM k=$MAXK
tc large-6 generator n=300 m=$MAXM k=$MAXK
tc large-7 generator n=$MAXN m=$MAXM k=$MAXK mode=all_max
tc large-8 generator n=$MAXN m=$MAXM k=$MAXK mode=all_max noise=1
tc large-subsetsum-1 generator n=$MAXN m=$MAXM k=$MAXK mode=random_subsetsum p=10
tc large-subsetsum-2 generator n=$MAXN m=$MAXM k=$MAXK mode=mod_subsetsum p=30
tc large-9 generator n=$MAXN m=$MAXM k=$MAXK ex=0.65
tc large-10 generator n=$MAXN m=$MAXM k=$MAXK ex=1.0
tc large-11 generator n=$MAXN m=$MAXM k=$MAXK mode=halves
tc large-12 generator n=$MAXN m=$MAXM k=$MAXK mode=halves p=5
tc large-13 generator n=$MAXN m=$MAXM k=$MAXK mode=halves p=100
tc large-14 generator n=$MAXN m=$MAXM k=$MAXK mode=halves p=1000
tc large-15 generator n=10000 m=$MAXM k=$MAXK mode=block ss=80
tc large-spam-1 generator n=3 m=95 k=97 mode=spam
tc large-spam-2 generator n=10 m=95 k=97 mode=spam
tc large-spam-3 generator n=50 m=95 k=97 mode=spam
tc large-force-1 generator n=5 m=95 k=100 mode=force x=97
tc large-force-2 generator n=5 m=93 k=99 mode=force x=97 am=100

