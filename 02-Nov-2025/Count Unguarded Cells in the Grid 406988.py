# Problem: Count Unguarded Cells in the Grid - https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

from collections import deque

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in walls:
            grid[i][j] = 1
            
        for i, j in guards:
            grid[i][j] = 2
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for guard in guards:
            x, y = guard
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                while 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 1 or grid[nx][ny] == 2:
                        break
                    grid[nx][ny] = 3
                    
                    nx += dx
                    ny += dy
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                    
        return count