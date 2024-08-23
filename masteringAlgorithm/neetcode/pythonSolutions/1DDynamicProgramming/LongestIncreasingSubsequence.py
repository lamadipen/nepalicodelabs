from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


solution = Solution()
actual1 = solution.lengthOfLIS([9,1,4,2,3,3,7]);
print(actual1==4)
actual2 = solution.lengthOfLIS([0,3,1,3,2,3]);
print(actual2==4)
actual3 = solution.lengthOfLIS([1,2,4,3]);
print(actual3==3)