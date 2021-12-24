# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s='^'+s+'$'
        p='^'+p+'$'
        p=list(p)
        for i in range(len(p)):
            if p[i]=='?':p[i]='.'
            if p[i]=='*':p[i]='.*'
        p=''.join(p)
        return re.match(p,s)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "aa"
    p = "*"
    solution=Solution()
    print(solution.isMatch(s,p))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
