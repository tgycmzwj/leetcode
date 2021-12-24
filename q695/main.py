# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = 1
                    grid[row][col] = '#'
                    q=[]
                    q.append((row, col))
                    while q:
                        r,c=q.pop(0)
                        for y,x in directions:
                            nr=r+y
                            nc=c+x
                            if nr<rows and nr>=0 and nc<cols and nc>=0 and grid[nr][nc]==1:
                                area+=1
                                grid[nr][nc]='#'
                                q.append((nr,nc))
                    max_area = max(max_area, area)
        return max_area

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    solution=Solution()
    print(solution.maxAreaOfIsland(grid))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
