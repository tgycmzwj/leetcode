# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



from typing import List
class Solution:
    def remove_dup(self,nums:List[int])->int:
        if len(nums)<=1:
            return nums
        i=0
        for i in range(len(nums)-1):
            if nums[i]!=nums[-1]:
                break
        nums=nums[i:]
        for i in range(len(nums)-2):
            if nums[i]!=nums[i+1]:
                nums=nums[i:]
                break
        for i in range(len(nums)-1,1,-1):
            if nums[i]!=nums[i-1]:
                nums=nums[:i+1]
                break
        return nums
    def find_break_point(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return left
        median = (left + right) // 2
        if nums[median] < nums[0]:
            return self.find_break_point(nums, left, median)
        else:
            return self.find_break_point(nums, median + 1, right)
    def findMin(self, nums: List[int]) -> int:
        nums=self.remove_dup(nums)
        index=self.find_break_point(nums,0,len(nums))
        if index==len(nums):
            return nums[0]
        return nums[index]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [4,5,6,7,0,1,4]
    #nums=[3,1,3,3]
    #nums=[1,2,2,2,0,1,1]
    #nums = [4, 5, 6, 7, 0, 1, 2]
    #nums = [11, 13, 15, 17]
    solution=Solution()
    print(solution.findMin(nums))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
