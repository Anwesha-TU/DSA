class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        if (nums[l]<nums[r]):
            return nums[0]
        while l<=r:
            mid=(l+r)//2
            if mid>0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[mid]>=nums[0]:
                l=mid+1
            else:
                r=mid-1
        return nums[0]