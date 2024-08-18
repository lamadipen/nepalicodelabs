#https://leetcode.com/problems/coin-change/description/

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount +1)
        dp[0] =0

        for amt in range(amount+1):
            for coin in coins:
                if (amt - coin) >=0:
                    dp[amt] = min(dp[amt], dp[amt-coin] +1)

        return -1 if dp[amount] == float('inf') else dp[amount]


solution = Solution()
actual1 = solution.coinChange([1,5,10],12)
print(actual1 == 3)
actual2 = solution.coinChange([3],2)
print(actual2 == -1)
actual3 = solution.coinChange([1],0)
print(actual3 == 0)