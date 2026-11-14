import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        for i in range (len(nums)):
            nums[i]=-nums[i]        
        heapq.heapify(nums)
        max=[]
        for i in range(k):
            max.append(heapq.heappop(nums))
        return -max[-1]
