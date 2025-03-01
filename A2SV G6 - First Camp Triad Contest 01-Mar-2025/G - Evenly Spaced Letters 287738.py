# Problem: G - Evenly Spaced Letters - https://codeforces.com/gym/589822/problem/G

n = int(input())
for _ in range(n):
    s = input()
    print("".join(sorted(s)))