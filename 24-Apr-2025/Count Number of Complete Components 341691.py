# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # comp = defaultdict(int)
        # graph = [[] for _ in range(n)]
        # for i in range(n):
        #     graph[i] = [i]
        # for l, r in edges:
        #     graph[l].append(r)
        #     graph[r].append(l)
        
        # for i in range(n):
        #     neigh = tuple(sorted(graph[i]))
        #     comp[neigh] += 1
        # count = 0
        # for key, val in comp.items():
        #     if len(key) == val:
        #         count += 1
        # return count

            


        visited = [False]*n
        count = 0

        for i in range(n):
            if visited[i]:
                continue
            q = deque([i])
            n_edges = 0
            m = 0
            visited[i] = True
            while q:
                node = q.popleft()
                m += 1
                for neigh in graph[node]:
                    n_edges += 1
                    if not visited[neigh]:
                        visited[neigh] = True
                        q.append(neigh)
           
            if m*(m-1)//2 == n_edges//2:
                count += 1
        return count
            



        