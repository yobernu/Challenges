# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        n = len(answers)
        counter = Counter(answers)
        res = 0

        for key, count in counter.items():
            num = (count-1)//(key+1)+1
            res += num*(key+1)

        return res

            
            
