# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C

import math

n = int(input())
array = list(map(int, input().split()))

g = 0
for num in array:
    g = math.gcd(g, num)

def strip_2_3(x):
    while x % 2 == 0:
        x //= 2
    while x % 3 == 0:
        x //= 3
    return x

for num in array:
    reduced = num // g
    if strip_2_3(reduced) != 1:
        print("No")
        break
else:
    print("Yes")