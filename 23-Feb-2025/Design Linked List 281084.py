# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        idx = 0
        while curr:
            if idx == index:
                return curr.val
            curr = curr.next
            idx += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        new_node = ListNode(val)
        curr = self.head
        count = 0
        prev = None

        while curr:
            if count == index:
                prev.next = new_node
                new_node.next = curr
                return
            prev = curr
            curr = curr.next
            count += 1

        if count == index:  # Add at tail if index is equal to length
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length():
            print("Error: Invalid index")
            return

        if index == 0:  # If deleting the head
            self.head = self.head.next
            return

        curr = self.head
        count = 0
        prev = None

        while curr:
            if count == index:
                prev.next = curr.next  # Skip the current node
                return
            prev = curr
            curr = curr.next
            count += 1

    def length(self) -> int:
        curr_node = self.head
        l = 0
        while curr_node:
            l += 1
            curr_node = curr_node.next
        return l



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)