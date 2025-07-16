#!/usr/bin/env python3

import sys
import random
import math

MAXN = 499999
MAXM = 500000

def cmdlinearg(name, default = None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

random.seed(int(cmdlinearg('seed', sys.argv[-1])))

MAXN = int(cmdlinearg('maxn', MAXN))
MAXM = int(cmdlinearg('maxm', MAXM))
n = int(cmdlinearg('n', random.randint(1, MAXN)))
m = int(cmdlinearg('m', random.randint(n+1, MAXM)))
st = int(cmdlinearg('st', 0))
ec = int(cmdlinearg('ec', 0))

ppl = []

if st == 1:
    m=n+1
    ppl = list(range(0, n))
    random.shuffle(ppl)
    if ec == 1:
        num = 0
        ppl.remove(num)
        ppl.insert(0, num)
        ppl.append(num)
    elif ec == 2:
        num = random.randint(0, n-1)
        ppl.insert(ppl.index(num), num)
    elif ec == 3:
        num = n-1
        ppl.append(num)
    else:
        ppl.insert(random.randint(0, n-1), random.randint(0, n-1))
elif st == 2:
    m=2*n
    ppl = list(range(0, n))
    random.shuffle(ppl)
    ppl2 = list(range(0, n))
    random.shuffle(ppl2)
    if ec == 1:
        for i, p in enumerate(ppl2):
            if p == ppl[n-1]:
                ppl2[i], ppl2[0] = ppl2[0], ppl2[i]
    if ec == 2:
        ppl2 = ppl
    if ec == 3:
        ppl2 = ppl
        ppl2.reverse()
    ppl += ppl2
elif st == 3:
    m=2*n
    if ec == 1:
        ppl2 = list(range(0, n))
        random.shuffle(ppl2)
        for p in ppl2:
            ppl += [p, p]
    elif ec == 2: # large case for break at the beginning
        tmp = m-8
        ppl = [3,0,2]
        for i in range(int(tmp/2)):
            ppl.append(i+4)
        for i in range(int(tmp/2)-1, -1, -1):
            ppl.append(i+4)
        ppl += [0,2,1,1,3]
    elif ec == 3: # large case for break at the end
        tmp = m-8
        ppl = [3,1,1,2,0]
        for i in range(int(tmp/2)):
            ppl.append(i+4)
        for i in range(int(tmp/2)-1, -1, -1):
            ppl.append(i+4)
        ppl += [2,0,3]
    elif ec == 4: # against heuristic
        tmp = m-4
        tmp /= 2
        for i in range(2*int(tmp)):
            if i < tmp/2:
                ppl.append(i+2)
            elif i >= 3*tmp / 2:
                ppl.append(i-int(tmp)+2)
            else:
                ppl.append(i-int(tmp/2)+2)
        ppl.insert(0,0)
        ppl.insert(int(tmp/2)+1,1)
        ppl.insert(3*int(tmp/2)+2,0)
        ppl.append(1)
    else:
        ppl = list(range(0, n)) + list(range(0, n))
        random.shuffle(ppl)
else:
    ppl = list(range(0, n))
    if ec == 1:
        random.shuffle(ppl)
        ind = random.randint(1, n-3)
        for i in range(m-n):
            ppl.append(ppl[ind])
    elif ec == 2:
        random.shuffle(ppl)
        ind = random.randint(2, n-2)
        for i in range(m-n):
            ppl.insert(0, ppl[ind])
            ind+=1
    elif ec == 3: # against heuristic
        m = n+2
        ppl = list(range(2, n))
        ppl.insert(0, 0)
        ppl.insert(int(m/2)-1, 1)
        ppl.insert(int(m/2), 0)
        ppl.append(1)
    else:
        for i in range(m-n):
            ppl.append(random.randint(0, n-1))
        random.shuffle(ppl)

print(n, m)
print(*ppl)
