# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(subs, left, right):
            while left < right:
                if subs[left] != subs[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:  
                return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
            left += 1
            right -= 1

        return True
