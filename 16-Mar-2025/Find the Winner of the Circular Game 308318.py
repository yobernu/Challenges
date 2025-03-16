# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def helper(nums, k, index):
            index = (index + k-1)%len(nums)
            if len(nums) == 1:
                return nums[0]
            nums.pop(index)
            return helper(nums, k, index)

        nums = list(range(1, n+1))
        return helper(nums, k, 0)
            
            
