# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    #move the number 1 from its original position and place at the place of the number i.
    #when place i at the position of 1, recursion to (n-2) case
    #when not at the positon of 1, recursion to (n-1) case
    def findDerangement(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(2,n+1):
            dp[i]=((i-1)*(dp[i-1]+dp[i-2]))%1000000007
        return dp[-1]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 2
    solution=Solution()
    solution=Solution()
    print(solution.findDerangement(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
