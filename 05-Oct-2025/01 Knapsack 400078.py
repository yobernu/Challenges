# Problem: 01 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt):
        # N = len(val)
        # memo = {}
        # for w in range(W+1):
        #     memo[(0 , w)] = 0
        # for i in range(1, N+1):
        #     for c in range(W+1):
        #         if wt[i-1] <= c:
        #             memo[(i, c)] = max(memo[(i-1, c)], val[i-1] + memo[(i-1, c-wt[i-1])])
        #         else:
        #             memo[(i, c)] = memo[(i-1, c)]
        # return memo[(N, W)]
        
        
        
        
        
        # solution-2 with iterative method for dp
        
        # dp = [0]*(W+1)
        # for i in range(len(val)):
        #     for c in range(W, wt[i]-1, -1):
        #         dp[c] = max(dp[c], val[i] + dp[c-wt[i]])
        # return dp[W]
        
        # solution -3 with recursive
        
        memo = {}
        def dfs(i, capacity):
            if i < 0 or capacity <=0:
                return 0
            state = (i, capacity)
            if state in memo:
                return memo[state]
            if wt[i] > capacity:
                result = dfs(i-1, capacity)
            else:
                take = val[i] + dfs(i-1, capacity-wt[i])
                skip = dfs(i-1, capacity)
                result = max(take, skip)
            memo[(i, capacity)] = result
            return result
        n = len(val)
        return dfs(n-1, W)
        
        
        
        
        
        
        
        
        
        
        
        