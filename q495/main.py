# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def findPoisonedDuration_old(self, timeSeries: List[int], duration: int) -> int:
        results=0
        cur_start=0
        cur_end=0
        flag=0
        for i in range(len(timeSeries)):
            if flag==0:
                results=results+(cur_end-cur_start)
                cur_start=timeSeries[i]
                cur_end=timeSeries[i]+duration
                flag=1
            else:
                if timeSeries[i]<=cur_end:
                    cur_end=timeSeries[i]+duration
                else:
                    flag=0
                    results=results+(cur_end-cur_start)
                    cur_start=timeSeries[i]
                    cur_end=timeSeries[i]+duration
        results=results+cur_end-cur_start
        return results

    def findPoisonedDuration(self, t, d):
        res = 0
        if not t: return 0
        for i in range(len(t) - 1):
            res += min(d, t[i + 1] - t[i])
        return res + d



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    timeSeries = [66962,67337,67507,67673,67987,68119,68519,68648,69038,69121,69609,69947,70287,70404,70566,70568,70768,70876,71395,71703,72091,72462,72516,72668,73008,73467,73935]
    duration=5
    solution=Solution()
    print(solution.findPoisonedDuration(timeSeries,duration))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
