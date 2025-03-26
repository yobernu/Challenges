# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def yigerem(capacity):
            curr = 0
            curr_days = 1
            for weight in weights:
                curr += weight
                if curr > capacity:
                    curr_days += 1
                    curr = weight
            return days >= curr_days

        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high)//2
            if yigerem(mid):
                high = mid - 1
            else:
                low  = mid + 1
        return low