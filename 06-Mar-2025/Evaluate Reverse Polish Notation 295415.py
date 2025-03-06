# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False

        stack = []
        
        for token in tokens:
            if is_number(token):
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                
                if token == "+":
                    temp = num1 + num2
                elif token == "-":
                    temp = num1 - num2
                elif token == "*":
                    temp = num1 * num2
                elif token == "/":
                    temp = int(num1 / num2)  
                
                stack.append(temp)

        return stack[0]