# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p_sum = [nums[0]]
        temp = nums[0]
        hash_map = Counter([0])

        for num in range(1, n):
            temp += nums[num]
            p_sum.append(temp)
        
        ans = 0
        for i in range(n):
            if p_sum[i] - k in hash_map:
                ans += hash_map[p_sum[i] - k]
            hash_map[p_sum[i]] += 1
        return ans

        
