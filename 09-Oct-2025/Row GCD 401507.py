# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

from math import gcd

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

g = 0
for i in range(1, n):
    g = gcd(g, abs(a[0] - a[i]))

ans = [gcd(a[0] + bj, g) for bj in b]
print(' '.join(map(str, ans)))
