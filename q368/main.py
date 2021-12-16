# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp=[[0]*len(nums) for i in range(len(nums))]  #whether num[i]%num[j] or num[j]%num[i]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]%nums[j]==0 or nums[j]%nums[i]==0:
                    dp[i][j]=1
                    dp[j][i]=1
        results=nums.copy()
        while sum(sum(i) for i in dp)!=len(dp)**2:
            cur_sum=[sum(i) for i in dp]
            argmin=[i for i in range(len(cur_sum)) if cur_sum[i]==min(cur_sum)]
            argmin=argmin[0]
            #remove row
            dp=[dp[i] for i in range(len(dp)) if i!=argmin]
            #remove col
            dp=[[x[j] for j in range(len(x)) if j!=argmin] for x in dp]
            results.pop(argmin)
        return results

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        divisibleSubset = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] % nums[j]) == 0 and len(divisibleSubset[i]) < len(divisibleSubset[j]) + 1:
                    divisibleSubset[i] = divisibleSubset[j] + [nums[i]]
        return max(divisibleSubset, key=len)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,3]
    solution=Solution()
    print(solution.largestDivisibleSubset(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
