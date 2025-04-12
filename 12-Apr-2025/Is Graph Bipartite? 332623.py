# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node):
            for neigh in graph[node]:
                if color[neigh] == -1:
                    color[neigh] = 1 - color[node] 
                    if not dfs(neigh):
                        return False
                elif color[neigh] == color[node]:
                    return False
            return True

        for node in range(n):
            if color[node] == -1:
                color[node] = 0 
                if not dfs(node):
                    return False
        return True
