# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n==0:
            return 0
        if n==1:
            return k
        if n==2:
            return k*k
        dp=[0,k,k*k]+[0]*(n-2)
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+dp[i-2])*(k-1)  #not
        return dp[-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 7
    k = 2
    solution=Solution()
    print(solution.numWays(n,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
