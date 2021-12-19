# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,1,2,3,3,4,4,8,8]
    solution=Solution()
    print(solution.singleNonDuplicate(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
