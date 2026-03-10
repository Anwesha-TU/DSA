class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n=len(intervals)
        merge=[]
        for i in range(n):
            if not merge:
                merge.append(intervals[i])
            elif (merge[-1][1]>=intervals[i][0]):
                merge[-1][1]=max(merge[-1][1],intervals[i][1])
            else:
                merge.append(intervals[i])
        return merge    