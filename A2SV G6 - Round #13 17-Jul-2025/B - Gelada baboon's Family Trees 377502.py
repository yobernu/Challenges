# Problem: B - Gelada baboon's Family Trees - https://codeforces.com/gym/607625/problem/B

import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * (n)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[y] < self.rank[x]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1
def main():
    input = sys.stdin.readline
    n = int(input())
    p = list(map(int, input().split()))
    p = [x - 1 for x in p]
    dsu = UnionFind(n)
    for i in range(n):
        dsu.union(i, p[i])
    roots = set(dsu.find(i) for i in range(n))
    print(len(roots))

if __name__ == '__main__':
    main()