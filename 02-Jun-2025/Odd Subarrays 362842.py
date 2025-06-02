# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    dq = deque()
    count = 0
    for i in range(n):
        if dq and dq[-1] > a[i]:
            dq = deque()
            count += 1
        else:
            if dq:
                dq.popleft()
            dq.append(a[i])
    print(count)