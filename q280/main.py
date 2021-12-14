# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new=sorted(nums)
        for i in range(1,len(new)-1,2):
            new[i],new[i+1]=new[i+1],new[i]
        for i in range(len(nums)):
            nums[i]=new[i]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3,5,2,1,6,4]
    solution=Solution()
    print(solution.wiggleSort(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
