# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sort=sorted(nums)
        i,j=0,0
        for i in range(len(nums)):
            if nums[i]!=nums_sort[i]:
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j]!=nums_sort[j]:
                break
        return j-i+1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [2,6,4,8,10,9,15]
    solution=Solution()
    print(solution)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
