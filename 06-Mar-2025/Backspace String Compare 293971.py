# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s:
            if i == "#" and stack1:
                stack1.pop()
            elif i == "#" and not stack1:
                continue
            else:
                stack1.append(i)
            print(stack1)

        for i in t:
            if i == "#" and stack2:
                stack2.pop()
            elif i == "#" and not stack2:
                continue
            else:
                stack2.append(i)
            print(stack2)
        # print(stack1, stack2)
        return stack1 == stack2
                
