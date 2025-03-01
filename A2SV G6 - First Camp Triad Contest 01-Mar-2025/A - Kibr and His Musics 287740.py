# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

n , k = map(int, input().split())
arr = []
for _ in range(n):
    c , t = map(int , input().split())
    arr.append(c*t)
 
for i in range(1, n):
    arr[i] +=  arr[i-1]
 
 
nums = list(map(int, input().split()))
 
i = 0
for q in nums:
    while i < n and arr[i] < q:
        i += 1
    print(i + 1)