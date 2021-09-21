# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def binary_search(self,nums,target):
        left=0
        right=len(nums)-1
        while right>=left:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                return mid
        return left
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums,target)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [1]
    target = 2
    print(solution.searchInsert(nums,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
