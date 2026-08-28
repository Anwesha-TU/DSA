# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        arr=[]
        def dfs(root, arr):
            if not root:
                return False
            arr.append(root.val)
            if not root.left and not root.right:
                if sum(arr)==targetSum:
                    return True
            a=dfs(root.left, arr)
            b=dfs(root.right, arr)
            arr.pop()
            return a or b
        return dfs(root,arr)