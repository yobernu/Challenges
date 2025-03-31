# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix.sort()
        last = defaultdict(int)
        i = 0
        for mat in matrix:
            last[i] = mat[-1]
            i+=1
        j = -1
        for i in last.values():
            j += 1
            if target <= i:
                opt = i
                break
        # print(last.values())
        # print(i, j, opt, matrix[j])
        if target in matrix[j]:
            return True
        return False