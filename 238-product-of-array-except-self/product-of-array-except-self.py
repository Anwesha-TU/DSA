class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        sec=nums.copy()
        zero_count=nums.count(0)
        ans=[0]*n
        import math
        product=math.prod(nums)
        for i in range (n):
            if (nums[i]==0):
                sec.remove(0)
                product1=math.prod(sec)
        for i in range (n):
            if (nums[i]!=0):
                ans[i]=product//nums[i]
            elif zero_count==1:
                ans[i]=product1
            elif zero_count>1:
                ans[i]==0
        return ans