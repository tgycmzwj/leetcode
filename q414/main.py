# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=sorted(list(set(nums)),reverse=True)
        return nums[2] if len(nums)>=3 else nums[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3,2,1]
    solution=Solution()
    print(solution.thirdMax(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
