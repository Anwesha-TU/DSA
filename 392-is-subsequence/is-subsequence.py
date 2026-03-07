class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        index=[]
        start=0
        for char in s:
            if char not in t:
                return False
        for char in s:
                pos=(t.find(char,start))
                index.append(pos)
                start = pos + 1
                for i in range(1, len(index)):
                    if (len(index)>1):
                        if index[i]<index[i-1]:
                         return False
                    
        return True
