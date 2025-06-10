# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for num in range(len(nums) + 1):
        #     if num not in nums:
        #         return num

        # tot = 0
        # for i in range(len(nums) + 1):
        #     tot += i

        # return tot - sum(nums)

        
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
