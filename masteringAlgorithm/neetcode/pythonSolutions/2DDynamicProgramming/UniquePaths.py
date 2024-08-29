# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for r in range(m - 1):
            temp = [1] * n
            for c in range(n - 2, -1, -1):
                temp[c] = temp[c + 1] + dp[c]
            dp = temp

        return dp[0]
