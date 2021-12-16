# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        nums=[i%k for i in nums]
        #continuous 0
        for i in range(len(nums)-1):
            if nums[i]==0 and nums[i+1]==0:
                return True
        nums=[i for i in nums if i!=0]
        mode_dic={0:1}
        running_sum=0
        for i in range(len(nums)):
            running_sum=(running_sum+nums[i])%k
            if running_sum in mode_dic:
                return True
            mode_dic[running_sum]=1
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [23,2,6,4,7]
    k = 6
    solution=Solution()
    print(solution.checkSubarraySum(nums,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
