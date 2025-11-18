# Problem: B - The Lord of Medianfell - https://codeforces.com/gym/599383/problem/B

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    k = (n+2)//2
    
    print(s//k)