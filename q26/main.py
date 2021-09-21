# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = (list(set(nums)))
        nums.sort()
        return len(nums)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(nums))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
