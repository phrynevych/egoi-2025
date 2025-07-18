#!/usr/bin/env python3

"""
Example usage:

First create an input file, like "sample1.in" with the following contents:
7
0 1
1 2
2 3
0 4
0 6
1 5

For python programs, say "solution.py" (normally run as "pypy3 solution.py"):

    python3 testing_tool.py pypy3 solution.py < sample1.in

For C++ programs, first compile it
(e.g. with "g++ -g -O2 -std=gnu++20 -static solution.cpp -o solution.out")
and then run

    python3 testing_tool.py ./solution.out < sample1.in

"""

from contextlib import contextmanager
from dataclasses import dataclass
from io import BufferedReader, BufferedWriter
import os
import signal
import sys
from typing import Iterator, List, Optional, Tuple


def error(msg: str) -> None:
    print("ERROR:", msg, file=sys.stderr)
    sys.exit(1)

def parse_int(s: str, what: str, lo: int, hi: int) -> int:
    try:
        ret = int(s)
    except Exception:
        error(f"Failed to parse {what} as integer: {s}")
    if not (lo <= ret <= hi):
        error(f"{what} out of bounds: {ret} not in [{lo}, {hi}]")
    return ret

def is_connected(adj: List[List[int]]) -> bool:
    q = [0]
    seen = set()
    while q:
        x = q.pop()
        if x not in seen:
            seen.add(x)
            for y in adj[x]:
                q.append(y)
    return len(seen) == len(adj)

@dataclass
class Submission:
    pid: Optional[int]
    fout: BufferedWriter
    fin: BufferedReader

    def wait(self) -> None:
        if self.pid is None:
            return
        pid, status = os.waitpid(self.pid, 0)
        self.pid = None
        if os.WIFSIGNALED(status):
            sig = os.WTERMSIG(status)
            error(f"Program terminated with signal {sig} ({signal.Signals(sig).name})")
        ex = os.WEXITSTATUS(status)
        if ex != 0:
            error(f"Program terminated with exit code {ex}")

    def kill(self) -> None:
        if self.pid is not None:
            os.kill(self.pid, 9)
            os.waitpid(self.pid, 0)
            self.pid = None

    def read_line(self, what: str) -> str:
        line = self.fin.readline()
        if not line:
            self.wait()
            error(f"Failed to read {what}: no more output")
        return line.decode("latin1").rstrip("\r\n")

    def write_line(self, line: str) -> None:
        try:
            self.fout.write((line + "\n").encode("ascii"))
            self.fout.flush()
        except BrokenPipeError:
            pass


@contextmanager
def run_submission(submission: List[str]) -> Iterator[Submission]:
    sys.stdout.flush()
    sys.stderr.flush()

    c2p_read, c2p_write = os.pipe()
    p2c_read, p2c_write = os.pipe()
    pid = os.fork()

    if pid == 0:
        os.close(p2c_write)
        os.close(c2p_read)

        os.dup2(p2c_read, 0)
        os.dup2(c2p_write, 1)

        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
        try:
            os.execvp(submission[0], submission)
        except Exception as e:
            error(f"Failed to execute program: {e}")
        assert False, "unreachable"
    else:
        os.close(c2p_write)
        os.close(p2c_read)

        with os.fdopen(p2c_write, "wb") as fout:
            with os.fdopen(c2p_read, "rb") as fin:
                sub = Submission(pid, fout, fin)
                try:
                    yield sub

                    # Wait for program to terminate, and read all its output
                    remainder = fin.read().decode("latin1")
                    if remainder.strip():
                        error(f"Unexpected trailing output: {remainder}")
                    try:
                        fin.close()
                    except BrokenPipeError:
                        pass
                    try:
                        fout.close()
                    except BrokenPipeError:
                        pass

                    sub.wait()
                except:
                    sub.kill()
                    raise

def main() -> None:
    silent = False
    args = sys.argv[1:]
    if args and args[0] == "--silent":
        args = args[1:]
        silent = True
    if not args:
        print("Usage:", sys.argv[0], "[--silent] program... <input.txt")
        sys.exit(0)

    n = parse_int(input(), "N", 1, 10**9)
    edges = []
    edges_set = set()
    adj: List[List[int]] = [[] for _ in range(n)]
    for i in range(n - 1):
        line = input()
        parts = line.split()
        if len(parts) != 2:
            error(f"Each line after the first must contain two numbers, but found: {line}")
        a = parse_int(parts[0], "vertex", 0, n-1)
        b = parse_int(parts[1], "vertex", 0, n-1)
        if a >= b:
            error(f"Edges must be ordered such that a < b, but found: {line}")
        edges.append((a, b))
        edges_set.add((a, b))
        adj[a].append(b)
        adj[b].append(a)

    if not is_connected(adj):
        error("Input is not a tree")

    print(f"[*] Running phase 1 (N = {n})")

    outs = []
    with run_submission(args) as sub:
        sub.write_line(f"1 {n}")
        for a, b in edges:
            sub.write_line(f"{a} {b}")
        help_str = sub.read_line("help bits")
        if not silent:
            print(f"[*] Got help string = {help_str}")
        if any(x not in "01" for x in help_str):
            error(f"Help string must contain only binary digits (0/1), but got: {help_str}")
        if len(help_str) > 1000:
            error(f"Help string must have length at most 1000, but got: {len(help_str)}")
        is_removed = [False] * n
        for i in range(n - 1):
            leaf = parse_int(sub.read_line("vertex"), "vertex", 0, n-1)
            if not silent:
                print(f"[*] Next vertex: {leaf}")
            if is_removed[leaf]:
                error(f"Vertex {leaf} is removed twice")
            adj_remaining = [x for x in adj[leaf] if not is_removed[x]]
            if len(adj_remaining) != 1:
                error(f"Vertex {leaf} is not a leaf")
            outs.append((leaf, adj_remaining[0]))
            is_removed[leaf] = True

    print(f"[*] Running phase 2")

    with run_submission(args) as sub:
        sub.write_line(f"2 {n}")
        sub.write_line(help_str)
        for edge in outs:
            tree_edge = edge if edge in edges_set else (edge[1], edge[0])
            sub.write_line(f"{tree_edge[0]} {tree_edge[1]}")
            guess = parse_int(sub.read_line("choice"), "choice", 0, n-1)
            if not silent:
                print(f"[*] Selecting between {tree_edge[0]}, {tree_edge[1]} -> {guess}")
            if guess not in tree_edge:
                print(f"[*] Wrong Answer: picked another vertex than the two allowed: program guessed {guess}, but only {tree_edge[0]} and {tree_edge[1]} are allowed")
                sys.exit(1)
            if guess != edge[0]:
                print(f"[*] Wrong Answer: picked the wrong vertex: program guessed {guess}, but the correct choice was {edge[0]}")
                sys.exit(1)

    print(f"[*] OK: K = {len(help_str)}")

if __name__ == "__main__":
    main()
