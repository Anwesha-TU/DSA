class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        max_area=0
        l=0
        r=n-1
        while l<r:
            area=(r-l)*(min(height[l],height[r]))
            max_area=max(max_area,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        # for i in range(n):
        #     for j in range(i+1,n):
        #         area=(j-i)*(min(height[i],height[j]))
        #         max_area=max(max_area,area)
        return max_area