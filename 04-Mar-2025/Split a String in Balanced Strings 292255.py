# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        count = 0
        left, right  = 0,0
        # while left < n:
        #     temp_l, temp_r = 0, 0
        #     right = left
        #     while right < n:
        #         if s[right] == "L":
        #             temp_l += 1
        #         elif s[right] == "R":
        #             temp_r += 1
        #         if temp_l == temp_r:
        #             count += 1
        #             break
        #         right += 1
        #     left = right+1
        b = 0
        for i in range(n):
            if s[i] == "R":
                b += 1
            elif s[i] == "L":
                b -= 1
            if b == 0:
                count += 1
        return count





