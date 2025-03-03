# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())
p = [0]*200002
rn = [0]*200002
for _ in range(n):
    l, r = map(int, input().split())
    p[l] += 1
    p[r+1] -= 1
for i in range(1, len(p)):
    p[i] += p[i-1]
    if p[i] >= k:
        rn[i] += rn[i-1] + 1
    else:
        rn[i] += rn[i-1]

for _ in range(q):
    a, b = map(int, input().split())
    print(rn[b] - rn[a-1])
    