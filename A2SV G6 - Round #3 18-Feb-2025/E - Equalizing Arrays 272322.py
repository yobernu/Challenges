# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))


if n == 0 or m == 0:
    print(-1)
elif sum(arr1) != sum(arr2):
    print(-1)
    exit()

for i in range(1, len(arr1)):
    arr1[i] += arr1[i-1]
for i in range(1, len(arr2)):
    arr2[i] += arr2[i-1]

right, left, count = 0, 0, 0
while left < n and right < m:
    if arr1[left] < arr2[right]:
        left += 1
    elif arr1[left] > arr2[right]:
        right += 1
    else:
        right += 1
        left += 1
        count += 1
        
if count:
    print(count)
else:
    print(-1)