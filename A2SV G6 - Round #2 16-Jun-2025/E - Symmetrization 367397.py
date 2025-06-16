# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    total_flips = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                x1, y1 = i, j
                x2, y2 = j, n - 1 - i
                x3, y3 = n - 1 - i, n - 1 - j
                x4, y4 = n - 1 - j, i
                
                positions = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
                unique_positions = []
                seen_pos = set()
                for pos in positions:
                    if pos not in seen_pos:
                        seen_pos.add(pos)
                        unique_positions.append(pos)
                ones = 0
                zeros = 0
                for x, y in unique_positions:
                    visited[x][y] = True
                    if grid[x][y] == '1':
                        ones += 1
                    else:
                        zeros += 1
                total_flips += min(ones, zeros)
    
    print(total_flips)