# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        #the maximum rob if the last one is the current element
        results=[0]*len(nums)
        results[0]=nums[0]
        if len(results)==1:
            return nums[0]
        if len(results)>=2:
            results[1]=nums[1]
        if len(results)>=3:
            results[2]=results[0]+nums[2]
        for i in range(3,len(nums)):
            results[i]=max(results[i-2]+nums[i],results[i-3]+nums[i])
        return max(results[-1],results[-2])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [2,7,9,3,1]
    # nums = [1, 2, 3, 1]
    nums=[1,2]
    solution=Solution()
    print(solution.rob(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
