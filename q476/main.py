# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def findComplement(self, num: int) -> int:
        num=str(bin(num))[2:]
        results=''
        for i in range(len(num)):
            results=results+str(1-int(num[i]))
        return int(results,2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num=1
    solution=Solution()
    print(solution.findComplement(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
