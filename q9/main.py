# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    x=-121
    print(solution.isPalindrome(x))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
