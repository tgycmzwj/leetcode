# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results=[]
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                k=j+1
                l=len(nums)-1
                while l>k:
                    temp_sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if temp_sum==target:
                        if [nums[i],nums[j],nums[k],nums[l]] not in results:
                            results.append([nums[i],nums[j],nums[k],nums[l]])
                        k=k+1
                    elif temp_sum<target:
                        while nums[k+1]==nums[k] and k+1<l:
                            k=k+1
                        k=k+1
                    elif temp_sum>target:
                        while nums[l-1]==nums[l] and k+1<l:
                            l=l-1
                        l=l-1
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0
    print(solution.fourSum(nums,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
