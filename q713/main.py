# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        results=0
        pos_left=0
        product=1
        for i in range(len(nums)):
            product=product*nums[i]
            if product>=k:
                while product>=k and pos_left<=i:
                    product=product/nums[pos_left]
                    pos_left=pos_left+1
            results=results+(i-pos_left)+1
        return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [10,5,2,6]
    k = 100
    solution=Solution()
    print(solution.numSubarrayProductLessThanK(nums,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
