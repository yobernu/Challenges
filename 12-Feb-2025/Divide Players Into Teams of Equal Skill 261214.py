# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left, right = 0, len(skill)-1
        temp = []
        skill = sorted(skill)
        while left < right:
            temp.append([skill[left], skill[right]])
            left+=1
            right-=1
        curr_sum = temp[0][0] + temp[0][1]
        for i in temp:
            if i[0] + i[1] != curr_sum:
                return -1
        ans = 0
        for j in temp:
            ans += j[0]*j[1]
        return ans

