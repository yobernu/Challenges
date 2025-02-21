# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #3,4,1,2 :-----> 3,1,2,4
        #3,6,5,4,1,2 : -----> 3,1,2,6,5,4
        #3,6,5,4,8,1,7,2 : ------> 3,1,2,6,5,4,8,7
        # all numbers less than x should be to left of x node
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        new = []
        n = len(arr)
        right = 0
        while right < n:
            if arr[right] < x:
                new.append(arr[right])
                arr.remove(arr[right])
                n-=1
            else:
                right += 1
        ans = new + arr
        dummy = ListNode(0)
        current = dummy
        for val in ans:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next