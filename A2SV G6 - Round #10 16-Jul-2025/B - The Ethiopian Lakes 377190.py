# Problem: B - The Ethiopian Lakes - https://codeforces.com/gym/602812/problem/B


import sys
import threading

def main():
    input = lambda: sys.stdin.readline().strip()
    sys.setrecursionlimit(1 << 25) 

    t = int(input())
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for _ in range(t):
        n, m = map(int, input().split())
        graph = [list(map(int, input().split())) for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        def dfs(r, c):
            stack = [(r, c)]
            total = 0
            while stack:
                x, y = stack.pop()
                if not (0 <= x < n and 0 <= y < m):
                    continue
                if visited[x][y] or graph[x][y] == 0:
                    continue
                visited[x][y] = True
                total += graph[x][y]
                for dr, dc in dir:
                    stack.append((x + dr, y + dc))
            return total

        ans = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] > 0 and not visited[i][j]:
                    ans = max(ans, dfs(i, j))
        print(ans)


threading.Thread(target=main).start()
