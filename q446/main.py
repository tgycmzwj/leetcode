# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        #(diff:the number of sequences with at least length 2, ends before this element)
        dp = [defaultdict(int) for _ in range(len(nums))]
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                diff=nums[i]-nums[j]
                dp[i][diff]+=dp[j][diff]+1
                res+=dp[j][diff]
        return res

#2,4,6,8,10
#with diff=2, ending with 10: [6,8,10],[4,6,8,10],[2,4,6,8,10]---the same as len([2,4,6,8])-1
#7,7,7,7,7
#with diff=0, ending with the fifth 5: [0,1,4],[0,2,4],[0,3,4],[1,2,4],[1,3,4],[2,3,4],[0,1,2,4],[0,2,3,4],[0,1,3,4],[0,1,2,3,4]--10cases

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    nums = [2,4,6,8,10]
    nums = [7, 7, 7, 7, 7]
    print(solution.numberOfArithmeticSlices(nums))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
