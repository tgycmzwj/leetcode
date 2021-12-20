# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0]*(n+1) for i in range(m+1)] #dp[i][j] largest subset with i 0s,j 1s
        for i in range(len(strs)):
            c0,c1=strs[i].count('0'),strs[i].count('1')
            for row in range(m,-1,-1):
                for col in range(n,-1,-1):
                    if row-c0>=0 and col-c1>=0:
                        dp[row][col]=max(dp[row][col],dp[row-c0][col-c1]+1)
        return max([max(row) for row in dp])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    strs = ["10","0001","111001","1","0"]
    m = 5
    n = 3
    solution=Solution()
    print(solution.findMaxForm(strs,m,n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
