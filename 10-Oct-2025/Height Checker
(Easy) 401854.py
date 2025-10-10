# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_h = sorted(heights)
        count = 0
        for i, j in zip(heights, sorted_h):
            if i != j:
                count += 1
        return count