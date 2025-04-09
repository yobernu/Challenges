# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE = 1
        GRAY = 2
        BLACK = 3
        colors = [WHITE]*numCourses
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)


        def dfs(node):
            colors[node] = GRAY
            for nbr in graph[node]:
                if colors[nbr] == WHITE:
                    if not dfs(nbr):
                        return False
                elif colors[nbr] == GRAY:
                    return False
            colors[node] = BLACK
            return True
        ans = True
        for node in range(numCourses):
            if colors[node] == WHITE:
                if not dfs(node):
                    return False
        return True
