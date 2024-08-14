# Question
# Good Solution: https://www.youtube.com/watch?v=FEkZxCl_-ik

class Solution:
    def numDecodings(self, s: str) -> int:
        dp= [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2,(len(s) +1)):
            single = int(s[i-1:i])
            double = int(s[i-2:i])

            if single >= 1:
                dp[i] += dp[i-1]

            if 10 <= double <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]


solution = Solution()
actual1 = solution.numDecodings("12")
print(actual1 == 2)
actual2 = solution.numDecodings("01")
print(actual2 == 0)
actual3 = solution.numDecodings("122016")
print(actual3 == 4)
