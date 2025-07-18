#!/usr/bin/env python3

import sys
import random
import math

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

random.seed(int(cmdlinearg('seed', sys.argv[-1])))
n = int(cmdlinearg('n'))
mode = cmdlinearg('mode')


e = []
def make_path(v):
    global e
    e += [(v[i],v[i+1]) for i in range(len(v)-1)]

if mode == 'one_and_half_path':
    v = list(range(n))
    va, vb = v[:3*n//4], v[3*n//4:]
    make_path(va)
    make_path(list(reversed(va)))
    make_path(vb)
    e += [(0,vb[0]), (va[-1],n-1)]
elif mode == 'ladder_dag':
    source, sink = 0, n-1
    v = list(range(1,n-1))
    x = (n-2)//8
    a = 3*x//2
    va, v = v[:x], v[x:]
    vb, v = v[:2*x], v[2*x:]
    vc, v = v[:a], v[a:]
    vd, v = v[:a+2*x], v[a+2*x:]
    make_path(va)
    make_path(vb)
    make_path(vc)
    make_path(vd)
    e += [(va[-1-i], vb[2*i]) for i in range(x)]
    e += [(0, u) for u in vd]
    e += [(0, va[0])]
    e += [(vb[-1], vc[0])]
    e += [(va[-1], vd[0])]
    e += [(vc[-1], n-1)]
    e += [(vd[-1], n-1)]
    e += [(0, u) for u in v]
    e += [(u, n-1) for u in v]
else:
    assert(False)

random.shuffle(e);

print(n,len(e))
for a in e:
    print(*a)
