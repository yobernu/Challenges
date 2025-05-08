# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1)) 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False 
        self.parent[rootY] = rootX
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ans = []
        n = len(edges)
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                ans.append([u, v])
        return ans[-1]