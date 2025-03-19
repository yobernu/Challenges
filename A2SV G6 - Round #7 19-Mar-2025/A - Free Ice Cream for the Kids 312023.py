# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

n,x = map(int, input().split())
dc = 0
tot = x
for _ in range(n):
    a,b = map(str, input().split())
    if a == "+":
        tot += int(b)
    else:
        if tot < int(b):
            dc += 1
        else:
            tot -= int(b)
print(tot, dc)