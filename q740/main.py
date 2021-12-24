# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq=[0]*(max(nums)+1)
        for num in nums:
            freq[num]+=num
        dp=[0]*len(freq)
        dp[1]=freq[1]
        for i in range(2,len(freq)):
            dp[i]=max(dp[i-1],dp[i-2]+freq[i])
        return max(dp[i],dp[i-1])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [2,2,3,3,3,4]
    solution=Solution()
    print(solution.deleteAndEarn(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
