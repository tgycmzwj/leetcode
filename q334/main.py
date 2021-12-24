# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        global_min=max(nums)+1
        min1,min2=global_min,global_min
        for i in range(len(nums)):
            if nums[i]>min1 and nums[i]>min2:
                return True
            if nums[i]>min1:
                min2=min(min2,nums[i])
            min1=min(min1,nums[i])
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,3,4,5]
    solution=Solution()
    print(solution.increasingTriplet(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
