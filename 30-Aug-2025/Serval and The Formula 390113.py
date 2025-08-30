# Problem: Serval and The Formula - https://codeforces.com/problemset/problem/2085/C

import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        x, y = map(int, sys.stdin.readline().split())
        if x == y:
            print(-1)
            continue
        else:
            k = 2**48 - max(x, y)
            print(k)
solve()