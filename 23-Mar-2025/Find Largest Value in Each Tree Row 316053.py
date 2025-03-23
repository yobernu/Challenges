# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = defaultdict(lambda: float("-inf"))
        def helper(node, level):
            if node:
                ans[level] = max(ans[level], node.val)
                helper(node.left, level+1)
                helper(node.right, level+1)
            return ans
        return list(helper(root, 0).values())