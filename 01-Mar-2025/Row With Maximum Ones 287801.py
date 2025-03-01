# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        for i in range(len(mat)):
            d[i] = sum(mat[i])
        for k, v in d.items():
            if v == max(d.values()):
                return [k, v]

