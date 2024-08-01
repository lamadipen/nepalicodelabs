# https://www.youtube.com/watch?v=UUaMrNOvSqg
#
class Solution:
    def climbStairsDPWithArray(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]

    def climbStairsDPWithVar(self, n: int) -> int:
        if n <= 3:
            return n
        s1, s2 = 1, 1

        while n - 1 > 0:
            temp = s1 + s2
            s1 = s2
            s2 = temp
            n -= 1

        return s2
