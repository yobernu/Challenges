# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target - 1
        count = 0
        l_num = target//2
        while maxDoubles:
            if l_num < 1:
                break
            if l_num * 2 == target:
                count += 1
            elif l_num * 2 != target:
                count += 2
            
            print(l_num, target, count)
            target = l_num
            l_num = l_num//2
            maxDoubles -= 1
        if l_num > 0:
            count += (target - 1)
        return count


