# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import Counter, defaultdict, deque
from cmath import inf
 
 
def iinput(): return int(input())
def sinput(): return input()
def iarray(): return list(map(int, input().split()))
def imatrix(rows): return [list(map(int,input().split())) for _ in range(rows)]
def smatrix(rows): return [input() for _ in range(rows)]
def mapinput(): return map(int, input().split())
 
v,e = mapinput()
indeg = defaultdict(int)
outdeg = defaultdict(int)
graph = [[] for i in range(v+1)]
for i in range(e):
    edge = iarray() 
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
twos = 0
star = 0
ones = 0
for liste in graph[1:]:
    if len(liste) == 2:
        twos+=1
    elif len(liste) == v-1:
        star+=1
    elif len(liste) == 1:
        ones+=1
 
if star == 1 and ones == v-star:
    print("star topology")
elif twos == v:
    print("ring topology")
elif ones == 2 and twos == v-ones:
    print("bus topology")
else:
    print("unknown topology")