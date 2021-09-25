# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        borderO=[]
        #collect all boarder 'O
        for i in range(len(board)):
            cur_row=[]
            for j in range(len(board[0])):
                if ((i==0) or (j==0) or (i==len(board)-1) or (j==len(board[0])-1)):
                    if board[i][j]=='O':
                        cur_row.append((i,j))
            borderO.append(cur_row)


        flag=1
        iteration=0
        while flag==1:
            flag=0
            iteration=iteration+1
            print(iteration)
        #scan from top to bottom
            for i in range(1,len(board)-1):
            #scan from left to right
                for j in range(1,len(board[0])-1):
                    if board[i][j]=='O':
                        if (i,j-1) in borderO[i] or (i,j+1) in borderO[i] or (i-1,j) in borderO[i-1] or (i+1,j) in borderO[i+1]:
                            if (i,j) not in borderO[i]:
                                borderO[i].append((i,j))
                                flag=1
                for j in range(len(board[0])-2,0,-1):
                    if board[i][j] == 'O':
                        if (i,j-1) in borderO[i] or (i,j+1) in borderO[i] or (i-1,j) in borderO[i-1] or (i+1,j) in borderO[i+1]:
                            if (i,j) not in borderO[i]:
                                borderO[i].append((i,j))
                                flag=1
        #scan from bottom to top
            for i in range(len(board)-2,0,-1):
            #scan from left to right
                for j in range(1,len(board[0])-1):
                    if board[i][j] == 'O':
                        if (i,j-1) in borderO[i] or (i,j+1) in borderO[i] or (i-1,j) in borderO[i-1] or (i+1,j) in borderO[i+1]:
                            if (i,j) not in borderO[i]:
                                borderO[i].append((i,j))
                                flag=1
                for j in range(len(board[0])-2,0,-1):
                    if board[i][j] == 'O':
                        if (i,j-1) in borderO[i] or (i,j+1) in borderO[i] or [i-1,j] in borderO[i-1] or (i+1,j) in borderO[i+1]:
                            if (i,j) not in borderO[i]:
                                borderO[i].append((i,j))
                                flag=1

        #modify value
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O' and (i,j) not in borderO[i]:
                    board[i][j]='X'
        return board




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = [["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","O","O","O","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","O","O","X","O","X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","X","O","X","O","X","O","O","O","X","X","X","X","X","X"],["X","X","X","X","X","O","X","O","O","O","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]]
    solution=Solution()
    print(solution.solve(board))
    print([["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","O","O","O","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","O","O","X","O","X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","X","O","X","O","X","O","O","O","X","X","X","X","X","X"],["X","X","X","X","X","O","X","O","O","O","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
