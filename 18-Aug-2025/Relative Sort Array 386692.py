# Problem: Relative Sort Array - https://leetcode.com/problems/relative-sort-array/description/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # counting sort o(n)
        freq = [0]*1001
        for num in arr1:
            freq[num] += 1

        res = []
        for num in arr2:
            res.extend([num]*freq[num])
            freq[num] = 0
        for i in range(1001):
            if freq[i] > 0:
                res.extend([i]*freq[i])
        return res


        # arr1.sort()
        # ans = defaultdict(int)
        # rest = []
        # hashmap = {}
        # for idx, num in enumerate(arr2):
        #     hashmap[idx] = num
        # revers = {}
        # for idx, num in enumerate(arr2):
        #     revers[num] = idx
        # for i in range(len(arr1)):
        #     if revers.get(arr1[i]) != None and revers.get(arr1[i]) > -1:
        #         ans[revers[arr1[i]]] += 1
        #     else:
        #         rest.append(arr1[i])
        # res = []
        # ans = sorted(ans.items())
        # for idx, val in ans:
        #     res += [hashmap[idx]]*val
        # return res + rest 


        
