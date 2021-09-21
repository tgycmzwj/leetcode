# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return [len(i) for i in s.split()][-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    s="Today is a nice day"
    print(solution.lengthOfLastWord(s))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
