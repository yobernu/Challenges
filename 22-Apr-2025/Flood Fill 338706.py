# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n,m = len(image), len(image[0])
        ans = [row[:] for row in image]
        visited = [[False for _ in range(m)] for _ in range(n)]
        q = deque([(sr, sc)])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        _match = image[sr][sc]
        ans[sr][sc] = color
        visited[sr][sc] = True
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    nr, nc = dx + r, dy + c
                    if inbound(nr, nc) and not visited[nr][nc] and image[nr][nc] == _match:
                        ans[nr][nc] = color
                        visited[nr][nc] = True
                        q.append((nr, nc))
        return ans
                
