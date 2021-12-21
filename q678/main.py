# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def checkValidString(self, s: str) -> bool:
        #remove unnecessary elements
        while s != s.replace("()", ""):
            s = s.replace("()", "")
        parent,star=[],[]
        for i in range(len(s)):
            if s[i]=='(':
                parent.append(i)
            elif s[i]==')':
                if len(parent)>0:
                    parent.pop(-1)
                elif len(star)>0: #use * as (
                    star.pop(-1)
                else:
                    return False
            elif s[i]=='*':
                star.append(i)
        #use * as )
        while len(parent)>0:
            if len(star)==0:
                return False
            if star[-1]<parent[-1]:
                return False
            parent.pop(-1)
            star.pop(-1)
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "(((*))"
    solution=Solution()
    print(solution.checkValidString(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
