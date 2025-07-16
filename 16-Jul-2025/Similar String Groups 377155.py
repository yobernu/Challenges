# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                if rank[px] > rank[py]:
                    parent[py] = px
                elif rank[px] < rank[py]: 
                    parent[px] = py
                else:
                    rank[px] += 1
                    parent[py] = px
        graph = defaultdict(int)
        
        for i in range(n):
            for j in range(i+1, n):
                count = 0
                for u, v in zip(strs[i], strs[j]):
                    if u != v:
                        count += 1
                if count <= 2:
                    union(i, j)
        ans = 0
        for i in range(n):
            if parent[i] == i:
                ans += 1
        return ans

