class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        n=len(nums)
        for i in range (n):
            h[nums[i]]=i
        for i in range (n):
            y=target-nums[i]
            if y in h and h[y]!=i:
                return [i,h[y]]