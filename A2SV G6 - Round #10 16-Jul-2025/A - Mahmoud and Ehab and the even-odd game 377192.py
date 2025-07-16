# Problem: A - Mahmoud and Ehab and the even-odd game - https://codeforces.com/gym/602812/problem/A

n = int(input())
if n == 1:
    print("Ehab")
else:
    if n % 2 == 0:
        print("Mahmoud")
    else:
        print("Ehab")