# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1,  max(piles)
        def checker(mid):
            hours = 0
            for pile in piles:
                hours +=  ceil(pile/mid)
                
            return hours
        ans = -1
        while low <= high:
            mid = (low + high)//2
            if checker(mid) <= h:
                high = mid - 1
                ans = mid
            else:
                low =  mid+1
        return ans