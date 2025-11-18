# Problem: B - The Lord of Medianfell - https://codeforces.com/gym/599383/problem/B

t = int(input()) 
for _ in range(t): 
   n, s = [int(i) for i in input().split()]
   m = n // 2 + 1 
   print(s // m) 