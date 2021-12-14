# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        stri=''.join([str(i) for i in nums])
        stri=stri.split('0')
        return max([len(i) for i in stri])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    solution=Solution()
    print(solution.findMaxConsecutiveOnes(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
