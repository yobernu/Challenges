# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_element or self.min_element[-1] >= val:
            self.min_element.append(val)

    def pop(self) -> None:
        if not self.stack:
            return 
        if self.min_element and self.min_element[-1] == self.stack[-1]:
            self.min_element.pop()
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.min_element:
            return -1
        return self.min_element[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()