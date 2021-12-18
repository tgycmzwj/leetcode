# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_diff,max_diff = 0,0
        for i in range(len(nums)-k):
            cur_diff += nums[i+k] - nums[i]
            if cur_diff > max_diff: max_diff = cur_diff
        return (sum(nums[:k])+max_diff)/k

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 5
    solution=Solution()
    print(solution.findMaxAverage(nums,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
