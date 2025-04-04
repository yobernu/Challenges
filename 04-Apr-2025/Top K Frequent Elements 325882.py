# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        ans = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            d[num] += 1
        for key, val in d.items():
            ans[val].append(key)

        res = []
        for i in ans[::-1]:
            if len(i) > 0:
                res.extend(i)
            if len(res) >= k:
                break
        return res[:k]