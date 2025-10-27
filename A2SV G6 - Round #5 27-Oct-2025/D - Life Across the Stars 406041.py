# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict

n = int(input())
p_dic = defaultdict(int)
lst = []
for _ in range(n):
    b, d = map(int, input().split())
    lst.append((b, d))
    p_dic[b] += 1
    p_dic[d] -= 1

p_sum = []
current_sum = 0
for key in sorted(p_dic.keys()):
    current_sum += p_dic[key]
    p_sum.append((key, current_sum))

mx = max(p_sum, key=lambda x: x[1])[1]
maximim = next(key for key, value in p_sum if value == mx)

count = sum(1 for b, d in lst if b <= maximim < d)
print(maximim, count)