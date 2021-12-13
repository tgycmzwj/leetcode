# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        if len(nums)<3:
            return 0
        dp=[0 for i in range(len(nums))]
        #starting point
        for i in range(0,len(nums)-2):
            j=i+1 #mid point
            k=len(nums)-1 #ending point
            while j<k:
                if nums[i]+nums[j]+nums[k]<target:
                    dp[i]=dp[i]+(k-j)
                    j=j+1
                else:
                    k=k-1
        return sum(dp)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [-2,0,1,3]
    target = 2
    solution=Solution()
    print(solution.threeSumSmaller(nums,target))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
