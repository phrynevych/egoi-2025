#!/usr/bin/env bash
. ../../../testdata_tools/gen.sh

compile gen.py

use_solution ../../data/empty.sh # empty .ans files

MAXN=30000

samplegroup
limits maxn=5
sample 1
sample 2
sample 3

# n <= 3
group group1 9
limits maxn=3
tc 2
tc tiny-sorted-3 gen n=3 mode=sorted
tc tiny-reversed-3 gen n=3 mode=reversed
tc tiny-rand-1 gen n=3 mode=random seed=10
#tc tiny-rand-2 gen n=3 mode=random seed=14
tc tiny-first gen n=3 mode=random seed=2 force_first=1
tc tiny-cyclic-1 gen n=3 mode=cyclic shift=1
#tc tiny-cyclic-2 gen n=3 mode=cyclic shift=-1


# n <= 30
group group2 15
limits maxn=30
include_group sample
include_group group1
tc 1
tc 3
tc tiny-rand-4 gen n=4 mode=random
tc tiny-rand-5 gen n=5 mode=random
tc tiny-rand-6 gen n=6 mode=random
tc tiny-rand-7 gen n=7 mode=random
tc tiny-rand-8 gen n=8 mode=random
tc tiny-rand-9 gen n=9 mode=random
tc tiny-rand-10 gen n=10 mode=random
tc small-sorted gen n=30 mode=sorted
tc small-rand-1 gen n=30 mode=random
tc small-rand-2 gen n=30 mode=random
tc small-rand-3 gen n=29 mode=random
tc small-first gen n=30 mode=random force_first=1
tc small-cyclic-1 gen n=30 mode=cyclic shift=1
tc small-cyclic-2 gen n=30 mode=cyclic shift=15
tc small-cyclic-3 gen n=30 mode=cyclic shift=14
tc small-cyclic-4 gen n=30 mode=cyclic shift=-1
tc half-rand-tiny-1 gen n=4 mode=random half=1
tc half-rand-tiny-2 gen n=4 mode=random half=1
tc half-rand-tiny-3 gen n=4 mode=random half=1
tc half-rand-tiny-4 gen n=4 mode=random half=1

# know first switch
group group3 17
limits maxn=$MAXN first=1
tc 3
tc tiny-sorted-3
tc tiny-first
tc small-first
tc tiny-rand-5
tc small-sorted
tc half-rand-tiny-1
tc half-rand-tiny-2
tc force-first-rand-1 gen n=16383 mode=random force_first=1
tc force-first-rand-2 gen n=16384 mode=random force_first=1
tc force-first-rand-3 gen n=16385 mode=random force_first=1
tc force-first-rand-4 gen n=$((MAXN-1)) mode=random force_first=1
tc force-first-rand-5 gen n=$((MAXN-1)) mode=random force_first=1
tc force-first-rand-6 gen n=$MAXN mode=random force_first=1
tc force-first-rand-7 gen n=$MAXN mode=random force_first=1
tc force-first-rand-8 gen n=$MAXN mode=random force_first=1
tc force-first-rand-9 gen n=$MAXN mode=random force_first=1
tc force-first-rand-10 gen n=$MAXN mode=random force_first=1
tc force-first-reversed gen n=$MAXN mode=reversed force_first=1
tc force-first-almost-cyclic gen n=$MAXN mode=cyclic shift=61234 force_first=1
tc large-sorted gen n=$MAXN mode=sorted

group group4 16
limits maxn=$MAXN half=1
tc 3
tc small-sorted
tc large-sorted
tc force-first-rand-7
tc force-first-rand-8
tc small-rand-2
tc force-first-rand-10
tc force-first-reversed
tc force-first-almost-cyclic
tc half-rand-tiny-1
tc half-rand-tiny-2
tc half-rand-tiny-3
tc half-rand-tiny-4
tc tiny-rand-6
tc tiny-rand-10
tc half-rand-1 gen n=16384 mode=random half=1
tc half-rand-2 gen n=$MAXN mode=random half=1
tc half-rand-3 gen n=$MAXN mode=random half=1
tc half-rand-4 gen n=$MAXN mode=random half=1
tc half-rand-5 gen n=$MAXN mode=random half=1
tc half-rand-6 gen n=$MAXN mode=random half=1
tc half-rand-7 gen n=$MAXN mode=random half=1
tc half-rand-8 gen n=$MAXN mode=random half=1
tc medium-rand-2 gen n=64 mode=random
tc large-rand-6 gen n=$MAXN mode=random
tc large-rand-7 gen n=$MAXN mode=random
tc small-cyclic-2
tc medium-cyclic-4 gen n=1000 mode=cyclic shift=500
tc cyclic-10 gen n=$MAXN mode=cyclic shift=15000

# n <= 1000
group group5 14
limits maxn=1000
include_group group2
tc medium-rand-0 gen n=63 mode=random
tc medium-rand-1 gen n=511 mode=random
tc medium-rand-2
tc medium-rand-3 gen n=512 mode=random
tc medium-rand-4 gen n=513 mode=random
tc medium-rand-5 gen n=999 mode=random
tc medium-rand-6 gen n=1000 mode=random
tc medium-cyclic-1 gen n=1000 mode=cyclic shift=1
tc medium-cyclic-2 gen n=1000 mode=cyclic shift=-1
tc medium-cyclic-3 gen n=1000 mode=cyclic shift=2
tc medium-cyclic-4

# n <= 30'000
group group6 29
limits maxn=$MAXN
include_group sample
include_group group1
include_group group2
include_group group3
include_group group4
include_group group5
tc large-rand-0 gen n=1001 mode=random
tc large-rand-1 gen n=16383 mode=random
tc large-rand-2 gen n=16384 mode=random
tc large-rand-3 gen n=16385 mode=random
tc large-rand-4 gen n=$((MAXN-1)) mode=random
tc large-rand-5 gen n=$((MAXN-1)) mode=random
tc large-rand-6
tc large-rand-7
tc large-rand-8 gen n=$MAXN mode=random
tc large-rand-9 gen n=$MAXN mode=random seed=432
tc large-rand-10 gen n=$MAXN mode=random
tc large-rand-11 gen n=$MAXN mode=random
tc large-rand-12 gen n=$MAXN mode=random
tc large-rand-13 gen n=$MAXN mode=random seed=321
tc large-rand-14 gen n=$MAXN mode=random seed=132
tc large-rand-15 gen n=$MAXN mode=random
tc cyclic-7 gen n=$MAXN mode=cyclic shift=1
tc cyclic-8 gen n=$MAXN mode=cyclic shift=-1
tc cyclic-9 gen n=$MAXN mode=cyclic shift=2
tc cyclic-10
