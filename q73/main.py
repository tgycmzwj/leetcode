# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j]==0):
                    #modify current row
                    for l in range(len(matrix[0])):
                        if matrix[i][l]!=0:
                            matrix[i][l]=''
                    #modify current col
                    for l in range(len(matrix)):
                        if matrix[l][j]!=0:
                            matrix[l][j]=''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='':
                    matrix[i][j]=0
        return matrix


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(solution.setZeroes(matrix))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
