# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s1=[]
        s2=[]
        def dfs(root,arr):
            if not root:
                arr.append(None)
                return
            arr.append(root.val)
            dfs(root.left, arr)
            dfs(root.right, arr)
        dfs(root,s1)
        dfs(subRoot, s2)
        n = len(s2)

        for i in range(len(s1) - n + 1):
            if s1[i:i+n] == s2:
                return True
        return False
