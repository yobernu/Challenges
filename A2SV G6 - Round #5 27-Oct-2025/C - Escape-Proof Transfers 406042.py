# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

n, t, c = map(int, input().split())
a = list(map(int, input().split()))

count = 0
l = 0
for num in a:
    if num <= t:
        l += 1
    else:
        l = 0
    
    if l >= c:
        count += 1

print(count)
