# Problem: House Robber IV - https://leetcode.com/problems/house-robber-iv/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        low, high = min(nums), max(nums)

        def is_possible(mid):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i+=1
            return count >= k

        while low < high:
            mid = (low + high)//2
            if is_possible(mid):
                high = mid
            else:
                low = mid + 1
        return high
