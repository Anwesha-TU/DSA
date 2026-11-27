class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        max_area=0
        def dfs(i,j):
            nonlocal area
            if i<0 or i>=m or j<0 or j>=n:
                return
            if grid[i][j]==0:
                return
            area+=1
            grid[i][j]=0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(m):
            for j in range(n):
                area=0
                dfs(i,j)
                max_area=max(area,max_area)
        return max_area