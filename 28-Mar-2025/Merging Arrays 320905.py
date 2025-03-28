# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


ans = []
left1, left2 = 0,0
while left1 < len(arr1) and left2  < len(arr2):
    if arr1[left1] < arr2[left2]:
        ans.append(arr1[left1])
        left1 += 1
    else:
        ans.append(arr2[left2])
        left2 += 1

ans.extend(arr1[left1:]) 
ans.extend(arr2[left2:])
print(*ans)