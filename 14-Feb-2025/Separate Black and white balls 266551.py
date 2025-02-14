# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        carry_idx = []
        for idx, val in enumerate(s):
            if val == "0":
                carry_idx.append(idx)
        
        ans = 0
        for i in range(len(carry_idx)):
            ans += carry_idx[i] - i
        return ans


