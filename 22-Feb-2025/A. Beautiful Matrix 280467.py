# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix = []
row = 0
for i in range(1, 6):
    arr = list(map(int, input().split()))
    if sum(arr) == 1:
        row = i
    matrix.append(arr)
col = 0
for i in range(1, 6):
    if matrix[row-1][i-1] == 1:
        col = i
ans = abs(row - 3) + abs(col-3)
print(ans)