# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        letters=[]
        for i in range(len(s)):
            if s[i].isalpha():
                letters.append(s[i])
        for i in range(len(s)):
            if s[i].isalpha():
                s[i]=letters.pop(-1)
        return ''.join(s)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "a-bC-dEf-ghIj"
    solution=Solution()
    print(solution.reverseOnlyLetters(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
