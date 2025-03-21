# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def recurse(res):
            if len(res) == (2**n) - 1:
                return res
            return recurse(res + "1" + invert(res)[::-1])

        def invert(prev):
            inv = ""
            for i in prev:
                if i == "0":
                    inv += "1"
                else:
                    inv += "0"
            return inv
        ans = recurse("0")
        return ans[k-1]
