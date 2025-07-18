#!/usr/bin/env python3

import sys
import random
import math
import heapq

none = object()
def cmdlinearg(name, default=none):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not none, name
    return default

def linestar_exp(n):
    news = set()
    cur = 1
    perm = list(range(n-1))
    random.shuffle(perm)
    cyclens = []
    seen = [0] * (n-1)
    for i in range(len(perm)):
        if seen[i]:
            continue
        j = i
        cyclen = 0
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            cyclen += 1
        news.add(cur)
        cur += cyclen
    assert cur == n
    return news

def line_alt(n):
    assert n%2==0
    eds = []
    eds.append((n//2,n//2-1))
    u = n//2
    v = n//2-1
    for i in range(n//2-1):
        eds.append((u,n//2-2-i))
        eds.append((v,n//2+1+i))
        u = n//2+1+i
        v = n//2-2-i
    assert len(eds) == n-1
    return eds

def broom_alt(n,k):
    eds = []
    eds.append((0,1))
    for i in range(2,k):
        eds.append((1,i))
    l = k-1
    h = n-1
    even = 1
    for i in range(n-k):
        eds.append((h,l))
        if even:
            l += 1
        else:
            h -= 1
        even = 1-even
    return eds

def pruefer(n):
    p = [random.randrange(n) for _ in range(n - 2)]
    d = [0] * n
    for i in p:
        d[i] += 1

    leaves = []
    for i in range(n):
        if d[i] == 0:
            heapq.heappush(leaves, i)

    eds = []
    for (i, u) in enumerate(p):
        v = heapq.heappop(leaves)
        eds.append((u, v))
        d[u] -= 1
        if d[u] == 0:
            heapq.heappush(leaves, u)
    eds.append((heapq.heappop(leaves), heapq.heappop(leaves)))
    assert not leaves
    return eds

def rand_partition(n, k):
    splits = [-1] + sorted(random.sample(range(n+k-1), k-1)) + [n+k-1]
    return [b - a - 1 for a,b in zip(splits, splits[1:])]

def is_interesting(tr):
    n = len(tr) + 1
    degs = [0] * n
    for (u, v) in tr:
        degs[u] += 1
        degs[v] += 1
    degc = [0] * n
    for i in range(n):
        degc[degs[i]] += 1
    if degc[1] + degc[2] >= n-1:
        # linestar or line
        return False
    return True

def stretch_tree(tr, n):
    small_n = len(tr) + 1
    edge_lens = [x + 1 for x in rand_partition(n-1 - len(tr), len(tr))]
    ind = small_n
    ned = []
    for i, (u, v) in enumerate(tr):
        prev = u
        for j in range(edge_lens[i] - 1):
            ned.append((prev, ind))
            prev = ind
            ind += 1
        ned.append((prev, v))
    return ned

def gen_tree(n, k, mode, maxdepth):
    if mode == 'line-alt':
        return line_alt(n)
    if mode == 'broom-alt':
        return broom_alt(n,k)
    if mode == 'pruefer':
        return pruefer(n)
    if mode == 'linestar':
        news = set([1] + random.sample(range(2, n), k-1))
    if mode == 'linestar-exp':
        news = linestar_exp(n)
        mode = 'linestar'
    if mode.startswith('stretched,'):
        _,mode2,n2 = mode.split(",")
        while True:
            small = gen_tree(int(n2), k, mode2, maxdepth)
            if is_interesting(small):
                break
        return stretch_tree(small, n)
    eds = []
    depths = [0]
    while len(depths) < n:
        i = len(depths)
        if mode == 'random':
            pred = random.randrange(i)
        elif mode == 'star':
            pred = 0
        elif mode == 'line':
            pred = i - 1
        elif mode == 'almostline':
            if i < n - k:
                pred = i - 1
            else:
                pred = random.randrange(1, i-1)
        elif mode == 'broom':
            if i <= k:
                pred = 0
            else:
                pred = i - 1
        elif mode == 'caterpillar-random':
            if i < k:
                pred = i - 1
            else:
                pred = random.randrange(k)
        elif mode == 'caterpillar':
            if i < k:
                pred = i - 1
            else:
                pred = i - k
        elif mode == 'dumbbell':
            if i <= k + 1:
                pred = 0
            elif i < n - k:
                pred = i - 1
            else:
                pred = n - k - 1
        elif mode in 'binary':
            pred = (i - 1) // 2
        elif mode == 'shallow':
            pred = int(random.uniform(0, i**0.1) ** 5)
        elif mode == 'shallower':
            pred = int(1.5**random.uniform(-2, math.log2(i)))
        elif mode == 'deep':
            pred = i-1 - int(random.uniform(0, i**0.1) ** 10)
        elif mode == 'deeper':
            if i < 4:
                pred = random.randrange(i)
            else:
                hi = math.log2(math.log2(i))
                pred = i - int(2 ** 2 ** min(random.uniform(-3, hi), random.uniform(-3, hi), random.uniform(-3, hi)))
        elif mode == 'linestar':
            if i in news:
                pred = 0
            else:
                pred = i - 1
        else:
            assert False, f"unknown mode {mode}"
        assert 0 <= pred < i
        ndep = depths[pred] + 1
        if ndep > maxdepth:
            continue
        eds.append((pred, i))
        depths.append(ndep)

    return eds

def main():
    random.seed(int(cmdlinearg("seed", sys.argv[-1])))
    n = int(cmdlinearg("n"))
    maxdepth = int(cmdlinearg("maxdepth", n))
    shuffle = int(cmdlinearg("shuffle", 1))
    rename = cmdlinearg("rename", "1")
    k = cmdlinearg("k", None)
    if k is not None:
        k = int(k)
    mode = cmdlinearg("mode")

    eds = gen_tree(n, k, mode, maxdepth)
    print(0)
    print(n)
    if shuffle:
        random.shuffle(eds)
    ren = list(range(n))
    if rename == "rev":
        ren = ren[::-1]
    elif rename.startswith("center,"):
        random.shuffle(ren)
        v = int(rename.split(",")[-1]) % n
        deg = [0] * n
        for a, b in eds:
            deg[a] += 1
            deg[b] += 1
        p = deg.index(max(deg))
        i = ren.index(v)
        ren[i], ren[p] = ren[p], ren[i]
    elif rename.startswith("extra,"):
        random.shuffle(ren)
        v = int(rename.split(",")[-1]) % n
        p = n-1
        i = ren.index(v)
        ren[i], ren[p] = ren[p], ren[i]
    elif rename == "fliphalf":
        ren[n//2:] = reversed(ren[n//2:])
    elif rename == "fliphalf2":
        ren[:n//2] = reversed(ren[:n//2])
    elif rename == "fliphalf3":
        ren[:n//2] = reversed(ren[:n//2])
        ren[n//2:] = reversed(ren[n//2:])
    elif int(rename):
        random.shuffle(ren)
    for a, b in eds:
        a,b = ren[a],ren[b]
        if a > b:
            a,b = b,a
        print(a, b)

main()
