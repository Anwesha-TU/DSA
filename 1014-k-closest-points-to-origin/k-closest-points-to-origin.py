import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist=[]
        for x,y in points:
            d=x**2+y**2
            heapq.heappush(dist, (d, [x,y]))
            ans=[]
        for i in range(k):
            ans.append(heapq.heappop(dist)[1])
        return ans