# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def checksd(self, num):
        if '0' in str(num):
            return False
        for i in str(num):
            if num % int(i) != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right + 1) if self.checksd(i)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    left = 1
    right = 22
    solution=Solution()
    print(solution.selfDividingNumbers(left,right))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
