# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def convertToBase7(self, num: int) -> str:
        s = []
        if num == 0:
            return "0"
        flag = False
        if num < 0:
            flag = True
            num = -num
        while num > 0:
            s.append(str(num % 7))
            num //= 7
        return ('-' if flag else '') + ''.join(s[::-1])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num = 100
    solution=Solution()
    print(solution.convertToBase7(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
