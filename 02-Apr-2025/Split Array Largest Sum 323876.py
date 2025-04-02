# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)
        def helper(mid):
            
            tot, count = 0, 1
            for num in nums:
                if tot + num > mid:
                    tot = num
                    count += 1
                else:
                    tot += num
            # print(mid, count)
            return count <= k

        ans = high
        while low <= high:
            mid = (low+high)//2
            if helper(mid):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans

