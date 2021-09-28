# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results1=[0]*len(nums)
        results2=[0]*len(nums)
        results1[0]=nums[0]
        for i in range(1,len(results1)):
            results1[i]=results1[i-1]*nums[i]
        results2[-1]=nums[-1]
        for i in range(len(results2)-2,-1,-1):
            results2[i]=results2[i+1]*nums[i]
        results=[0]*len(nums)
        results[0]=results2[1]
        results[-1]=results1[-2]
        for i in range(1,len(results1)-1):
            results[i]=results1[i-1]*results2[i+1]
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,3,4]
    solution=Solution()
    print(solution.productExceptSelf(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
