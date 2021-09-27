# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    # def padding(self,matrix:List[List[str]])->List[List[str]]:
    #     row,col=len(matrix)+2,len(matrix[0])+2
    #     new_matrix=[['0']*col for i in range(row)]
    #     for i in range(1,row-1):
    #         for j in range(1,col-1):
    #             if matrix[i-1][j-1]=='1':
    #                 new_matrix[i][j]='1'
    #     return new_matrix
    def maximalSquare_slow(self, matrix: List[List[str]]) -> int:
        row,col=len(matrix),len(matrix[0])
        collections=set([matrix[i][j] for i in range(row) for j in range(col)])
        if '1' not in collections:
            return 0
        if min(row,col)==1:
            return 1
        max_size=1
        for cur_size in range(2,min(row,col)+1):
            if cur_size>max_size+1:
                break
            for starting_i in range(row-cur_size+1):
                for starting_j in range(col-cur_size+1):
                    if '0' not in set([matrix[i][j] for i in range(starting_i,starting_i+cur_size) for j in range(starting_j,starting_j+cur_size)]):
                        max_size=cur_size
                        break
        return max_size**2

    def maximalSquare(self,matrix:List[List[str]])->int:
        row,col=len(matrix),len(matrix[0])
        matrix_dp=[[0]*col for i in range(row)]
        matrix_dp[0][0]=1 if matrix[0][0]=='1' else 0
        #upper side
        for i in range(1,col):
            matrix_dp[0][i]=1 if (matrix[0][i]=='1') else 0
        #left side
        for i in range(1,row):
            matrix_dp[i][0]=1 if (matrix[i][0]=='1') else 0

        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]=='0':
                    matrix_dp[i][j]=0
                else:
                    matrix_dp[i][j]=min(matrix_dp[i-1][j-1]+1,matrix_dp[i-1][j]+1,matrix_dp[i][j-1]+1)
                    #look at the left cell
                    for k in range(matrix_dp[i][j-1]):
                        if matrix[i-k][j]=='0':
                            matrix_dp[i][j]=k
                    #look at the upper cell
                    for k in range(matrix_dp[i-1][j]):
                        if matrix[i][j-k]=='0':
                            matrix_dp[i][j]=min(matrix_dp[i][j],k)

        return max([max(i) for i in matrix_dp])**2




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    #matrix=[["1","1"],["1","1"]]
    #matrix = [["0"]]
    #matrix = [["0", "1"], ["1", "0"]]
    #matrix=[["0", "0", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"], ["0", "1", "1", "1"], ["0", "1", "1", "1"]]
    solution=Solution()
    print(solution.maximalSquare(matrix))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
