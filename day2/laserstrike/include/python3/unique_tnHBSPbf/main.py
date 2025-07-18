#!/usr/bin/env python3
from dataclasses import dataclass
from io import BufferedReader, BufferedWriter
import os
import runpy
import sys
from typing import Callable, List, Optional, Tuple


def judge_main() -> None:
    HANDSHAKE_REQ = "must_use_cpp_or_python"
    HANDSHAKE_RESP = "NPMzpA53vMVb"
    ACCEPTED_MSG = "OK:LWWe75RrS4Vq"

    assert input() == HANDSHAKE_REQ
    print(HANDSHAKE_RESP)

    # Identify the submission file
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    relevant_files = []
    for dname, dirs, files in os.walk(parent_dir):
        if "unique_tnHBSPbf" in dname:
            continue
        for fname in files:
            if fname.endswith(".py"):
                relevant_files.append(os.path.join(dname, fname))
    assert len(relevant_files) == 1, "must be exactly one Python file in submission"
    sub_file = relevant_files[0]

    is_sample = int(input())
    interaction = ""
    N = int(input())
    full_tree = []
    full_tree_set = set()
    for i in range(N-1):
        a, b = map(int, input().split())
        full_tree.append((a, b))
        full_tree_set.add((a, b))

    # send stdout to stderr for the user program
    real_stdout = os.fdopen(os.dup(1), "w", closefd=False)
    os.dup2(2, 1)

    # redirect the stdin fd to make it slightly harder to read stdin twice
    os.close(0)
    os.open("/dev/null", os.O_RDONLY)

    def print_and_exit(msg: str):
        real_stdout.write(msg + "\n")
        sys.exit(0)

    def fail(msg: str):
        msg = msg.split("\n")[0]
        print_and_exit(f"WA:zzxUGG46vWcg\n{msg}\n{interaction}")

    def parse_int(s: str, what: str, lo: int, hi: int) -> int:
        # parse a base-10 number, ignoring leading/trailing spaces
        try:
            ret = int(s)
        except Exception:
            fail(f"failed to parse {what} as integer: {s}")
        if not (lo <= ret <= hi):
            fail(f"{what} out of bounds: {ret} not in [{lo}, {hi}]")
        return ret

    @dataclass
    class Submission:
        pid: int
        fout: BufferedWriter
        fin: BufferedReader

        def wait(self) -> None:
            pid, status = os.waitpid(self.pid, 0)
            if os.WIFSIGNALED(status):
                # propagate the signal, or if not possible at least exit with an error
                os.kill(os.getpid(), os.WTERMSIG(status))
                sys.exit(1)
            ex = os.WEXITSTATUS(status)
            if ex != 0:
                sys.exit(ex)

        def read_line(self, what: str) -> str:
            nonlocal interaction
            line = self.fin.readline()
            if not line:
                self.wait()
                fail(f"Failed to read {what}: no more output")
            ret = line.decode("latin1").rstrip("\r\n")
            if is_sample:
                interaction += f">{ret}\n"
            return ret

        def write(self, s: str) -> None:
            nonlocal interaction
            if is_sample:
                interaction += f"<{s}"
            try:
                self.fout.write(s.encode("ascii"))
                self.fout.flush()
            except BrokenPipeError:
                pass

    def run_submission(callback: Callable[[Submission], None]):
        sys.stdout.flush()
        sys.stderr.flush()

        # CPython and Pypy don't currently use threads, so using fork without exec
        # here is safe.
        c2p_read, c2p_write = os.pipe()
        p2c_read, p2c_write = os.pipe()
        pid = os.fork()

        if pid == 0:
            os.close(p2c_write)
            os.close(c2p_read)

            os.dup2(p2c_read, 0)
            os.dup2(c2p_write, 1)

            runpy.run_path(sub_file, {}, "__main__")

            sys.stdout.flush()
            sys.stderr.flush()
            os._exit(0)
        else:
            os.close(c2p_write)
            os.close(p2c_read)

            with os.fdopen(p2c_write, "wb") as fout:
                with os.fdopen(c2p_read, "rb") as fin:
                    sub = Submission(pid, fout, fin)
                    callback(sub)

                    # Wait for program to terminate, and check for trailing output
                    remainder = fin.read().decode("latin1")
                    if remainder.strip():
                        nonlocal interaction
                        if is_sample:
                            interaction += f">{remainder}\n"
                        fail(f"Unexpected trailing output: {remainder}")
                    try:
                        fin.close()
                    except BrokenPipeError:
                        pass
                    try:
                        fout.close()
                    except BrokenPipeError:
                        pass

                    sub.wait()

    comm_edges = []
    comm_str = []
    help_str = ""

    def phase1(sub: Submission) -> None:
        nonlocal help_str

        sub.write(f"1 {N}\n" + "".join(f"{a} {b}\n" for a, b in full_tree))

        help_str = sub.read_line("help string")
        if any(c not in "01" for c in help_str):
            fail(f"help is not a binary string: {help_str}")
        if len(help_str) > 1000:
            fail("help string is too long")

        deg = [0] * N
        adj_xor = [0] * N
        for (a, b) in full_tree:
            deg[a] += 1
            deg[b] += 1
            adj_xor[a] ^= b
            adj_xor[b] ^= a

        for i in range(N - 1):
            line = sub.read_line("node index")
            a = parse_int(line, "node index", 0, N-1)
            if deg[a] != 1:
                fail("must remove a leaf node in each stage")
            b = adj_xor[a]
            deg[a] -= 1
            deg[b] -= 1
            adj_xor[a] ^= b
            adj_xor[b] ^= a
            comm_edges.append((a, b))
            if (a, b) not in full_tree_set:
                a, b = b, a
            assert (a, b) in full_tree_set
            comm_str.append(f"{a} {b}\n")

    def phase2(sub: Submission) -> None:
        sub.write(f"2 {N}\n{help_str}\n")

        for (a, b), out_line in zip(comm_edges, comm_str):
            sub.write(out_line)
            line = sub.read_line("guessed index")
            x = parse_int(line, "guessed index", 0, N-1)
            if x != a and x != b:
                fail("guessed a vertex that was not an endpoint")
            if x != a:
                fail("guessed the wrong vertex")

    run_submission(phase1)
    run_submission(phase2)

    sys.stdout.flush()

    print_and_exit(f"{ACCEPTED_MSG}\n{len(help_str)}")

if __name__ == "__main__":
    judge_main()
