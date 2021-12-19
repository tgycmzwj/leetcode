# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def to_minutes(self,str_time:str):
        h,m=str_time.split(':')
        return int(h)*60+int(m)
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints=sorted(timePoints)
        mindiff=1500
        old_time=self.to_minutes(timePoints[0])
        for i in range(1,len(timePoints)):
            new_time=self.to_minutes(timePoints[i])
            mindiff=min(mindiff,new_time-old_time)
            old_time=new_time
        mindiff=min(mindiff,self.to_minutes(timePoints[0])+1440-old_time)
        return mindiff

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    timePoints = ["23:59","00:00"]
    solution=Solution()
    print(solution.findMinDifference(timePoints))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
