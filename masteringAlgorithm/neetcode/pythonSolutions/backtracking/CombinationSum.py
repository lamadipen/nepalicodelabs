from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, current, total):
            if total == target:
                result.append(current.copy())
                return
            if total > target or index >= len(candidates):
                return
            current.append(candidates[index])
            dfs(index, current, total + candidates[index])
            current.pop()
            dfs(index + 1, current, total)

        dfs(0, [], 0)
        return result

solution = Solution()
actual1 = solution.combinationSum( [2,3,6,7], 7)
print(actual1 == [[2,2,3],[7]])
actual2 = solution.combinationSum( [2,3,5], 8)
print(actual2 == [[2,2,2,2],[2,3,3],[3,5]])
actual3 = solution.combinationSum( [2], 1)
print(actual3 == [])