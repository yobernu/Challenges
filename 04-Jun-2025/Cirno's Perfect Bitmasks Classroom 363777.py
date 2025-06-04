# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

def solve():
    x = int(input())
    y = x & -x

    if x ^ y > 0:
        print(y)
    else:
        print(y + (~x & (x + 1)))  
                                          
t = int(input())  
for _ in range(t):
    solve()