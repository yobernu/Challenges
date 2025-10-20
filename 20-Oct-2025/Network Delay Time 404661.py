# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        distances = [float("inf")] * (n + 1)
        distances[k] = 0
        heap = [(0, k)]
        
        while heap:
            current_dist, node = heapq.heappop(heap)
            # if current_dist > distances[node]:
            #     continue
            for neigh, weight in graph[node]:
                new_dist = current_dist + weight
                if new_dist < distances[neigh]:
                    distances[neigh] = new_dist
                    heapq.heappush(heap, (new_dist, neigh))
        
        answer = max(distances[1:])
        return answer if answer != float("inf") else -1
