# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sol=int(float(dividend)/float(divisor))
        if sol<=pow(2,31)-1 and sol>=-pow(2,31):
            return sol
        elif sol>pow(2,31)-1:
            return pow(2,31)-1
        else:
            return -pow(2,31)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    dividend = -2147483648
    divisor = -1
    print(solution.divide(dividend,divisor))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
