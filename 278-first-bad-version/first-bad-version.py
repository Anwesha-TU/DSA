# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if (n==1):
            return 1
        l=1
        r=n
        while (l<=r):
            m=(l+r)//2
            if (isBadVersion(m)==True):
                ans=m
                r=m-1
            else:
                l=m+1
        return ans