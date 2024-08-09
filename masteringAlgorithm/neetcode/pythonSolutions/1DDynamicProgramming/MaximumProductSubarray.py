from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] * nums[i]

            result = max(dp[i], nums[i], result)

        return result

    def maxProductOptimizedSpace(self, nums: List[int]) -> int:
        dp = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            dp= dp * nums[i]

            result = max(dp, nums[i], result)

        return result


solution = Solution()
actual1 = solution.maxProduct([1,2,-3,4])
print(actual1 == 4)
actual2 = solution.maxProduct([-2,-1])
print(actual2 == 2)
