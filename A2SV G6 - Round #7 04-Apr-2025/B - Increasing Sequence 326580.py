# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    last_elem = 0
    for num in a:
        last_elem += 1
        if last_elem == num:
            last_elem += 1
    print(last_elem)