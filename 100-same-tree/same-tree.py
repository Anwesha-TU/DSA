# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1=[]
        arr2=[]
        def dfs(node,arr):
            if not node:
                arr.append(None)
                return
            arr.append(node.val)
            dfs(node.left,arr)
            dfs(node.right,arr)
        dfs(p,arr1)
        dfs(q,arr2)
        return (arr1==arr2)