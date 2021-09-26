# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums[:] = nums[-k:] + nums[:-k]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution=Solution()
    print(solution.rotate(nums,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
