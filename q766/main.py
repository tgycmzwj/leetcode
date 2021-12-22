# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    solution=Solution()
    print(solution.isToeplitzMatrix(matrix))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
