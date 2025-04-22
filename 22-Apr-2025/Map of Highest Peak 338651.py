# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        q = deque()
        n, m = len(isWater), len(isWater[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        ans = [[-1 for _ in range(m)]for _ in range(n)]
        def inbound(r, c):
            return 0 <= r < len(isWater) and 0 <= c < len(isWater[0])

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    ans[i][j] = 0
                    visited[i][j] = True
                    q.append((i, j))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    nr, nc = dx + r, dy + c
                    if inbound(nr, nc) and not visited[nr][nc]:
                        ans[nr][nc] = ans[r][c] + 1
                        visited[nr][nc] = True
                        q.append((nr, nc))
        return ans
