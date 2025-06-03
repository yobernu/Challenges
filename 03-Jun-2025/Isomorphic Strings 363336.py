# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = {}
        t_to_s = {}
        for a, b in zip(s, t):
            if a in s_to_t:
                if s_to_t[a] != b:
                    return False
            else:
                if b in t_to_s:
                    return False
                s_to_t[a] = b
                t_to_s[b] = a
        
        return True
