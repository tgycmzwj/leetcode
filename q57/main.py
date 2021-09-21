# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        if newInterval[0]>intervals[-1][1]:
            return intervals+[newInterval]
        if newInterval[1]<intervals[0][0]:
            return [newInterval]+intervals
        starting=len(intervals)
        for i in range(len(intervals)):
            if intervals[i][1]>=newInterval[0]:
                starting=i
                break
        ending=0
        for i in range(len(intervals)-1,-1,-1):
            if intervals[i][0]<=newInterval[1]:
                ending=i
                break
        results=intervals[:starting]+[[min(intervals[starting][0],newInterval[0]),max(intervals[ending][1],newInterval[1])]]+intervals[ending+1:]
        return results
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    intervals = [[1,5]]
    newInterval = [2,7]
    print(solution.insert(intervals,newInterval))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
