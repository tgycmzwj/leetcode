# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    solution=Solution()
    print(solution.search(nums,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
