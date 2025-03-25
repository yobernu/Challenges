# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set() 

        def checker(option):
            stack = []
            for i in option:
                if i == "(":
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False  
            return len(stack) == 0

        def backtrack(path):
            if len(path) == 2 * n:
                path_str = "".join(path)
                if checker(path_str):
                    ans.add(path_str) 
                return
            path.append("(")
            backtrack(path)
            path.pop()

            path.append(")")
            backtrack(path)
            path.pop()

        backtrack([])
        return list(ans) 
