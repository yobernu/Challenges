# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traversal(p) == self.traversal(q)
    
    def traversal(self, root):
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if root is None:
            ans.append(None)
            return
        ans.append(root.val)
        self.helper(root.left, ans)
        self.helper(root.right, ans)
        return root
