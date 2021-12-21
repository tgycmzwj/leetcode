# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp=[[1,1]]*len(nums) #ending with nums[i], length, ways
        for i in range(1,len(nums)):
            cu_max=-1e7
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    if nums[j]>=cu_max:
                        cu_max=max(cu_max,nums[j])
                        if dp[i][0]==dp[j][0]+1:
                            dp[i][1]=dp[i][1]+dp[j][1]
                        elif dp[i][0]<dp[j][0]+1:
                            dp[i]=[dp[j][0]+1,dp[j][1]]
        max_length=max([i[0] for i in dp])
        counter=0
        for i in dp:
            if i[0]==max_length:
                counter=counter+i[1]
        return counter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,3,5,4,7]
    nums=[1,2,4,3,5,4,7,2]
    nums=[1,1,1,2,2,2,3,3,3]
    solution=Solution()
    print(solution.findNumberOfLIS(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
