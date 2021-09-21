# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0,count1,count2=0,0,0
        for i in nums:
            if i==0:
                count0=count0+1
            elif i==1:
                count1=count1+1
            else:
                count2=count2+1
        for i in range(len(nums)):
            if count0>0:
                count0=count0-1
                nums[i]=0
            elif count1>0:
                count1=count1-1
                nums[i]=1
            else:
                count2=count2-1
                nums[i]=2



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [2, 0, 2, 1, 1, 0]
    print(solution.sortColors(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
