# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                self.parent[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            else:
                self.parent[rootx] = rooty
                self.size[rooty] += self.size[rootx]
            

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        eml_idx = {}
        for i , account in enumerate(accounts):
            for e in account[1:]:
                if e in eml_idx:
                    uf.union(i, eml_idx[e])
                else:
                    eml_idx[e] = i
        eml_grp = defaultdict(list)
        for e, i in eml_idx.items():
            par = uf.find(i)
            eml_grp[par].append(e)
        res = []
        for i, e in eml_grp.items():
            name = accounts[i][0]
            res.append([name] + sorted(eml_grp[i]))
        return res


            
                    
            




            

        