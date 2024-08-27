from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        leftTop = False
        ROW = len(matrix)
        COL = len(matrix[0])

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    if r == 0 and c == 0:
                        leftTop = True
                    else:
                        matrix[0][c] = 0

                    matrix[r][0] = 0

        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for c in range(COL):
                matrix[0][c] = 0

        if leftTop:
            for r in range(ROW):
                matrix[r][0] = 0



solution = Solution()
list1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(list1)
print(list1)
print(list1 == [[1,0,1],[0,0,0],[1,0,1]])
