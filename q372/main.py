# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ans = 1
        for bb in b:
            ans = (pow(ans,10)%1337)*(pow(a,bb)%1337)
        return ans % 1337

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = 2147483647
    b = [2,0,0]
    solution=Solution()
    print(solution.superPow(a,b))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
