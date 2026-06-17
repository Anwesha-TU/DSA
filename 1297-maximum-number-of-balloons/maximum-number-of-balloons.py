class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        # n=len(str)
        count=Counter(text)
        output=0
        required={'b':1,'a':1,'l':2,'o':2,'n':1}
        while all(count.get(ch, 0) >= required[ch] for ch in required):
            for ch in required:
                count[ch]-=required[ch]
            output+=1
        return output