# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
            else:
                return len(nums)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    solution=Solution()
    print(solution.removeElement(nums,val))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
