class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        n=len(jewels)
        m=len(stones)
        count=Counter(stones)
        sum=0
        for i in count.keys():
            if i in jewels:
                sum+=count[i]
        return sum