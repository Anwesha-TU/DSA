class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count_s1={}
        count_s2={}
        for ch in s1:
            if ch in count_s1:
                count_s1[ch] += 1
            else:
                count_s1[ch] = 1
        l=0
        n=len(s2)
        for r in range(n):
            ch=s2[r]
            if ch in count_s2:
                count_s2[ch]+=1
            else:
                count_s2[ch]=1
            if (r-l+1)>len(s1):
                count_s2[s2[l]]-=1
                if count_s2[s2[l]]<=0:
                    del count_s2[s2[l]]
                l+=1
            if (r-l+1==len(s1)):
                if count_s1==count_s2:
                    return True
        return False