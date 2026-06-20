class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        import re
        s = re.sub(r'[^a-z0-9]', '', s)
        n=len(s)
        l=0
        r=n-1
        while l<r:
            if s[l]!=s[r]:
               return False
            l+=1
            r-=1
        return True