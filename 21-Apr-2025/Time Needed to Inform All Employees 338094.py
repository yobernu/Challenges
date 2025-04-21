# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)
        def dfs(hid):
            if not graph[hid]:
                return 0
            tot_time = 0
            for i in graph[hid]:
                time = dfs(i)
                tot_time = max(time, tot_time)
            return tot_time + informTime[hid]
        return dfs(headID)