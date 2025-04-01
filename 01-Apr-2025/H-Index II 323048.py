# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        low , high = 0, n-1
        ans = 0
        while low <= high:
            mid = (low + high)//2
            if  n - mid <= citations[mid]:
                high = mid - 1
                ans = n - mid
            else:
                low = mid + 1
        return ans