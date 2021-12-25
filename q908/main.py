# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        num_min = min(nums)
        num_max = max(nums)
        if num_max - num_min <= 2 * k: return 0
        return num_max - num_min - 2 * k


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,3,6]
    k = 3
    solution=Solution()
    print(solution.smallestRangeI(nums,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
