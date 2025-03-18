# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root and root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root and root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            successor = self.helper(root)
            root.val = successor.val  
            root.right = self.deleteNode(root.right, successor.val)  
        return root
    def helper(self, node):
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr