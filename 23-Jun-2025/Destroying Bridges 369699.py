# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k > n-2:
        print(1)
    else:
        print(n)
