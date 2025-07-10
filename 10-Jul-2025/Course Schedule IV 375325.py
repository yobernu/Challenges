# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isPre = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            isPre[u][v] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if isPre[i][k] and isPre[k][j]:
                        isPre[i][j] = True
        return [isPre[u][v] for u, v in queries]
