# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def expand(self,board:List[List[int]])->List[List[int]]:
        m,n=len(board)+2,len(board[0])+2
        new_board=[[0]*n for i in range(m)]
        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i-1][j-1]==1:
                    new_board[i][j]=1
        return new_board
    def counter(self,board:List[List[int]],i,j)->int:
        counter=0
        for k1 in range(i-1,i+2):
            for k2 in range(j-1,j+2):
                if ((k1==i) and (k2==j))==False:
                    if board[k1][k2]==1:
                        counter=counter+1
        return counter

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board) + 2, len(board[0]) + 2
        new_board=self.expand(board)
        for i in range(1,m-1):
            for j in range(1,n-1):
                if self.counter(new_board,i,j)<2:
                    board[i-1][j-1]=0
                elif self.counter(new_board,i,j)==2 and new_board[i][j]==1:
                    board[i-1][j-1]=1
                elif self.counter(new_board,i,j)==3:
                    board[i-1][j-1]=1
                else:
                    board[i-1][j-1]=0
        return board




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    board = [[1, 1], [1, 0]]
    print(solution.gameOfLife(board))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
