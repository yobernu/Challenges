# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        left, right = 0, len(people)-1
        people = sorted(people)
        print(people)
        while left <= right:
            print(left)
            if people[left] + people[right] <= limit:
                ans += 1
                right -= 1
                left += 1
            else:
                ans+=1
                right -= 1
        return ans