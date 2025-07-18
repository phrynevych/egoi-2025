#!/usr/bin/env python3

import sys
import random
import math

MAXN = 20000
MAXM = 100
MAXK = 100

def gen_scores(lo, hi, target):
    res = []
    assert lo*m <= target <= hi*m
    for i in range(m):
        res.append(lo)
        target -= lo
    while target > 0:
        i = random.randrange(0, m)
        if res[i] < hi:
            res[i] += 1
            target -= 1
    return res

def cmdlinearg(name, default = None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

random.seed(int(cmdlinearg('seed', sys.argv[-1])))

n = int(cmdlinearg('n', random.randint(1, MAXN)))
m = int(cmdlinearg('m', random.randint(1, MAXM)))
k = int(cmdlinearg('k', random.randint(1, MAXM)))

mode = cmdlinearg('mode', 'random')
A = []

if mode == "random":
    ex = float(cmdlinearg('ex', 0.0))
    for i in range(n):
        row = []
        for _ in range(m):
            if random.random() < ex:
                if random.randint(0,1) == 0:
                    row.append(0)
                else:
                    row.append(k)
            else:
                row.append(random.randint(0, k))
        A.append(row)

elif mode == "all_max":
    noise = int(cmdlinearg('noise', 0))
    for i in range(n):
        row = [k] * m
        A.append(row)
    for _ in range(noise):
        i = random.randrange(0, n)
        j = random.randrange(0, m)
        A[i][j] = random.randint(0, k-1)

elif mode == "random_subsetsum":
    p = int(cmdlinearg('p', 3))
    B = [random.randint(0, k) for _ in range(m)]
    tries = 0
    lim = 100
    while tries < lim:
        x = sum(random.sample(B, p))
        if m <= x <= (k-1)*m - (m-p)*k:
            break
        B = [random.randint(0, k) for _ in range(m)]
        tries += 1
    assert tries < lim

    for i in range(n//2):
        A.append(gen_scores(0,k-1,x+(m-p)*k))
    A.append(B)
    while len(A) < n:
        A.append(gen_scores(1, k, x))

elif mode == "mod_subsetsum":
    p = int(cmdlinearg('p', 3))
    B = []
    tries = 0
    lim = 100
    while tries < lim:
        B = [(p+1) * (random.randint(0, k // (p+1) - 1)) + 1 for _ in range(m)]
        inds = random.sample(range(m), p)
        x = 0
        for i in inds:
            B[i] -= 1
            x += B[i]
        if m <= x <= (k-1)*m - (m-p)*k:
            break
        tries += 1
    assert tries < lim
    for i in range(n//2):
        A.append(gen_scores(0,k-1,x+(m-p)*k))
    A.append(B)
    while len(A) < n:
        A.append(gen_scores(1, k, x))

elif mode == "halves":
    p = int(cmdlinearg('p', 0))
    flip = int(cmdlinearg('flip', 0))
    # Half of scores are in [0, p] and half are in [m*k-p,m*k]
    for i in range(n):
        target = random.randint(0, p)
        if i%2 == flip:
            target = m*k-target
        A.append(gen_scores(0, k, target))

elif mode == "tiny":
    mask = int(cmdlinearg('mask'))
    n = 2
    m = 2
    k = 1
    s = ""
    s01 = "01"
    for _ in range(4):
        s += s01[mask%2]
        mask //= 2
    A.append([s[0], s[1]])
    A.append([s[2], s[3]])

elif mode == "block":
    ss = int(cmdlinearg('ss'))
    A.append([0] * m)
    prev = 0
    while prev < m*k:
        goal = prev+1
        if ss*k < goal:
            ss = (goal+k-1) // k
        lst = [0] * ss
        for _ in range(goal):
            j = random.randrange(0, ss)
            while lst[j] == k:
                j = random.randrange(0, ss)
            lst[j] += 1
        while len(lst) < m:
            lst.append(random.randint(0, k))
            #lst.append(k)
        
        random.shuffle(lst)
        A.append(lst)

        nex = goal + (m-ss)*k + 1
        if nex > m*k:
            break
        nex2 = nex
        lst2 = []
        while nex2 > 0:
            lst2.append(min(k, nex2))
            nex2 -= lst2[-1]
        while len(lst2) < m:
            lst2.append(0)
        prev = nex
        random.shuffle(lst2)
        A.append(lst2)
    n = len(A)

elif mode == "spam":
    X = []
    for _ in range(n):
        X.append(random.randint(0, k))
    X.sort()
    X = X[::-1]
    for i in range(n):
        A.append([X[i]] * m)

elif mode == "force":
    x = int(cmdlinearg(('x')))
    am = int(cmdlinearg('am', 2))
    a = m // am
    d = (m - a) * x
    goal = a * x

    score1 = [0] * m
    score1 = gen_scores(0, k, goal)
    A.append(score1)

    goal2 = goal
    score2 = [0] * m
    for i in range(m):
        score2[i] = min(k, goal2)
        goal2 -= score2[i]
    random.shuffle(score2)
    A.append(score2)

    A.append([x]*m)

    hi = a*x + (m-a)*k
    score3 = gen_scores(0, k, hi)
    score4 = gen_scores(0, k, hi)

    A.append(score3)
    A.append(score4)
    A = A[::-1]

    n = len(A)

print(n,m,k)
for i in range(n):
    print(*A[i])



