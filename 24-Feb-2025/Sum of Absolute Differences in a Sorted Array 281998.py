# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_sum = [nums[0]]
        suf_sum = [nums[-1]]


        for i in range(1, n):
            pre_sum.append(nums[i] + pre_sum[i-1])
        for i in range(n-2, -1, -1):
            suf_sum.append(nums[i] + suf_sum[n-i-2])

        suf_sum = suf_sum[::-1]
        print(pre_sum, suf_sum)
        ans = []
        for i in range(n):
            if i == 0:
                left = 0
            if i > 0:
                left = i*nums[i] - pre_sum[i-1]
            if i < n-1:
                right = suf_sum[i+1] - (n-1-i)*nums[i]
            if i == n-1:
                right = 0
            ans.append(left+right)
        return ans

