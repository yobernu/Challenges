# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapq.heapify(nums)
        while len(nums) > 1:
            if nums[0] >= k:
                return ans
            f = heapq.heappop(nums)
            s = heapq.heappop(nums)
            to_add = min(f, s)*2 + max(f, s)
            heapq.heappush(nums, to_add)
            ans += 1
        return ans
