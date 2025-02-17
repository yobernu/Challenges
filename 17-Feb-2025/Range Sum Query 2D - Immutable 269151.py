# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]: 
            return
        
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * self.cols for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                up = self.prefix_sum[row-1][col] if row > 0 else 0
                left = self.prefix_sum[row][col-1] if col > 0 else 0
                diag = self.prefix_sum[row-1][col-1] if row > 0 and col > 0 else 0
                
                self.prefix_sum[row][col] = matrix[row][col] + up + left - diag

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_sum[row2][col2]
        up = self.prefix_sum[row1-1][col2] if row1 > 0 else 0
        left = self.prefix_sum[row2][col1-1] if col1 > 0 else 0
        diag = self.prefix_sum[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return total - up - left + diag



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)