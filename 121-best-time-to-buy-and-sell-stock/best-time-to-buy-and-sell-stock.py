class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxx=0
        buy=prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit=prices[i]-buy
                if (profit>maxx):
                    maxx=profit
              
        return maxx