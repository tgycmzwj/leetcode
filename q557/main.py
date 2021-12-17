# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def reverseWords(self, s: str) -> str:
        results=s.split(' ')
        return ' '.join([i[::-1] for i in results])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    solution=Solution()
    print(solution.reverseWords(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
