# Problem: E - Simple Cycle With Minimal Lightest Edge - https://codeforces.com/gym/607625/problem/E

class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)}
        self.sizes = {i:1 for i in range(size)}
    
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
        
    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        
        if root1 == root2:
            return False
        
        if self.sizes[root2] > self.sizes[root1]:
            root1,root2 = root2,root1
        
        self.parent[root2] = root1
        self.sizes[root1] += self.sizes[root2]
        
        return True



def find_cycle_path(start, end, graph):
    que = [start]
    visited = set([start])
    
    parent = {start : -1} # this will be useful to track our path back
    
    while que:
        curr = que.pop()
        
        if curr == end:
            break
        
        for nbr in graph[curr]:
            if curr == start and nbr == end: 
                # we dont want the direct path we want to cycle back so
                continue
            
            if nbr not in visited:
                parent[nbr] = curr # mark the next nodes come after curr
                
                visited.add(nbr)
                que.append(nbr)
    
    
    #now let’s track our path back
    path = []
    
    curr = end
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    
    
    return path[::-1] # since this path is a cycle there is no need for reversing.
    
        
        
def solve():
    n,m = map(int, input().split())
    
    edges = [] #lets store the edges
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        u, v, w =  map(int, input().split())

        #for the graph we realy don't need the weights
        graph[u].append(v)
        graph[v].append(u)
        
        edges.append((u, v, w))
    
    edges.sort(key = lambda x : x[2], reverse = True)
    
    
    dsu = UnionFind(n+1)
    
    start = end = b = -1
    for u, v, w in edges:
        if not dsu.union(u, v):
            #already connected
            #now we know there must be a cycle 
            #we can just find a way from u to v the other way around
            start = u
            end = v
            b = w
            #this can be an answer but we might find better answer
    
    path = find_cycle_path(start, end, graph)
    
    print(b, len(path))
    print(*path)
    
    



for _ in range(int(input())):
    solve()