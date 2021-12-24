# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.match('^'+p+'$', s) is not None

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "aa"
    p = "a*"
    solution=Solution()
    print(solution.isMatch(s,p))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
