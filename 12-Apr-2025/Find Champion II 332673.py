# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[b].append(a)
        # print(graph)
        # for i in range(n):
        #     if len(graph[i]) > 1:
        #         return -1
        hold = []
        for i in range(n):
            if i not in graph.keys():
                hold.append(i)
        if len(hold) == 1:
            return hold[0]
        return -1