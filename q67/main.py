# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a,2)+int(b,2)))[2:]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    a = "1010"
    b = "1011"
    print(solution.addBinary(a,b))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
