class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        max_freq=0
        n=len(s)
        max_w=0
        l=0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(count.values())
            while ((r-l+1)-max_freq)>k:
                count[s[l]]-=1
                l+=1
            max_w=max(max_w, r-l+1)
        return max_w