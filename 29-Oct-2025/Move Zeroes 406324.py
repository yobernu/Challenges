# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        while l < len(nums):
            if nums[l] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                r+=1
            l+=1