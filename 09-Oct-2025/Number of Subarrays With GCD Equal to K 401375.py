# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        count = 0
        while i < len(nums):
            j = i
            g = 0
            while j < len(nums):
                g = gcd(g, nums[j])
                if g < k:
                    break
                if g == k:
                    count += 1
                j+=1
            i += 1
        return count


            
            

