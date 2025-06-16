# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # count_min, count_max = 0, 0
        # ans = 0
        # l, r = 0, 0
        # for i in range(len(nums)):
        #     if nums[i] == minK:
        #         count_min += 1
        #     elif nums[i] == maxK:
        #         count_max += 1
        #     if nums[i] < minK or nums[i] > maxK:
        #         while nums[l] != minK and nums[l] != maxK:
        #             ans += 1
        #             l += 1
        #         while nums[l] == minK or

            

        
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
