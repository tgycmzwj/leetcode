# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    haystack = "hello"
    needle = "ll"
    print(solution.strStr(haystack,needle))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
