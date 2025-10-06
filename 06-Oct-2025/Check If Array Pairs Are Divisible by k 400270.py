# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0 for i in range(k)]

        for num in arr:
            freq[num%k] += 1
        print(freq)
        for num in range(1, k):
            if num == k-num and freq[num]%2 == 1:
                return False
            if freq[num] != freq[k-num]:
                return False
        return True
