# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def binary_search_left(self,nums: List, target: int)-> int:
        left=0
        right=len(nums)-1
        while right>=left:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]==target:
                if ((mid==0) or (nums[mid]!=nums[mid-1])):
                    return mid
                right=mid-1
        return -1
    def binary_search_right(self,nums: List, target: int)-> int:
        left=0
        right=len(nums)-1
        while right>=left:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]==target:
                if ((mid==len(nums)-1) or (nums[mid]!=nums[mid+1])):
                    return mid
                left=mid+1
        return -1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binary_search_left(nums,target),self.binary_search_right(nums,target)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums=[2,2]
    target = 2
    print(solution.searchRange(nums,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
