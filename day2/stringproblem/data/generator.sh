#!/usr/bin/env bash
# We use a patched version of gen.sh that puts test groups in a wrapper
# subdirectory with a point-rescaling grader, to allow Kattis to reuse case
# result between groups despite them having different max scores.
. ./gen.sh  # ../../../testdata_tools/gen.sh

use_solution wendy.cpp

compile gen_random.py

MAXN=100000

samplegroup
limits maxn=$MAXN minn=4
# simple general case
sample_manual 1
# small special case
# sample 2
# adjacent hair
sample 2
# answer 0 or 2
sample 3
# once wrong high answer
sample 4

# NOTE: testgroup scores must be even for the "just K gives 50%" rule to make sense.
# This is enforced in grader.py.

group group1 14
limits maxn=$MAXN minn=4 mode=adjacent
tc 2
tc adj_n4 gen_random n=4 mode=adjacent
tc adj_n10 gen_random n=10 mode=adjacent
tc adj_n11 gen_random n=11 mode=adjacent
tc adj_rand1 gen_random maxn=$MAXN mode=adjacent
tc adj_rand2 gen_random maxn=$MAXN mode=adjacent
tc adj_maxn1 gen_random n=$MAXN mode=adjacent
tc adj_maxn2 gen_random n=$MAXN mode=adjacent

group group2 16
limits maxn=$MAXN minn=4 mode=ans02
tc 3
tc adj_n4
tc swap_n4_1 gen_random n=4 mode=swap swaps=1 5
tc swap_n4_2 gen_random n=4 mode=swap swaps=0 11
tc swap_n4_close gen_random n=5 mode=swap swaps=1 close=1
tc swap_n1000_close gen_random n=1000 mode=swap swaps=1 close=1
tc swap_maxn100 gen_random maxn=100 mode=swap swaps=1
tc swap_maxn1000 gen_random maxn=1000 mode=swap swaps=0
tc swap_rand_1 gen_random mode=swap swaps=1
tc swap_rand_2 gen_random mode=swap swaps=1
tc swap_rand_3 gen_random mode=swap swaps=0
tc swap_rand_4 gen_random mode=swap swaps=0
tc swap_maxn_1 gen_random n=$MAXN mode=swap swaps=1
tc swap_maxn_2 gen_random n=$MAXN mode=swap swaps=1
tc swap_maxn_3 gen_random n=$MAXN mode=swap swaps=1
tc swap_maxn_4 gen_random n=$MAXN mode=swap swaps=0
tc swap_maxn_5 gen_random n=$MAXN mode=swap swaps=0
tc swap_maxn_close1 gen_random n=$MAXN mode=swap swaps=1 close=1
tc swap_maxn_close2 gen_random n=$MAXN mode=swap swaps=1 close=1
tc swap_maxn_close3 gen_random n=$MAXN mode=swap swaps=1 close=1
tc swap_maxn_close4 gen_random n=$MAXN mode=swap swaps=1 close=1

group group3 12
limits maxn=$MAXN minn=4 mode=angle1
include_group group1
tc 2
tc 4
tc adj_n4
tc angle_nsmall1 gen_random n=5 mode=swap angle=1 swaps=2
tc angle_nsmall2 gen_random n=10 mode=swap angle=1 swaps=3
tc angle_nmed1 gen_random minn=900 maxn=1000 mode=swap angle=1 swaps=100
tc angle_nmed2 gen_random minn=400 maxn=1000 mode=swap angle=1 swaps=1000
tc angle_nlarge1 gen_random n=$MAXN mode=swap angle=1 swaps=500000
tc angle_nlarge2 gen_random n=$MAXN mode=swap angle=1 swaps=500000
tc angle_nlarge3 gen_random n=$MAXN mode=swap angle=1 swaps=500000
tc angle_nlarge4 gen_random n=$MAXN mode=swap angle=1 swaps=500000
tc maxsol1 gen_random n=1000 mode=maxsol
tc maxsol2 gen_random n=1000 mode=maxsol
tc maxsol_large gen_random minn=10000 maxn=$MAXN mode=maxsol
tc against_rand gen_random mode=against_random n=$MAXN
tc against_rand2 gen_random mode=against_random maxn=$MAXN

group group4 28
limits maxn=1000 minn=4
tc 1
tc 2
tc 3
tc 4
tc adj_n4
tc swap_n4_1
tc swap_n4_2
tc swap_n4_close
tc swap_n1000_close
tc swap_maxn100
tc swap_maxn1000
tc adj_n10
tc adj_n11
tc angle_nsmall1
tc angle_nsmall2
tc angle_nmed1
tc angle_nmed2
tc n10 gen_random n=10
tc n101 gen_random n=101
tc nmax1000_rand1 gen_random maxn=1000
tc nmax1000_rand2 gen_random maxn=1000
tc n1000_rand1 gen_random n=1000
tc n1000_rand2 gen_random n=1000
tc maxsol1
tc maxsol2
tc maxsol3 gen_random n=999 mode=maxsol
tc maxsol4 gen_random n=999 mode=maxsol

group group5 30
limits maxn=$MAXN minn=4
include_group group1
include_group group2
include_group group3
include_group group4
tc nmax1 gen_random minn=1000 n=$MAXN
tc nmax2 gen_random minn=1000 n=$MAXN
tc nmax3 gen_random minn=1000 n=$MAXN
tc n_rand1 gen_random minn=1000 maxn=$MAXN
tc n_rand2 gen_random minn=1000 maxn=$MAXN
tc n_rand3 gen_random minn=1000 maxn=$MAXN
tc n_rand4 gen_random minn=1000 maxn=$MAXN
tc n_rand5 gen_random minn=1000 maxn=$MAXN
tc n_rand6 gen_random minn=1000 maxn=$MAXN mode=maxsol
tc n_rand7 gen_random minn=1000 maxn=$MAXN mode=maxsol
tc maxsol5 gen_random n=$MAXN mode=maxsol
tc maxsol6 gen_random n=99999 mode=maxsol
