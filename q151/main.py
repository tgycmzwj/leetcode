# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def reverseWords(self, s: str) -> str:

        return ' '.join([i for i in s.split(' ')[::-1] if i !=''])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "the sky is blue"
    s="  hello world  "
    s = "a good   example"
    solution=Solution()
    print(solution.reverseWords(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
