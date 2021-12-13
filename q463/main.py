# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        d1,d2=len(grid)+2,len(grid[0])+2
        pad=[[0]*d2 for i in range(d1)]
        for i in range(1,d1-1):
            for j in range(1,d2-1):
                pad[i][j]=grid[i-1][j-1]
        num=0
        for i in range(1,d1-1):
            for j in range(1,d2-1):
                if pad[i][j]==1:
                    num=num+(pad[i-1][j]==0)+(pad[i+1][j]==0)+(pad[i][j-1]==0)+(pad[i][j+1]==0)
        return num







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    solution=Solution()
    print(solution.islandPerimeter(grid))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
