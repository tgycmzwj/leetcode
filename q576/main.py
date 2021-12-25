# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        results=[[[0 for i in range(maxMove)] for col in range(n)] for row in range(m)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        modulo = 10 ** 9 + 7
        for move in range(maxMove):
            for i in range(m):
                for j in range(n):
                    #boundary case: can go out in one single move
                    if move==0:
                        for di in directions:
                            adj_x,adj_y=i+di[0],j+di[1]
                            if not (adj_x>=0 and adj_x<=m-1 and adj_y>=0 and adj_y<=n-1):
                                results[i][j][move]+=1
                    #
                    else:
                        for di in directions:
                            adj_x,adj_y=i+di[0],j+di[1]
                            if adj_x>=0 and adj_x<=m-1 and adj_y>=0 and adj_y<=n-1:
                                results[i][j][move]=results[i][j][move]+results[adj_x][adj_y][move-1]
        return sum(results[startRow][startColumn])%modulo

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    m = 36
    n = 5
    maxMove = 50
    startRow = 15
    startColumn = 3
    solution=Solution()
    print(solution.findPaths(m,n,maxMove,startRow,startColumn))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
