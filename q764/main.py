# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        m=len(mines)
        if m==n*n: return 0
        seen=set()
        for i,j in mines:
            seen.add((i,j))
        ans=1
        #(left,up,right,down)
        dp=[[[0,0,0,0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if (i,j) not in seen:
                    dp[i][j][0]=(dp[i][j-1][0]+1) if j-1>=0 else 1
                    dp[i][j][1]=(dp[i-1][j][1]+1) if i-1>=0 else 1
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (i,j) not in seen:
                    dp[i][j][2]=(dp[i][j+1][2]+1) if j+1<n else 1
                    dp[i][j][3]=(dp[i+1][j][3]+1) if i+1<n else 1
                ans=max(ans,min(dp[i][j]))
        return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 5
    mines = [[4,2]]
    solution=Solution()
    print(solution.orderOfLargestPlusSign(n,mines))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
