# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        low, high = 0, len(queries)
        n = len(nums)
        def search(mid):
            prefix_sum = [0]*(n+1)
            for l, r, val in queries[:mid]: 
                prefix_sum[l] -= val
                prefix_sum[r+1] += val
            for i in range(1, n):
                prefix_sum[i] += prefix_sum[i-1]
            for i in range(n):
                if nums[i] + prefix_sum[i] > 0:
                    return False
            return True

        while low <= high:
            mid = (low + high)//2
            if search(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low if search(low) else -1