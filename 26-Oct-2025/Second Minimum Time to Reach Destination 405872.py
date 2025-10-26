# Problem: Second Minimum Time to Reach Destination - https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dist1 = [float("inf")]*(n+1)
        dist2 = [float("inf")]*(n+1)
        freq = [0]*(n+1)
        queue = [(0, 1)]
        dist1[1] = 0
        while queue:
            timeTaken, node = heapq.heappop(queue)
            freq[node] += 1
            if freq[node] == 2 and node == n:
                return timeTaken
            if (timeTaken // change) % 2:
                timeTaken = change * (timeTaken // change + 1) + time
            else:
                timeTaken = timeTaken + time

            for neighbor in graph[node]:
                if freq[neighbor] == 2:
                    continue
                if dist1[neighbor] > timeTaken:
                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = timeTaken
                    heapq.heappush(queue, (timeTaken, neighbor))
                elif (
                    dist2[neighbor] > timeTaken and dist1[neighbor] != timeTaken
                ):
                    dist2[neighbor] = timeTaken
                    heapq.heappush(queue, (timeTaken, neighbor))
        return 0


