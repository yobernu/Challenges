# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return n > 0 and (1 << 31)%n == 0

        return n > 0 and  (n & (n-1) == 0)