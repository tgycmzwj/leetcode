# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, res = [], [-1] * len(nums) #stack: positions that we haven't find a next greater element yet
        for i, num in enumerate(nums):  # 2
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(i)
        for i, num in enumerate(nums):  # 3
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
        return res

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,3,3,4,2,3]
    solution=Solution()
    print(solution.nextGreaterElements(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
