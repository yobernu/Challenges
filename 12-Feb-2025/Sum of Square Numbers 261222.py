# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**0.5)  # Two pointers: start at 0 and sqrt(c)
        while left <= right:
            total = left**2 + right**2
            if total == c:
                return True
            elif total < c:
                left += 1  # Increase the smaller pointer
            else:
                right -= 1  # Decrease the larger pointer
        return False