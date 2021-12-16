# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def profit(self,price:List[int])->int:
        if len(price)<2:
            return 0
        dpp=[0]*len(price)
        for i in range(len(price)-1):
            dpp[i]=max(max(price[i+1:])-price[i],0)
        return max(dpp)

    def maxProfit(self,prices:List[int])->int:
        dp=[0]*len(prices)
        for i in range(1,len(prices)):
            pft1=max(prices[i]-min(prices[:i]),0)
            pft2=self.profit(prices[i+1:])
            dp[i]=pft1+pft2
        return max(dp)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prices=[3,3,5,0,0,3,1,4]
    solution=Solution()
    print(solution.maxProfit(prices))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
