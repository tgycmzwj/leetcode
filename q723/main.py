# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m,n=len(board),len(board[0])
        while True:
            stable=True
            crushable = set()
            # 1. check for horizontal crushables
            for x in range(m):
                for y in range(n-2):
                    if board[x][y]==board[x][y+1]==board[x][y+2]!=0:
                        stable=False
                        crushable.update([(x,y),(x,y+1),(x,y+2)])
            # 2. check for vertical crushables
            for x in range(m-2):
                for y in range(n):
                    if board[x][y]==board[x+1][y]==board[x+2][y]!=0:
                        stable=False
                        crushable.update([(x,y),(x+1,y),(x+2,y)])
            # 5. if no candies were crushed, we're done
            if stable:
                return board
            # 3. crush the candies
            for x,y in crushable:
                board[x][y] = 0
            # 4. let the candies "fall"
            for y in range(n):
                offset=0
                for x in range(m-1,-1,-1):  # loop through column backward
                    k=x+offset
                    if (x,y) in crushable:  # this will help us put items at bottom of the board
                        offset+=1
                    else:
                        board[k][y]=board[x][y]  # notice the use of k
                # now that all items have been copied to their right spots, place zero's appropriately at the top of the board
                for x in range(offset):
                    board[x][y]=0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
    solution=Solution()
    print(solution.candyCrush(board))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
