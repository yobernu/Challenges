# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B



import sys
from collections import defaultdict


def solve():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())

    arr1 = list(map(int, data[1].split()))
    arr2 = list(map(int, data[2].split()))
    
    ans = []
    j = 0
    count = 0
    for num in arr2:
        while j < n and num > arr1[j]:
            count += 1
            j += 1
        ans.append(count)
    print(*ans)
solve()
        
