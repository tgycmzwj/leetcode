# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def detectCapitalUse(self, w: str) -> bool:
        return w[1:].islower() or w.isupper() or len(w) < 2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    word = "FlaG"
    solution=Solution()
    print(solution.detectCapitalUse(word))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
