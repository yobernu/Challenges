# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # ans = []
        def helper(start, end):
            if start == end:
                return
            mid = (start + end)//2
            node = TreeNode(nums[mid])
            node.left = helper(start, mid)
            node.right = helper(mid+1, end)
            return node
        return helper(0, len(nums)) 
        