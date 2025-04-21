# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, query_id):
        emap = {e.id: e for e in employees}
        def dfs(eid):
            employee = emap[eid]
            curr = employee.importance
            sub_tot = 0
            for eid in employee.subordinates:
                sub_imp = dfs(eid)
                sub_tot += sub_imp
            tot = curr + sub_tot
            return tot

        return dfs(query_id)
        