# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        num_paths=[[0]*n for i in range(m)]
        #generate values for last row and last col
        for i in range(len(num_paths)):
            num_paths[i][-1] = 1
        for i in range(len(num_paths[0])):
            num_paths[-1][i] = 1
        #modification for obstacles
        diag_row=-1
        diag_col=-1
        for i in range(n-1,-1,-1):
            if obstacleGrid[-1][i]==1:
                diag_row=i
                break
        for i in range(m-1,-1,-1):
            if obstacleGrid[i][-1]==1:
                diag_col=i
                break
        for i in range(0,diag_col+1):
            num_paths[i][-1]=0
        for i in range(0,diag_row+1):
            num_paths[-1][i]=0
        #dynamic programming part
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if obstacleGrid[i][j]!=1:
                    num_paths[i][j]=num_paths[i+1][j]+num_paths[i][j+1]
        return num_paths[0][0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obstacleGrid = [[0,1],[0,0]]
    solution=Solution()
    print(solution.uniquePathsWithObstacles(obstacleGrid))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
