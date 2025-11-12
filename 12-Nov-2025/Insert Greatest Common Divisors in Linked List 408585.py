# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        curr = dummy

        while head and head.next:
            curr.next = ListNode(head.val)
            curr = curr.next
            mid_gcd = gcd(head.val, head.next.val)
            curr.next = ListNode(mid_gcd)
            curr = curr.next
            head = head.next
        curr.next = ListNode(head.val)
        return dummy.next



        