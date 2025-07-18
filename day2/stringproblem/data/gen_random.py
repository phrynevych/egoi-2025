#!/usr/bin/env python3

import sys
import random
import math

MAXN = 10000

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

def all_parallel(n, angle):
    # offset must be odd
    assert angle % 2 == 1
    return [[i, (angle - i + 2 * n) % (2 * n)] for i in range(2 * n) if i < (angle - i + 2 * n) % (2 * n) ]

random.seed(int(cmdlinearg('seed', sys.argv[-1])))

MAXN = int(cmdlinearg('maxn', MAXN))
n = int(cmdlinearg('n', random.randint(2, MAXN)))
mode = cmdlinearg('mode', '')
swaps = int(cmdlinearg('swaps', random.randint(0, n)))
close = int(cmdlinearg('close', 0))

if mode == '':
    endpoints = list(range(n)) + list(range(n))
    random.shuffle(endpoints)
    hair = [[] for _ in range(n)]
    for i, h in enumerate(endpoints):
        hair[h].append(i)
elif mode == 'swap':
    angle = int(cmdlinearg('angle', 2 * random.randint(0, n - 1) + 1))
    # halfangle = random.randint(0, n - 1)
    hair = all_parallel(n, angle)
    # print(hair, n, halfangle, swaps)
    for _ in range(swaps):
        h1 = 0
        h2 = 0
        while h1 == h2:
            h1 = random.randint(0, n - 1)
            e1 = random.randint(0, 1)
            h2 = random.randint(0, n - 1)
            e2 = random.randint(0, 1)
        # print(h1, e1, h2, e2)

        if close == 1:
            hair[h1][e1], hair[(h1 + 1) % n][e1] = hair[(h1 + 1) % n][e1], hair[h1][e1]
        else:
            hair[h1][e1], hair[h2][e2] = hair[h2][e2], hair[h1][e1]
        # print(hair)
    random.shuffle(hair)
    # print(hair)
elif mode == 'adjacent':
    hair = [[2 * i, 2 * i + 1] for i in range(n)]
elif mode == 'against_random':
    hair = [[n, n + 1], [n - 1, n + 2]]
    hair += [[i % (2 * n), (i + n - 2) % (2 * n)] for i in range(n + 3, 2 * n + 1)]
    random.shuffle(hair)
elif mode == 'maxsol':
    odd = [i for i in range(n) if i % 2 == 1] + [i for i in range(n) if i % 2 == 1]
    even = [i for i in range(n) if i % 2 == 0] + [i for i in range(n) if i % 2 == 0]
    random.shuffle(odd)
    random.shuffle(even)
    hair = [[] for _ in range(n)]
    for i, h in enumerate(odd):
        hair[h].append(2 * i + 1)
    for i, h in enumerate(even):
        if 2 * i >= 2 * n:
            hair[h].append(2 * i - 1)
        else:
            hair[h].append(2 * i)
    random.shuffle(hair)

print(n)
for h in hair:
    random.shuffle(h)
    print(*h)
