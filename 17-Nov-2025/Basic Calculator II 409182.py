# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        signs = ["+", "-", "*", "/"]
        stack = []
        s = s.replace(" ", "")
        n = len(s)
        i = 0
    
        while i < n:
            if s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                stack.append(num)
                continue
            elif s[i] in signs:
                if s[i] == "*" or s[i] == "/":
                    operator = s[i]
                    i += 1
                    num = 0
                    while i < n and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    prev_num = stack.pop()
                    if operator == "*":
                        result = prev_num * num
                    else:
                        result = int(prev_num / num)
                    stack.append(result)
                    continue
                else:
                    stack.append(s[i])
                    i += 1
            else:
                i += 1
        result = 0
        if stack:
            result = stack[0]
        i = 1
        while i < len(stack):
            operator = stack[i]
            if i + 1 < len(stack):
                next_num = stack[i + 1]
                
                if operator == "+":
                    result += next_num
                else:
                    result -= next_num
                
            i += 2
        
        return result