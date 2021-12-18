# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        p= str(Fraction(str(eval(expression))).limit_denominator(10000000))
        if "/" not in p:
            return p+"/"+"1"
        return p

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    expression = "-1/2+1/2+1/3"
    solution=Solution()
    print(solution.fractionAddition(expression))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
