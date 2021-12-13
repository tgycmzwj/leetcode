# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        nums=sorted(nums)
        return max([nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3]])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,3,4]
    solution=Solution()
    print(solution.maximumProduct(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
