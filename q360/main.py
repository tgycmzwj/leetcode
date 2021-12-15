# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        for i in range(len(nums)):
            nums[i]=a*nums[i]*nums[i]+b*nums[i]+c
        return sorted(nums)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [-4,-2,2,4]
    a = 1
    b = 3
    c = 5
    solution=Solution()
    print(solution.sortTransformedArray(nums,a,b,c))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
