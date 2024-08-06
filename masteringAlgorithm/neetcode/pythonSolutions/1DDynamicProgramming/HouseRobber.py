# https://www.youtube.com/watch?v=VXqUQYGMnQg
from typing import List


class Solution:
    def robDP(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        result = [0] * len(nums)
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            result[i] = max(result[i - 1], result[i - 2] + nums[i])

        return result[len(nums) - 1]


    def robDPOptimized(self, nums: List[int]) -> int:
        rob1,rob2=0,0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

solution = Solution()
actual1= solution.robDP([2,9,8,3,6])
print(actual1 == 16)
actual2 = solution.robDP([1,1,3,3])
print(actual2 == 4)

actual1= solution.robDPOptimized([2,9,8,3,6])
print(actual1 == 16)
actual2 = solution.robDPOptimized([1,1,3,3])
print(actual2 == 4)