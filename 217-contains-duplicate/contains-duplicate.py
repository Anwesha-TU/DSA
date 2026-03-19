class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter=defaultdict(int)
        for i in nums:
            counter[i]+=1
        for i in counter.keys():
            if counter[i]>=2:
                return True
        return False