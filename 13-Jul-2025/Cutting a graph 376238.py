# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1]*size
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1   
        return self.find(x) == self.find(y)
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
import sys
input = lambda: sys.stdin.readline().strip()
v, e, o = map(int, input().split())
uf = UnionFind(v)
for _ in range(e):
    a, b = map(int, input().split())
    pass
res = []
for _ in range(o):
    accept = input().split()
    key = accept[0]
    a, b = int(accept[1]), int(accept[2])
    res.append([key, a, b])
 
ans = []
for key, a, b in reversed(res):
    if key == "ask":
        if uf.connected(a-1, b-1):
            ans.append("YES")
        else:
            ans.append("NO")
    else:
        uf.union(a-1, b-1)
 
for response in reversed(ans):
    print(response)