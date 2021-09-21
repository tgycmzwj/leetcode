# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        problematic_loc=len(nums)+1
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1]>nums[i]:
                problematic_loc=i
                break
        if problematic_loc<len(nums)+1:
            exchange_loc=len(nums)+1
            for i in range(len(nums)-1,problematic_loc,-1):
                if nums[i]>nums[problematic_loc]:
                    exchange_loc=i
                    break
            temp=nums[problematic_loc]
            nums[problematic_loc]=nums[exchange_loc]
            nums[exchange_loc]=temp
            nums[problematic_loc+1:]=nums[problematic_loc+1:][::-1]

        if problematic_loc==len(nums)+1:
            nums.reverse()
        return nums


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [1,3,2]
    print(solution.nextPermutation(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
