# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low , high = 1, max(candies)
        def possible(mid):
            count = 0
            for candy in candies:
                count += (candy//mid)
            return count >= k
        
        ans = 0
        while low <= high:
            mid = (low + high)//2
            if possible(mid):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans
        