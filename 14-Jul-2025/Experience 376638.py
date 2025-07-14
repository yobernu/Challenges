# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.experience = {}  
        self.difference = {}   

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
            self.experience[x] = 0
            self.difference[x] = 0
            return x
        if self.parent[x] != x:
            orig_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.difference[x] += self.difference[orig_parent]
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        sizex = self.size[rootx]
        sizey = self.size[rooty]

        if sizex < sizey:
            self.parent[rootx] = rooty
            self.size[rooty] += sizex
            self.difference[rootx] = self.experience[rootx] - self.experience[rooty]
        else:
            self.parent[rooty] = rootx
            self.size[rootx] += sizey
            self.difference[rooty] = self.experience[rooty] - self.experience[rootx]

    def add(self, x, val):
        root = self.find(x)
        self.experience[root] += val

    def get(self, x):
        self.find(x)  
        return self.experience[self.parent[x]] + self.difference[x]


uf = UnionFind()
n, m = map(int, input().split())
for _ in range(m):
    query = input().split()
    if query[0] == "add":
        uf.add(int(query[1]), int(query[2]))
    elif query[0] == "join":
        uf.union(int(query[1]), int(query[2]))
    elif query[0] == "get":
        print(uf.get(int(query[1])))