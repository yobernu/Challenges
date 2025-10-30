# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ans = float("inf")
        temp = 0
        for r in range(len(nums)):
            temp += nums[r]
            while temp >= target:
                temp -= nums[l]
                ans = min(ans, r-l+1)
                l+=1
        return 0 if ans == float("inf") else ans