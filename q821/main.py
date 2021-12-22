# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        pos = []
        for i in range(len(s)):
            if s[i] == c:
                pos.append(i)
        for i in range(len(s)):
            mn = len(s)
            for p in pos:
                mn = min(mn, abs(i-p))
            res.append(mn)
        return res
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "loveleetcode"
    c = "e"
    solution=Solution()
    print(solution.shortestToChar(s,c))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
