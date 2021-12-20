# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        return [k for (k,v) in c.items() if v==2]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    solution=Solution()
    print(solution.findDuplicates(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
