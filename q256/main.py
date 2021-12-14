# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        tot_cost=[[0]*len(costs[0]) for i in range(len(costs))]
        for i in range(len(costs)):
            for j in range(len(costs[0])):
                if i==0:
                    tot_cost[i][j]=costs[i][j]
                else:
                    cand=[tot_cost[i-1][k] for k in range(len(costs[0])) if k!=j]
                    tot_cost[i][j]=min(cand)+costs[i][j]
        return min(tot_cost[-1])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    solution=Solution()
    print(solution.minCost(costs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
