# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
def solve(arr, n):
    freq1 = Counter(arr)
    opt = list(freq1.values())
    opt.sort()
    res = float('inf')
    for i in range(len(opt)):
        rem = n - (len(opt) - i) * opt[i]
        res = min(res, rem)

    return res

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr, n))