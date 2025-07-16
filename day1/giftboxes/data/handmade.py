#!/usr/bin/env python3

import sys

def cmdlinearg(name, default = None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

c = int(cmdlinearg('c', 0))

if c == 1:
    print("4 8")
    print("3 0 2 0 2 1 1 3")
elif c == 2:
    print("4 8")
    print("3 1 1 2 0 2 0 3")
