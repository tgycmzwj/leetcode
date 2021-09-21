# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        results=[[0]*n for i in range(m)]
        results[-1][-1]=grid[-1][-1]
        for i in range(m-2,-1,-1):
            results[i][-1]=results[i+1][-1]+grid[i][-1]
        for i in range(n-2,-1,-1):
            results[-1][i]=results[-1][i+1]+grid[-1][i]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                results[i][j]=grid[i][j]+min(results[i][j+1],results[i+1][j])
        return results[0][0]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    grid = [[1,2,3],[4,5,6]]
    print(solution.minPathSum(grid))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
