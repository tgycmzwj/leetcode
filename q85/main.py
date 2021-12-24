# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if sum([sum([int(j) for j in i]) for i in matrix])==len(matrix)*len(matrix[0]):return len(matrix)*len(matrix[0])
        height_matrix=[[0]*len(matrix[0]) for i in range(len(matrix))]
        width_matrix=[[0]*len(matrix[0]) for i in range(len(matrix))]
        #height matrix
        cur_max=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0:
                    height_matrix[i][j]=1 if matrix[i][j]=='1' else 0
                else:
                    if matrix[i][j]=='0':
                        height_matrix[i][j]=0
                    else:
                        height_matrix[i][j]=height_matrix[i-1][j]+1
                if j==0:
                    width_matrix[i][j]=1 if matrix[i][j]=='1' else 0
                else:
                    if matrix[i][j]=='0':
                        width_matrix[i][j]=0
                    else:
                        width_matrix[i][j]=width_matrix[i][j-1]+1
                for k in range(height_matrix[i][j]):
                    actual_width=min([width_matrix[i-t][j] for t in range(k+1)])
                    cur_max=max(cur_max,(k+1)*actual_width)
        return cur_max


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    solution=Solution()
    print(solution.maximalRectangle(matrix))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
