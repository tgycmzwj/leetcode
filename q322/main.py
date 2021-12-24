# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)  #minimal number of coins needed if need dp[i]
        dp[0]=0
        for i in range(1,len(dp)):
            if i in coins:dp[i]=1
            for coin in coins:
                if i-coin>=0:
                    dp[i]=min(dp[i],1+dp[i-coin])

        return dp[-1] if dp[-1]<amount+1 else -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    solution=Solution()
    print(solution.coinChange(coins,amount))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
