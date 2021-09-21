# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max=nums[0]
        max_here_as_last=nums[0]
        for x in range(1,len(nums)):
            max_here_as_last=max(nums[x],max_here_as_last+nums[x])
            cur_max=max(cur_max,max_here_as_last)
        return cur_max



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
