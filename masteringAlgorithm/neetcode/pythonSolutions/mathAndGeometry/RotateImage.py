from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:
            top, bottom = left, right
            for i in range(left, right):
                temp = matrix[top][left + i]

                # bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left to top right
                matrix[top + i][right] = temp

            left += 1
            right -= 1

solution = Solution()
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution.rotate(list1)
print(list1)
print(list1 == [[7,4,1],[8,5,2],[9,6,3]])

list2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution.rotate(list2)
print(list2)
print(list2 == [[7,4,1],[8,5,2],[9,6,3]])
print(list2 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
