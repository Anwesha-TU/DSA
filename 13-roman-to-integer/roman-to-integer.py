class Solution:
    def romanToInt(self, s: str) -> int:
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        summ=0
        n=len(s)
        for i in range(0,n):
            if (i<n-1) and (dict[s[i]]<dict[s[i+1]]):
                summ-=dict[s[i]]
                # i+=2
            else:
                summ+=dict[s[i]]
                i+=1
        return summ