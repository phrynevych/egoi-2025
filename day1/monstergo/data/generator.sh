#!/usr/bin/env bash
REQUIRE_SAMPLE_REUSE=0
. ../../../testdata_tools/gen.sh

use_solution jb.py

compile echo.sh

#TODO: should we have a sample or not?
samplegroup
limits group=2
sample_manual 1

for i in {1..50}; do
  group $(printf "group%03d" $i) 2
  limits group=$i
  tc tc$i echo $i
done
