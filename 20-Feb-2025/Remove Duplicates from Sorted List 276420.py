# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        s = set()
        s.add(head.val)
        curr = head
        while curr.next:
            if curr.next.val in s:
                curr.next = curr.next.next
            else:
                s.add(curr.next.val)
                curr = curr.next
        return head
