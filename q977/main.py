# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=[i**2 for i in nums]
        return sorted(nums)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    solution=Solution()
    print(solution.sortedSquares(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
