# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def pre_order(node):
            if not node:
                return 0
            left=pre_order(node.left)
            right=pre_order(node.right)
            return 1+max(left,right)
        return pre_order(root)