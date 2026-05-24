class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxx=0
        buy=prices[0]
        for i in range(1, len(prices)):
            # if prices[i] < buy:
            #     buy = prices[i]
            buy=min(buy,prices[i])

            # else:
            maxx = max(maxx, prices[i] - buy)
              
        return maxx