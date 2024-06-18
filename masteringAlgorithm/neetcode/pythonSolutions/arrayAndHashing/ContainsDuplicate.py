# https://leetcode.com/problems/contains-duplicate/description/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False

solution = Solution()
actual1=solution.containsDuplicate([1,2,3,1])
print(actual1==True)
actual2=solution.containsDuplicate([1,2,3,4])
print(actual2==False)
actual3=solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(actual3==True)