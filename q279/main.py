# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution_old:
    def numSquares(self, n: int) -> int:
        dp=[0]*(n+1)
        for i in range(1,len(dp)):
            print('i=',str(i))
            #itself is a perfect square
            if pow(i,0.5)==int(pow(i,0.5)):
                dp[i]=1
                continue
            #search for smaller numbers
            min_perfect=i
            for j in range(1,i):
                if dp[j]+1>=min_perfect:
                    continue
                if pow(i-j,0.5)==int(pow(i-j,0.5)):
                    min_perfect=min(min_perfect,dp[j]+1)
            dp[i]=min_perfect
        return dp[-1]

class Solution(object):
    #directly save everything here
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=9764
    solution=Solution()
    print(solution.numSquares(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
