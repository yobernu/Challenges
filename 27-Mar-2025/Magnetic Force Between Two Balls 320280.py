# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low, high = 1 , max(position)
        def search(mid):
            balls = 1
            curr = position[0]
            for i in range(1, len(position)):
                force = position[i] - curr
                if force >= mid:
                    curr = position[i]
                    balls += 1
            return balls >= m
        while low <= high:
            mid = (low + high)//2
            if search(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high


                