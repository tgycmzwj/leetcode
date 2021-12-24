# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3:
            return False
        min_nums = [nums[0]]
        for i in range(1, len(nums)):
            min_nums.append(min(nums[i], min_nums[-1]))
        stack = []
        i = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if (nums[i] > min_nums[i]):  #if treat nums[i] as the mid element, there exists a smaller element
                while (stack and stack[-1] <= min_nums[i]):
                    stack.pop()
                if (stack and min_nums[i] < stack[-1] < nums[i]):
                    return True
                stack.append(nums[i])
        return False


    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,0,-4,-1,-3,-3,-5]
    solution=Solution()
    print(solution.find132pattern(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
