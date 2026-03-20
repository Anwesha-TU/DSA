class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        count=Counter(s)
        count2=Counter(t)
        return (count==count2)