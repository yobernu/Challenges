# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n = int(input())
word = input()
count = 1
ans = ""
l = 0
while l < n:
    ans += word[l]
    l += count
    count += 1
    
print(ans)