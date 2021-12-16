# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1,num2=num1.split('+'),num2.split('+')
        real=int(num1[0])*int(num2[0])-int(num1[1][:-1])*int(num2[1][:-1])
        image=int(num1[0])*int(num2[1][:-1])+int(num1[1][:-1])*int(num2[0])
        return str(real)+'+'+str(image)+'i'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num1 = "1+-1i"
    num2 = "1+-1i"
    solution=Solution()
    print(solution.complexNumberMultiply(num1,num2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
