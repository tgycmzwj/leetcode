# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,5,1,1,6,4]
    solution=Solution()
    print(solution.wiggleSort(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
