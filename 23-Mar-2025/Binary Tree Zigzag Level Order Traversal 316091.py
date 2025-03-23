# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = defaultdict(list)
        def helper(node, level=0):
            if node:
                ans[level].append(node.val)
                helper(node.left, level+1)
                helper(node.right, level+1)
            return ans
        helper(root)
        res = []
        for i in range(len(ans)):
            if i%2 == 0:
                res.append(ans[i])
            else:
                res.append(ans[i][::-1])
        return res


