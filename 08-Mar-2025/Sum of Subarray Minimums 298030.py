# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [-math.inf] + arr + [-math.inf]
        stack = []
        res = 0
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                mid = stack.pop()
                left = stack[-1]
                right = i
                res += arr[mid]*(mid-left)*(right-mid)
            stack.append(i)
        return res%(10**9 + 7)

                    

            