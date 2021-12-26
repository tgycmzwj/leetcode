# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
import math
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return math.mode(A)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,3,3]
    solution=Solution()
    print(solution.repeatedNTimes(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
