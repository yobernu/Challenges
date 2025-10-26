# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    arr = []
    if a > max(b, c):
        arr.append(0)
    else:
        arr.append(max(b, c) - a+1)
    if b > max(a, c):
        arr.append(0)
    else:
        arr.append(max(a, c) - b+1)
    if c > max(a, b):
        arr.append(0)
    else:
        arr.append(max(a, b) - c+1)
    print(*arr)

