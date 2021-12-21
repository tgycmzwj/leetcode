# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        i=1
        cur_max=1
        cur_count=1
        while i!=len(nums):
            if nums[i]-nums[i-1]>0:
                cur_count=cur_count+1
            else:
                cur_max=max(cur_max,cur_count)
                cur_count=1
            i=i+1
        cur_max=max(cur_max,cur_count)
        return cur_max

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums=[1,3,5,7]
    solution=Solution()
    print(solution.findLengthOfLCIS(nums))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
