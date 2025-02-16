# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums  
        mid = len(nums) // 2 
        left_half = self.sortArray(nums[:mid])  
        right_half = self.sortArray(nums[mid:])  
        return self.merge(left_half, right_half)  

    def merge(self, left, right):
        sorted_nums = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_nums.append(left[i])
                i += 1
            else:
                sorted_nums.append(right[j])
                j += 1
        sorted_nums.extend(left[i:])
        sorted_nums.extend(right[j:])

        return sorted_nums

