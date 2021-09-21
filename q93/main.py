# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        collec=[]
        for a in range(1,4):
            for b in range(1,4):
                for c in range(1,4):
                    for d in range(1,4):
                        if (a+b+c+d==len(s)) and int(s[:a])<=255 and int(s[a:a+b])<=255 and int(s[a+b:a+b+c])<=255 and int(s[a+b+c:])<=255 and (s[:a][0]!='0' or s[:a]=='0') and (s[a:a+b][0]!='0' or s[a:a+b]=='0') and (s[a+b:a+b+c][0]!='0' or s[a+b:a+b+c]=='0') and (s[a+b+c:][0]!='0' or s[a+b+c:]=='0'):
                            collec.append(s[:a]+'.'+s[a:a+b]+'.'+s[a+b:a+b+c]+'.'+s[a+b+c:])
        return collec

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "25525511135"
    solution=Solution()
    print(solution.restoreIpAddresses(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
