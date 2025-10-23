# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        s = "\n".join(source)
        res = ""
        i = 0
        while i < len(s):
            two = s[i:i+2]
            if two == "//":
                i += 2
                while i < len(s) and s[i] != "\n":
                    i += 1
            elif two == "/*":
                i += 2
                while s[i:i+2] != "*/":
                    i +=1
                i += 2
            else:
                res += s[i]
                i += 1
        a = []
        for x in res.split("\n"):
            if x != "":
                a.append(x)
        return a