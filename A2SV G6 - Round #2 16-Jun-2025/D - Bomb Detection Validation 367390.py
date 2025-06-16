# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

def solve(lst, n, m):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1),
           (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def in_bounds(row, col):
        return 0 <= row < n and 0 <= col < m

    def helper(row, col):
        count = 0
        for dr, dc in dir:
            new_row, new_col = row + dr, col + dc
            if in_bounds(new_row, new_col) and lst[new_row][new_col] == "*":
                count += 1
        return count

    for i in range(n):
        for j in range(m):
            if lst[i][j] not in ("*", "."):
                if int(lst[i][j]) != helper(i, j):
                    return "NO"
            if lst[i][j] == ".":
                if helper(i, j) != 0:
                    return "NO"
    return "YES"

n, m = map(int, input().split())
lst = [input() for _ in range(n)]
result = solve(lst, n, m)
print(result)
