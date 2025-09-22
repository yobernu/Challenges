# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(index):
            if index < 0:
                return 0
            if index in memo:
                return memo[index]
            memo[index] = max(dp(index - 1), dp(index - 2) + nums[index])
            return memo[index]

        return dp(len(nums) - 1)


