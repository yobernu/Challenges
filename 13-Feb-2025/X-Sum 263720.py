# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

import sys
from collections import defaultdict
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr1 = []
    for i in range(n):
        mat = list(map(int, input().split()))
        arr1.append(mat)
    

    dict1 = {} 
    dict2 = {}  
    
    for i in range(n):
        for j in range(m):
            key1, key2 = i - j, i + j
            dict1[key1] = dict1.get(key1, 0) + arr1[i][j]
            dict2[key2] = dict2.get(key2, 0) + arr1[i][j]
    
    max_sum = 0
    for i in range(n):
        for j in range(m):
            key1, key2 = i - j, i + j
            total_sum = dict1[key1] + dict2[key2] - arr1[i][j] 
            max_sum = max(max_sum, total_sum)
    
    print(max_sum)
