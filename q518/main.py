# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def change_slow(self, amount: int, coins: List[int]) -> int:
        #dp[i]---number of exchange method for i+1 amount
        if amount==0:
            return 1
        dp=[[] for i in range(amount)]
        for i in range(amount):
            for coin in coins:
                if (i+1)-coin==0:
                    dp[i].append([coin])
                if (i+1)-coin>0:
                    for method in dp[i-coin]:
                        new=method.copy()+[coin]
                        new=sorted(new)
                        if new not in dp[i]:
                            dp[i].append(new)
        return len(dp[-1])
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[1]+[0 for i in range(amount)]
        #only use coins before cur_coin
        for cur_coin in coins:
            for small_amount in range(cur_coin,amount+1):
                dp[small_amount]+=dp[small_amount-cur_coin]
        return dp[amount]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    amount = 5
    coins = [1,2,5]
    # amount = 3
    # coins = [2]
    # amount = 10
    # coins = [10]
    # amount=0
    # coins=[7]
    # amount=500
    # coins=[1,2,5]
    solution=Solution()
    print(solution.change(amount,coins))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
