class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        count=Counter(ransomNote)
        count2=Counter(magazine)
        for i in count.keys():
            if (count[i]>count2[i]):
                return False
        return True