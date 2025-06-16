# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l, r = 0, 0
        n, m = len(version1), len(version2)
        while l < n or r < m:
            v1 = 0
            while l < n and version1[l] != ".":
                v1 = v1*10 + int(version1[l])
                l += 1
            l += 1
                
            v2 = 0
            while r < m and version2[r] != ".":
                v2 = v2*10 + int(version2[r])
                r += 1
            r += 1
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
            