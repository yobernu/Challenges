# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter

t = int(input())
for _ in range(t):
    s, t_str, p = input(), input(), input()
    idx = 0
    cou = Counter(p)
    flag = False

    for ch in t_str:
        if idx < len(s) and ch == s[idx]:
            idx += 1
        elif cou[ch] > 0:
            cou[ch] -= 1
        else:
            flag = True
            break

    if flag or idx < len(s):
        print("NO")
    else:
        print("YES")
