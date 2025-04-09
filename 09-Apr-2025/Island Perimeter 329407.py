# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        # ans = 0
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        p = 0
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == 1:
        #             for r, c in dir:
        #                 n_row = row + r
        #                 n_col = col + c
        #                 if not (inbound(n_row, n_col) and grid[n_row][n_col] != 0):
        #                     p += 1
        # return p



        
        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] == 0:
                return 1
            elif visited[row][col]:
                return 0
            ans = 0
            visited[row][col] = True
            for r, c in dir:
                n_row = row + r
                n_col = col + c
                ans += dfs( n_row, n_col)
            return ans
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0
