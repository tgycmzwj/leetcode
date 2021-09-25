# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def reverseBits(self, n: int) -> int:
        return int('{0:032b}'.format(n)[::-1],2)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    n= 10100101000001111010011100
    print(solution.reverseBits(n))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
