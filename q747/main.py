# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums_copy = sorted(nums)
        if nums_copy[-1] >= nums_copy[-2] * 2:
            return nums.index(nums_copy[-1])
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3,6,1,0]
    solution=Solution()
    print(solution.dominantIndex(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
