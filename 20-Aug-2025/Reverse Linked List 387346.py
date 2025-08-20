# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next  
            curr.next = prev  
            prev = curr  
            curr = next_node  

        return prev 