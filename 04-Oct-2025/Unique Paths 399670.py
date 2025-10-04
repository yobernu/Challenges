# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}
        # def dp(i, j):
        #     state = (i, j)
        #     if state in memo:
        #         return memo[state]
        #     if state == (m-1, n-1): return 1
        #     if i >= m or j >= n: return 0
            
        #     result = dp(i+1, j) + dp(i, j+1)
        #     memo[state] = result
        #     return result
        # return dp(0, 0)

        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]