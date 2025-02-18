# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        
        prefix_prod = 1
        for i in range(len(nums)):
            ans[i] = prefix_prod
            prefix_prod *= nums[i]
        
        suffix_prod = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffix_prod
            suffix_prod *= nums[i]
        
        return ans