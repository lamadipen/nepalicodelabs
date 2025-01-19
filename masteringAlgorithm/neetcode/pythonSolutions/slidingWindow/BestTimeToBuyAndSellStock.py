#Best Time to Buy and Sell Stock
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for price in prices:
            if buy > price:
                buy = price
            else:
                profit = price - buy
                maxProfit = max(profit,maxProfit)
        return maxProfit

solution = Solution()
result1 = solution.maxProfit([7,1,5,3,6,4])
print(result1)
result2 = solution.maxProfit([7,6,4,3,1])
print(result2)
