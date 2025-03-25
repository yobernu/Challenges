# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        left = 0
        right = len(nums)
        mid = (left + right)//2
        
        while left <= right:
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                break
            mid = (left + right)//2
        return mid