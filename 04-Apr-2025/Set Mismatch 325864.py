# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash = defaultdict(int)
        for i in nums:
            hash[i] += 1
        for i in range(1, len(nums) + 1):
            if hash[i] == 2:
                dup = i
            if hash[i] == 0:
                diff = i
        # print(hash)
        return [dup, diff]