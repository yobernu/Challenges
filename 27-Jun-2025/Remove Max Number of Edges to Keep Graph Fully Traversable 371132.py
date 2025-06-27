# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        self.components -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dsu_alice = UnionFind(n)
        dsu_bob = UnionFind(n)
        remove = 0

        for _type, u, v in edges:
            u -= 1
            v -= 1
            if _type == 3:
                added_alice = dsu_alice.union(u, v)
                added_bob = dsu_bob.union(u, v)
                if not (added_alice or added_bob):
                    remove += 1
        for _type, u, v in edges:
            u -= 1
            v -= 1
            if _type == 1:
                if not dsu_alice.union(u, v):
                    remove += 1
        for _type, u, v in edges:
            u -= 1
            v -= 1
            if _type == 2:
                if not dsu_bob.union(u, v):
                    remove += 1
        if dsu_alice.components > 1 or dsu_bob.components > 1:
            return -1
        return remove
