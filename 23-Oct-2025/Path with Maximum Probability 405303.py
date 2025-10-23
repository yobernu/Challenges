# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # adjacency list
        graph = [[] for _ in range(n)]
        for idx, edge in enumerate(edges):
            u, v = edge
            graph[u].append((v, succProb[idx]))
            graph[v].append((u, succProb[idx]))
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        heap = [(-1, start_node)]
        
        while heap:
            neg_prob, node = heapq.heappop(heap)
            curr_prob = -neg_prob
            if curr_prob < max_prob[node]:
                continue
            for neigh, weight in graph[node]:
                new_prob = curr_prob * weight
                if new_prob > max_prob[neigh]:
                    max_prob[neigh] = new_prob
                    heapq.heappush(heap, (-new_prob, neigh))
        
        return max_prob[end_node]