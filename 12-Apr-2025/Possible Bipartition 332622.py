# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1 for i in range(n)]
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
    
        def dfs(node):
            for neigh in graph[node]:
                if color[neigh] == -1:
                    color[neigh] = 1 - color[node]
                    if not dfs(neigh):
                        return False
                if color[neigh] == color[node]:
                    return False
            return True 
        
        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                if not dfs(node):
                    return False
        return True
