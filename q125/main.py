# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        list=[s[i].lower() for i in range(len(s)) if s[i].isalnum()]
        return list==list[::-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    s = "race a car"
    solution=Solution()
    print(solution.isPalindrome(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
