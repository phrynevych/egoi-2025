#!/usr/bin/env bash
# We use a patched version of gen.sh that puts test groups in a wrapper
# subdirectory with a point-rescaling grader, to allow Kattis to reuse case
# result between groups despite them having different max scores.
REQUIRE_SAMPLE_REUSE=0
. ./gen.sh  # ../../../testdata_tools/gen.sh

compile gen.py

use_solution ../../data/noop.py

N=1000

samplegroup
limits n=7
sample 1

group group1 8
limits n=$N star=1
tc star-1 gen n=$N mode=star
tc star-2 gen n=$N mode=star
tc star-3 gen n=$N mode=star rename=0
tc star-4 gen n=$N mode=star rename=rev

group group2 9
limits n=$N line=1
tc line-1 gen n=$N mode=line
tc line-2 gen n=$N mode=line
tc line-3 gen n=$N mode=line rename=0
tc line-4 gen n=$N mode=line rename=rev
tc line-5 gen n=$N mode=line rename=fliphalf
tc line-6 gen n=$N mode=line rename=fliphalf2
tc line-7 gen n=$N mode=line rename=fliphalf3
tc line-8 gen n=$N mode=line
tc line-alt gen n=$N mode=line-alt rename=0

group group3 21
limits n=$N linestar=1
include_group group1
tc linestar-lineplus1 gen n=$N mode=almostline k=1
tc linestar-998-2 gen n=$N mode=linestar k=998
for K in 3 4 5 20 30 40 100 300 500 900 997 998; do
tc linestar-$K gen n=$N mode=linestar k=$K
done
tc linestar-exp gen n=$N mode=linestar-exp
tc broom-balanced gen n=$N k=500 mode=broom 
tc broom-long gen n=$N k=3 mode=broom
tc broom-short gen n=$N k=981 mode=broom
tc broom-short-alt-odd gen n=$N k=994 mode=broom-alt rename=0
tc broom-short-alt-even gen n=$N k=995 mode=broom-alt rename=0 
tc broom-long-2 gen n=$N k=3 mode=broom rename=0
tc broom-long-3 gen n=$N k=3 mode=broom rename=rev
tc linestar-lineplus1-2 gen n=$N mode=almostline k=1
tc linestar-lineplus1-3 gen n=$N mode=almostline k=1
tc linestar-lineplus1-4 gen n=$N mode=almostline k=1
tc linestar-lineplus1-5 gen n=$N mode=almostline k=1 rename=extra,0
tc linestar-lineplus1-6 gen n=$N mode=almostline k=1 rename=extra,-1
tc linestar-lineplus1-7 gen n=$N mode=almostline k=1 rename=center,0
tc linestar-lineplus1-8 gen n=$N mode=almostline k=1 rename=center,-1
tc linestar-3-2 gen n=$N mode=linestar k=3 rename=center,0
tc linestar-3-3 gen n=$N mode=linestar k=3 rename=center,-1
tc linestar-3-4 gen n=$N mode=linestar k=3

group group4 36
limits n=$N maxdiameter=10  
include_group group1
tc linestar-997
tc linestar-998
tc linestar-998-2
tc linestar-900
tc broom-short-alt-odd
tc broom-short-alt-even
tc shallow gen n=$N mode=shallow
tc shallower gen n=$N mode=shallower
tc random-maxdep1 gen n=$N mode=random maxdepth=5
tc random-maxdep2 gen n=$N mode=random maxdepth=5
tc deep-maxdep gen n=$N mode=deep maxdepth=5
tc doublestar gen n=$N mode=dumbbell k=499

group group5 26
limits n=$N
include_group group2
include_group group3
include_group group4
tc random gen n=$N mode=random
tc binary gen n=$N mode=binary
tc caterpillar gen n=$N mode=caterpillar k=500
tc caterpillar-random gen n=$N mode=caterpillar-random k=500
tc dumbbell-2 gen n=$N mode=dumbbell k=2
tc deep gen n=$N mode=deep
tc deeper gen n=$N mode=deeper
tc lineplus2 gen n=$N mode=almostline k=2
tc pruefer gen n=$N mode=pruefer
tc stretched-rand6 gen n=$N mode=stretched,random,6
tc stretched-rand10 gen n=$N mode=stretched,random,10
