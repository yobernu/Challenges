# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == "]":
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp 
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(temp * int(num)) 
            else:
                stack.append(char)

        return "".join(stack)