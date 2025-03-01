# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

t = int(input())
lst = []
for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    # print(arr)
    for _ in range(q):
        l = list(map(int, input().split()))
        left = l[0]
        right = l[1]
        left -= 1
        right -= 1
        
        tot = arr[-1]
        if left == 0:
            new_tot = tot - (arr[right]) + (right - left+1)*l[2]
        else:
            new_tot = tot - (arr[right] - arr[left - 1]) + (right - left+1)*l[2]
        # print(arr, tot,  new_tot)
        if new_tot%2 != 0:
            print("YES")
        else:
            print("NO")
        
    # print("------second case--------")



