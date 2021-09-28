# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums)+1)*len(nums)//2-sum(nums)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3,0,1]
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    nums = [0, 1]
    solution=Solution()
    print(solution.missingNumber(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
