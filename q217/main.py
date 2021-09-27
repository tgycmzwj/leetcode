# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums))!=len(nums):
            return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    solution=Solution()
    print(solution.containsDuplicate(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
