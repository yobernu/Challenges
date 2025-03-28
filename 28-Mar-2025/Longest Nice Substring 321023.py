# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        _set = set(s)
        if len(_set) <= 1:
            return ""
        
        for i in range(len(s)):
            ch = s[i]
            if ch.swapcase() not in _set:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                if len(left) < len(right):
                    return right
                else:
                    return left
        return s