# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) <= 2: return '/'.join([str(i) for i in nums])
        return str(nums[0]) + '/' + '(' + '/'.join([str(nums[i]) for i in range(1, len(nums))]) + ')'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1000,100,10,2]
    solution=Solution()
    print(solution.optimalDivision(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
