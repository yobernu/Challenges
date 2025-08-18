# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        ans = defaultdict(int)
        rest = []
        hashmap = {}
        for idx, num in enumerate(arr2):
            hashmap[idx] = num
        revers = {}
        for idx, num in enumerate(arr2):
            revers[num] = idx
        for i in range(len(arr1)):
            if revers.get(arr1[i]) != None and revers.get(arr1[i]) > -1:
                ans[revers[arr1[i]]] += 1
            else:
                rest.append(arr1[i])
        print(ans)
        res = []
        ans = sorted(ans.items())
        print(ans)
        for idx, val in ans:
            res += [hashmap[idx]]*val
        return res + rest 


        
