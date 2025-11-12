# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        dummy = ListNode(0, head)
        curr = dummy.next
        length = 0
        result = []
        while curr:
            curr = curr.next
            length += 1
        
        curr = head
        base = length//k
        extra = length%k
        for i in range(k):
            part_head = curr 
            part_size = base + (1 if i < extra else 0)
            while curr and part_size-1 > 0:
                curr = curr.next
                part_size -= 1
            if curr:
                next_head = curr.next   #hold next head on new var
                curr.next = None          #cut the chain
                curr = next_head
                result.append(part_head)
            else:
                result.append(None)
        return result