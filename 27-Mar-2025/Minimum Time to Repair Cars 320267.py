# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 1 , min(ranks)*cars*cars
        def helper(mid):
            mcars = 0
            for rank in ranks:
                temp = int((mid//rank)**0.5)
                mcars += temp
                if mcars >= cars:
                    return True
            return False
        
        while low < high:
            mid = (low+high)//2
            if helper(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
                