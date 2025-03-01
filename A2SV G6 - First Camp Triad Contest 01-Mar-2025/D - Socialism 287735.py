# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

t = int(input())
for _ in range(t):
    n, min_wealth = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    
    count, tot = 0, 0
    for i in range(n):
        tot += lst[i]
        if tot/(i+1) < min_wealth:
            break
        count = i+1
    print(count)
