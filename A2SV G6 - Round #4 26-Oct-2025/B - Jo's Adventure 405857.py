# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
heights = list(map(int, input().split()))
f = [0] * n
b = [0] * n
for i in range(1, n):
    if heights[i] < heights[i - 1]:
        f[i] = f[i - 1] + (heights[i - 1] - heights[i])
    else:
        f[i] = f[i - 1]
for i in range(n - 2, -1, -1):
    if heights[i] < heights[i + 1]:
        b[i] = b[i + 1] + (heights[i + 1] - heights[i])
    else:
        b[i] = b[i + 1]
for _ in range(m):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    if s < t:
        print(f[t] - f[s])
    else:
        print(b[t] - b[s])
