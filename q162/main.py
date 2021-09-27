# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            return 1
        if nums[0]>nums[1]:
            return 0
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        if nums[-1]>nums[-2]:
            return len(nums)-1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,3,1]
    solution=Solution()
    print(solution.findPeakElement(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
