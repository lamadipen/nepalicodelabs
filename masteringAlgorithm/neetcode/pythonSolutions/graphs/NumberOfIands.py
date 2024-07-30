from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        maxRow = len(grid)
        maxCol = len(grid[0])
        ilands =0

        def bfs(currentRow, currentCol):
            queue = deque()
            queue.append((currentRow, currentCol))

            directions = [[-1,0],[0,-1],[1,0],[0,1]]

            while queue:
                r , c = queue.popleft()

                for x,y in directions:
                    if x in range(maxRow) and y in range(maxCol) and (x+r, c+y) not in visited and grid[r + x][c + y] == '1':
                        visited.add((r+x,y+c))
                        queue.append((r+x,y+c))



        for row in range(maxRow):
            for col in range(maxCol):
                if grid[row][col] == '1' and (row, col) not in visited:
                    visited.add((row,col))
                    ilands+=1
                    bfs(row, col)
        return ilands


solution=Solution()
actual1=solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(actual1)


