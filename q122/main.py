# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(-1)
        total_profit=0
        holding=0
        i=0
        price_buy=0
        while i<len(prices)-1:
            if holding==0:
                if prices[i+1]>prices[i]:
                    holding=1
                    price_buy=prices[i]
                i=i+1
            else:
                if prices[i+1]<prices[i]:
                    holding=0
                    total_profit=total_profit+prices[i]-price_buy
                    continue
                i=i+1
        return total_profit





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    prices = [1, 2, 3, 4, 5]
    prices = [7, 6, 4, 3, 1]
    solution=Solution()
    print(solution.maxProfit(prices))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
