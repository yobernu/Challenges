# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import deque

def solve():
    n, m = map(int, input().split())
    rail = [[False] * n for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        rail[u][v] = True
        rail[v][u] = True
    has_direct_rail = rail[0][n-1]
    
    # BFS for shortest path
    def bfs(use_rail):
        dist = [-1] * n
        dist[0] = 0
        queue = deque([0])
        while queue:
            u = queue.popleft()
            for v in range(n):
                if u != v:
                    if use_rail:
                        if rail[u][v] and dist[v] == -1:
                            dist[v] = dist[u] + 1
                            queue.append(v)
                    else:
                        if not rail[u][v] and dist[v] == -1:
                            dist[v] = dist[u] + 1
                            queue.append(v)
        return dist[n-1]
    train_time = bfs(True)
    bus_time = bfs(False)
    if train_time == -1 or bus_time == -1:
        print(-1)
    else:
        print(max(train_time, bus_time))
if __name__ == "__main__":
    solve()