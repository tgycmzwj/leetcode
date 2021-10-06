# This is a sample Python script.

from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        for i in range(len(dp)):
            for num in nums:
                if num==i:
                    dp[i]=dp[i]+1
                if num<i:
                    dp[i]=dp[i]+dp[i-num]
        return dp[-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,3]
    target = 4
    solution=Solution()
    print(solution.combinationSum4(nums,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
