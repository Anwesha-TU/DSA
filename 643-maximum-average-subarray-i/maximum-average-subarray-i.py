class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        add=0
        for i in range(k):
            add+=nums[i]
        avg=add/k
        for i in range (k,n):
            add+=nums[i]
            add-=nums[i-k]
            curr_avg=add/k
            avg=max(avg,curr_avg)
        return avg