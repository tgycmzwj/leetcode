# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        x = sorted(score, reverse=True)
        d = {}
        for i,j in enumerate(x):
            if i == 0:
                d[j] = "Gold Medal"
            elif i == 1:
                d[j] = "Silver Medal"
            elif i == 2:
                d[j] = "Bronze Medal"
            else:
                d[j] = str(i+1)
        return [d[i] for i in score]
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    score = [10,3,8,9,4]
    solution=Solution()
    print(solution.findRelativeRanks(solution))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
