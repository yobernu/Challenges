# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(index):
            if index in memo:
                return memo[index]
            if index >= len(cost):
                return 0
            result = cost[index] + min(dp(index + 1), dp(index + 2))
            memo[index] = result
            return result
        return min(dp(0), dp(1))