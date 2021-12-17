# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        bound=sum(nums)
        if abs(target)>bound:
            return 0
        dp=[[0]*(1+bound) for i in range(len(nums))]
        #dp[i][j]--the number of ways of generating value j with the first i element
        #dp[i][j]--the number of ways of generating value -j with the first i element
        for i in range(len(nums)):
            if i==0:
                if nums[i]!=0:
                    dp[i][nums[i]]=1
                else:
                    dp[i][nums[i]]=2
                continue
            for j in range(1+bound):
                case_add=0
                case_minus=0
                if abs(j-nums[i])<=bound:
                    case_add=dp[i-1][abs(j-nums[i])]
                if abs(j+nums[i])<=bound:
                    case_minus=dp[i-1][abs(j+nums[i])]
                dp[i][j]=case_add+case_minus
        return dp[len(nums)-1][abs(target)]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,1,1,1,1]
    target = 3
    nums=[1]
    target=2
    # nums=[1000]
    # target=-1000
    # nums=[0,0,0,0,0,0,0,0,1]
    # target=1
    solution=Solution()
    print(solution.findTargetSumWays(nums,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
