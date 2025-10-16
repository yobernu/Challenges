# Problem: The Meeting Place Cannot Be Changed - https://codeforces.com/problemset/problem/780/B

n = int(input())
coordinates = list(map(int, input().split()))
speed = list(map(int, input().split()))

low, high = 0, max(coordinates) - min(coordinates)
precision = 1e-6 

def is_valid(mid):
    min_right = float("inf")
    max_left = float("-inf")
    
    for c, s in zip(coordinates, speed):
        d = s * mid
        left = c - d
        right = c + d
        max_left = max(max_left, left)
        min_right = min(min_right, right)
    return max_left <= min_right 

while high - low > precision:  
    mid = (low + high) / 2
    if is_valid(mid):
        high = mid
    else:
        low = mid

print((low + high) / 2) 
