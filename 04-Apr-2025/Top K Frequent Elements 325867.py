# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        maxScores =[] 
        hold = []
        for val in nums:
            d[val] += 1
        for value in d.values():
            maxScores.append(value)
        maxScores.sort()
        count = 0
        for maxs in range(len(maxScores)-1, -1, -1):
            hold.append(maxScores[maxs])
            count +=1
            if count == k:
                break
        final = []
        hold.sort()
        for key in d.keys():
            if d[key] in hold:
                final.append(key)
        return sorted(final)