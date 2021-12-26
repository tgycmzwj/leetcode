# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(str(int("".join([str(i) for i in num])) + k))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num = [1,2,0,0]
    k = 34
    solution=Solution()
    print(solution.addToArrayForm(num,k))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
