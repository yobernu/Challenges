# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        my_dict= defaultdict(list)
        for i in paths:
            dirr, *files = i.split()

            for f in files:
               f_name, f_content = f.split("(")
               my_dict[f_content].append(dirr + "/" + f_name)
        ans = []
        for values in  my_dict.values():
            if len(values) >1 :
                ans.append(values)
        return ans