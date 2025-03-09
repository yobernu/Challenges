# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
a = list(map(int, input().split()))


res = []
for i in range(1, n):
    res.append(a[i] - a[i-1])

res.sort()
print(sum(res[:n-k]))