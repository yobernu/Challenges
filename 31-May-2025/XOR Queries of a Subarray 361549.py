# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] ^ arr[i]
        return [prefix[r + 1] ^ prefix[l] for l, r in queries]
