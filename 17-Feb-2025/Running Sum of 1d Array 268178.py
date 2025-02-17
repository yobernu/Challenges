# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for idx in range(1, len(nums)):
            ans.append(nums[idx] + ans[idx-1])
        return ans