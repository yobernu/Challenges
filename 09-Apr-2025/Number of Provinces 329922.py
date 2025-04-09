# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n

        def dfs(city):
            for nbr in range(n):
                if isConnected[city][nbr] == 1 and not visited[nbr]:
                    visited[nbr] = True
                    dfs(nbr)
        
        count = 0
        for city in range(n):
            if not visited[city]:
                visited[city] == True
                dfs(city)
                count += 1
        return count
                