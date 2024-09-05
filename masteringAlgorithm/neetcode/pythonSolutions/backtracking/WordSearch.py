#https://leetcode.com/problems/word-search/description/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(row,col, index):
            if index == len(word):
                return True
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or word[index] != board[row][col] or (row, col) in visited:
                return False
            visited.add((row,col))
            result = dfs(row-1,col,index+1) or dfs(row+1,col,index+1) or dfs(row,col-1,index+1) or dfs(row, col+1 , index +1)
            visited.remove((row,col))
            return result

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False

solution = Solution()
acutal1= solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
print(acutal1)
acutal2= solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
print(acutal2)
acutal3= solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
print(acutal3)