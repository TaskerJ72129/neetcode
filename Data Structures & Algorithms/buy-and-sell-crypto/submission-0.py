class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMin = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < currentMin:
                currentMin = prices[i]
            else:
                profit = prices[i] - currentMin
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit