# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            if root.val == p.val or root.val == q.val:
                return root
            if (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
                return root
            if root.val > p.val and root.val > q.val:
                return self.lowestCommonAncestor(root.left, p, q)
            if root.val < p.val and root.val < q.val:
                return self.lowestCommonAncestor(root.right, p, q)
        return None




    #     self.store = []
    #     store_1 = self.helper(root, p)
    #     self.store = []
    #     store_2 = self.helper(root, q)
    #     for i in range(min(len(store_1), len(store_2))-1, -1, -1):
    #         if store_1[i].val == store_2[i].val:
    #             return store_1[i]

    # def helper(self, node, k):
    #     if node:
    #         self.store.append(node)
    #         if node.val > k.val:
    #             self.helper(node.left, k)
    #         elif node.val < k.val:
    #             self.helper(node.right, k)
    #         else:
    #             return self.store
    #     return self.store