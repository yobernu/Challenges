# Problem: D - Lakes in Bahirdar - https://codeforces.com/gym/602812/problem/D

import sys, threading
input = lambda : sys.stdin.readline().strip()
sys.setrecursionlimit(10**6)

row, col, k = map(int, input().split())
grid = [list(input().strip()) for _ in range(row)]

lakes = []

def dfs(r, c, a):
    if r < 0 or r >= row or c < 0 or c >= col:
        return 0, True  
    if grid[r][c] != '.':
        return 0, False

    grid[r][c] = 'v'  
    a.append((r, c))
    size = 1
    touches_border = (r == 0 or r == row - 1 or c == 0 or c == col - 1)

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        s, touches = dfs(r + dr, c + dc, a)
        size += s
        touches_border |= touches

    return size, touches_border
for i in range(row):
    for j in range(col):
        if grid[i][j] == '.':
            a = []
            size, touches_border = dfs(i, j, a)
            if not touches_border:
                lakes.append(a)
lakes.sort(key=len)
to_fill = lakes[:len(lakes) - k]
filled = sum(len(lake) for lake in to_fill)

for lake in to_fill:
    for r, c in lake:
        grid[r][c] = '*'

for i in range(row):
    for j in range(col):
        if grid[i][j] == 'v':
            grid[i][j] = '.'
print(filled)
for line in grid:
    print("".join(line))

