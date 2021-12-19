# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        dp=[[] for i in range(len(nums))]
        for i in range(1,len(nums)):
            #arrays with length2
            for j in range(i):
                if nums[j]<=nums[i]:
                    dp[i].append([nums[j],nums[i]])
                    for ele in dp[j]:
                        dp[i].append(ele+[nums[i]])
        results=[]
        for lst in dp[1:]:
            for ele in lst:
                if ele not in results:
                    results.append(ele)
        return results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [4,6,7,7]
    solution=Solution()
    print(solution.findSubsequences(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
