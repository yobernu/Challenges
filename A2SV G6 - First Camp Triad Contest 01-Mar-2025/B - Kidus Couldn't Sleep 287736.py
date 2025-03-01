# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

n , k = map(int , input().split())
arr = list(map(int, input().split()))
 

window_sum = sum(arr[:k])
tot = window_sum

for i in range(k, n):
    window_sum += arr[i] - arr[i-k]
    tot += window_sum
print(tot/(n-k+1))