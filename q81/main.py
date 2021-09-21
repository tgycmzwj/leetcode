# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def find_break_point(self, nums: List[int], left: int, right: int) ->int:
        if left==right:
            return left
        median=(left+right)//2
        if nums[median]<nums[0]:
            return self.find_break_point(nums,left,median)
        else:
            return self.find_break_point(nums,median+1,right)
    def binary_search(self,nums:List[int],target:int,left,right)->int:
        if left>=right:
            if left<=len(nums)-1:
                if nums[left]==target:
                    return left
                if nums[right]==target:
                    return right
            return -1
        else:
            median=(left+right)//2
            if nums[median]==target:
                return median
            elif nums[median]>target:
                return self.binary_search(nums,target,left,median-1)
            else:
                return self.binary_search(nums,target,median+1,right)
    def remove_dup(self,nums:List[int])->int:
        if len(nums)<=1:
            return nums
        for i in range(len(nums)-2):
            if nums[i]!=nums[i+1]:
                nums=nums[i:]
                break
        for i in range(len(nums)-1,1,-1):
            if nums[i]!=nums[i-1]:
                nums=nums[:i+1]
                break
        return nums



    def search_pos(self, nums: List[int], target: int) -> int:
        break_point=self.find_break_point(nums,0,len(nums)-1)
        if break_point==len(nums)-1:
            if nums[len(nums)-1]>nums[0]:
                return self.binary_search(nums,target,0,len(nums)-1)
        if target==nums[len(nums)-1]:
            return len(nums)-1
        elif target>nums[len(nums)-1]:
            return self.binary_search(nums,target,0,break_point-1)
        else:
            return self.binary_search(nums,target,break_point,len(nums)-1)

    def search(self,nums:List[int],target:int)-> int:
        if self.search_pos(self.remove_dup(nums),target)==-1:
            return False
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [1,0,1,1,1]
    target = 0
    print(solution.search(nums,target))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
