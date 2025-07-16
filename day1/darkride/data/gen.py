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

if mode == 'random':
    perm = list(range(n))
    random.shuffle(perm);
elif mode == 'sorted':
    perm = list(range(n))
elif mode == 'cyclic':
    perm = []
    shift = int(cmdlinearg('shift', random.randint(0,n)))
    for i in range(n):
        perm.append((i + shift + n) % n)
elif mode == 'reversed':
    perm = list(reversed(list(range(n))))
else:
    assert(False)

if int(cmdlinearg('force_first', 0)):
    a = perm.index(0)
    perm[a], perm[0] = perm[0], perm[a]
    assert(perm[0] == 0)

if int(cmdlinearg('half', 0)):
    while perm.index(0)*2 >= n or perm.index(n-1)*2 < n:
        random.shuffle(perm);

print(n)
print(*perm)
