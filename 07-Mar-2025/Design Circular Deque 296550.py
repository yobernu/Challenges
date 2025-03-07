# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

from collections import deque

class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.enque = deque()

    def insertFront(self, value: int):
        if self.isFull(): 
            return False
        self.enque.appendleft(value) 
        return True

    def insertLast(self, value: int):
        if self.isFull():  
            return False
        self.enque.append(value)  
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.enque.popleft() 
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.enque.pop()  
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.enque[0]  

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.enque[-1]  

    def isEmpty(self):
        return len(self.enque) == 0 

    def isFull(self):
        return len(self.enque) == self.k  
