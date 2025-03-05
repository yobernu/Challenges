# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if 5 not in bills:
            return False
        count_5, count_10 = 0, 0
        for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10:
                if count_5 > 0:
                    count_5 -= 1
                    count_10 += 1
                else:
                    return False
            else:
                if count_5 and count_10:
                    count_5 -= 1
                    count_10 -= 1
                elif count_5 > 2:
                    count_5 -= 3
                else:
                    return False
        return True