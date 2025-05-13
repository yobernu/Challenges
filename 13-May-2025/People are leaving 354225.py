# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys

sys.setrecursionlimit(1 << 25)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 2))
        self.n = n

    def find(self, x):
        if x > self.n:
            return -1
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def remove(self, x):
        self.parent[x] = self.find(x + 1)


def main():
    n, m = map(int, input().split())
    dsu = UnionFind(n)

    for _ in range(m):
        parts = input().split()
        sign = parts[0]
        num = int(parts[1])

        if sign == '-':
            dsu.remove(num)
        else:
            res = dsu.find(num)
            print(res if res != -1 and res <= n else -1)


if __name__ == '__main__':
    main()
