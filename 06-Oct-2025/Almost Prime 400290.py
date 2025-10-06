# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

from collections import Counter;
def almostprime(n):
    factors = []
    d = 2
    while d*d <= n:
        while n%d == 0:
            factors.append(d)
            n//=d
        d += 1
    if n > 1: factors.append(n)
    
    counter = Counter(factors)
    return len(counter) == 2

num = int(input())
ans = 0
for i in range(1, num+1):
    if almostprime(i):
        ans += 1
print(ans)
    