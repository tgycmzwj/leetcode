# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(n).count('1')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=int(str("00000000000000000000000000001011"))
    solution=Solution()
    print(solution.hammingWeight(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
