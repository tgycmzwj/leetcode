# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution=Solution()
    print(solution.transpose(matrix))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
