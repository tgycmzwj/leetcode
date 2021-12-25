# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        i=1
        while i<len(nums):
            if nums[i]<nums[i-1]:
                nums[i-1],nums[i]=nums[i],nums[i-1]
                i=i+2
            else:
                i=i+1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return False
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,0]
    solution=Solution()
    print(solution.isIdealPermutation(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
