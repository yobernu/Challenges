# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self,size):
        self.root = {chr(i + 97): chr(i + 97) for i in range(size)}  
    def find(self,x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x
    
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx < rooty:
            self.root[rooty] = rootx
        else:
            self.root[rootx] = rooty
    def connected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        size = 26
        dsu = UnionFind(size)
        for i in range(n):
            dsu.union(s1[i],s2[i])

        arr = []
        for i in baseStr:
            arr.append(dsu.find(i))
        return ''.join(arr)