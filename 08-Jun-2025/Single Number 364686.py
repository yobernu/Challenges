# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # counter = Counter(nums)
        # for key, value in counter.items():
        #     if value == 1:
        #         return key
        res = 0
        for num in nums:
            res ^= num
        return res