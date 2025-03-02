# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        seen = {0:1}
        s = 0

        for y in nums:
            s += y
            if s-goal in seen:
                res += seen[s-goal]
            seen[s] = seen.get(s, 0)+1
        return res
            

    

        



