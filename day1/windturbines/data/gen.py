#!/usr/bin/env python3

import sys 
import random
import math
import heapq 
def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

random.seed(int(cmdlinearg('seed', sys.argv[-1])))
n = int(cmdlinearg('n'))
m = int(cmdlinearg('m'))
q = int(cmdlinearg('q',200000))
maxw = int(cmdlinearg('maxw'))
mode = cmdlinearg('mode')
tree = cmdlinearg('tree','random')
weights = cmdlinearg('weights','random')
cc = int(cmdlinearg('cc',1))
shuffle = int(cmdlinearg('shuffle',1))
maxl = 0
minr = n-1

def gen_tree(n, tree):
    e = []
    if tree == "random":
        for i in range(1,n):
            p = random.randint(0,i-1)
            e.append((i,p))
    elif tree == "caterpillar":
        pathlen = random.randint(2,n-2)
        for i in range(0,pathlen):
            e.append((i,i+1))
        for i in range(pathlen+1,n):
            p = random.randint(0,pathlen)
            e.append((i,p))
    elif tree == "broom":
        pathlen = random.randint(2,n-2)
        for i in range(0,pathlen):
            e.append((i,i+1))
        for i in range(pathlen+1,n):
            p = 0
            e.append((i,p))
    elif tree == "pruefer":
        length = n - 2
        p = [random.randint(0, length + 1) for _ in range(length)]
        d = [0 for _ in range(n)]
        for i in p:
            d[i] += 1

        leaves = []
        for i in range(n):
            if d[i] == 0:
                heapq.heappush(leaves,i)

        for (i, u) in enumerate(p):
            v = heapq.heappop(leaves)
            e.append((u,v))
            d[u] -= 1
            if d[u] ==0:
                heapq.heappush(leaves,u)
        e.append((heapq.heappop(leaves),heapq.heappop(leaves)))
        assert(not leaves)
    elif tree=="1or2":
        global maxl
        global minr
        if cc > n//10:
            cc = max(n//10,1) 
        ccs = [0]+sorted(ccs)+[n]
        e = []
        assert len(ccs) == cc+1
        for c in range(cc):
            base = ccs[c]
            tr = gen_tree(ccs[c+1] - base, 'random')
            for ed in tr:
                ed = (ed[0] + base, ed[1] + base,1)
                e.append(ed)
        for c in range(cc-1):
            ed = (random.randrange(ccs[c],ccs[c+1]),random.randrange(ccs[c+1],ccs[c+2]),2)
        for c in range(cc):
            l = n
            r = 0
            for i in range(ccs[c],ccs[c+1]):
                r = max(r,perm[i])
                l = min(l,perm[i])
            maxl = max(l,maxl)
            minr = min(r,minr)
        weights = 'treeset'
        
    return e

def graph(tree):
    global m
    perm = list(range(n))
    if shuffle:
        random.shuffle(perm)
    e = []
    e_set = set()
    tr = gen_tree(n, tree)
    assert(len(tr)==n-1)
    for ed in tr:
        e.append(ed)
        e_set.add((ed[0], ed[1]))
        e_set.add((ed[1], ed[0]))
    fails = 0
    while len(e) < m and fails < 1000:
        u = random.randrange(0,n)
        v = random.randrange(0,n)
        if u == v:
            continue
        if (u,v) not in e_set:
            e_set.add((u,v))
            e_set.add((v,u))
        else:
            fails += 1
    if weights == 'random':
        e = [(perm[u],perm[v],random.randint(1,maxw)) for (u,v) in e]
    if weights == 'increasing':
        start = 0
        for i in range(len(e)):
            w = random.randint(start,(i+1)*maxw//(m+1))
            start = w
            (u,v) = e[i]
            e[i] = (perm[u],perm[v],w)
    if weights == 'decreasing':
        start = 0
        for i in range(len(e)):
            w = random.randint(start,(i+1)*maxw//(m+1))
            start = w
            (u,v) = e[i]
            e[i] = (perm[u],perm[v],w)
    if weights == 'treeset':
        et = [(perm[u],perm[v],w) for (u,v,w) in e[:n]]
        er = [(perm[u],perm[v],2) for (u,v) in e[n:]]
    m = len(e)
    return e



if mode == 'path':
    m = n-1
    e = [(i,i+1,random.randint(1,maxw)) for i in range(m)]
    ql = [(x,random.randint(x,n-1)) for x in [random.randint(0,n-1) for _ in range(q)]]
elif mode == 'smallw':
    e = graph(tree)
    ql = []
    for _ in range(q):
        poss = random.random() < 0.6 or cc==1 or minr < maxl

        if poss and cc>1:
            l = random.randint(0,maxl)
            r = random.randint(max(l,minr),n-1)
        elif poss:
            l = random.randint(0,n-1)
            r = random.randint(l,n-1)
        else:
            if random.randint(0,1):
                l = random.randint(maxl+1,n-1)
                r = random.randint(l,n-1)
            else:
                r =random.randint(0,minr-1)
                l = random.randint(0,r)
            
        ql.append((l,r))
elif mode == 'sum_many':
    maxs  = int(cmdlinearg('maxs'))
    size = int(cmdlinearg('size',10))
    e = graph(tree)
    ql = []
    while maxs > 0 and len(ql)<q:
        l = random.randint(0,n-1)
        r = random.randint(l,l+min(size,maxs-1))
        if r>n-1:
            r=n-1
        ql.append((l,r))
        maxs -= (r-l+1)
    q = len(ql)
elif mode == 'sum_random':
    maxs  = int(cmdlinearg('maxs'))
    e = graph(tree)
    ql = []
    while maxs >0:
        l = random.randint(0,n-1)
        r = random.randint(l,n-1)
        if r - l +1 >maxs:
            r = l + maxs-1
        ql.append((l,r))
        maxs -= (r-l+1)
    q = len(ql)

elif mode == 'tuple':
    e = graph(tree)
    ql = []
    while len(ql) < q:
        l = random.randint(0,n-2)
        r = l+1
        ql.append((l,r))
elif mode=='left': 
    e = graph(tree)
    ql = []
    for _ in range(q):
        l = 0
        r = random.randint(l,n-1)
        ql.append((l,r))
else:
    e = graph(tree)
    ql = [(l,random.randint(l,n-1)) for l in [random.randint(0,n-1) for _ in range(q)]]


# print everything
if mode != 'path':
    random.shuffle(e)
random.shuffle(ql)
print(n,m,q)
for ei in e:
    print(*ei)
for qi in ql:
    assert(qi[0]<=qi[1])
    print(*qi)

