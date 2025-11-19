# Problem: Number of Parallelograms - https://codeforces.com/contest/660/problem/D

import math
import heapq
import sys, threading
from bisect import bisect_left, bisect_right
from collections import defaultdict, Counter, deque

input = lambda: sys.stdin.readline().rstrip()
def si():
    return input()
def ii():
    return int(input())
def lsi():
    return input().split()
def mi():
    return map(int, input().split())
def li():
    return list(map(int, input().split()))
yn = lambda condition: 'YES' if condition else 'NO'

# ========================================
# =========================================
def solve():
    n =  ii()
    xs = []
    ys = []
    for _ in range(n):
        x , y = li()
        xs.append(x)
        ys.append(y)
    
    x_count = Counter(xs)
    y_count = Counter(ys)
  
    for val in x_count.values():
        if val > 2:
            print(0)
            return
    for val in y_count.values():
        if val > 2:
            print(0)
            return
        
    dictt = defaultdict(int)

    for i in range(n):
        x1 , y1 = xs[i] , ys[i]
        for j in range(i+1 , n):
            x2 , y2 = xs[j] , ys[j]
            x3 = x1+x2
            y3 = y1+y2
            dictt[(x3<<32) + y3] += 1
    
    ans = 0
    for key , val in dictt.items():
        ans += math.comb(val, 2)

    print(ans)
    
    
    
    return

# =========================================
def main():
    t = 1
    for _ in range(t):
        solve()
main()

# if __name__ == '__main__':
#     sys.setrecursionlimit(1 << 25)
#     threading.stack_size(1 << 27)
#     thread = threading.Thread(target=main)
#     thread.start()
#     thread.join()





