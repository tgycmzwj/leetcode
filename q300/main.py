# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #the longest increasing subsequence whose last element is at position i
        dp=[0]*len(nums)
        dp[0]=1
        for i in range(1,len(dp)):
            pos_set=[dp[j] for j in range(i) if nums[j]<nums[i]]
            dp[i]=1+max(pos_set) if len(pos_set)>0 else 1
        return max(dp)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [0, 1, 0, 3, 2, 3]
    nums = [7, 7, 7, 7, 7, 7, 7]
    nums=[1]
    solution=Solution()
    print(solution.lengthOfLIS(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
