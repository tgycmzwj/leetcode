# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum=0
        count=0
        results={0:1}
        for i in range(len(nums)):
            running_sum=running_sum+nums[i]
            count=count+results.get(running_sum-k,0)
            results[running_sum]=results.get(running_sum,0)+1
        return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,3]
    k = 3
    solution=Solution()
    print(solution.subarraySum(nums,k))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
