# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        solution=[]
        while columnNumber>0:
            residual=columnNumber-(columnNumber//26)*26
            if residual==0:
                residual=26
            solution.append(chr(64+int(residual)))
            columnNumber=(columnNumber-residual)/26
        solution.reverse()
        return ''.join(solution)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    columnNumber = 2147483647
    solution=Solution()
    print(solution.convertToTitle(columnNumber))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
