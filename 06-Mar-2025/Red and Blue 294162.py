# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))

    ans = 0
    for i in range(1, n):
        red[i] += red[i-1]
    for i in range(1, m):
        blue[i] += blue[i-1]
    print(max(0, max(red), max(blue), max(red) + max(blue)))