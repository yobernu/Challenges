# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(0, 1), (0, -1), (1, 0),( -1, 0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        inbound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[-1])

        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] == "0" or visited[row][col]:
                return 
            
            visited[row][col] = True
            for r, c in dir:
                n_row = row + r
                n_col = col + c
                dfs( n_row, n_col)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    count += 1
        return count