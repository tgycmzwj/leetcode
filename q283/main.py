# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                for j in range(i+1,len(nums)):
                    if nums[j]!=0:
                        nums[i],nums[j]=nums[j],nums[i]
                        break



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    solution=Solution()
    print(solution.moveZeroes(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
