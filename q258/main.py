# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def addDigits(self, num: int) -> int:
        length=len(str(num))
        if length==1:
            return num
        nextiter=0
        while length>1:
            for i in str(num):
                nextiter=nextiter+int(i)
            num=nextiter
            length=len(str(num))
            nextiter=0
        return num



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num = 123215215234
    solution=Solution()
    print(solution.addDigits(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
