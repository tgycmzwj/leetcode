# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def hasAlternatingBits(self, n):
        s = bin(n)
        return '00' not in s and '11' not in s

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 5
    solution=Solution()
    print(solution.hasAlternatingBits(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
