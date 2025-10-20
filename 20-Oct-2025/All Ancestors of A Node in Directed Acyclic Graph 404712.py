# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[v].append(u)
        
        memo = {}
        def dfs(node):
            if node in memo:
                return memo[node]
            ancestors = set()
            for neigh in graph[node]:
                ancestors.add(neigh)
                ancestors.update(dfs(neigh))
            memo[node] = ancestors
            return ancestors
        
        answer = []
        for i in range(n):
            ancestors = sorted(dfs(i))
            answer.append(ancestors)
        return answer
                
