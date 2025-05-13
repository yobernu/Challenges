# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        def find(i):
            count = 0
            while i:
                curr = i//2
                carry = i - 2*curr
                if carry == 1:
                    count += 1
                i = curr
            return count

        ans = []
        for i in range(n+1):
            ans.append(find(i))
        return ans
        
        