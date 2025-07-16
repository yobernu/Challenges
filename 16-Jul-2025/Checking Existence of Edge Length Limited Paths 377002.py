# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[px] = py
        edgeList.sort(key=lambda x:x[2])
        q = [(lim, u, v, i) for i, (u, v, lim) in enumerate(queries)]
        q.sort()
        e_i = 0
        m = len(queries)
        possible = [False]*m
        for lim, u, v, i in q:
            while e_i < len(edgeList) and edgeList[e_i][2] < lim:
                union(edgeList[e_i][0], edgeList[e_i][1])
                e_i += 1
            possible[i] = (find(u) == find(v))
        return possible
