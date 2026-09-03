# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
            return arr
        dfs(root)
        diff=[]
        for i in range(1,len(arr)):
            diff.append(arr[i]-arr[i-1])
        return abs(min(diff))