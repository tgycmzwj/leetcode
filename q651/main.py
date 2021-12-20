# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def maxA(self, n: int) -> int:
        dp=[i for i in range(n+1)]
        for i in range(0,n-2):
            for j in range(i+3,n+1):
                dp[j]=max(dp[j],(j-i-1)*dp[i])
        return dp[-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=10
    solution=Solution()
    print(solution.maxA(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
