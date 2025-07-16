# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        parent = [i * n + j for i in range(m) for j in range(n)]
        rank = [1] * (m * n)
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        def union(u, v):
            u_root = find(u)
            v_root = find(v)
            if u_root == v_root:
                return
            if rank[u_root] > rank[v_root]:
                parent[v_root] = u_root
                rank[u_root] += rank[v_root]
            else:
                parent[u_root] = v_root
                rank[v_root] += rank[u_root]
        
        street_directions = {
            1: [(0, -1), (0, 1)],  # left, right
            2: [(-1, 0), (1, 0)],   # up, down
            3: [(0, -1), (1, 0)],    # left, down
            4: [(0, 1), (1, 0)],     # right, down
            5: [(-1, 0), (0, -1)],   # up, left
            6: [(-1, 0), (0, 1)]     # up, right
        }
        for i in range(m):
            for j in range(n):
                current = grid[i][j]
                for di, dj in street_directions[current]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        neighbor = grid[ni][nj]
                        valid = False
                        for ndi, ndj in street_directions[neighbor]:
                            if ni + ndi == i and nj + ndj == j:
                                valid = True
                                break
                        if valid:
                            u = i * n + j
                            v = ni * n + nj
                            union(u, v)
        start = 0
        end = (m - 1) * n + (n - 1)
        return find(start) == find(end)