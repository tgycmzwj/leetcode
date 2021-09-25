# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def find_break_point(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return left
        median = (left + right) // 2
        if nums[median] < nums[0]:
            return self.find_break_point(nums, left, median)
        else:
            return self.find_break_point(nums, median + 1, right)
    def findMin(self, nums: List[int]) -> int:
        index=self.find_break_point(nums,0,len(nums))
        if index==len(nums):
            return nums[0]
        return nums[index]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3,4,5,1,2]
    #nums = [4, 5, 6, 7, 0, 1, 2]
    #nums = [11, 13, 15, 17]
    solution=Solution()
    print(solution.findMin(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
