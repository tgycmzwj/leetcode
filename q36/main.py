from typing import List
class Solution:
    def check_cols(self,nums:List[str]):
        if (len(nums)==len(set(nums))):
            return True
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #all rows
        for i in range(len(board)):
            flag=self.check_cols([item for item in board[i] if item!="."])
            if flag==False:
                return False
        #all cols
        for i in range(len(board)):
            flag=self.check_cols([item[i] for item in board if item[i]!="."])
            if flag==False:
                return False
        #all 3*3 cells
        for i in range(len(board)//3):
            for j in range(len(board)//3):
                cur_cell=[item[i*3:i*3+3] for item in board[j*3:j*3+3]]
                flag=self.check_cols([k for sublist in cur_cell for k in sublist if k!="."])
                if flag==False:
                    return False
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    board =[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    print(solution.isValidSudoku(board))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
