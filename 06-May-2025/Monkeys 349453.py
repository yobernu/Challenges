# Problem: Monkeys - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/E

from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.root = {i: i for i in range(1, n + 1)}
        self.rank = defaultdict(int)
        self.fall_time = defaultdict(lambda: -1)

    def find(self, x):
        if self.root[x] == x:
            return x, self.fall_time[x]
        rootx, max_time = self.find(self.root[x])
        self.root[x] = rootx
        self.fall_time[x] = max(self.fall_time[x], max_time)
        return self.root[x], self.fall_time[x]

    def union(self, x, y, time):
        rootx, _ = self.find(x)
        rooty, _ = self.find(y)
        if rootx == rooty:
            return
        if rootx == 1:
            self.root[rooty] = 1
            self.fall_time[rooty] = time
        elif rooty == 1:
            self.root[rootx] = 1
            self.fall_time[rootx] = time
        else:
            rankx, ranky = self.rank[rootx], self.rank[rooty]
            if rankx < ranky:
                self.root[rootx] = rooty
            elif rankx > ranky:
                self.root[rooty] = rootx
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1

n, m = map(int, input().split())
hands = []
for _ in range(n):
    l, r = map(int, input().split())
    hands.append([l, r])  

set_removed = set()
removed_list = []

for _ in range(m):
    mon, hand = map(int, input().split())
    set_removed.add((mon, hand))
    removed_list.append((mon, hand))

dsu = UnionFind(n)

for mon in range(1, n+1):
    left, right = hands[mon-1]  
    if left != -1 and (mon, 1) not in set_removed:
        dsu.union(mon, left, -1)
    if right != -1 and (mon, 2) not in set_removed:
        dsu.union(mon, right, -1)

for t in range(m-1, -1, -1):
    mon, hand = removed_list[t]
    neighbor = hands[mon-1][hand-1]
    if neighbor != -1:
        dsu.union(mon, neighbor, t)

for i in range(1, n+1):
    _, time = dsu.find(i)
    print(time)
