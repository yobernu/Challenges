# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        q = deque()
        time, fresh = 0 , 0
        n, m = len(grid), len(grid[0])

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    nr , nc = dx + r, dy + c
                    if not inbound(nr, nc) or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append([nr, nc])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1


