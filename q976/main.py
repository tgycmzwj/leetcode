# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i=0
        while i+2<len(nums):
            if nums[i]<nums[i+1]+nums[i+2]:
                return sum(nums[i:i+3])
            else:
                i+=1
        return 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [2,1,2]
    solution=Solution()
    print(solution.largestPerimeter(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
