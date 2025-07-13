# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

import sys
import math

def solve():
    input = sys.stdin.read().split()
    i = 0
    t = int(input[i])
    i += 1
    for _ in range(t):
        n = int(input[i])
        i += 1
        a = list(map(int, input[i:i + n]))
        i += n
        
        bit_counts = [0] * 30
        for num in a:
            for bit in range(30):
                if num & (1 << bit):
                    bit_counts[bit] += 1
        
        overall_gcd = 0
        for cnt in bit_counts:
            if cnt > 0:
                if overall_gcd == 0:
                    overall_gcd = cnt
                else:
                    overall_gcd = math.gcd(overall_gcd, cnt)
        
        if overall_gcd == 0:
            valid_ks = list(range(1, n + 1))
        else:
            valid_ks = []
            for k in range(1, overall_gcd + 1):
                if k > n:
                    break
                if overall_gcd % k == 0:
                    valid_ks.append(k)
        print(' '.join(map(str, valid_ks)))

solve()