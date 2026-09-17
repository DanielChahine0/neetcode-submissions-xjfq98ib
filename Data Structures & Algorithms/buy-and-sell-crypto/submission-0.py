class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxV = 0
        while r<len(prices):
            buy = prices[l]
            sell = prices[r]
            if sell > buy:
                maxV = max(maxV, sell-buy)
            else:
                l=r

            r+=1
        return maxV