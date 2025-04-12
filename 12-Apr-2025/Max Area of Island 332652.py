# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid[0])  
        m = len(grid)     
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        color = [["WHITE" for _ in range(n)] for _ in range(m)]
        
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] == 0 or color[row][col] != "WHITE":
                return 0

            color[row][col] = "YELLOW"
            area = 1
            for i, j in dir:
                n_row = row + i
                n_col = col + j
                area += dfs(n_row, n_col)
                
            return area
                
        count = 0
        for row in range(m):
            for col in range(n):
                if color[row][col] == "WHITE" and grid[row][col] == 1:
                    count = max(count, dfs(row, col))
        return count


