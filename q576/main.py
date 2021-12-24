# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        results=[[[0 for i in range(maxMove)] for col in range(n)] for row in range(m)]
        return results[startRow][startColumn][maxMove-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    m = 2
    n = 2
    maxMove = 2
    startRow = 0
    startColumn = 0
    solution=Solution()
    print(solution.findPaths(m,n,maxMove,startRow,startColumn))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
