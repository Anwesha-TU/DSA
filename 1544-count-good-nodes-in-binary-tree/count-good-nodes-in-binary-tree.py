# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val):
            if not root:
                return 0
            good=0
            if (root.val>=max_val):
                good+=1
            max_val = max(max_val, root.val)
            a=dfs(root.left,max_val) 
            b=dfs(root.right,max_val)
            return good+a+b
        return dfs(root,root.val)