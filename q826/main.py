# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
from collections import defaultdict
import bisect
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        #remove low efficiency tasks
        profits = defaultdict(int)
        for d, p in zip(difficulty, profit):
            if profits[d] < p:
                profits[d] = p
        difficulty = sorted(profits.keys())
        maxProfit = [profits[difficulty[0]]]
        for i in range(1, len(difficulty)):
            maxProfit.append(max(maxProfit[-1], profits[difficulty[i]]))

        ans = 0
        for w in worker:
            i = bisect.bisect(difficulty, w)
            if i > 0:
                ans += maxProfit[i-1]
        return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    difficulty = [2,4,6,8,10]
    profit = [10,20,30,40,50]
    worker = [4,5,6,7]
    solution=Solution()
    print(solution.maxProfitAssignment(difficulty,profit,worker))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
