# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy = ListNode()
        # dummy.next = head
        # length  = 0
        # curr = dummy
        # while curr:
        #     length += 1
        #     curr = curr.next
        # curr = dummy
        # idx = length - n - 1
        # for _ in range(idx):
        #     curr = curr.next
        # curr.next = curr.next.next
        # return dummy.next



        #Two pointer approach
        dummy = ListNode()
        dummy.next = head
        count = 0
        right = dummy
        while count < n:
            right = right.next
            count += 1
        left = dummy
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
