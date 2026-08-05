class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        nums_zeros=0
        max_w=0
        n=len(nums)
        l=0
        for r in range(n):
            if nums[r]==0:
                nums_zeros+=1
            while nums_zeros>k:
                if nums[l]==0:
                    nums_zeros-=1
                l+=1
            w=r-l+1
            max_w=max(max_w,w)
        return max_w