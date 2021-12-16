# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        total_num=10
        for i in range(2,n+1):
            total_num+=9*math.factorial(9)//math.factorial(9-i+1)
        return total_num

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=8
    solution=Solution()
    print(solution.countNumbersWithUniqueDigits(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
