#!/usr/bin/env bash
. ../../../testdata_tools/gen.sh

use_solution katharina.cpp

compile generator.py
compile handmade.py

MAXN=499999
MAXM=500000

samplegroup
limits maxn=$MAXN maxm=$MAXM
sample 1
sample 2
sample 3
sample 4
sample 5
sample 6

group group1 8
limits maxn=$MAXN maxm=$MAXM mode="plusOne"
tc 1
tc st1-1 generator n=499999 st=1
tc st1-2 generator n=499999 st=1
tc st1-3 generator n=499999 st=1
tc st1-4 generator n=499999 st=1
tc st1-5 generator n=499999 st=1
tc st1-n1-1 generator n=1 st=1
tc st1-ec1-1 generator n=499999 st=1 ec=1
tc st1-ec2-1 generator n=499999 st=1 ec=2
tc st1-ec3-1 generator n=499999 st=1 ec=3
tc n-xs-st1 generator n=499 st=1
tc n-sm-st1 generator n=4999 st=1

group group2 11
tc 2
limits maxn=$MAXN maxm=$MAXM mode="doubleSort"
tc st2-1 generator n=250000 st=2
tc st2-2 generator n=250000 st=2
tc st2-3 generator n=250000 st=2
tc st2-4 generator n=250000 st=2
tc st2-5 generator n=250000 st=2
tc st1-n1-1
tc st2-ec1-1 generator n=250000 st=2 ec=1
tc st2-ec2-1 generator n=250000 st=2 ec=2
tc st2-ec3-1 generator n=250000 st=2 ec=3
tc n-xs-st2 generator n=250 st=2
tc n-sm-st2 generator n=2500 st=2

group group3 14
limits maxn=500 maxm=500
tc 1
tc 2
tc 3
tc 4
tc 5
tc 6
tc st1-n1-1
tc nm-xs-rand-1 generator maxn=499 maxm=500
tc nm-xs-rand-2 generator maxn=499 maxm=500
tc nm-xs-rand-3 generator maxn=499 maxm=500
tc nm-xs-rand-4 generator maxn=499 maxm=500
tc nm-xs-rand-5 generator maxn=499 maxm=500
tc n-xs-rand-1 generator maxn=499 m=500
tc n-xs-rand-2 generator maxn=499 m=500
tc n-xs-rand-3 generator maxn=499 m=500
tc n-xs-rand-4 generator maxn=499 m=500
tc n-xs-rand-5 generator maxn=499 m=500
tc n1-xs-1 generator n=1 m=500
tc n-xs-rand-ec1-1 generator maxn=499 m=500 ec=1
tc n-xs-rand-ec2-1 generator maxn=499 m=500 ec=2
tc n-xs-st1
tc n-xs-st2
tc n-xs-st3 generator n=250 st=3
tc st4-ec2-1 handmade c=1
tc st4-ec3-1 handmade c=2
tc n-xs-ec3 generator n=498 ec=3

group group4 21
limits maxn=$MAXN maxm=$MAXM mode="double"
include_group group2
tc 3
tc n-xs-st3
tc st4-1 generator n=250000 st=3
tc st4-2 generator n=250000 st=3
tc st4-3 generator n=250000 st=3
tc st4-4 generator n=250000 st=3
tc st4-5 generator n=250000 st=3
tc st4-ec1-1 generator n=250000 st=3 ec=1
tc st4-ec2-1
tc st4-ec3-1
tc n-sm-st3 generator n=2500 st=3
tc st4-heuristic-ec4 generator n=250000 st=3 ec=4 
tc st4-ec2 generator n=250000 st=3 ec=2
tc st4-ec3 generator n=250000 st=3 ec=3

group group5 22
limits maxn=5000 maxm=5000
include_group group3
tc nm-sm-rand-1 generator maxn=4999 maxm=5000
tc nm-sm-rand-2 generator maxn=4999 maxm=5000
tc nm-sm-rand-3 generator maxn=4999 maxm=5000
tc nm-sm-rand-4 generator maxn=4999 maxm=5000
tc nm-sm-rand-5 generator maxn=4999 maxm=5000
tc n-sm-rand-1 generator maxn=4999 m=5000
tc n-sm-rand-2 generator maxn=4999 m=5000
tc n-sm-rand-3 generator maxn=4999 m=5000
tc n-sm-rand-4 generator maxn=4999 m=5000
tc n-sm-rand-5 generator maxn=4999 m=5000
tc n1-sm-1 generator n=1 m=5000
tc n-sm-rand-ec1-1 generator maxn=4999 m=5000 ec=1
tc n-sm-rand-ec2-1 generator maxn=4999 m=5000 ec=2
tc n-sm-st1
tc n-sm-st2
tc n-sm-st3
tc n-sm-ec3 generator n=4998 ec=3

group group6 24
limits maxn=$MAXN maxm=$MAXM
include_group group1
include_group group2
include_group group3
include_group group4
include_group group5
tc nm-rand-1 generator
tc nm-rand-2 generator
tc nm-rand-3 generator
tc nm-rand-4 generator
tc nm-rand-5 generator
tc n-rand-1 generator m=$MAXM
tc n-rand-2 generator m=$MAXM
tc n-rand-3 generator m=$MAXM
tc n-rand-4 generator m=$MAXM
tc n-rand-5 generator m=$MAXM
tc n1-1 generator n=1 m=$MAXM
tc n-rand-ec1-1 generator m=$MAXM ec=1
tc n-rand-ec2-1 generator m=$MAXM ec=2
tc n-ec3 generator n=$((MAXN-1)) ec=3
