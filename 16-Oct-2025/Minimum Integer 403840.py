# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

n = int(input())
for _ in range(n):
    l, r, d = map(int, input().split())
    if l <= d <= r:
        x = ((r // d) + 1) * d
        print(x)
    else:
        print(d)