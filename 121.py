class Solution:
    def maxProfit(self, prices: list) -> int:
        min_price = 10000
        profit = 0
        
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif (prices[i] - min_price) > profit:
                profit = prices[i] - min_price
                
        return profit
        