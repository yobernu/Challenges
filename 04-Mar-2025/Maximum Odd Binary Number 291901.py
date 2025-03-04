# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s1 = ""
        s0 = ""
        for i in s:
            if i == "1":
                s1 += i
            else:
                s0 += i
        for i in s1:
            s0 += i
            break
        s1 = s1[:-1]
        return s1+s0
