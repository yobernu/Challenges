# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
max_length = 0
result = [1, 1]
freq = defaultdict(int)
unique_count = 0

for right in range(n):
    if freq[arr[right]] == 0:
        unique_count += 1
    freq[arr[right]] += 1

    while unique_count > k:
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            unique_count -= 1
        left += 1 

    if (right - left + 1) > max_length:
        max_length = right - left + 1
        result = [left + 1, right + 1]  

print(*result)

