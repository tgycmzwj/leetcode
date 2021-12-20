# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def helper(self,i,j):
        if i<j and not self.dp[i][j]:
            #when player take the left element, the remaining game is the opposite with one less game
            self.dp[i][j]=max(self.nums[i]-self.helper(i+1,j),self.nums[j]-self.helper(i,j-1))
        return self.dp[i][j]
    def PredictTheWinner(self, nums: List[int]) -> bool:
        #dp[i][j]----player1 score - player2 score when start at i and end at j
        self.nums=nums
        self.dp = [[0]*len(nums) for i in range(len(nums))]
        return self.helper(0,len(nums)-1)>=0



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,5,233,7]
    solution=Solution()
    print(solution.PredictTheWinner(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
