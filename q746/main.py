# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*len(cost)
        dp[-1]=cost[-1]
        dp[-2]=cost[-2]
        for i in range(len(dp)-3,-1,-1):
            dp[i]=min(dp[i+1],dp[i+2])+cost[i]
        return dp[0]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cost = [1,100,1,1,1,100,1,1,100,1]
    solution=Solution()
    print(solution.minCostClimbingStairs(cost))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
