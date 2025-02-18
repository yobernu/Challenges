# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        fr = [0] *(n+1)
        for left, right in requests:
            fr[left] += 1
            fr[right + 1] -= 1
        for i in range(1, n):
            fr[i] += fr[i-1]
        nums.sort(reverse=True)
        fr.sort(reverse=True)
        fr.pop()
        ans = 0
        for i, j in zip(fr, nums):
            ans += i*j
        print(fr, nums)
        return ans  % (10**9 + 7)



