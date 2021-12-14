# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals)<=1:
            return True
        intervals=sorted(intervals,key=lambda x:x[0])
        for i in range(len(intervals)-1):
            if intervals[i+1][0]<intervals[i][1]:
                return False
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    intervals = [[0,30],[5,10],[15,20]]
    solution=Solution()
    print(solution.canAttendMeetings(intervals))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
