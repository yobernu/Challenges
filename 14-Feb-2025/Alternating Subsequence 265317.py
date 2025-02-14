# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    right, left = 0, 0  
    ans_carry = []
    
    # for left in range(len(arr)):
    while left < len(arr):
        temp = [arr[left]]  
        right = left + 1  
        
        while right < len(arr):
            # Negative alternates
            if temp[-1] < 0 and arr[right] < 0:
                temp.append(arr[right])
            # Positive alternates
            elif temp[-1] > 0 and arr[right] > 0:
                temp.append(arr[right])
            else:
                break  
            
            right +=1
        left = right
        ans_carry.append(max(temp))  
    print(sum(ans_carry))  
