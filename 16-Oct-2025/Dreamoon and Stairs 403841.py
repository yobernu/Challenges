# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

n, m = map(int, input().split())

min_moves = (n + 1) // 2
answer = -1

if n < m:
    print(answer)
else:
    for i in range(min_moves, n + 1):  # include n
        if i % m == 0:
            answer = i
            break
    print(answer)
