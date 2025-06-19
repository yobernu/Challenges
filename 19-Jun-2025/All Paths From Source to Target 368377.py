# Problem: All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = defaultdict(list)
        for i, edge in enumerate(graph):
            self.graph[i] = (edge)
        res = []
        
        def dfs(path, node):
            if node == len(self.graph) - 1:
                res.append(list(path))
            for conn in self.graph[node]:
                path.append(conn)
                dfs(path, conn)
                path.pop()
                    
        dfs([0], 0)
        return res
