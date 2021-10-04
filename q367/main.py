# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return pow(num,0.5)==int(pow(num,0.5))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num=16
    solution=Solution()
    print(solution.isPerfectSquare(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
