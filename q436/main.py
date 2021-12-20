# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def bin_search(self, arr, v):
        low,high=0,len(arr)-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]<v:
                low=mid+1
            else:
                high=mid-1
        return low
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic={} #starting point, pos
        starts=[]
        for i in range(len(intervals)):
            dic[intervals[i][0]]=i
            starts.append(intervals[i][0])
        starts.sort()
        results=[-1]*len(intervals)
        for i in range(len(intervals)):
            if not (self.bin_search(starts,intervals[i][1])==len(intervals)):
                results[i]=dic[starts[self.bin_search(starts,intervals[i][1])]]
        return results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    intervals = [[1,4],[2,3],[3,4],[5,9],[4,6],[11,13],[7,12]]
    solution=Solution()
    print(solution.findRightInterval(intervals))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
