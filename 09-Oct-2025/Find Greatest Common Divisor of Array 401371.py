# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        s = nums[0]
        l = nums[-1]
        return gcd(s, l)