# Problem: Different Ways to Add Parentheses - https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def recurse(expr: str) -> List[int]:
            results = []
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = recurse(expr[:i])
                    right = recurse(expr[i+1:])
                    for l in left:
                        for r in right:
                            if ch == "+":
                                results.append(l + r)
                            elif ch == "-":
                                results.append(l - r)
                            elif ch == "*":
                                results.append(l * r)
            if not results:
                results.append(int(expr))
            return results
        
        return recurse(expression)