# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        top=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>0:
                    top=top+1
        left=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j==0:
                    left=left+grid[i][j]
                else:
                    left=left+max(grid[i][j]-grid[i][j-1],0)
        front=0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if j==0:
                    front=front+grid[j][i]
                else:
                    front=front+max(0,grid[j][i]-grid[j-1][i])
        return 2*(top+front+left)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    grid = [[1,2],[3,4]]
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    grid = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
    solution=Solution()
    print(solution.surfaceArea(grid))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
