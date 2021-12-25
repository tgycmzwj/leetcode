# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum([1 for i in grid for j in i if j != 0]+[max(i) for i in grid]+[max(i) for i in list(zip(*grid))])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    grid = [[1,2],[3,4]]
    solution=Solution()
    print(solution.projectionArea(grid))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
