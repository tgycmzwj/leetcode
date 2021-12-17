# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        #horizontal, vertical, diagonal, antidiagonal
        dp=[[[0,0,0,0] for i in range(len(mat[0]))] for j in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    #horizontal
                    if j==0:dp[i][j][0]=1
                    else:dp[i][j][0]=dp[i][j-1][0]+1
                    #vertical
                    if i==0:dp[i][j][1]=1
                    else:dp[i][j][1]=dp[i-1][j][1]+1
                    #diagonal
                    if i==0 or j==0:dp[i][j][2]=1
                    else:dp[i][j][2]=dp[i-1][j-1][2]+1
                    #antidiagonal
                    if i==0 or j==len(mat[0])-1:dp[i][j][3]=1
                    else:dp[i][j][3]=dp[i-1][j+1][3]+1
        return max([max(arr) for eles in dp for arr in eles])




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
    solution=Solution()
    print(solution.longestLine(mat))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
