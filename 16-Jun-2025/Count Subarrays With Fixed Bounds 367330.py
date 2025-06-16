# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        last_minK = last_maxK = last_invalid = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last_invalid = i
            if num == minK:
                last_minK = i
            if num == maxK:
                last_maxK = i
            
            if last_minK != -1 and last_maxK != -1:
                count += max(0, min(last_minK, last_maxK) - last_invalid)

        return count
