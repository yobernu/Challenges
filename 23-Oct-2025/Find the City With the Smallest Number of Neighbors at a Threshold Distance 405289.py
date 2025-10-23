# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        min_reachable = float('inf')
        result_city = -1
        
        # Dijkstra
        for i in range(n):
            distances = [float('inf')] * n
            distances[i] = 0
            heap = [(0, i)]
            
            while heap:
                current_dist, node = heapq.heappop(heap)
                if current_dist > distances[node]:
                    continue
                
                for neighbor, weight in graph[node]:
                    new_dist = current_dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor))
            
            reachable_count = 0
            for j in range(n):
                if i != j and distances[j] <= distanceThreshold:
                    reachable_count += 1
            if reachable_count < min_reachable or (reachable_count == min_reachable and i > result_city):
                min_reachable = reachable_count
                result_city = i
                
        return result_city