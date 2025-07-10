# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    
        def dfs(graph, visited, src, target):
            visited[src] = True
            if src == target:
                return True
            for adj in graph[src]:
                if not visited[adj]:
                    if dfs(graph, visited, adj, target):
                        return True
            return False
        
        graph = [[] for _ in range(numCourses)]
        for pre, course in prerequisites:
            graph[pre].append(course)
        
        ans = []
        for u, v in queries:
            visited = [False]*numCourses
            ans.append(dfs(graph, visited, u, v))
        return ans

