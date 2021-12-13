# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        results=set([i for i in range(1,len(nums)+1)])
        nums=set(nums)
        return list(results-nums)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    solution=Solution()
    print(solution.findDisappearedNumbers(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
