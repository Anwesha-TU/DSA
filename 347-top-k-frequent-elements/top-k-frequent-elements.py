import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count=Counter(nums)
        heap=[]
        for key,val in count.items():
            heapq.heappush(heap,(-val,key))
        ans=[]
        for i in range (k):
            ans.append(heapq.heappop(heap)[1])
        return ans