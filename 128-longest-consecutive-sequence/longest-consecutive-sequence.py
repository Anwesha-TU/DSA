class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        # length=0
        max_len=0
        for i in sett:
            if (i-1) not in sett:
                current=i
                length=1
                while (current+1) in sett:
                    current+=1
                    length+=1
                max_len=max(length,max_len)
        return max_len