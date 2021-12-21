# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start=-1
        end=-1
        flag=0
        intervals=[]
        for i in range(len(nums)):
            if flag==0:
                if nums[i]==1:
                    start=i
                    flag=1
            if flag==1:
                if nums[i]==0:
                    end=i
                    intervals.append([start,end])
                    flag=0
        if flag==1:
            intervals.append([start,len(nums)])
        if len(intervals)==0:return 1
        if len(intervals)==1 and intervals[0][0]==0 and intervals[0][1]==len(nums):return intervals[0][1]-intervals[0][0]
        cur_max=max(intervals[0][1]-intervals[0][0]+1,intervals[-1][1]-intervals[-1][0]+1)
        for i in range(1,len(intervals)):
            if intervals[i][0]-intervals[i-1][1]==1:
                cur_max=max(cur_max,intervals[i][1]-intervals[i-1][0])
            else:
                cur_max=max(cur_max,intervals[i][1]-intervals[i][0]+1)
        return cur_max

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1]
    solution=Solution()
    print(solution.findMaxConsecutiveOnes(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
