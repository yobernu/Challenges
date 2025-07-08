# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev_graph = defaultdict(list)
        outdegree = [0 for _ in range(n)]
        for i in range(n):
            outdegree[i] = len(graph[i])
            for v in graph[i]:
                rev_graph[v].append(i)

        queue = deque([i for i in range(n) if outdegree[i] == 0])
        safe = [False]*n

        while queue:
            node = queue.popleft()
            safe[node] = True

            for neigh in rev_graph[node]:
                outdegree[neigh] -= 1
                if outdegree[neigh] == 0:
                    queue.append(neigh)
        return [i for i in range(n) if safe[i]]
        
        
        
        
        
        
        



        # n = len(graph)
        # colors = [0] * n
        # result = []

        # def dfs(node):
        #     if colors[node] == 1:
        #         return False 
        #     if colors[node] == 2:
        #         return True
        #     colors[node] = 1
        #     for neigh in graph[node]:
        #         if not dfs(neigh):
        #             return False
        #     colors[node] = 2
        #     return True

        # for i in range(n):
        #     if dfs(i):
        #         result.append(i)

        # return result
