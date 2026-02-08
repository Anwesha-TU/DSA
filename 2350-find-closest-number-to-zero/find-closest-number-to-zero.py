class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        n=len(nums)
        a=[inf]*n
        for i in range (n):
            dist=abs(nums[i])
            a.append(dist)
        mini=min(a)
        if mini in nums:
            return mini
        elif -(mini) in nums:
            return -mini