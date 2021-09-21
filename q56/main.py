# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]
        sorted_intervals=sorted(intervals,key=lambda x:x[0])
        waiting_interval = sorted_intervals.pop(0)
        while len(sorted_intervals)!=0:
            cur_interval=sorted_intervals.pop(0)
            if cur_interval[0]<=waiting_interval[1]:
                waiting_interval[1]=max(waiting_interval[1],cur_interval[1])
            else:
                result.append(waiting_interval)
                waiting_interval=cur_interval
        result.append(waiting_interval)
        return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    intervals = [[1,3],[2,6],[8,10],[10,18]]
    print(solution.merge(intervals))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
