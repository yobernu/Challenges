# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
points = list(map(int, input().split()))
points.sort() 

if n % 2 == 0:
    median = points[n // 2 - 1]
else:
    median = points[n // 2] 
print(median)
