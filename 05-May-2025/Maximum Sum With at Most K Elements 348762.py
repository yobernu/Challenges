# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        pool = []
        for row, limit in zip(grid, limits):
            lar = heapq.nlargest(limit, row)
            pool.extend(lar)
        
        return sum(heapq.nlargest(k, pool))
