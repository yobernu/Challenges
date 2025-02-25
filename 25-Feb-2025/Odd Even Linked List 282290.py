# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        o = odd
        even = ListNode()
        e = even
        new_node = ListNode()
        while head and head.next:
            o.next = head
            o = o.next
            e.next = head.next
            e = e.next

            head = head.next.next
        if head:
            o.next = head
            o = o.next
        e.next = None
        o.next = even.next
        return odd.next 
        