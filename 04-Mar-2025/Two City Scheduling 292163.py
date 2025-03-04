# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        lst = []
        for a,b in costs:
            lst.append((a-b, a, b))
        lst.sort()
        print(lst)
        tot, count = 0, 0
        for d, a, b in lst:
            if count < n/2:
                tot += a
            else:
                tot += b
            count += 1
        return tot
