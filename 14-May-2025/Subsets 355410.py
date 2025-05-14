# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        for mask in range(1 << len(nums)):
            subset = []
            for i in range(len(nums)):
                if mask & (1 << i):
                    subset.append(nums[i])
            power_set.append(subset)
        return power_set
            



        # def backtrack(i, path, length):
        #     if len(path) == length:
        #         res.append(path[:])
        #         return
            
        #     for j in range(i, n):
        #         path.append(nums[j])
        #         backtrack(j+1, path, length)
        #         path.pop()
        
        # n = len(nums)
        # res = []
        # for l in range(n+1):
        #     backtrack(0, [], l)
        # return res