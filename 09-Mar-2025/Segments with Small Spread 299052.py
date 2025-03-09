# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
n,k = map(int, input().split())
a = list(map(int, input().split()))

max_dq = deque()  
min_dq = deque()  

left = 0
res = 0

for right in range(len(a)):
    while max_dq and a[max_dq[-1]] < a[right]:
        max_dq.pop()
    max_dq.append(right)

    while min_dq and a[min_dq[-1]] > a[right]:
        min_dq.pop()
    min_dq.append(right)

    while a[max_dq[0]] - a[min_dq[0]] > k:
        left += 1  
        if max_dq[0] < left:
            max_dq.popleft()
        if min_dq[0] < left:
            min_dq.popleft()
    # print(max_dq, min_dq)
    res += right - left + 1
print(res)