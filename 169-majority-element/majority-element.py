class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        count=Counter(nums)
        n=len(nums)
        # max_len=0
        for k in count.keys():
            if (count[k]>(n//2)):
                length=count[k]
                return k
        #         max_len=max(length,max_len)
        # keys = [k for k, v in count.items() if v == max_len]
        # ans=int(keys)
        # return ans
        