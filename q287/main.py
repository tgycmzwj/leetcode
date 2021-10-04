# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return (sum(nums)-sum(set(nums)))/(len(nums)-len(set(nums)))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,3,4,2,2]
    solution=Solution()
    print(solution.findDuplicate(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
