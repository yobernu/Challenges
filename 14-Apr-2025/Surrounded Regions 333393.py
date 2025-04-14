# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        r, c = len(board) , len(board[0])
        visited = [[False for _ in range(c)] for _ in range(r)]
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        hold = []
        def inbound(row, col):
            return 0 <= row < r and 0 <= col < c
        def dfs(row, col):
            visited[row][col] = True
            board[row][col] = "#"
            for dx, dy in dir:
                n_r = row + dx
                n_c = col + dy
                if inbound(n_r, n_c) and not visited[n_r][n_c] and board[n_r][n_c] == "O":
                    dfs(n_r, n_c)
        for i in range(r):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][c-1] == "O":
                dfs(i, c-1)
        for j in range(c):
            if board[0][j] == "O":
                dfs(0, j)
            if board[r-1][j] == "O":
                dfs(r-1, j)        

        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        