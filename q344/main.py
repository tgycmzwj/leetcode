# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length=len(s)
        for i in range(length//2):
            s[i],s[length-1-i]=s[length-1-i],s[i]
        return s


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = ["h", "e", "m", "n", "p", "o"]
    s=['g']
    solution=Solution()
    print(solution.reverseString(s))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
