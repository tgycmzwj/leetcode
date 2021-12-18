# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def findMissingRanges(self, A, lower, upper):
        result = []
        A.append(upper+1)
        pre = lower - 1
        for i in A:
            if (i == pre + 2):
                result.append(str(i-1))
            elif (i > pre + 2):
                result.append(str(pre + 1) + "->" + str(i -1))
            pre = i
        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [0,1,3,50,75]
    lower = 0
    upper = 99
    solution=Solution()
    print(solution.findMissingRanges(nums,lower,upper))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
