class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # clean version
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP