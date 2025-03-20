# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.child = [0]*k
        self.mn = float('inf')
        def backtrack(i, child):
            if i == len(cookies):
                self.mn = min(self.mn, max(self.child))
                return 
            for j in range(k):
                self.child[j] += cookies[i]
                backtrack(i+1, self.child)
                # print(self.child)
                self.child[j] -= cookies[i]

                if child[j] == 0:
                    break
        backtrack(0, self.child)
        return self.mn
            