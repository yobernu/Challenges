# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sorted_trips = sorted(lst, key=lambda x: x[1])
        i, j= 0, 0
        n = len(trips)

        pref = [0]*(1002)
        for p, f, t in trips:
            pref[f] += p
            pref[t] -= p
        for i in range(1, 1002):
            pref[i] += pref[i-1]
        print(pref)
        return capacity >= max(pref)
        