# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        ans = 0
        total = 0
        for i in range(len(costs)):
            total += costs[i]
            if total <= coins:
                ans += 1
        return ans

