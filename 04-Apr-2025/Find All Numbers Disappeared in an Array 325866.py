# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        hash = defaultdict(int)
        for i in nums:
            hash[i] += 1
        for i in range(1, len(nums) + 1):
            if hash[i] == 0:
                ans.append(i)
        return ans