# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    solution=Solution()
    print(solution.findKthLargest(nums,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
