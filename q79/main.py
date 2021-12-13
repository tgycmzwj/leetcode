# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def dfs(self,board,word,i,j):
        if ((i<0) or (j<0) or (i>len(board)-1) or (j>len(board[0])-1)):
            return False
        if (len(word)==1):
            if board[i][j]==word[0]:
                return True
            return False
        if board[i][j]==word[0]:
            temp=board[i][j]
            board[i][j]='NA'
            if self.dfs(board,word[1:],i+1,j):
                return True
            if self.dfs(board,word[1:],i-1,j):
                return True
            if self.dfs(board,word[1:],i,j-1):
                return True
            if self.dfs(board,word[1:],i,j+1):
                return True
            board[i][j]=temp

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        for i in range(rows):
            for j in range(cols):
                if self.dfs(board,word,i,j):
                    return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "CBCB"
    solution=Solution()
    print(solution.exist(board,word))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
