# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for _ in range(n):
    a = list(map(int, input().split()))
    dic[a[0]] += 1
    dic[a[1] + 1] -= 1

sorted_keys = sorted(dic.keys())
count = 0
active_intervals = defaultdict(int)

for i in range(len(sorted_keys) - 1): 
    count += dic[sorted_keys[i]]
    active_intervals[count] += sorted_keys[i + 1] - sorted_keys[i]

result = [0] * n
for k, v in active_intervals.items():
    if k > 0: 
        result[k - 1] = v

print(*result)
