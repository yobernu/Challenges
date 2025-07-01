# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size           

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False 
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True  

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = []
        
        for i in range(n - 1):
            u, v = points[i][0], points[i][1]
            for j in range(i+1, n):
                l, m = points[j][0], points[j][1]
                cost = abs(u - l) + abs(v - m)
                graph.append([cost, i, j])
        
        graph.sort()
        uf = UnionFind(n)
        count = 0
        res = 0
        for cost, i, j in graph:
            if uf.union(i, j):
                count += 1
                res += cost
                if count == n-1:
                    return res
        return res

