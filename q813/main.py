# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def ave(self,num):
        return sum(num)/len(num)
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp=[[0]*(k+1) for i in range(len(nums)+1)]  #dp[i][j] partition first i words into j pieces
        for i in range(1,len(dp)):
            for j in range(1,min(i+1,k+1)):
                if i==j:dp[i][j]=sum(nums[:i])
                elif j==1:dp[i][j]=self.ave(nums[:i])
                else:
                    for t in range(1,i):
                        dp[i][j]=max(dp[i][j],dp[t][j-1]+self.ave(nums[t:i]))
        return max(dp[-1])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 4
    solution=Solution()
    print(solution.largestSumOfAverages(nums,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
