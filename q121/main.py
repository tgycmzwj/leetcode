# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_calculator=[0]*len(prices)
        max_calculator[-1]=prices[-1]
        for i in range(len(prices)-2,-1,-1):
            max_calculator[i]=max(max_calculator[i+1],prices[i])
        return max(max([max_calculator[i]-prices[i] for i in range(len(max_calculator))]),0)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    prices=[7, 6, 4, 3, 1]
    solution=Solution()
    print(solution.maxProfit(prices))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
