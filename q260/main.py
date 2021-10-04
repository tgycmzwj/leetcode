# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=Counter(nums)
        final = []
        for value in x:
            if x[value] == 1:
                final.append(value)
        return final


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 2, 1, 3, 2, 5]
    solution=Solution()
    print(solution.singleNumber(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
