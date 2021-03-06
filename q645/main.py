# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        lack=list(set([i for i in range(1,len(nums)+1)])-set(nums))
        actual_sum=sum(nums)
        target_sum=len(nums)*(len(nums)+1)//2
        return [lack[0]-target_sum+actual_sum,lack[0]]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,2,4]
    solution=Solution()
    print(solution.findErrorNums(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
