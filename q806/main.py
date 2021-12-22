# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]
        x = 1
        s1 = 0
        for i in s:
            a = l.index(i)
            if (s1 + widths[a] > 100):
                s1 = widths[a]
                x += 1
            else:
                s1 = s1 + widths[a]
        return ([x, s1])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    s = "bbbcccdddaaa"
    solution=Solution()
    print(solution.numberOfLines(widths,s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
