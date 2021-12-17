# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return sum(nums[::2])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,4,3,2]
    solution=Solution()
    print(solution.arrayPairSum(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
