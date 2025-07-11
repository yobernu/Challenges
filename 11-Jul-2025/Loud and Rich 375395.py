# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1

        answer = list(range(n))
        queue = deque([i for i in range(n) if indegree[i] == 0])
        while queue:
            person = queue.popleft()
            for nei in graph[person]:
                if quiet[answer[person]] < quiet[answer[nei]]:
                    answer[nei] = answer[person]
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return answer
