
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size=len(matrix)
        n = size - 1
        for i in range(size // 2):
            for j in range(i, n - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j][i]
                matrix[n - j][i] = matrix[n - i][n - j]
                matrix[n - i][n - j] = matrix[j][n - i]
                matrix[j][n - i] = temp



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.rotate(matrix))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
