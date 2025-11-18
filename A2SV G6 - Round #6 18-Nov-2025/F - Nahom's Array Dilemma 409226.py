# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

import sys

def solve():
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))

    def prevGreater(nums):
        stack = []
        pref = [0]
        
        for num in nums:
            pref.append(pref[-1] + num)
    
        for i in range(n):

            while stack and nums[stack[-1]] <= nums[i]:
                v = stack.pop()

                if  pref[i] - pref[v]> 0:
                    return False
                
            stack.append(i)

        return True
    
    if prevGreater(nums) and prevGreater(nums[::-1]):
        return "YES"
    
    return "NO"

t = int(sys.stdin.readline().strip())
for _ in range(t):
    print(solve())