# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        def reverse_sort(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums
        reverse_sort(nums, 0, len(nums)-1)
        reverse_sort(nums, 0, k-1)
        reverse_sort(nums, k, len(nums)-1)

        
