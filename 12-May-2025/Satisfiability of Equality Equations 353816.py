# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]

class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        uf = UnionFind(26)
        for eq in equations:
            if eq[1:3] == "==":
                uf.union(ord(eq[0]) - 97, ord(eq[3]) - 97)
        for eq in equations:
            if eq[1:3] == "!=":
                if uf.find(ord(eq[0]) - 97) == uf.find(ord(eq[3]) - 97):
                    return False
        return True
