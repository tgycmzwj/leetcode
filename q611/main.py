# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        counter=0
        #要用最大的作为最外层，因为这样做的是加法
        for side1 in range(len(nums)-1,1,-1):
            side2=0
            side3=side1-1
            while side2<side3:
                if nums[side2]+nums[side3]>nums[side1]:
                    counter=counter+side3-side2
                    side3=side3-1
                else:
                    side2=side2+1
        return counter



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [2,2,3,4]
    solution=Solution()
    print(solution.triangleNumber(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
