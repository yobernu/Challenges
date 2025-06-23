# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict
nodes_n, edges_n = map(int, input().split())
graph = defaultdict(list)
def solve(graph, nodes_n):
    deg = [len(graph[i]) for i in range(nodes_n)]
    if all(d == 2 for d in deg):
        return "ring topology"
    
    elif deg.count(1) == 2 and deg.count(2) == nodes_n - 2:
        return "bus topology"
    elif deg.count(1) == nodes_n - 1 and deg.count(nodes_n-1) == 1:
        return "star topology"
    return "unknown topology"
    
for _ in range(edges_n):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
print(solve(graph, nodes_n))
