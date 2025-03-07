# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    temp = 0
                    while stack[-1] != "(":
                        temp += stack.pop()
                    if stack:
                        stack.pop()
                    stack.append(2*temp)
        # print(stack)
        return sum(stack)


