# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

# class Solution:
#     def hammingDistance(self, x: int, y: int) -> int:
#         def find(i):
#             ans = []
#             while i:
#                 mode = i & 1
#                 ans.append(mode)
#                 i >>= 1
#             return ans
#         a , b = deque(), deque()
#         a.extend(find(x))
#         while len(a) < 32:
#             a.appendleft(0)
#         b.extend(find(y))
#         while len(b) < 32:
#             b.appendleft(0)

#         print(a)
#         print(b)
#         count = 0
#         for i , j in zip(list(a), list(b)):
#             if i != j:
#                 count += 1

#         return count





class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def to_32(n):
            bits = []
            while n:
                bits.append(n & 1)
                n >>= 1
            while len(bits) < 32:
                bits.append(0)
            return bits 

        a = to_32(x)
        b = to_32(y)

        return sum(i != j for i, j in zip(a, b))
