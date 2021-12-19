# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cumsum=[0]*len(nums)
        cumsum[0]=nums[0]
        for i in range(1,len(nums)):
            cumsum[i]=cumsum[i-1]+nums[i]
        if cumsum[-1]-nums[0]==0:
            return 0
        for i in range(1,len(nums)-1):
            if cumsum[i-1]==cumsum[-1]-cumsum[i]:
                return i
        if cumsum[-2]==0:
            return len(cumsum)-1
        return -1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    solution=Solution()
    print(solution.pivotIndex(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
