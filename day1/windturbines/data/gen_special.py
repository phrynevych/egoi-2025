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
q = int(cmdlinearg('q',200000))
cc = int(cmdlinearg('cc',1))
mode = cmdlinearg('mode')
maxl = 0
minr = n-1

def genrange():
  x = random.randint(0,n-1)
  y = random.randint(0,n-1)
  return (min(x,y),max(x,y))

if mode == 'path_increasing_costs':
  e = [(i,i+1,i+1) for i in range(n-1)]
  ql = [genrange() for i in range(q)]
elif mode == 'bitinv':
  e = []
  def go(v,b):
    global e
    if len(v) <= 1:
     return v
    v0 = go([x for x in v if not ((x>>b)&1)], b+1)
    v1 = go([x for x in v if (x>>b)&1], b+1)
    nn = n//100
    e.append((v0[-1], v1[0], nn*100-b*nn+len(e)//100))
    return v0+v1
  go(list(range(n)),0)
  ql = [genrange() for i in range(q)]
  random.shuffle(e)
  random.shuffle(ql)
else:
  assert(False)

if int(cmdlinearg('shuffle',0)):
  perm = list(range(n))
  random.shuffle(perm)
  for i in range(len(e)):
      e[i] = (perm[e[i][0]], perm[e[i][1]], e[i][2])

print(n,len(e),len(ql))
for ei in e:
  print(*ei)
for qi in ql:
  print(*qi)
