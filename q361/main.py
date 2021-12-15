# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def maxKilledEnemies_old(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        rows,cols = len(grid),len(grid[0])
        max_count = 0
        for row in range(0, rows):
            for col in range(0, cols):
                if grid[row][col] == '0':
                    max_count = max(max_count, self.killEnemies(row,col,grid,rows,cols))
        return max_count
    def killEnemies(self,row,col,grid,rows,cols):
            enemy_count = 0
            row_ranges = [range(row - 1, -1, -1), range(row + 1, rows, 1)]
            for row_range in row_ranges:
                for r in row_range:
                    if grid[r][col] == 'W':
                        break
                    elif grid[r][col] == 'E':
                        enemy_count += 1
            col_ranges = [range(col - 1, -1, -1), range(col + 1, cols, 1)]
            for col_range in col_ranges:
                for c in col_range:
                    if grid[row][c] == 'W':
                        break
                    elif grid[row][c] == 'E':
                        enemy_count += 1
            return enemy_count
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        l1,l2=len(grid),len(grid[0])
        dp = [[[0, 0, 0, 0] for __ in range(l2)] for _ in range(l1)]
        #left to right
        for i in range(l1):
            runningSum = 0
            for j in range(l2):
                if (grid[i][j] == "E"):
                    runningSum += 1
                elif (grid[i][j] == "W"):
                    runningSum = 0
                else:
                    dp[i][j][0] = runningSum
        #right to left
        for i in range(l1):
            runningSum = 0
            for j in range(l2 - 1, -1, -1):
                if (grid[i][j] == "E"):
                    runningSum += 1
                elif (grid[i][j] == "W"):
                    runningSum = 0
                else:
                    dp[i][j][1] = runningSum
        # top to bottom
        for j in range(l2):
            runningSum = 0
            for i in range(l1):
                if (grid[i][j] == "E"):
                    runningSum += 1
                elif (grid[i][j] == "W"):
                    runningSum = 0
                else:
                    dp[i][j][2] = runningSum
        # bottom to top
        for j in range(l2):
            runningSum = 0
            for i in range(l1 - 1, -1, -1):
                if (grid[i][j] == "E"):
                    runningSum += 1
                elif (grid[i][j] == "W"):
                    runningSum = 0
                else:
                    dp[i][j][3] = runningSum
        result=0
        for i in range(l1):
            for j in range(l2):
                if grid[i][j]=='0':
                    result=max(result,sum(dp[i][j]))
        return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
    solution=Solution()
    print(solution.maxKilledEnemies(grid))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
