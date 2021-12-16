# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A')>=2:
            return False
        counter=0
        for i in range(len(s)):
            if s[i]=='L':
                counter=counter+1
                if counter>=3:
                    return False
            else:
                counter=0
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "PPALLP"
    solution=Solution()
    print(solution.checkRecord(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
