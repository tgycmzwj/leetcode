# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from typing import List

import functools
class Solution:
    def greater_than(self,x,y):
        return x+y>y+x
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(i) for i in nums]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if self.greater_than(nums[i],nums[j]):
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        nums.reverse()
        results=''.join(nums).lstrip('0')
        if results=='':
            return '0'
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [3, 30, 34, 5, 9]
    nums=[0,0]
    print(solution.largestNumber(nums))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
