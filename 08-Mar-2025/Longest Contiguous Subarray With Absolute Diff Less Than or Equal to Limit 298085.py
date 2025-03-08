# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq = deque()  
        min_dq = deque()  

        left = 0
        res = 0

        for right in range(len(nums)):
            while max_dq and nums[max_dq[-1]] < nums[right]:
                max_dq.pop()
            max_dq.append(right)

            while min_dq and nums[min_dq[-1]] > nums[right]:
                min_dq.pop()
            min_dq.append(right)

            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                left += 1  
                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()
            # print(max_dq, min_dq)
            res = max(res, right - left + 1)
        return res
