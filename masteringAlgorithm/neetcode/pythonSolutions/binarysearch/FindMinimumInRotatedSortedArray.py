#Find Minimum in Rotated Sorted Array
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1

        while left < right:
            mid = (left + right) //2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]



solution = Solution()
result1 = solution.findMin([3,4,5,1,2])
print(result1)
print(result1 == 1)
result2 = solution.findMin([4,5,6,7,0,1,2])
print(result2)
print(result2 == 0)
result3 = solution.findMin([11,13,15,17])
print(result3)
print(result3 == 11)