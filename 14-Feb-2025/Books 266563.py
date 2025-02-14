# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
minutes = list(map(int, input().split()))

left, total, ans = 0, 0, 0
for right in range(n):
    total += minutes[right] 
    while total > t:  
        total -= minutes[left]
        left += 1
    ans = max(ans, right - left + 1)

print(ans)
