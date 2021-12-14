# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms=[]
        intervals=sorted(intervals,key=lambda x:x[0])
        for i in range(len(intervals)):
            if i==0:
                rooms.append(intervals[i][1])
            else:
                if intervals[i][0]<rooms[0]:
                    rooms.append(intervals[i][1])
                    rooms=sorted(rooms)
                else:
                    rooms[0]=intervals[i][1]
                    rooms=sorted(rooms)
        return len(rooms)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    solution=Solution()
    print(solution.minMeetingRooms(intervals))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
