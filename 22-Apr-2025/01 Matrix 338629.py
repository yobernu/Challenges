# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = [[False for j in range(len(mat[0]))] for i in range(len(mat))]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        ans = [[-1 for _ in range(len(mat[0]))]for _ in range(len(mat))]
        def inbound(r, c):
            return 0 <= r < len(mat) and 0 <= c < len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i, j))
                    visited[i][j] = True
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    nr, nc = dx + r, dy + c
                    if inbound(nr, nc) and not visited[nr][nc]:
                        ans[nr][nc] = ans[r][c] + 1
                        q.append((nr, nc))
                        visited[nr][nc] = True
                # ans[r][c] += 1
        return ans
