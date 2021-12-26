# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            if len(e) > 0:
                a,b = e.split('@')[0],e.split('@')[1]
                if '+' in a:
                    s.add(a.split('+')[0].replace('.', '') + '@' + b)
                else:
                    s.add(a.replace('.', '') + '@' + b)
        return len(s)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    solution=Solution()
    print(solution.numUniqueEmails(emails))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
