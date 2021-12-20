# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def merge(self,intervals:List[List[int]])->List[List[int]]:
        results=[]
        sorted_intervals=sorted(intervals,key=lambda x:x[0])
        waiting_interval=sorted_intervals.pop(0)
        while len(sorted_intervals)!=0:
            cur_interval=sorted_intervals.pop(0)
            if cur_interval[0]<=waiting_interval[1]:
                waiting_interval[1]=max(waiting_interval[1],cur_interval[1])
            else:
                results.append(waiting_interval)
                waiting_interval=cur_interval
        results.append(waiting_interval)
        return results
    def complement(self,intervals:List[List[int]],pre)->List[List[int]]:
        results=[]
        if len(intervals)==0:
            return [[0,1e9+1]]
        if intervals[0][0]>0:
            results.append([0,intervals[0][0]-pre])
        for i in range(1,len(intervals)):
            if intervals[i][0]-pre>=intervals[i-1][1]+pre:
                results.append([intervals[i-1][1]+pre,intervals[i][0]-pre])
        results.append([intervals[-1][1]+pre,1e9+1])
        return results
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        comp1=self.complement(firstList,0.01)
        comp2=self.complement(secondList,0.01)
        merged=comp1+comp2
        merged=self.merge(merged)
        merged=self.complement(merged[:len(merged)],0.001)[:-1]
        merged=[[round(i[0]),round(i[1])] for i in merged]
        return merged

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    firstList = [[1, 3], [5, 9]]
    secondList = []
    # firstList = []
    # secondList = [[4, 8], [10, 12]]
    # firstList = [[1, 7]]
    # secondList = [[3, 10]]
    # firstList=[[20, 31], [32, 35]]
    # secondList=[[22, 24], [30, 32], [37, 40]]
    solution=Solution()
    print(solution.intervalIntersection(firstList,secondList))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
