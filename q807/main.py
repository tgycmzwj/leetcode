# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        # Transpose grid: Interchange rows and columns
        grid_t = zip(*grid)
        # Vertical and horizontal skylines
        sk_v = [max(row) for row in grid]
        sk_h = [max(row) for row in grid_t]
        res = 0
        for i in range(N):      # Rows of original grid
            for j in range(M):  # Columns of original grid
                # The new building cannot be higher than either skylines
                diff = min(sk_h[j], sk_v[i]) - grid[i][j]
                res += diff
        return res

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    solution=Solution()
    print(solution.maxIncreaseKeepingSkyline(grid))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
