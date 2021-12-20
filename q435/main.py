# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x:x[-1])
        counter=1
        end = intervals[0][-1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>=end:
                end=intervals[i][1]
                counter=counter+1
        return len(intervals)-counter
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    solution=Solution()
    print(solution.eraseOverlapIntervals(intervals))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
