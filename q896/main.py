# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sorted_nums=sorted(nums)
        return nums==sorted_nums or nums[::-1]==sorted_nums

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,2,3]
    solution=Solution()
    print(solution.isMonotonic(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
