# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums))*3-sum(nums))//2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [2,2,3,2]
    solution=Solution()
    print(solution.singleNumber(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
