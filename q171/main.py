# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        results=0
        for i in range(0,len(columnTitle)):
            results=results+(ord(columnTitle[len(columnTitle)-1-i])-64)*(26**(i))
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    columnTitle = "ZY"
    columnTitle = "AB"
    columnTitle = "A"
    columnTitle = "FXSHRXW"
    solution=Solution()
    print(solution.titleToNumber(columnTitle))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
