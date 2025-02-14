# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: i for i, char in enumerate(s)}

        result = []
        left, max_end = 0, 0
        for right, char in enumerate(s):
            max_end = max(max_end, last_occurrence[char]) 

            if right == max_end:
                result.append(right - left + 1)
                left = right + 1 

        return result
