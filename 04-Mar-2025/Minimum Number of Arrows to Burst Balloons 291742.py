# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        sorted_points = sorted(points, key=lambda x: x[1])
        # print(sorted_points)
        count = 1
        temp = sorted_points[0]
        for i in range(1, n):
            if sorted_points[i][0] <= temp[1]:
                continue
            else:
                count += 1
                temp = sorted_points[i]
        return count


