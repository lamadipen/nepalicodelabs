from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:

            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result

solution = Solution()
actual1 = solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(actual1)
print(actual1 == [1,2,3,6,9,8,7,4,5])

actual2 = solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(actual2)
print(actual2 == [1,2,3,6,9,8,7,4,5])
print(actual2 ==  [1,2,3,4,8,12,11,10,9,5,6,7])

