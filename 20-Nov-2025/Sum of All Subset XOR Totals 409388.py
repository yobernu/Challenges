# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(1 << n):
            t = 0
            for j in range(n):
                if i & (1 << j):
                    t ^= nums[j]
            res += t
        return res