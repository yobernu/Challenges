# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hold = []
        counter = Counter(nums)
        for key, value in counter.items():
            if value == 2:
                hold.append(key)
        return hold