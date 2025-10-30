# Problem: Number of Submatrices That Sum to Target - https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        rows, cols = len(matrix), len(matrix[0])
        count = 0

        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                for c in range(cols):
                    col_sums[c] += matrix[bottom][c]

                prefix_sum = defaultdict(int)
                prefix_sum[0] = 1
                curr_sum = 0

                for val in col_sums:
                    curr_sum += val
                    count += prefix_sum[curr_sum - target]
                    prefix_sum[curr_sum] += 1

        return count